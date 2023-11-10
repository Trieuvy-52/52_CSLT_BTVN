n=int(input("Nhap tuoi cho theo nam cua con nguoi: "))
tuoicho=n

if n<0:
    print("So tuoi con nguoi khong am")
if n<=2:
    i=n*10.5
    
else:
    i=21+(n-2)*4
print("So tuoi cho theo nam cua cho la:",i)
    