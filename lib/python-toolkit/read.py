import sys
import os
import json
import RPi.GPIO as GPIO
import MFRC522
import signal

configPath = os.path.dirname(os.path.realpath(__file__)) + '/../config.json'

if os.path.isfile(configPath) and os.access(configPath, os.R_OK):
	readData = open(configPath)
	config = json.load(readData)
	readData.close()
else:
	print json.dumps({
		"event": "error",
		"message": "Config file not found does not have access to read.",
		"path": configPath
	});
	sys.exit(0)

live = True

# handle signal interuptions
def closeReader(signal, frame):
	global live
	live = False
	print(json.dumps({
		"event": "close",
		"signal": signal
	}))
	GPIO.cleanup()

signal.signal(signal.SIGINT, closeReader)

print(json.dumps({
	"event": "open"
}))

#GPIO.setwarnings(False)
MIFAREReader = MFRC522.MFRC522()

while live:

	# live scan
	(readStatus, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
	(uidStatus, uid) = MIFAREReader.MFRC522_Anticoll()
	# get uid
	if (readStatus == 2) or (uidStatus == 2):
		continue

	if (readStatus != MIFAREReader.MI_OK) or (uidStatus != MIFAREReader.MI_OK):
		print json.dumps({
			"event": "read",
			"status": "read_error",
			"debug": {
				"read": readStatus,
				"uid": uidStatus
			}
		})
		continue

	# verify security
	MIFAREReader.MFRC522_SelectTag(uid)
	# default status
	status = MIFAREReader.MI_OK

	# MIFAREReader.MFRC522_DumpClassic1K(config['rfid']['key'], uid)
	sectors = config['rfid']['sectors']
	if isinstance(sectors, int):
		sectors = [sectors]

	data = {}
	for sector in sectors:
		print "reading loop " + str(sector)
		status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, sector, config['rfid']['key'], uid)
		if status != MIFAREReader.MI_OK:
			break;
		data[sector] = MIFAREReader.MFRC522_Read(sector)

	if status != MIFAREReader.MI_OK:
		print json.dumps({
			"event": "read",
			"status": "error",
			"debug": status,
			"sectors": sectors
		})
	else:
		print json.dumps({
			"event": "read",
			"status": "success",
			"uid": uid,
			"data": data
		})
	MIFAREReader.MFRC522_StopCrypto1()
