def interest(prin,rate = 10, time = 2):
    si = (prin * rate * time)/100
    return si


prn = float(input("Enter the Principal Amount : "))
rate = float(input("Enter the Rate of Interest : "))
time = float(input("Enter the Time Period (in yrs) : "))


inter = interest(prn,rate,time)
print("Simple Interest : ",inter)
