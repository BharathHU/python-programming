def nthfibo(pos):
    if pos<=1:
        return pos
    return nthfibo(pos-1)+nthfibo(pos-2)
pos=int(input("Enter the value of position:"))
res=nthfibo(pos)
print(f"The ele present at pos:{pos} is:{res}")