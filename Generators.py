#Generators bellek üzerinde yer tutmayan yapıdır.

#llist=[1,2,3]
#iterator=iter(llist)
#print(iterator)

def double(numb):
    List=[]
    for i in range(1,numb):
        List.append(i*2)
    return List
print(double(100))

def doubl(num):
    for i in range(1,num):
        yield i*2

for i in doubl(100):
    print(i)