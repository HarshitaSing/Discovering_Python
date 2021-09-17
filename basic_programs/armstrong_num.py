sum = 0
for i in str(num): # num = given integer
    sum += int(i) ** 3
if sum != num:
    print ("Not Armstrong !")
else:
  print ("Armstrong")
