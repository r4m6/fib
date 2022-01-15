a=1
b=1
c=a+b

print("This program only displays fibonaccis - if you want to save them use fib2.py, but it takes much longer to load and save then to just display them. Have fun!")
print("How much fibunaccis do you want to display?")
i = int(input())
i = i - 3 

print("fib( 1 )=", a)
print("fib( 2 )=", b)
print("fib( 3 )=", c)
for num in range(i):
    a = b
    b = c
    c = a+b
    print("fib(",num+4,")=",c)

count = len(str(c))
print("fib(",num+4,") has ", count, " chars.")
