from datetime import date
d1 = input().strip()
d2 = input().strip()

y1,m1,day1 =map(int,d1.split('-'))
y2,m2,day2 =map(int, d2.split('-'))
date1 = date(y1,m1,day1)
date2 = date(y2,m2,day2)
diff = date2 - date1
print(diff.days)