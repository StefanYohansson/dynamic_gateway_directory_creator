this repository is a tool that mimic half of mod_telnyx_rtc behavior

- add user
  - create directory file
  - create gateway file
  - reloadxml
  - rescan profile
- delete user
  - delete directory file
  - delete gateway file
  - kill gateway
  - reloadxml


the purpose of the test is to stress test B2BUA without mod_telnyx_rtc and investigate if the leak is on sofia (gateway logic not prepared to be dynamic) or some other place on mod_telnyx_rtc
