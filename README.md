# eyecare-daemon

![Alt text](https://i.imgur.com/B5HF85r.png "Demonstration")

Save your eyes by following the [20/20/20](http://www.labnol.org/software/computer-eye-exercise/14069/) rule! `eyecare-daemon` will send you a notification every 20 minutes, urging you to protect your eyes by looking 20 feet away for 20 seconds. Once your eyes have recovered from their toil, the daemon will let you know that you can get back to work. ^Such ^an ^essential ^for ^health ^script ^should ^be ^included ^by ^default ^in ^all ^distros.

____

## Installation

Simplicity itself.

Download both `eyecare.py` and `enums.py` and place them in the same folder. Set the following code to run at startup (eg. putting it in `xinit.rc` or your window manager config file):

    python ~/path/to/file/eyecare.py

## Details

| Setting  | Detail        |
|----------|---------------|
| `work_time` |  Default `1200`, in seconds |
| `relax_time` | Default `20`, in seconds |
| `notification_expire` - Linux only | Default `5000`, in ms |
| `command_method` | `modern` is preferred, but try `legacy` if you encounter an `OSError`-- this error happens when your shell python path variable is not set, so please do set it. `legacy` is also the default for osx as most people (I presume) do not have the path variable set, and those who do will comment out this default anyway :) |

## Dependencies

* python
* `libnotify` for linux notification (sometimes packaged as `libnotify-bin`)

____

## Hall of Fame

* @ragerin for a very helpful fork which was merged a long while ago
* /u/guiltydoggy for testing the osx script and putting up with my relentless revisions

