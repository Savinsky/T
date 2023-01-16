
#i = 0
#for i in range(5):
#    print(i, ' 0000000000')
#    i+=1

#c=0
#for i in range(10):
#    s=int(input())
#    if s == 5:
#        c+=1
#print(c)

#sum = 0
#for i in range(1,101):
#    sum+=i
#print(sum)

#prod = 1
#for i in range(1,10):
#    prod = prod*i
#print(prod)

#integer_number = 2129
#print(integer_number%10,integer_number//10)
#while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

#integer_number = 2129
#suma = 0
#while integer_number > 0:
#    suma = suma + integer_number % 10
#    integer_number //= 10
#print('Suma =', suma)

#integer_number = 2129
#prod = 1
#while integer_number > 0:
#    prod *= integer_number % 10
#    integer_number = integer_number//10
#print('Prod =', prod)

#integer_number = 213413
#while integer_number>0:
#    if integer_number%10 == 5:
#        print('Yes')
#        break
#    integer_number = integer_number//10
#else: print('No')

integer_number = 213
m=integer_number%10
integer_number=integer_number//10
while integer_number>0:
    if integer_number%10 > m:
        m=integer_number%10
        integer_number = integer_number//10
print(m)