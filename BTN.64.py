def tinhsotienphaitra(tongcong):
  """Tinh so tien phai thanh toan bang tien mat, lam tron den dong niken gan nhat."""

  pennies = round(tongcong * 100)
  conlai = pennies % 5

  if conlai < 2.5:
    tienmat = tongcong - conlai / 100
  else:
    tienmat = tongcong + (5 - conlai) / 100

  return tienmat


sogia = []
while True:
  gia = input("Nhap mot gia (hoac de trong de hoan thanh): ")
  if gia == "":
    break
  else:
    sogia.append(float(gia))

toanbochiphi = sum(sogia)
print("Toan bo chi phi: ", toanbochiphi)
tienmat = tinhsotienphaitra(toanbochiphi)
print("So tien den han thanh toan bang tien mat: ", tienmat)