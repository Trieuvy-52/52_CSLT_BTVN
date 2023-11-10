n=input("Nhap ten thang: ")
if n in ["thang 1","thang 3","thang 5","thang 7","thang 8","thang 10","thang 12"]:
    print(n,"co 31 ngay")
elif n in ["thang 4","thang 6","thang 9","thang 11"]:
    print(n,"co 30 ngay")
elif n=="thang 2":
    print(n, "co 28 hoac 29 ngay")
else:
    print("thang",n,"khong ton tai")