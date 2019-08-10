z_n=(u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',u'巨蟹座')
z_ds=(1,28),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23)
int_month = int(input ('请用户输入月份:'))
int_days = int(input('请用户输入日期:'))
#请用户输入月份和日期
for  zd_num in range(len(z_ds)):
    if z_ds[zd_num]>=(int_month,int_days):
        print(z_n[zd_num],z_ds[zd_num])
        break
    elif int_month == 7 and int_days > 23:
        print(z_n[0])
        break
n = 0
while z_ds[n] < (int_month,int_days):
if int_month ==7 and int_days > 23:
n =+1
print(z_n[zd_num],z_da[zd_num])

