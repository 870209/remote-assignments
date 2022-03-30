def find_max(number):
    i=1
    numberReturn=number[0]
    while i<=(len(number)-1):
        if numberReturn > number[i]:
            numberReturn=numberReturn
        else:
            numberReturn=number[i]
        i+=1
    return numberReturn

def find_position(numbers,target):
    i=0
    while i<=(len(numbers)-1):
        if target==numbers[i]:
            return i
        else:
            i+=1
    return -1

print(find_position([5, 2, 7, 1, 6], 5)) 
print(find_position([5, 2, 7, 1, 6], 7)) 
print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) 
print(find_position([5, 2, 7, 1, 6], 8)) 
