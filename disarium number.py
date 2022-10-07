Number=int(input("enter the number to check disarium number="))
length=len(str(Number))
temp=Number
sum=0
rem=0
while temp>0:
    rem=temp%10
    sum=sum+int(rem**length)
    temp=temp//10
    length=length-1
if sum==Number:
    print(Number,"is a disarium number")
else:
    print(Number,"is not a disarium number")
