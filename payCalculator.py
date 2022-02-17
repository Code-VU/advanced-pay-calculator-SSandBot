# This first line is provided for you
hrs = input("Enter Hours:")
rate = input("Enter rate:")
Salary = float(hrs)*float(rate)
if hrs >= 40:
    print("Pay:",Salary)
if hrs < 40:
    Overtime = float(hrs-40)*1.5
print("Pay:",Overtime)
  
# end assignment
## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay 