n=float(input("Nhap mot gia tri: "))
if n==0:
    print("Sai: Gia tri dau tien khong the la 0")
    exit(1)
trungbinhcuagiatri= n
sogiatri=1
m=float(input("Nhap gia tri khac(0 la dung): "))
while m==0:
    
    trungbinhcuagiatri+=m
    sogiatri+=1
S=trungbinhcuagiatri/sogiatri
print("Trung binh la: ", S)

    
    
    