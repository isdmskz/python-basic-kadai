# 課題の内容
# 商品を購入して、消費税を加えた計算結果を返す関数を記述してください。
# 第1引数に商品の金額、第2引数に消費税（10%）を設定できるようにしてください。

price = int(input('税抜き価格は？　'))
tax_rate = int(input('消費税は何パー？　'))

def culculate_total(price,tax_rate):
  tax = price * (tax_rate / 100)
  total = price + tax
  print(f'税込み価格は {int(total)}円です。')
 
culculate_total(price,tax_rate)