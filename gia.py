ie = input('Digite a IE: ')

if ie.endswith('0') or ie.endswith('1'):
	print('O vencimento da GIA é dia 16')
if ie.endswith('2') or ie.endswith('3') or ie.endswith('4'):
	print('O vencimento da GIA é dia 17')
if ie.endswith('5') or ie.endswith('6') or ie.endswith('7'):
	print('O vencimento da GIA é dia 18')
if ie.endswith('8') or ie.endswith('9'):
	print('O vencimento da GIA é dia 19')
