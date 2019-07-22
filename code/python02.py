a= (1,2,3,4,5,6,7)
b= 4
filter (lambda x: x<b , a)
#取出a中小于4的元素
print(list(filter(lambda x : x<b ,a)))
#取出a中小于4的元素
z_n=(u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',u'巨蟹座')
z_ds=((1,28),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23))
(m,d)=(2,22)
print(list(filter(lambda x : x<=(m,d),z_ds)))
#取出星座日期中小于等于2.22的日期
zodac_len=len(list(z_ds))%7
print (z_n[zodac_len])
(m,d2)=(5,3)
print(list(filter(lambda x: x<=(m,d2),z_ds)))
#取出z_ds中小于等于5.3的日期
zodac_len=len(list(z_ds))%7
print (z_n[zodac_len])