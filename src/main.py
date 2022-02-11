import argparse
import SmartBulbSunrise, SmartBulbSunset

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	
	parser.add_argument("-a", "--action", choices=["sunrise", "sunset"], default="sunrise")
	args = parser.parse_args()
	
	if(args.action == 'sunrise'):
		SmartBulbSunrise.run()
	elif(args.action == 'sunset'):
		SmartBulbSunset.run()
	
