def loaidiemdatduoc(loai):
  """Tra ve diem chu cai da cho."""
  if loai == "A":
    return 4.0
  elif loai == "A-":
    return 3.7
  elif loai == "B+":
    return 3.3
  elif loai == "B":
    return 3.0
  elif loai == "B-":
    return 2.7
  elif loai == "C+":
    return 2.3
  elif loai == "C":
    return 2.0
  elif loai == "C-":
    return 1.7
  elif loai == "D+":
    return 1.3
  elif loai == "D":
    return 1.0
  elif loai == "D-":
    return 0.7
  else:
    return 0.0
cacloai = []
while True:
  loai = input("Nhap loai diem chu cai: ")
  if loai == "":
    break
  else:
    cacloai.append(loai)
gpa = sum([loaidiemdatduoc(loai) for loai in cacloai]) / len(cacloai)
print("Diem trung binh cua lop la: ", gpa)