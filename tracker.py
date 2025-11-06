#Name: Samarth Sharma
#Class: B.tech CSE 1st Year (AI ML) Section A
#Roll No: 2501730279
#Date: 06/11/2025
#Daily Calorie Tracker Application

import datetime
print("Welcome to the Daily Calorie Tracker Application! \n" \
"This application helps you track your daily calorie intake and expenditure.\n")
res=int(input("How many meals they would like to log today? "))#number of meals
lst=[]
cal_lst=[]
ct=0
for i in range(res):
    Meal_nm=input("Enter the meal name (e.g., Breakfast, Lunch, Dinner, Snack): ")
    Cal_amt=float(input(f"Enter the calories consumed for {Meal_nm} in kcal: "))
    lst.append((Meal_nm, Cal_amt))#storing meal name and calorie amount as tuple in list
for j in lst:
    cal_lst.append(j[1])
    ct=ct+1
total_calories=sum(cal_lst)  #total calories consumed
avg_calories=total_calories/ct  #average calories per meal
daily_cal=float(input("Enter your daily calorie goal: "))
#comparing total calories with daily calorie goal
if total_calories>daily_cal:
    print(f"Warning: You have exceeded your daily calorie goal by {total_calories - daily_cal} kcal.")
elif total_calories<daily_cal:
    print(f"Good job! You are within your daily calorie goal. You have {daily_cal - total_calories} kcal remaining.")
else:
    print("Great! You have met your daily calorie goal exactly.")
#displaying summary of meals
print("\nSummary of your meals today:\n" 
"Meal Name\tCalories (kcal)\n" 
"-------------------------------")
for meal in lst:
    print(f"{meal[0]}\t{meal[1]}")
print(f"\nTotal:\t {total_calories} kcal")#total calories consumed displayed
print(f"\nAverage:\t {avg_calories} kcal")#average calories per meal displayed
print("\nThank you for using the Daily Calorie Tracker Application! Stay healthy!")
resp=input("Would you like to save your meal data? \n"
"Enter 'yes' to save or 'no' to exit: ").lower()
if resp=="yes":
    f=open("calorie_log.txt","w")#opening file in write mode to save data
    f.write("Meal Name\tCalories (kcal)\n")
    f.write("-------------------------------\n")
    for meal in lst:
        f.write(f"{meal[0]}\t\t{meal[1]}\n")
    f.write(f"\nTotal Calories Consumed:\t {total_calories} kcal\n")
    f.write(f"\nAverage Calories per Meal:\t {avg_calories} kcal\n")
    f.write(f"\nLog Date and Time: {datetime.datetime.now()}\n")
    f.close()
    print("Your meal data has been saved to 'calorie_log.txt'.")