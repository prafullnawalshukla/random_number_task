import struct
import time
f = open("/dev/urandom","r")
a= list()
b = list()
c = list()
while 1:
	val = struct.unpack("i",f.read(4))[0]
	if val > 1:
		random_value = int(str(val)[1:2])
		if (random_value <= 5):
			a.append(random_value)
		if len(a) == 25:
			break
while 1:
	val = struct.unpack("i",f.read(4))[0]
	if val > 1:
		random_value = int(str(val)[1:2])
		if (random_value > 5):
			b.append(random_value)
		if len(b) == 75:
			break
c = a + b
print c

# Test Case 
count  = 0
count1 = 0
for ele in c:
	if ele <= 5:
		count +=1
	else:
		count1+=1
print 'less then 5:', count
print 'greater then 5:', count1