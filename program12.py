principle=int(input("ENTER THE PRINCIPLE AMOUNT:"))
rate=float(input("ENTER THE RATE:"))
time=int(input("ENTER THE TIME:"))
n=int(input("ENTER THE N :"))
def compound_interest(principle,time,rate,n):
    r=(rate/100)
    A=principle*(1+r/n)**(n*time)
    print ("TOTAL SIMPLE INTEREST:",A)
compound_interest(principle,time,rate,n)
