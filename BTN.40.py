a=float(input("Nhap do dai a: "))
b=float(input("Nhap do dai b: "))
c=float(input("Nhap do dai c: "))
if a==b and b==c:
    print("Tam giac deu")
elif a==b or a==c or b==c:
    print("Tam giac can")
else:
    print("Tam giac thuong")
