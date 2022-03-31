def count(input1):
    dict={}
    for key in input1:
        dict[key] = dict.get(key,0)+1
    return dict

    
input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']


print(count(input1))





def group_by_key(input2):
    
    info_dic={}
    for d in input2:
       if d['key'] not in info_dic:      
          info_dic[d['key']]=d['value']
       else: info_dic[d['key']]+=d['value']
    new_info={}
    for n,v in info_dic.items():
       new_info[n]=v
    return new_info

input2 = [
 {'key': 'a', 'value': 3},
 {'key': 'b', 'value': 1},
 {'key': 'c', 'value': 2},
 {'key': 'a', 'value': 3},
 {'key': 'c', 'value': 5}
]
print(group_by_key(input2))
