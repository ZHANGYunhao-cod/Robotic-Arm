# -*- coding: utf-8 -*-
# This script is written in Python 3

'''
This document is applicable to the myCobot series (280,320) of robotic arms. 
The function is to modify the joint motor configuration parameters 
and verify the modification results.Please ensure that the robot 
control port is not occupied when using it. If you encounter failure, 
please run the file again.

本文件适用于myCobot系列机械臂(280,320), 功能为修改关节电机配置参数并校验修改结果,
使用时请保证未占用机器人控制端口,如遇到失败请重新运行文件.
'''

#Import dependent library files. 导入相关库文件。
import time
from pymycobot.mycobot import MyCobot

#Define data address and data. 定于数据地址及内容。
data_address = [13, 14, 21, 22, 23, 24, 26, 27]      
data_value = [90, 130, 32, 8, 0, 0, 1, 1]

#Define the serial port of the robotic arm，Please check your robot model and fill in the corresponding content.
#定义机器人串口配置数据，请检查你的机器人型号，并根据具体型号填写。
_port = '/dev/ttyAMA0'
_baud = 115200

# _port = 'COM4'
# _baud = 115200
#Instantiate a hardware serial port. 实例化硬件串口。
try:
    mc = MyCobot(_port, _baud)
except Exception as e:
    print(e)
    print("错误：当前串口无法使用，请检查串口序号是否正确，确认无误后请重新运行程序。")
    exit()


#Loop modification and display modification results. 循环修改关节电机配置参数并校验是否修改成功。
#joint_id = 1 - 6.
for joint_id in range(1,7):                                                            
    print('')
    #read data_address len. 读取数据地址长度，作为循环参数。
    for _address in range(len(data_address)):
        #write data_value. 向机器人写入关节伺服参数。
        mc.set_servo_data(joint_id, data_address[_address], data_value[_address])
        #delay 0.2s
        time.sleep(0.1)                                                                
        #read data_value. 读取写入后的关节伺服参数。
        _data_value = mc.get_servo_data(joint_id, data_address[_address])
        #delay 0.2s
        time.sleep(0.1)
        #check modify result. 检查读取到的参数和设定参数是否一致。
        if _data_value == data_value[_address]:                                               
            check_result = "  modify successfully "
        else:
            check_result = "  modify error "
        #print. 打印结果。
        print("joint_id:"  + str(joint_id) + 
            "  data_address : " + str(data_address[_address]) + 
            "   data: " + str(_data_value) + 
            check_result)
input("The program ends, please press any key to exit. 程序结束，请按任意键退出。")
exit()

