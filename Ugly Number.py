def ugly(n,div):
    while(n%div==0):
        n = n//div
    return n

n=int(input("enter a number:"))
n=ugly(n,2)
n=ugly(n,3)
n=ugly(n,5)

if(n==1):
    print(n ,"is an ugly number")
else:
    print(n ,"is not an ugly number")