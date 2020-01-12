# VEX IQ Python-Project
import sys
import vexiq

#region config
motor_left        = vexiq.Motor(1)
motor_right       = vexiq.Motor(2)
motor_translation = vexiq.Motor(3)
motor_fire_left   = vexiq.Motor(4)
motor_fire_right  = vexiq.Motor(5)
joystick          = vexiq.Joystick()
#endregion config


while True:
    a = joystick.axisA()
    c = joystick.axisC()
    
    motor_left.run(a)
    motor_right.run(-a)
    motor_translation.run(c)
    
    if joystick.bLup():
        motor_fire_left.run(100)
        motor_fire_right.run(-100)
        sys.sleep(10)
    else:
        motor_fire_left.run(0)
        motor_fire_right.run(0)


'''
底盘由三个马达控制，一个控制左轮，一个控制右轮，一个控制平移。
'''




