from flask import Flask, render_template, request, session, redirect
from bin import tooltip

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route('/', methods=['GET', 'POST'])
def index(name=None):

    host_segment_tt = tooltip.host_segment
    whitelist_tt = tooltip.whitelist
    host_regex_tt = tooltip.host_regex
    crcsalt_tt = tooltip.crcsalt
    blacklist_tt = tooltip.blacklist
    ignoreolderthan_tt = tooltip.ignoreolderthan
    
    host_segment_input = ""
    whitelist_input = ""
    host_regex_input = ""
    crcsalt_input = ""
    blacklist_input = ""
    ignoreolderthan_input = ""

    props_conf_input = ""
    path_input = ""
    os_type = ""
    index_input = ""
    sourcetype_input = ""
    
    if request.method == 'POST':
    
        if request.form['type'] == 'HEC':
            print("works")
            
            index_input = request.form['index']
            sourcetype_input = request.form['sourcetype']
            
            props_conf_input = index_input + sourcetype_input
    
    
        if request.form['type'] == 'File monitor' and request.form['path']!="":

            os_type = request.form['os']
            path_input = request.form['path']
            index_input = request.form['index']
            sourcetype_input = request.form['sourcetype']
            
            host_segment_input = request.form.getlist('host-segment')
            whitelist_input = request.form.getlist('whitelist')
            host_regex_input = request.form.getlist('host-regex')
            crcsalt_input = request.form.getlist('crcsalt')
            blacklist_input = request.form.getlist('blacklist')
            ignoreolderthan_input = request.form.getlist('ignoreolderthan')
            
            if os_type == 'Linux':
                props_conf_input = f'''
[monitor://{path_input}]
index = {index_input}
sourcetype = {sourcetype_input}'''

            elif os_type == 'Windows':
                props_conf_input = f'''
[monitor:\\\\{path_input}] 
index = {index_input}
sourcetype = {sourcetype_input}'''

            else:
                props_conf_input = ''
                
            if host_segment_input:
                props_conf_input += "\nhost_segment = "
            
            if host_regex_input:
                props_conf_input += "\nhost_regex = "
             
            if whitelist_input:
                props_conf_input += "\nwhitelist = "
            
            if blacklist_input:
                props_conf_input += "\nblacklist = "
            
            if crcsalt_input:
                props_conf_input += "\ncrcSalt = "
            
            if ignoreolderthan_input:
                props_conf_input += "\nignoreOlderThan = "
            

    return render_template('index.html', props_conf_input=props_conf_input, path_input=path_input, os_type=os_type, index_input=index_input, sourcetype_input=sourcetype_input, host_segment_tt=host_segment_tt, whitelist_tt=whitelist_tt, host_regex_tt=host_regex_tt, crcsalt_tt=crcsalt_tt, blacklist_tt=blacklist_tt, ignoreolderthan_tt=ignoreolderthan_tt)


@app.route('/props/', methods=['GET', 'POST'])
def props():
    props_conf_input = ""
    path_input = ""
    os_type = ""
    index_input = ""
    sourcetype_input = ""
    
    return render_template('props.html', props_conf_input=props_conf_input, path_input=path_input, os_type=os_type, index_input=index_input, sourcetype_input=sourcetype_input)