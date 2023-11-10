n=int(input("Nhap so canh: "))
if n<3:
    print("Mot hinh phai co it nhat 3 canh.")
elif n>10:
    print("Mot hinh khong the co hon 10 canh.")
else:
    loaihinh=["tam giac","tu giac","ngu giac","luc giac","that giac","bat giac","cuu giac","thap giac"]
    hinh=loaihinh[n-3]
    print("Hinh dang",n,"canh goi a", hinh+".")