# Tooltip notes

host_segment = '''
host_segment = &lt;integer&gt; <br />
* If set to N, the Splunk platform sets the Nth "/"-separated segment of the path
  as 'host'.<br />
* For example, if you set "host_segment = 3" and the path is
      /logs/servers/host08/abc.txt, the third segment, "host08", is used.<br />
* If the value is not an integer or is less than 1, the default 'host'
  setting is used.<br />
* On Windows machines, the drive letter and colon before the backslash *does not*
  count as one segment.<br />
    * For example, if you set "host_segment = 3" and the monitor path is
      D:\logs\servers\host01, Splunk software sets the host as "host01" because
      that is the third segment.<br />
* No default.
'''

whitelist = '''
whitelist = &lt;regular expression&gt; <br />
* If set, files from this input are monitored only if their path matches the
  specified regular expression.<br />
* Takes precedence over the deprecated '_whitelist' setting, which functions
  the same way.<br />
* No default.
'''

host_regex = '''
host_regex = &lt;regular expression&gt; <br />
* If specified, &lt;regular expression&gt extracts host from the path to the file
  for each input file. <br />
    * Detail: This feature examines the source key; if source is set
      explicitly in the stanza, that string is matched, not the original
      filename. <br />
* Specifically, the first group of the regular expression (regex) is used
  as the host. <br />
* If the regex fails to match, the input uses the default 'host' setting. <br />
* If 'host_regex' and 'host_segment' are both set, the input ignores 'host_regex'. <br />
* No default.
'''

crcsalt = '''
crcSalt = &lt;string&gt; <br />
* Use this setting to force the input to consume files that have matching CRCs,
  or cyclic redundancy checks. <br />
    * By default, the input only performs CRC checks against the first 256
      bytes of a file. This behavior prevents the input from indexing the same
      file twice, even though you might have renamed it, as with rolling log
      files, for example. Because the CRC is based on only the first
      few lines of the file, it is possible for legitimately different files
      to have matching CRCs, particularly if they have identical headers. <br />
* If set, &lt;string&gt; is added to the CRC. <br />
* If set to the literal string "&lt;SOURCE&gt;" (including the angle brackets), the
  full directory path to the source file is added to the CRC. This ensures
  that each file being monitored has a unique CRC. When 'crcSalt' is invoked,
  it is usually set to &lt;SOURCE&gt;. <br />
* Be cautious about using this setting with rolling log files; it could lead
  to the log file being re-indexed after it has rolled. <br />
* In many situations, 'initCrcLength' can be used to achieve the same goals. <br />
* Default: empty string
'''

blacklist = '''
blacklist = &lt;regular expression&gt; <br />
* If set, files from this input are NOT monitored if their path matches the
  specified regex. <br />
* Takes precedence over the deprecated '_blacklist' setting, which functions
  the same way. <br />
* If a file matches the regexes in both the deny list and allow list settings, <br />
  the file is NOT monitored. Deny lists take precedence over allow lists. <br />
* No default.
'''

ignoreolderthan = '''
ignoreOlderThan = &lt;non-negative integer&gt;[s|m|h|d] <br />
* The monitor input compares the modification time on files it encounters
  with the current time. If the time elapsed since the modification time
  is greater than the value in this setting, Splunk software puts the file
  on the ignore list. <br />
* Files on the ignore list are not checked again until the Splunk
  platform restarts, or the file monitoring subsystem is reconfigured. This
  is true even if the file becomes newer again at a later time. <br />
  * Reconfigurations occur when changes are made to monitor or batch
    inputs through Splunk Web or the command line. <br />
* Use 'ignoreOlderThan' to increase file monitoring performance when
  monitoring a directory hierarchy that contains many older, unchanging
  files, and when removing or adding a file to the deny list from the
  monitoring location is not a reasonable option.
'''
