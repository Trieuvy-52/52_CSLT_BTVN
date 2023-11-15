giagoc = [4.95, 9.95, 14.95, 19.95, 24.95]
sotienchietkhau = []
giamoi = []
for gia in giagoc:
  tienchietkhau = gia * 0.6
  giamoi.append(gia - tienchietkhau)
  sotienchietkhau.append(tienchietkhau)

print("Gia goc | So tien chiet khau | Gia moi")
print("------- | ------------------ | -------")
for i in range(len(giagoc)):
  print(f"{giagoc[i]} | {sotienchietkhau[i]} | {giamoi[i]}")