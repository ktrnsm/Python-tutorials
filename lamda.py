def sum(x,y):
    result=x+y
    return result
print(sum(2,7))

#lamda yapısı

sum=lambda x,y:x+y
print(sum(2,7))


square=lambda num:num**4
List=[1,3,5,7,9]
result=list(map(square,List))
print(result)