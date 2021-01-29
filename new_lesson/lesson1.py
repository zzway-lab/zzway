# # print("今天天气很好")
# # print("明天天气也不错")
# # print(type({"大":"1"}))
# print(str)
# #
# # print(isinstance(16,float))
# print('aaa' , end="~")#end=""不换行标志，""里面可以一种标志去进行分割
# print('bbb')
#
# # name = "老广"
# # gender ="neutral"
# # hobby = "basketball"
# #
# # print('''-----%s信息登记-----
# # name:%s
# # gender:%s
# # hobby:%s
# # '''%(name,name,gender,hobby))
#
# # strl1 ="alien of Mars"
# # # # print(strl1)
# # # # print(len(strl1))
# # # print(strl1[0:len(strl1):1])
# #
# # # print(strl1.count(l))
# # # print(strl1.index('o'))
# # # print(strl1.find('o'))
# # print(strl1.replace('Mars','Mercury'))
#
# # print(100 + 100)
#
# # word = "你"
# # print(str(100) + word))
#
# # formula = int(input("请输入号码"))
# # print(formula + 10)
# # formula = int(input("请输入数字"))
# # print(formula + 10)
#
# # print(100*"你好")
# # a =5
# # a = (a + 10)*80
# # print(a)
#
# # print(4>3)
# # print("登陆成功"=="登陆成功")
# #
# # print(4>5 and 5>1)
# # print(4>5 or 5>1)
# # print (not(4>5 or 5>1))
#
# # strl2 = 'pyhon'
# # print('p' in strl2)
# #
# # N = str(input("请输入姓名:"))
# # A = str(input("请输入年龄:"))
# # G = str(input("请输入性别:"))
# # print('''***********************
# # "姓名:%s"
# # "年龄:%s"
# # "性别:%s"
# # '''%(N,A,G))
# a = 98
# print("the rating is : %d%%"%(a))
# # '''
# # %s (string)
# # %f (floating)
# # %d (digit)
# # '''
#random随机
import random
from new_lesson import ui_automatic_data
# my_list =[]
# i= 0
# while i < 10:#while循环
#     random_number = random.randint(1,100)#随机抽取
#     my_list.append(random_number)
#     i += 1
# print(my_list)
# my_list.sort()#排序
# print(my_list)
# my_list.sort(reverse= True)#默认是false,为从小到大的升序，ture则是从大到小,注意大小写,此处reverse是形参
# print(my_list)
# my_list.reverse()#逆序，原来第一个变最后一个，原来最后一个变第一个
# #choice抽取
# random_number1 = random.choice(ui_automatic_data.data_list)#在一个列表随机取一个数
# print(random_number1)
# print(ui_automatic_data.data_list)
# a = list(range(5))
# print(a)
# str = 'python hello aaa 123123aabb'
# # one
# # print(str[0:7])
# # two
# # print('o a' in str)
# # print('he' in str)
# # print('ab' in str)
# #three
# # print(str.replace('python','lemon'))
# # four
# # print(str.find('aaa'))
#列表查找加扩展
# num = input("请输入数字")
# num = eval(num)
# my_list1 = [10,20,30]
# if num in my_list1:
#     search = my_list1.index(num)
#     print("该数字在列表为第%s位元素"%(search+1))
# else:
#     print("%s不在列表my_list1内"%(num))
#
#while循环的扩展 抽奖
# count = 0
# while count <= 4:
#     count += 1
#     num = input("请输入号码")
#     num = eval(num)
#     if num in ui_automatic_data.data_list:
#         print("恭喜你中奖了")
#         break
#     else:
#         if count <= 4:
#             print("请继续抽奖")
#         else:
#             print("本轮抽奖已结束，谢谢参与")

#split分割元素
# abc = "hello welcome to here"
# ccc = abc.split(" ")# 以每个元素的共同点为一个准则进行分开，常见的有,./和空格等（" "," ")第一个天准则第二个填分拆到哪个位置
# lista = list(ccc)
# print(lista)
# list1 = [1,10,80,"solitary",[1,2,3]]
# a = list(range(len(list1)))
# print(a)
# # # print(len(list1))
# print(list1[0:5:1])
# # 列表嵌套
# # print(list1[4][2])
# #增加元素
# list1.append("等")
# # print(list1)
# list1.insert(3,"一个字")
# print(list1)
# list1.extend(["自由","健康","财富"])
# print(list1)
# # 删除
# list1.pop()
# print(list1)
#指定元素的删除
# list1.pop(0)
# print(list1)
# #指定值元素删除
# list1.remove(10)
# print(list1)
# # list1.clear() 清除整张列表
# #修改重新赋值
# list1 [0] = "鸡翅"
# print(list1)
# list1 [1] = "鸡翅"
# print(list1)
# #元祖,和列表不同，其不可修改里面的元素
# tuple1 = ("鸡翅","火腿","筷子")
# print(tuple1)
# #一定要修改只能用list作为转换
# list2 = list(tuple1)
# print(list2)
# list2[1] = "泡面"
# print(list2)
# tuple2 = tuple(list2)
# print(tuple2)
# #dict {}
# dict1 = {"name":"jacky cheung","age":"60","gender":"male"}
# print(dict1["age"])
# print(dict1.get("age"))#得到的是value值
# print(dict1.keys()) #key取值不可以重复，不可以改变
# print(dict1.values())#value 可以改可以重复
# #字典替代
# dict1["hobby"] = "singing" # 无已存键值的，增加键值和对应元素
# print(dict1)
# # dict1["gender"] = "hi"     有键值的，更新元素
# print(dict1)
# #元祖删除
# # dict1.pop("hobby") #因为字典无顺序，则需要指定键值来进行删除
# # print(dict1)
# # print(len(dict1))
# #元祖增加多个
# dict1.update({"city":"hongkong","height":"175"})
# print(dict1)
#
# # #set 集合
# list3 = [10,22,33,58]
# set1 = set(list3)
# # list4 = list(set1)
# print(set1)
# #
# # if判断语法
# #
# # if
# #     子代码
# # elif
# #     子代码
# # elif
# #     子代码
# # else
#
# # money = int(input("请输入金额"))
# #
# # if money>200:
# #     print("首付")
# # elif money>100:
# #     print("买车")
# # elif money>50:
# #     print("买保险")
# # else:
# #     print("努力赚钱")
#
# # for 循环
# # count1 = 0
# # strl = "我只想平安健康加有钱" #循环由元素个数决定它的次数
# # for k in strl:
# #     print(k)
# #     print("*" * 25)
# #     count1 += 1
# #     print(len(strl))
# #     print(count1)
# #
# # list6 = ['notagia','esthetic','seductive','brace']
# # for word in list6:
# #      if word == 'seductive':
# #
# #          # break
# #          continue
# #      print(word)
# #
# #作业
# #1
# # i = input("请输入：")
# # list8 = ['1','2','6','summer']
# # a = list8
# # if "i" in a:
# #     print("存在")
# # else:
# #     print("不存在")
# # #2
# # input("请输入已到班级人数：")
# # dict_1 = {"class_id":"45","num":"20"}
# # c = int(dict_1.get("num"))
# # if c> 5:
# #     print('''
# #     "班级人数:%s"
# #     '''%(c))
# # else:
# #     print("由于人数少于20故不显示")
# #3 (1)
# list7 = ['肥兔','鹿鹿','freestyle','等','地球','阑珊','柠檬']
# dict2 = {"姓名":"肥兔","性别":"女","年龄":"18","城市":"深圳"}
# dict3 = {"姓名":"鹿鹿","性别":"男","年龄":"18","城市":"深圳"}
# dict4 = {"姓名":"freestyle","性别":"男","年龄":"18","城市":"深圳"}
# dict5 = {"姓名":"等","性别":"男","年龄":"18","城市":"深圳"}
# dict6 = {"姓名":"地球","性别":"男","年龄":"18","城市":"深圳"}
# dict7 = {"姓名":"阑珊","性别":"男","年龄":"18","城市":"深圳"}
# dict8 = {"姓名":"柠檬","性别":"男","年龄":"18","城市":"深圳"}
# list9 = [dict2,
#          dict3,
#          dict4,
#          dict5,
#          dict6,
#          dict7,
#          dict8]
# for q in list9:
#     print("*" * 65)
#     print(q)
# list7 = ['肥兔','鹿鹿','freestyle','等','地球','阑珊','柠檬']
# list6 = ['女','男','男','男','男','男','男']
# list5 = [18,18,18,18,18,18,18] # 数字不需要''号或者"号
# list4 = ['深圳','深圳','深圳','深圳','深圳','深圳','深圳']
# # list3 = list(range(len(list7)))
# list0 = []
# # range(len(list7))
# for i in range(len(list7)):
#     dict0 = dict(姓名 = list7[i],性别 = list6[i],年龄 = list5[i],城市 = list4[i])
#     list0.append(dict0)
# print(list0)


# # ['肥兔','鹿鹿','freestyle','等','地球','阑珊','柠檬']
# # t = (list7.get("姓名"))#得到的是value值
# # dict1["gender"] = "hi"     有键值的，更新元素
# list1 = ['肥兔','鹿鹿','freestyle','等','地球','阑珊','柠檬']
# list7 = [list1]
# for w in list7:
#     dict2 = dict(姓名 ="肥兔",性别 ="女",年龄 ="18",城市 ="深圳")
#     print(dict2)
#     print("*" * 65)
#     dict3 = dict(姓名="鹿鹿",性别="女",年龄="18",城市="深圳")
#     print(dict3)
#     print("*" * 65)
#     dict4 = dict(姓名="freestyle", 性别="女", 年龄="18", 城市="深圳")
#     print(dict4)
#     print("*" * 65)
#     dict5 = dict(姓名="等", 性别="男", 年龄="18", 城市="深圳")
#     print(dict5)
#     print("*" * 65)
#     dict6 = dict(姓名="地球", 性别="男", 年龄="18", 城市="深圳")
#     print(dict6)
#     print("*" * 65)
#     dict7 = dict(姓名="阑珊", 性别="男", 年龄="18", 城市="深圳")
#     print(dict7)
#     print("*" * 65)
#     dict8 = dict(姓名="柠檬", 性别="男", 年龄="18", 城市="深圳")
#     print(dict8)
#     print("*" * 65)
    # list11 =[1]
    # list11.append(dict2,dict3,dict4,dict5,dict6,dict7,dict8)
    # print(list11)
# print("666")
# def good_job(salary,bonus,subsidy = 500 ,*args,**kwargs):
#     # 定义函数------形参-----subsidy= 200(默认值的设定）----*args(不定长参数值,里面数值以元组形式显示）
#     # salary = 9000
#     # bonus  = 2000
#     # subsidy = 800
#     sum1 = (salary + bonus + subsidy)
#     for i in args:
#         sum1 += i
#     for l in kwargs:
#         sum1 += kwargs[l]
#     return sum1 #定义函数的返回值，标志着函数的结束，不会在后面再成功显示其他,如再print其他也已经无效
#     # 用到成员指令时一定要格式对齐，否则不能得到结果
#     # print('薪资总和:{}'.format(sum1))
# result = good_job(9000,2000,100,aa = 300,bb = 100) # 调用函数--------实参
# print(result)
# print('薪资总和:{}'.format(result))
# #good_job(salary=9000,bonus=2000,subsidy=600,300,100)------关键字传参,若已经在调取函数中定义，则调取函数
# #agrs不定长参数在形参和实参确定后再进行加入,
# #kwagrs代表不定长参数在形参和实参确定后再进行加入且以字典形式保存，收纳对调用函数里面已被定位的数值,for循环只能取到键值，
# # 所以需要提取value来进行使用

#z作业
# z = input("请输入数据:")

# def T(z):
# #     print(type(a))
# #     e = len(a)
# #     return e
# # result = T(a)
# # if result > 5:
# #     print("ture")
# # else:
# #     print("false")
#     if type(z) == str:
#         if len(z) >= 5:
#             print("ture")
#         else:
#             print("false")
#         print('''%s是字符串类型'''%(z))
#     elif type(z) == list:
#         if len(z) >= 5:
#             print("ture")
#         else:
#             print("false")
#         print('''%s是列表类型'''%(z))
#     elif type(z) == dict:
#         if len(z) >= 5:
#             print("ture")
#         else:
#             print("false")
#         print('''%s是字典类型'''%(z))
#     else:
#         print('''%s既不是字符类型，也不是列表类型，更不是字典类型，请重新输入'''%(z))
# T([1,2,3,4])
#     dd = len(z)
#     return dd
# result = T(z)
# if result >= 5:
#     print("ture")
# else:
#     print("false")

#
# if type(a) == str:
#     print("你成功了")
#
# else:
#     print("非str")
#
#

#
# a = int(input("请输入数字："))
# #方式一
# # b = list(range(a + 1))
# # sum1 = sum(b)
# # print(b)
# # print(sum1)
# #方式二
# # b = []
# # for i in range(1,a+1):
# #     b.append(i)
# #     d = sum(b)
# #     print(d)
#
# # 方法三(1)
# def sum1(a):
#     sumx = sum(list(range(a+1)))
#     # print(sumx)
# # (2)
# #     return sumx
# # result = sum1(a)
#     print("这个数的整数求和等于：%s"%(sumx))
# sum1(a)
# import requests
# requests.post()
import jsonpath
#面试题
# a =[3,5,7,9]
# b =[5,3,7,6]
# c =[]
# d =[]
# for i in a:
#     if i in b:
#         c.append(i)
#     else:
#         d.append(i)
# print(c)
# print(d)
#随机抽取和放入

teacher_list =[]
for i in list(range(8)):
    teacher_name = ("老师") + str(i+1)
    teacher_list.append(teacher_name)
print(teacher_list)



class_list = [[],[],[]]
for teacher in teacher_list:
    index = random.randint(0,len(class_list)-1)
    class_list[index].append(teacher)
print(class_list)

j = 0
for class1 in class_list:
    print("第%s间教室一共有%s个老师"%(j,(len(class1))))
    j= j+1
    for name in class1:
        print("分别是%s"%(name))
    print("-"*105)





