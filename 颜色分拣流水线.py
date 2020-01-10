import sys
import vexiq

while True:  
  a = color_1.named_color()
  motor_2.run(20)
  if a==1:
    sys.sleep(1)#这里是从颜色识别装置到分拣装置所需要的时间。
    motor_3.run_raw_until(100,200)
    motor_3.run_raw_until(-100,200)
  else:
    motor_3.off()
    
    
    
'''
RobotMeshStudio软件中，
named_color()这个方法，将每个颜色设置了对应的序号，比如红色，序号是1。
我们设计的分拣机器，只分拣红色的积木块。
'''
