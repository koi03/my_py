dict1={}
print (type(dict1))

dict2={'x ':1 ,'y' : 2}
dict2['z'] = 3
#把z=3加入dict2里
print(dict2)

dict3={'q':3 , 'd': 4}
dict3['f']= 5 
print(dict3)

dict4={'e': 5 , 'f' : 4}
dict4['g'] = 7
print(dict4)

z_n=(u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',u'巨蟹座')
z_ds=(1,28),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23)

cz_num = {}
for i in z_n :
    cz_num [i] = 0
cz_num = {}
for i in z_ds :
    cz_num [i] = 0

while True :
    int_days = int(input('请用户输入日期:'))
    int_month = int(input ('请用户输入月份:'))
    int_year = int (input('请用户输入年份'))
    n = 0
    while z_ds[n] < (int_month,int_days):
        if int_month ==7 and int_days > 23:
            n =+1
            print(z_n[zd_num],z_da[zd_num])
    #输入生肖和星座
    print('%s 年的生肖是 %s'(yesr,z_n[year % 12]))

cz_num[c_z[year % 12]]+=1
z_num[z_n[n]]+=1
#输出生肖和星座的统计信息

for each_key in cz_num.keys() :
    print('生肖%s有%d个'%(each_key,cz_num[each_key]))
for each_key in z_num.key():
    print('星座%s有%d个'%(each_key, cz_num[each_key]))








    








