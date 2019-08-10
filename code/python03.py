a_list=["abc","12"]
a_list.append("x")
#在列表中加x
print(a_list)
a_list.remove("12")
#在列表中加12
print(a_list)
a_list.append("15")
#在列表中加15
print(a_list)
a_list.remove("abc")

x = 'abcd'
if x== 'abc' :
    print('x的值和abc相等')
else :
    print('x的值和abc不相等')




c_z = ('猴鸡狗猪鼠牛虎兔龙蛇马羊')
year = int(input('请用户输入年份'))
print (c_z[year%12])
if(c_z[year%12]) == '狗' :
    print('狗年运势。。。')
for ax in c_z :
    print(ax)
for ac in c_z :
    print(ac)
for year in range (2000,2018):
    print ('%s 年的生肖是 %s ' %(year,c_z [year%12]))
for year in range (1998,2019):
    print('%s 年的生肖是 %s'%(year,c_z[year%12]))
    



while True :
    print('a')
    break
num=5
while True:
    print ('a')
    num =num + 1
    if num == 10 :
        break
    print(num)
num = 0
while num <10 :
    print ('a')
    num = num +1
    if num==4:
        continue
    print(num)


