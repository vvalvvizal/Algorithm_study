month = {'January' : 31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}
mon, da, year, time = map(str, input().split())
hour, minute = map(int, time.split(':'))

day = ''
for d in da:
    if d==',':
        continue
    else:
        day+=d

#윤년체크 
day = int(day)
year = int(year)

if year % 400==0 or (year%4==0 and year%100!=0):
    month['February'] = 29

today = -1

for m in month:
    if m == mon:
        today += day
        break
    else:
        today += month[m]


allminutes = 365 * 24 * 60
if month['February'] == 29:
    allminutes += 24 * 60  # 윤년이면 1일 추가

    
todayminutes = today * 24 * 60 + hour * 60 + minute
print((todayminutes/allminutes) * 100 )