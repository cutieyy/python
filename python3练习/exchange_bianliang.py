# -*- coding: UTF-8 -*-

x=input("输入x的值为：")
y=input("输入y的值为：")

temp=x
x=y
y=temp

print("交换后x的值为：{}".format(x))
print("交换后y的值为：{}".format(y))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

x,y=y,x
print("交换后x的值为：{}".format(x))
print("交换后y的值为：{}".format(y))
