def avg(data):
    i=0
    total=0
    while (i<len(data)):
        addNum = data[i]['price']
        total=total+addNum
        average=total/(i+1)
        i=i+1
    return average
    
print(avg( [ { "name": "Product 1","price": 100},
 { "name": "Product 2", "price": 700 },
 { "name": "Product 3", "price": 300 }]
))
