# coding=utf-8
import easyquotation
import pprint
import sys
import codecs
from astropy.table import Table, Column
import numpy as np
import astropy.io.ascii as ascii

output_file=sys.argv[1]

if not output_file:
    print("output file name is empty")
    sys.exit(0)

output_file = codecs.open(output_file, 'w', 'utf-8')

quotation = easyquotation.use('sina') # 新浪 ['sina'] 腾讯 ['tencent', 'qq']

#result = quotation.market_snapshot(prefix=True) # prefix 参数指定返回的行情字典中的股票代码 key 是否带 sz/sh 前缀

#print(result)

# 股票
stocks = quotation.all_market()

print('-------------stocks----------------')
print(stocks)
#sys.exit(0)


table = Table(names=('sequence', 'scene', 'amount'), dtype=('S', 'S', 'S'))
for key, value in stocks.items():
    scene = key
    amount = str(value['open'])
    sequence = value['date']
    table.add_row((sequence, scene, amount))

table.sort(['scene', 'sequence'])
print(table)
#sys.exit(0)

#for row in table:
#    print(table['sequence'], table['scene'], table['amount'])
#    sys.exit(0)
    #output_file.write('%s, %s, %s\n' % (table['sequence'], table['scene'], table['amount']))

ascii.write(table, 'values.csv', format='csv', fast_writer=False, overwrite=True)
