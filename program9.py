s1=float(input("SUBJECT 1 ="))
s2=float(input("SUBJECT 2 ="))
s3=float(input("SUBJECT 3 ="))
s4=float(input("SUBJECT 4 ="))
s5=float(input("SUBJECT 5 ="))
avg=s1+s2+s3+s4+s5
mean=avg/5
per=(avg*100)/500
print("TOTAL = ",avg)
print("MEAN = ",mean)
print("PERCENTAGE = ",per,"%")
if (per<=35):
    print ("RESULT : FAIL")
else :
    print ("RESULT = PASS")
