n=int(input("Nhap mot muc am thanh theo db: "))
i={"bua khoan": 130,"may cat co": 106,"dong ho bao thuc": 70,"phong yen ang": 40}
if n<40:
    print("Muc do am thanh la thap hon phong yen ang")
elif n<70:
    print("Muc do am thanh la muc giua phong yen ang va dong ho bao thuc")
elif n<106:
    print("Muc do am thanh la muc giua dong ho bao thuc va may cat co")
elif n<=130:
    print("Muc do am thanh la bua khoan")
else:
    print("Muc do am thanh la cao hon bua khoan")  