import json
import boto3
import time
import pprint
import re
import base64
import gzip
import datetime

def lambda_handler(event, context):
    cw = boto3.client('cloudwatch')
    #print(event['awslogs']['data'])
    
    decode_b64 = base64.b64decode(event['awslogs']['data'])
    decompress = gzip.decompress(decode_b64)
    log = json.loads(decompress)
    
    #print(log['message'])
    print(log)
    
    #print(log['message'])
    
    for line in log['logEvents']:
        print(line['message'])
        group = re.findall("group\=(.*?)\,", line['message'])[0]
        name = re.findall("name\=(.*?)\,", line['message'])[0]
        max_size_kb = re.findall("max_size_kb\=(.*?)\,", line['message'])[0]
        current_size_kb = re.findall("current_size_kb\=(.*?)\,", line['message'])[0]
    
        cw.put_metric_data(
        Namespace='Splunk Metrics',
        MetricData=[
            {
                'MetricName': 'Splunk Current Queue Size',
                'Dimensions': [
                    {
                        'Name': 'Queue',
                        'Value': name
                    },
                    {
                        'Name': 'Max Queue Size',
                        'Value': max_size_kb
                    }
                ],
                'Value': float(current_size_kb),
                'Unit': 'Kilobytes'
            },
        ]
        )