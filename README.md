# SmartBulbSunriseSunset
Simulate a sunrise or sunset with your Tuya / Smart Life bulb.

In addition to the alarm, wouldn't it be great if your smart-bulb gently wakes you up?

SmartBulbSunriseSunset is a collection of Python scripts which enable you to slowly increase / decrease the brightness of your device.


## Configuration

Some of the configuration entries are:

* _access_id_ and _access_key_: The values from your Tuya cloud project registration. How to: https://developer.tuya.com/en/docs/iot/config-cloud-project?id=Kat2eytbffx3v
    - Required API Services: IoT Core, Authorization, Device Status Notification, Industry Project Client Service
    - Ensure that this project is configured to have permission on the device that you want to control
* _device_id_: The ID of the bulb.
* _duration_: How long should the entire dimming / brightening process last.
* _delay_: Governs how smooth the dimming / brightening would be. A higher value would result in a more choppy experience.
* _debug_: If set to 'true', the configuration values for _duration_ and _delay_ are ignored. A hard-coded duration of 30s and delay of 3s is used. I use this for  testing whether the script is actually working.


## Arguments

* -a / --action
    - _sunrise_: (Default) The bulb is turned on. The mode is set to _white_. The temperature to _warm_. The brightness it set to minimum, and incrementally increased to maximum.
    - _sunset_: If the bulb is not on, the script exits early and does nothing. Else: The mode is set to _color_. The colour to _yellow_. The brightness it set to maximum, and incrementally reduced to minimum.


## How to run

I use a CRON job to schedule the sunrise and sunset.

* Fill in the configuration file
* pip install -r requirements.txt _(Better to do this in a Python virtual environment though)_
* python main.py --action sunrise / sunset


## Containerization

You can use the Dockerfile to create an image and run it in a container.

My setup uses it like this in CRON:
docker-compose -f /home/\<username>/projects/smart-bulb-sunrise-sunset/docker-compose-sunrise.yml up
