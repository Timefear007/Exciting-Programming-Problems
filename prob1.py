#Three ways to compute a sum of elements in list

List=[1,2,3]
N=len(List)-1

#using for-loop
def func1(li):
    ans=0
    for i in li:
        ans+=i
    return ans

#using while-loop
def func2(li):
    ans=0
    i=0
    while i<len(li):
        ans += li[i]
        i+=1
    return ans

#using recursion
def func3(li,n):
    if n==0:
        return li[n]
    else:
        return li[n]+func3(li,n-1)
    

print(func1(List))
print(func2(List))
print(func3(List,N))
        
