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
	minTemp = conf['min_temp']
	duration = conf['duration']
	delay = conf['delay']

	#TUYA_LOGGER.setLevel(logging.DEBUG)
	DEBUG = conf['debug']

	openapi = TuyaOpenAPI(tuyaOpenApiRoot, accessId, accessKey)
	openapi.connect()

	# If device is off, don't do anything
	response = openapi.get('/v1.0/iot-03/devices/{}/status'.format(deviceId))
	status = response['result'][0]['value']

	if status == False:
		exit()

	openapi.post('/v1.0/iot-03/devices/{}/commands'.format(deviceId), {'commands': [
	{'code': 'work_mode', 'value': 'white'},
	{'code': 'temp_value_v2', 'value': minTemp}]})

	brightness = response['result'][2]['value']

	brightnessRange = brightness - minBrightness

	if DEBUG == True:
		duration = 30
		delay = 3

	step = int(brightnessRange / (duration / delay))

	for brightness in range(brightness-step, 10, -1 * step):
		openapi.post('/v1.0/iot-03/devices/{}/commands'.format(deviceId), {'commands': [{'code': 'bright_value_v2', 'value': brightness}]})
		sleep(delay)

	openapi.post('/v1.0/iot-03/devices/{}/commands'.format(deviceId), {'commands': [{'code': 'switch_led', 'value': False}]})

