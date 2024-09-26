"""
Name: Ali Shirazi Zamani
Level: 2
Homework: 3
Exercise: 4
To do: Read Gregorian birth date of user and calculate
- Number of seconds he has been alive
- Number of days and minutes elft untill next birthday and congratulate
- Using jdatetime package convert birth date to jalai calender.
"""
import datetime
import jdatetime

birth_date = input("Enter your birth date in the format year-month-day: ")
birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")
time_now = datetime.datetime.now()
total_time_alive = time_now - birth_date
print(f"Total seconds you have lived: {total_time_alive.total_seconds()}")

# If birthday has not happened yet in current year
if birth_date.month > time_now.month or (birth_date.month == time_now.month and birth_date.day > time_now.day):
    date_str = str(time_now.year) + '-' + str(birth_date.month) + '-' + str(birth_date.day)
    upcoming_birth_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    day_count = (upcoming_birth_date - time_now).days
    minute_count = (upcoming_birth_date - time_now).seconds / 60
    print(f"Congratulations! there are {day_count} days and {minute_count} minutes untill your next birth day!")
# If today is the birthday    
elif birth_date.month == time_now.month and birth_date.day == time_now.day:
    print("Congratulations! Today is your birthday!")
# If birthday has already happened this year, so next birthday is next year    
else:
    date_str = str(time_now.year + 1) + '-' + str(birth_date.month) + '-' + str(birth_date.day)
    upcoming_birth_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    day_count = (upcoming_birth_date - time_now).days
    minute_count = (upcoming_birth_date - time_now).seconds / 60
    print(f"Congratulations! there are {day_count} days and {minute_count} minutes untill your next birth day!")    

birth_date_jalai = jdatetime.GregorianToJalali(birth_date.year, birth_date.month, birth_date.day)
print(f"Birth date in jalai calendar is: {birth_date_jalai.jyear}-{birth_date_jalai.jmonth}-{birth_date_jalai.jday}")