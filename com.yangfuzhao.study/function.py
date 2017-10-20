# def area(width, height):
#     return width * height
#
#
# def print_welcome(name):
#     print("Welcome", name)
#
# w ,h = 6,'da'
# print("width =", w, " height =", h, " area =", area(w, h))


# 可写函数说明
# def printinfo(sex,age,name='e'):
#     "打印任何传入的字符串"
#     print("名字: ", name);
#     print("年龄: ", age);
#     print("性别: ", sex);
#     return;
#
#
# # 调用printinfo函数
# printinfo(1,1);
# print("------------------------")
# printinfo("runoob");


# questions = ['name', 'quest', 'favorite color',1]
# answers = ['lancelot', 'the holy grail', 'blue',1]
# for q, a in zip(questions, answers):
#     print('What is your {0}?  It is {1}.'.format(q, a))


if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')