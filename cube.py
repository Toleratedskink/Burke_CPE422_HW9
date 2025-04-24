# Problem 3 of Homework 8

def cb(x):
  cube = x**3
  print(cube)

for i in range(20):
  if (i % 2) == 0:
    print(i)
  else:
    cb(i)
