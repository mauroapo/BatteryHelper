import psutil, win32api
from apscheduler.schedulers.blocking import BlockingScheduler

def checkBattery():
	global scheduler
	battery = psutil.sensors_battery()
	plugged = battery.power_plugged
	percent = int(battery.percent)
	if(not plugged and percent <= 35):
		win32api.MessageBox(0, 'Conecte o carregador', 'Battery Notification', 0x00001000)
scheduler = BlockingScheduler()
checkBattery();
scheduler.add_job(checkBattery, 'interval', minutes=1, id='battery helper')
scheduler.start()