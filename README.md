# openwebnet-alarm
###Description
Python scripts that allow you to control the openwebnet alarm. 
You can retrieve the status and enable/disable it.
OpenWebNet does not allow you to enable (\*5\*8##) and disable(\*5\*9##) alarm with the default commands. You need to define two auxiliary commands (see the scripts for more info).

### Tested devices
- Alarm control unit 3486
- Web server F453AV

### Scripts description
##### enable_alarm.py
This script enables the alarm.
Requires an auxiliary command.

##### disable_alarm.py
This script disables the alarm
Requires an auxiliary command.

##### alarm_status.py
Retrieve the alarm status.
Doesn't need an auxiliary command.

##### OpenWebNet.py
This is modified version of this https://github.com/pippocla/OpenWebNet library.
It is used for authentication and to send command to the Web Server.
