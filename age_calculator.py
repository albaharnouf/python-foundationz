from datetime import datetime 

def check_birthdate(year, month, day):
    today = datetime(2020, 1, 26)
    birthday = datetime(int(year), int(month), int(day))
    if today > birthday:
        return True
    return False


def calculate_age(year, month, day):
    today = datetime(2020, 1, 26)
    birthday = datetime(int(year), int(month), int(day))
    difference = today - birthday
    diffrence_in_years = int(difference.days / 365)
    print("You are %d years old" %(diffrence_in_years))


year = input("Enter year of birth")
month = input("Enter month of birth")
day = input("Enter day of birth")

if check_birthdate(year,month,day) ==True:
    calculate_age(year,month,day)
else:
    print("Birthdate is invalid")
