a = 1
b = 1
n = 0
length = 0
val = ""
val2 = ""
print("checking if a file fib.csv containing fibonaccis already exists...")
try:
    ## open file
    f = open("fib.txt", "r")  
    print("fib.txt found! will continue with last results. ")

    ## evaluate n, len, val and val2
    while n==0:
        line = f.readline()
        if line.startswith("C:"):
            while not line.startswith("B:"):
                if "=" not in line:
                    val += line
                else:
                    val += line.split("=")[1]
                line = f.readline()
            
            length = line.split("=")[1]
            line = f.readline()
            n = line.split("=")[1]
            line = f.readline()
            while not line.startswith("B:"):
                if "=" not in line:
                    val2 += line
                else:
                    val2 += line.split("=")[1]
                line = f.readline()

    ## close file
    f.close()

    s = "last result was f(" + str(n) + "). with a length of " + str(length) + " numbers and the value of:"
    s = s.replace("\n", "")
    s += "\n" + str(val)
    print(s)
    
    ## assign f(n-2) as a and f(n-1) as b
    n = int(n)
    a = int(val)
    b = int(val2)
    print("a:", a)
    print("b:", b)
except IOError:
    print("fib.txt does not exist. we'll start from scratch and create a new file...")
    f = open("fib.txt", "x")
    s = "C:value=1\nB:length=1\nA:n=2\nC:value=1\nB:length=1\nA:n=1\n"
    f.write(s)
    f.close()
    print("file created. \n")

# file exists, n and val of n-1 and n-2 evaluated
print("How many new fibonaccis do you want to calculate?")
i = int(input())

# start list for fib collection
fib_list = []
for num in range(i):
    n += 1
    print("...calculating f(" + str(n) + ")")
    c = a+b
    s = "C:value="+str(c)+"\nB:length="+str(len(str(c)))+"\nA:n="+str(n)+"\n"
    fib_list += [s] 
    a = b
    b = c

fib_list = reversed(fib_list)

# save existing data before prepend new one
with open("fib.txt", "r+") as file:
    content = file.read()

    f = open("fib.txt.sv", "w")
    f.write(content)
    f.close()

    file.seek(0)
    for new_line in fib_list:
        file.write(new_line)

    file.write(content)
