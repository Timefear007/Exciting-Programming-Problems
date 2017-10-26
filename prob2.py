listA=[1,2,3,4,5]
listB=[5,4,5,5,5]

def combine_these_guys(A,B):
    new_list = []
    i=0
    j=0
    while i<len(A) and j<len(B):
        new_list.append(A[i])
        new_list.append(B[j])
        i+=1
        j+=1

    return new_list

print(combine_these_guys(listA,listB)) 
