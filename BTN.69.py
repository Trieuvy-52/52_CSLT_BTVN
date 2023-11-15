def sopixapxi(n):
  """tinh gia tri gan dung cua pi bang cach su dung n so hang cua chuoi vo han."""

  pi = 3
  for i in range(1, n + 1):
    pi += 4 / (2 * i * (2 * i + 1) * (2 * i + 2))
  return pi
for i in range(1, 16):
  print("pi xap xi voi {} dieu kien: {}".format(i, sopixapxi(i)))