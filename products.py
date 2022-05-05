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
#可用excel打開，用','區隔
with open ('products.csv', 'w' , encoding='utf-8') as f:
	f.write('商品名稱,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')


