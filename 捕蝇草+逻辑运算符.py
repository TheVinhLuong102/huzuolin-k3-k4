import sys
import vexiq

while True:
	if bumper_1.is_pressed() and bumper_2.is_pressed():
		motor_3.run_raw_until(100,400)
		sys.sleep(5)
		motor_3.run_raw_until(-50,400)
	else:
		motor_3.off()
		
		
		
		
		
		
		
		
		
		
		
'''
捕蝇草。
当同时触碰到两个感应器的时候，捕蝇夹迅速合拢，消化5秒后，缓慢打开。
'''
