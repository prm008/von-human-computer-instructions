"""
1. nginput (data) <- (isi data)
    M0 <- S0
    M1 <- S1

2. isi "Accu" dengan Mn
3. isi "temP" dengan M(n+1)

4. accu <- Acuu + temP
5. isi "temP" dengan M(n+2)
{loop ke 4 (sampai n)}

6. accu <- accu/n
"""
x = input("mau anggka data? (data > 1) ")

n = int(x) # n > 2
for i in range(n+1):
    global no1
    no1 = i+1
    print (str(no1)+". M"+str(i)+ " <- "+"b"+str(i))
    if i == n-1:
        print(str(no1+1)+". M" + str(n+1) + " <- " +str(n))
        break

print(str(no1+2)+". Accu <- M0")
print(str(no1+3)+". temp <- M1")
no3=0

for j in range(n):
    global no2
    no2 = no1+j+4+no3
    print(str(no2)+ ". Accu <- Acuu + temp" )
    print(str(no2+1)+ ". tmp <- M" + str(j+2))
    no3+=1
    if j == n-2 :
        break

print(str(no2+2)+ ". Accu <- Accu/temp")

