print("hello wangyun!")
#!/usr/bin/python
# -*- coding: UTP-8 -*-
print("你好，王云！")


print('hello');print('wangyun')

one=1
two=2
total=one + \
    two
print(total)

days=['monday','tuesday','wedensday',
      'thursday','friday']
print(days)

word='word'
sentense="这是一个句子"
paragrath="""这是一个段落
包含了多个句子"""
print(word)
print(sentense)
print(paragrath)
#注释
'''
这是多行注释
多行注释
多行注释
'''

"""
多行注释
多行注释
多行注释
"""

x="a"
y="b"
print (x)
print (y)


print (x,y)


counter=100
mile=1000.34
name="wangyun"
print (counter)
print (mile)
print (name)


a=b=c=1
print (a,b,c)

a,b,c=1,2,"wangyun"
print (a,b,c)



s="wangyun"
print (s[1:])

print (s)
print (s[0])
print (s[2:5])
print (s[2:])
print (s*2)
print (s+"good")



list=['wangyun',222,33,'jon',32]
tinylist=[123,45]
print (list)
print (list[0])
print (list[1:3])
print (list[2:])
print (tinylist*2)
print (list+tinylist)



dict ={}
dict['one']="this is one"
dict[2]="this is two"
tinydict={'name':'john','code':423,'dept':'sales'}

print (dict['one'])
print (dict[2])
print (tinydict)
print (tinydict.keys())
print (tinydict.values())




a=34
b=2
c=12

if a==b:
    print ("1--a等于b")
else:
    print ("1--a不等于b")



count=0
while (count<9):
    print ("this count is:",count)
    count=count +1
print ('goodbye')


for letter in 'wangyun':
    print ('当前字母:',letter)


fruit=['banana','apple','mango']
for index in range(len(fruit)):
    print ('当前水果:',fruit[index])

import time;
ticks=time.time()
print ("当前的时间戳为：",ticks)

localtime=time.localtime(time.time())
print ("本地时间为：",localtime)

dangditime=time.asctime(time.localtime(time.time()))
print ("本地时间为：",dangditime)


import calendar
cal=calendar.month(2018,1)
print ("输出2018年1月份的日历：",cal)

shijian=time.clock()
print (shijian)

list=[1996,1998,1999,2000,2012,2014,2016,2018]
for number in list:
    if (calendar.isleap(number)):
        print (number,"是闰年")
    else:
        print (number,"不是闰年")


runnian=calendar.leapdays(1996,2018)
print ("1996-2018年之间的闰年年份有:",runnian)


def printme(str):
    "打印任何传入的字符串"
    print (str);
    return;

printme("我要调用用户自定义的函数！")
printme("再次调用同一个函数")


def changeint(a):
    a=10

b=2
changeint(b)
print (b)


def changeme(mylist):
    "修改传入的列表"
    mylist.append([1,2,3,4])
    print ("函数内取值：",mylist)
    return

mylist=[12,13,23]
changeme(mylist)
print ("函数外取值:",mylist)

def sum(arg1,arg2):
    "返回两个参数的和"
    total=arg1+arg2
    print ("函数内：",total)
    return total

total=sum(10,20)





wy=input("请输入：")
print ("你输入的内容是：",wy)

fo=open("foo.txt","w")
print (fo.name)
print (fo.closed)
print (fo.mode)

fo=open("foo.txt","w")

fo.write("王云是一个\n非常积极乐观的人！\n")

fo.close()

fo=open("foo.txt","r+")

str=fo.read(10)
print ("读取的字符串是:",str)

position=fo.tell()
print ("当前文件的位置为：",position)
fo.close()


import os
os.rename("foo.txt","wy.txt")



class Employee:
    '所有员工的基类'
    empCount=0

    def __init__(self, name, salary):
        """

        :type salary: object
        """
        self.name=name
        self.salary=salary
        Employee.empCount+=1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name:",self.name,"Salary:",self.salary)




emp1=Employee("zara",2000)
emp2=Employee("manni",5000)




emp1.displayEmployee()
emp2.displayEmployee()

print("Total Employee %d" % Employee.empCount)

print("----------------------------------------------")

class Parent:
    parentAttr=100
    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print("调用父类方法")

    def setAttr(self ,attr):
        Parent.parentAttr=attr

    def getAttr(self):
        print("父类属性：",Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("调用子类的构造函数")

    def childMethod(self):
        print("调用子类的方法")

c=Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

print("---------------------------------------------")

import re
print(re.match('www','www.runoob.com').span())
print(re.match('com','www.runoob.com'))


line="cat are smarter than dogs"
matchobj=re.match(r'(.*) are (.*?) .*',line,re.M|re.I)

if matchobj:
    print("matchobj.group():",matchobj.group())
    print("matchobj.group(1)",matchobj.group(1))
    print("matchobj.group(2)",matchobj.group(2))

else:
    print("No match!!!")

print("----------------------------------------")

print(re.search('www','www.runoob.com').span())
print(re.search('com','www.runoob.com').span())


print("----------------------------------------------")

line = "Cats are smarter than dogs";

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print("search --> matchObj.group() : ", matchObj.group())

else:
    print("No match!!")



print("-----------------------------------------")

phone="150-7609-6297 #这是一个河北的电话号码"
num=re.sub(r'#.*$',"",phone)
print("电话号码是：",num)

num=re.sub(r'\D',"",phone)
print("电话号码是：",num)



print("---------------------------------------")

pattern=re.compile(r'\d+')
result1=pattern.findall('runoob 123 google 456')
result2=pattern.findall('runoob123google456',0,10)

print(result1)
print(result2)


print("--------------------------------------------")

it=re.finditer(r'\d+',"123a32bc45ddd22224e")
for match in it:
    print(match.group())

print ("------------------------------------")







