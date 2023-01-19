#1
for i in range(5):
    print(i+1, ' 0000000000')
    i+=1

#2
c=0
for i in range(10):
    s=int(input('Enter 10 the numbers: '))
    if s == 5:
        c+=1
print(c)

#3
sum = 0
for i in range(1,101):
    sum+=i
print(sum)

#4
prod = 1
for i in range(1,11):
    prod = prod*i
print(prod)

#5
integer_number = 2129
print(integer_number%10,integer_number//10)
while integer_number>0:
     print(integer_number%10)
     integer_number = integer_number//10

#6
integer_number = int(input('Enter the number: '))
suma = 0
while integer_number > 0:
    suma = suma + integer_number % 10
    integer_number //= 10
print('Suma =', suma)

#7
integer_number = int(input('Enter the number: '))
prod = 1
while integer_number > 0:
    prod *= integer_number % 10
    integer_number = integer_number//10
print('Prod =', prod)

#8
integer_number = int(input('Enter the number: '))
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

#-----
#a = 1234 #int(input('enter- '))
#m = a%10
#a = a//10
#print(m)
#while (a) >0:
#    if a%10 > m:
    #m = a%10
    #a = a//10
   # print(m)
#print(m)

#-----
#a = 12345 #int(input())
#m = 0
#a = a//10
#while (a):

   # if a%10 > m:
 #       m = a%10

#print(a)
#-----

#integer_number = 5552513
#a =  [0]*integer_number
#c=0
#i=0
#while integer_number>0:
#    for i in range(integer_number):
#        if integer_number[i] == 5:
#            c += 1

    #integer_number = integer_number//10
        #print(c)
    #c -= 1
#else: print('No')
#for i in range(c):
#print(c)

#11
import os, sys
from random import randint
n = randint(1,20)
c = 0
while True:
  c += 1
  r = int(input('I will pick number one to 20. Try to guess: '))
  if r < n:
      print('The number is less than you entered. Try again ')
  if r > n:
      print('The number is more than you entered. Try again ')
  if r == n:
      print(n, 'You win! Number of attempts:', c)
      break