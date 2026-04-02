node_01=input('Enter the node 1 : ') #01
node_02=input('Enter the node 2 : ')
flag=0
d1 = {"A" : ["D", "E"], "B" : ["E", "C"], "C" : ["B"], "D" : ["A", "E"], "E" : ["A", "B", "D"]}
for i in d1[node_01]:
    for j in d1[node_02]:
        if i==j:
            flag=1
            break
        else:
            flag=0

if flag==1:
    print(f"{node_01} and {node_02} are connected with each other")
else:
    print(f"{node_01} and {node_02} are not connected with each other")