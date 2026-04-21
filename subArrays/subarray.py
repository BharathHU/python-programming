# An array formed by including the continuous sequence of ele's from a major array.
# eg: arr=[1,3,10,14]
         #  0 1 2  3
# i=0
# [1],[1,3],[1,3,10],[1,3,10,14]
# i=1
# [3],[3,10],[3,10,14]
# i=2
# [10],[10,14]
# i=3
# [14]
def createIntArr():
    print("Enter the array elements:")
    l1=[]
    while True:
        try:
            n=int(input("Enter the array:"))
            l1.append(n)
        except Exception as e:
            return l1
        
def displaySubArr(arr):
    for i in range(0,len(arr)):
        res=[]
        for j in range(i,len(arr)):
            res.append(arr[j])
            print(res)     
arr=createIntArr()
print("The original array:",arr)
displaySubArr(arr)

