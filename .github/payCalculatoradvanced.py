def paycalculatoradvanced()

# This first line is provided for you
hrs = input("Please input your hours:")
rate = input("Enter your rate:")
Salary = float(hrs)*float(rate)
if float(hrs) <=40:
    print ("Reg Time:",Salary)
elif float(hrs) >40:
    print ("Full Pay:",(float(hrs)-40) * (float(rate) * 1.5))
# end assignment
## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay 
