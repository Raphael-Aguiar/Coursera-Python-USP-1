def maximo(x,y,z):
  if x > y and x > z:
    return x
  elif y > x and y > z:
    return y
  else:
    return z

'''
print(maximo(18,12,3))
print(maximo(-1,129,23))
print(maximo(-1,12,546))
'''