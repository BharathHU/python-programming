def isleapyearornot(year):
    return (( year%100!=0 and year%4==0) or year%400==0)
sr=int(input("Enter the year:"))
er=int(input("Enter the year:"))
if sr>er:
    print("Invalid input")
else:
    print("leap year's")
    for i in range(sr,er+1):
        flag=isleapyearornot(i)
        if flag:
            print(i,end=" ")
    print("\n Non-leap year's")
    for i in range(sr,er+1):
        flag=isleapyearornot(i)
        if not flag:
            print(i,end=" ")