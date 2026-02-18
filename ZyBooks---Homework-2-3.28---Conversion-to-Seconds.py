num_sec = int(input("Enter the number of seconds: "))
sec_hr = num_sec / 3600
sec_min = (num_sec - 3600) / 60
sec_sec = num_sec - sec_min
print("Seconds:", int(sec_sec), "\nMinutes:", int(sec_min), "\nHours:", int(sec_hr))
