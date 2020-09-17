#留言分析系統
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:#%求餘數
			print (len(data))
		elif count % 500 ==0:
			print (len(data))
			#count = count - 1000

print (data[0])
print ('---------------------')
print (data[1])
