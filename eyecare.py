import subprocess as s  # to pass system commands
import time  # for pausing the script
import platform as p  # to detect linux or osx
from enums import Urgency


# timer settings
work_time = 1200
relax_time = 20
notification_expire_time_ms = 5000  # linux only

# message settings
warning_title = 'Your eyes'
warning_message = 'Take a break. Just {} seconds.'.format(relax_time)
warning_urgency = Urgency.high  # linux only. can be either low, medium or high

success_title = 'Good job'
success_message = 'You can get back to work.'
success_urgency = Urgency.low   # linux only. can be either low, medium or high


# get the system platform
os = p.system().lower()


if os == 'linux':
    command = 'notify-send'  # command being used
    expiration = '--expire-time={}'.format(notification_expire_time_ms)

    while True:
        time.sleep(work_time)
        s.call([command, warning_urgency, expiration, warning_title, warning_message])
        time.sleep(relax_time)
        s.call([command, success_urgency, expiration, success_title, success_message])

if os == 'darwin':  # thats OSX
    command1 = 'osascript -e'
    command2 = 'display notification'  # osx command, extra ' has to be there!

    while True:
        time.sleep(work_time)
        s.call([command1, '\'' + command2, '\"' + warning_message + '\"', 'with title', '\"' + warning_title + '\"'])
        time.sleep(relax_time)
        s.call([command1, '\'' + command2, '\"' + success_title + '\"', 'with title', '\"' + success_message + '\"'])
>>>>>>> afe5d4b355d3cf61f5199ae9375f0a60805ff825
