#留言分析系統
#C:\Users\HOME\OneDrive\桌面\review-analytics
#這個程式寫法是計算有幾個字元含符號 (句號/空格/逗號/ '\n'換行符號)

data = []
length = 0
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		length = length + len(data[count]) #也可寫成 length += len(data[count]), 累積計算每則留言長度
		count += 1
		if count % 100000 == 0:# % count除於 1000000 的餘數
			print (len(data))
			print ('累計計算至', count, '則留言, 共有', length, '個字串') #當計算至特定數目的留言, 計算累積的字母數
		'''
		elif count % 50000 ==0:
			print (len(data))
		'''

# print (len(data[0]))
# 印出第一行文字的字元字母長度
print ('----------------------------------')
print ('讀取完畢, 共有', len(data),'筆留言')
print ('共有',length ,'個字串')
aver = length / len(data)
print ('平均',aver ,'個字串')

new = []
for d in data: #每則留言依迴圈加入 d 中
	if len(d) < 100: #當留言字母符號長度小於100, 加入'new'矩陣中
		new.append(d)
print (len(new)) #印出矩陣中共有的留言數目
print (new[0]) #印出呼叫矩陣中的留言
print (len(new[0])) #印出呼叫矩陣中的留言