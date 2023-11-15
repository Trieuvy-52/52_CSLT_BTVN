def thaydoinhietdo(C):
  """Chuyen doi nhiet do tu do C sang do F."""
  F = (C * 9/5) + 32
  return F
doC = range(0, 101, 10)
doF = [thaydoinhietdo(do) for do in doC]
print("C\tF")
print("-\t-")
for i in range(len(doC)):
  print(f"{doC[i]}\t{doF[i]}")
