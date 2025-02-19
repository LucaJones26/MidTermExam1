def days_since_birthday(birthday):

    birth_year = int(birthday[-4:])

    current_year = int(input("Enter the current year (YYYY): "))

    full_years_passed = current_year - birth_year - 1 #exlcuding birth and current year


    total_days = full_years_passed * 365  # convert years to days and leap years are ignored

    return total_days

print(days_since_birthday("26-02-2005"))