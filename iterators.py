#iterators
llist=[1,2,3,4,5]

for i in llist: # kendisine iteratör tanımlıyor
    print(i)

iterator=iter(llist)
#aşağıdaki şekilde listenin elemanlarını tek tek yazıyor.
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

while True: # for döngüsünün açık iter fonksionu hali
    try:
        seach=next(iterator)
        print(seach)
    except StopIteration:
        break

class Numbers:
    def __init__(self,start,finish):
        self.start=start
        self.finish=finish
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<=self.finish:
            x=self.start
            self.start+=1
            return x
        else:
            raise StopIteration
print(Numbers)

List=Numbers(1,100)

for i in List:
    print(i)
        


 