a="hello"
def Hi_There():
    a="hello"
    print(a)

Hi_There()
print(a)


def Hi_There2nd():
    print(a)

Hi_There2nd

# global değişken dereri localde değiştiriliebilir.

a="Hi There"
def hello():
    global a
    a="Hi there"
    print(a)