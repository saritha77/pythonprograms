#palindrome
n = input("enter a number")
fact =1
for i in range(n, 1, -1):
    fact*=i
print "factorial of ", n, fact
