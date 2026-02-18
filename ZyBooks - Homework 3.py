#My version
num_sec = int(input("Enter the number of seconds: "))
num_min = int(input("Enter the number of minutes: "))
num_hr = int(input("Enter the number of hours: "))
hr_sec = (num_hr % 60 * 60) * 60
min_sec = num_min * 60
time_sec = hr_sec + min_sec + num_sec
print("\nYour time in seconds: ", time_sec, "seconds")
