import datetime as dt
import pytz

# dates
print(dt.date(2016,7,24))  # prints(year,month,date) as year-month-date

print(dt.date.today())  # prints today's date we can also use this to just print year, date, month or weekday
# for instance
print(dt.date.today().month)
print(dt.date.today().weekday()) # weekday is (0-6) and isoweekday is (1-7)

tdelta=dt.timedelta(days=10) # used to make difference between two dates
print(dt.date.today()+tdelta)

# timedelta = date1 +or- date2
bd=dt.date(2018,10,2) # bd is my birthday
# days and time left in my birthday
print(bd-dt.date.today())  # to print the difference between the two dates 
print((bd-dt.date.today()).days)  # prints the days only and not time
print((bd-dt.date.today()).total_seconds()) # prints the seconds



# now time

t=dt.time(9,30,45,100000) # (hrs,min,sec,microseconds)
print(t)
print(t.hour)



# now both time and date

k=dt.datetime(2018,7,26,12,30,45,100000) # (yr,mon,date,hr,min,sec,microsecs)
print(k)
print(k.month) # only the month
print(k.date()) # only the date

ttdelta=dt.timedelta(hours=10)
print(k+ttdelta)

tod=dt.datetime.today() # current local datetime with timezone none
tod_now=dt.datetime.now() # option of passing a timezone
tod_utcnow=dt.datetime.utcnow() # current utc time but not timezone aware

print(tod) 
print(tod_now)
print(tod_utcnow)

dtim=dt.datetime(2018,4,18,10,30,45,100000,tzinfo=pytz.UTC)
print(dtim)

a=dt.datetime.now(tz=pytz.UTC)  # current time with time zone but not local time
print(a) 
print(dt.datetime.utcnow().replace(tzinfo=pytz.UTC)) # current time with timezone


# all timezones
for t in pytz.all_timezones:
	print(t)

datloc=a.astimezone(pytz.timezone('Asia/Calcutta'))
print(datloc)        #prints the local time with timezone

#converting a naive datetime to an aware one

dt_cal=dt.datetime.now()    # naive timezone
print(dt_cal)
cal=pytz.timezone('Asia/Calcutta')
dt_cal=cal.localize(dt_cal)
print(dt_cal)

dt_east=dt_cal.astimezone(pytz.timezone('US/Eastern')) # from calcutta to US
print(dt_east)

dti=dt.datetime.now(tz=pytz.timezone('Asia/Calcutta'))
print(dti.isoformat())    

print(dti.strftime('%B %d,%Y %z'))  # B=month, d=2 digit date, Y=year e.g=July 26, 2018

# converting a string in to datetime format 
dt_str='June 26,2017'
dts=dt.datetime.strptime(dt_str,'%B %d,%Y')
print(dts)



