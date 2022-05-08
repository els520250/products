products1 = []

#讀取檔案
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		#strip()除去換行、空白等特殊符號
		#split()切割後會變為清單
		#s = line.strip().split(',')
		#若要分類儲存的話,在左側以,分隔

		if '商品,價格' in line:
			continue 
			#判斷有商品,價格的title就跳到下一次迴圈，
			#不再執行本輪迴圈後面的程式
		name, price = line.strip().split(',')
		products1.append([name, price])
print(products1)

products = []

while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)
	products.append([name, price])

print(products)

#分別印出清單中的項目
for p in products:
	print(p)

#蠻常用.csv來儲存資料
#可用excel打開，以英文','區隔
with open ('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品名稱,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')


