Name = ("Name: Prabukumar")
print(Name)
Roll = ("Roll Number: IITP_AIMLTN_2602728")
print(Roll)
Assign = ("Assignment: Python Loops & Automation - Subjective Question")
print(Assign)


print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

# Initialize max and min with first value
highest = temperatures[0]
lowest = temperatures[0]

for temp in temperatures:
    if temp > highest:
        highest = temp
    if temp < lowest:
        lowest = temp

print(f"Highest Temperature: {highest}°C")
print(f"Lowest Temperature: {lowest}°C")


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

hot_days = 0

for temp in temperatures:
    if temp <= 30:
        continue
    hot_days += 1

print(f"Hot Days (>30°C): {hot_days}")


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

hot_days = 0
day = 0

for temp in temperatures:
    day += 1
    
    if temp >= 40:
        print(f"Hot Days before alert: {hot_days}")
        print(f"Alert! Extreme temperature {temp}°C detected on Day {day}")
        break
    
    if temp > 30:
        hot_days += 1