country = input ('請問你是哪國人：')
age = input('請輸入年齡：')
if country == '台灣':
	if int(age) >= 18:
		print('妳可以考駕照')
	else:
		print('你還不能考駕照')
elif country == '美國':
	if int(age) >= 16:
		print('你可以考駕照')
	else:
		print('你不可以考駕照')
		