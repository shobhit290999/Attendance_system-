import time
f = open('attendence.txt','r+')
data = f.read().split('\n')[0].split('\t')
s = f"\n{time.strftime('%d-%m')}"
f.write(s)
print('Enter P for Present and A for abscent')
for i in data[1:]:
    
    s = f"\t{input(f'{i}-->').upper()}"
    
    f.write(s)
    
f.close()

f = open('attendence.txt','r')
data  = f.read().split('\n')
data2=[]
for i in data:
    data2.append(i.split('\t'))


for i in range(1,8):
    l=[]
    for j in range(0,len(data2)):
        l.append(data2[j][i])
    present = l.count('P') 
    absent = l.count('A')
    print(l)
    print(f"present:{present}")
    print(f"absent:{absent}")