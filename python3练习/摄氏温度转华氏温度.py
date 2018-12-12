

# -*- coding: UTF-8 -*-

#摄氏度和华氏度互相转换

#其他

celsius=float(input("输入摄氏温度为："))

fahrenheit=(celsius*1.8)+32

print("%0.1f 摄氏温度转化为华氏温度为%0.1f" %(celsius,fahrenheit))


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

fahrenheit_1=float(input("输入华氏温度为："))

celsius_1=(fahrenheit_1-32)/1.8

print('%0.1f 华氏温度转化为摄氏温度为%0.1f' %(fahrenheit_1,celsius_1))