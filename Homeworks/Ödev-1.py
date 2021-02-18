from random import shuffle 

a=[]

for k in range(2,100):
  for i in range(2,k):
      if (k % i) == 0:
          break
  else:
      a.append(k)

shuffle(a)


print(a[0:3])
print(a[3:6])
print(a[6:9])