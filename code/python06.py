#在文件中加入哆啦A梦的人物名字
filte1 = open('name.txt','w')
filte1.write('野本大雄')
filte1.close()
filte2 =open ('name.txt','w')
filte2.write('野本大雄静香')
filte2.close()
filte3 = open('name.txt','w')
filte3.write('哆啦A梦，野本大雄，静香，胖虎，小夫')
filte3.close()
#读取文件内容
filte4 = open('name.txt')
print(filte4.read())
filte4.close()
filte5 = open('name.txt')
print(filte5.read())
filte5.close()
#加入人物名称
filte6 = open('name.txt','a')
filte6.write('小喵')
filte6.close()
#读出一行或依次读出
filte7 = open('name.txt')
for line in filte7.readlines():
    print(line)
    print('=====')
