#留言分析系統
data = []
length = 0
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		length = length + len(data[count].strip())
		count += 1
		if count % 100000 == 0:#%求餘數
			print (len(data))
			print ('累計計算至', count, '則留言, 共有', length, '個字串')
		'''
		elif count % 500 ==0:
			print (len(data))
		'''

print ('讀取完畢, 共有', len(data),'筆留言')
print ('共有',length ,'個字串')
aver = length / len(data)
print ('平均',aver ,'個字串')


'''
print (len(data[1000000-1].strip()))
print (len(data[count-1]))
print (data[count-1])
print (data[count-1].strip())



print (data[0])
print ('---------------------')
print (data[1])
'''