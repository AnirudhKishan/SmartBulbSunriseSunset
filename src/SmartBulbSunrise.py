import logging
from time import sleep

from tuya_connector import TuyaOpenAPI, TUYA_LOGGER

from ConfigurationReader import ConfigurationReader


def run():

	tuyaOpenApiRoot = "https://openapi.tuyain.com"

	conf = ConfigurationReader.Read("conf.json")
	
	accessId = conf['access_id']
	accessKey = conf['access_key']
	deviceId = conf['device_id']
	minBrightness = conf['min_brightness']
	maxBrightness = conf['max_brightness']
	minTemp = conf['min_temp']
	maxTemp = conf['max_temp']
	duration = conf['duration']
	delay = conf['delay']

	#TUYA_LOGGER.setLevel(logging.DEBUG)
	DEBUG = conf['debug']

	openapi = TuyaOpenAPI(tuyaOpenApiRoot, accessId, accessKey)
	openapi.connect()

	openapi.post('/v1.0/iot-03/devices/{}/commands'.format(deviceId), {'commands': [
	{'code': 'work_mode', 'value': 'white'},
	{'code': 'temp_value_v2', 'value': minTemp},
	{'code': 'bright_value_v2', 'value': minBrightness},
	{'code': 'switch_led', 'value': True}]})

	brightnessRange = maxBrightness - minBrightness

	if DEBUG == True:
		duration = 30
		delay = 3

	step = int(brightnessRange / (duration / delay))

	for brightness in range(minBrightness, maxBrightness, step):
		openapi.post('/v1.0/iot-03/devices/{}/commands'.format(deviceId), {'commands': [{'code': 'bright_value_v2', 'value': brightness}]})
		sleep(delay)

	openapi.post('/v1.0/iot-03/devices/{}/commands'.format(deviceId), {'commands': [
	{'code': 'temp_value_v2', 'value': maxTemp},
	{'code': 'bright_value_v2', 'value': maxBrightness}]})

