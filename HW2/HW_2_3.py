def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("високосный год")
    else:
        print("an usual year")

leap_year(2024)
leap_year(2004)
leap_year(1200)
leap_year(500)
