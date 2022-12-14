def generapares(limite):

    num=1
    
    while num<limite:
        yield num*2
        num=num+1
    
devuelvePares=generapares(10)

for i in devuelvePares:
    print(i)

print(next(devuelvePares))
print(next(devuelvePares))
print(next(devuelvePares))


