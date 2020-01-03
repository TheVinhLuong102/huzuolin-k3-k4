import sys
import vexiq


def fw(power,sec):
    motor_t.off()
    motor_l.run(power)
    motor_r.run(-power)
    sys.sleep(sec)

def tn(power,sec):
    motor_l.off()
    motor_r.off()
    motor_t.run(power)
    sys.sleep(sec)
    
fw(100,2)
tn(100,2)
fw(-100,2)
tn(-100,2)








'''
小车安装有五个万向轮
四个负责前后移动，一个负责左右移动

motor_l：左马达
motor_r：右马达
motor_t：中间负责转弯的马达


这里创建的是函数，即Founction，在调用函数的时候，直接写上函数的名称和参数就可以了。

定义的时候，括号里面的字母，比如power，sec等，这种没有具体数字的参数，是形式上的参数，我们把它叫做形参。

在调用函数的时候，我们输入了具体的数字，这些数字，是实际参数，我们把它叫做实参。

对比Founction和Method，函数和方法：

fw(100,2)

motor.run(100,2)

fw是函数
run是方法
'''
