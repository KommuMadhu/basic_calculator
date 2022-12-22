
print('__________PYTHON CALUCLATOR_________')

while True:
  print("Calculator")   
  print("1.Add")
  print("2.Multiply")
  print("3.Divide")

  c=int(input('select above ='))

  if c==1:
    a=int(input('+'))
    b=int(input(''))
    c=a+b
    print('Total=',c)

  elif c==2:
    a=int(input('*'))
    b=int(input(''))
    c=a*b
    print('Total=',c)

  elif c==3:
    a=int(input('/'))
    b=int(input(''))
    c=a/b
    print('Total=',c)

  Another_try = input("Again Calculation ?(Yes/No) | ")
  if Another_try == "N" or Another_try == "n":
        break
  elif Another_try == "Y" or Another_try == "y":
      continue
else :
        print('invalid')

