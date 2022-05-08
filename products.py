import os #作業系統



#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
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
			products.append([name, price])
	return products

#使用者輸入商品和價格
def user_input(products):
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入商品價格:')
		price = int(price)
		products.append([name, price])

	print(products)
	return products

#分別印出清單中的項目
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#寫入檔案
#蠻常用.csv來儲存資料
#可用excel打開，以英文','區隔
def write_file(filename, products):
	with open (filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):#檢查檔案在不在
		print('讀取成功')
		products = read_file(filename)
	else:
		print('找不到檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()