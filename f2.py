#recursion-whic call itself again n again

def factorial(num):
     if num==0:
        return 0
     return num*factorial(num-1)      
      
ans=factorial(5)
print(ans)


