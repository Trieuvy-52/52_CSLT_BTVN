def tinhchiphinhapvao(tuoi):
  """Tinh chi phi nhap hoc cho mot khach o do tuoi nhat do."""

  if tuoi <= 2:
    return 0.0
  elif 3 <= tuoi <= 12:
    return 14.0
  elif tuoi >= 65:
    return 18.0
  else:
    return 23.0
sotuoi = []
while True:
  tuoi =(input("Nhap tuoi cua mot khach: "))
  if tuoi == "":
    break
  else:
    sotuoi.append(float(tuoi))
tinhchiphinhapvao = sum([float(tinhchiphinhapvao(tuoi)) for tuoi in sotuoi])
print("Tong chi phi nhap hoc cho mot nhom la ${:.2f}.".format(tinhchiphinhapvao))