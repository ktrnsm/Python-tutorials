MorsCode={
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..'
}

sentence=input("Please write your sentence to translate")
for i in range(0,len(sentence)):
    index=sentence[i]
    result=MorsCode.get(index)
    print(result,end=" ")