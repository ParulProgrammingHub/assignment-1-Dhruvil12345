principle=int(input("ENTER THE PRINCIPLE AMOUNT:"))
rate=int(input("ENTER THE RATE:"))
time=int(input("ENTER THE TIME:"))
def simple_interest(principle,time,rate):
    A=principle*(1+rate*time)
    print ("TOTAL SIMPLE INTEREST:",A)
simple_interest(principle,time,rate)
