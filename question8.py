#lets create simple calculator that perform arithematic operation .create a function calculator(a , b , operation )
#that perform addition , substraction , multiplication , or division based on the operation parameter .
#(operation parameter can have value + , - , * , /
calculator = lambda a , b , op :{
    '+': a + b ,
    '-': a - b,
    '*': a * b,
    '/': a / b,
}[op]
print(calculator(3 , 4 , '+'))
print(calculator(3 , 4 , '-'))
print(calculator(3 , 4 , '*'))
print(calculator(3 , 4 , '/'))