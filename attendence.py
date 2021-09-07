f = open('attandance.txt','w')
s = "Name"
f.write(s)
for i in range(int(input('Enter the number of student: '))):
 
 s = '\t'+input('Enter Name: ')
 f.write(s)
 
f.close()
import time
f = open('attandance.txt','r+')
data = f.read()
data = data.split('\n')[0].split('\t')
s = f"\n{time.strftime('%d-%m')}"
f.write(s)
print('Enter P for Present and A for abscent')
for i in data[1:]:
 
 s = f"\t{input(f'{i}-->').upper()}"
 
 f.write(s)
 
f.close()
