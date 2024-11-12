def Fmax(a, b, c):
  a = int(input("Введи число: "))
  
  if a > 0:
    z = max(a, b, c)
    return z;
  else:
    return -1;
    
res = Fmax (4, 9)
print ("Результат: ", res)
