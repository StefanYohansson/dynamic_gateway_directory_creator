this repository is a tool that try to expose a problem after gateway deletion

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


the purpose of the test is to stress test B2BUA and investigate if the leak is on sofia (gateway logic not prepared to be dynamic)
