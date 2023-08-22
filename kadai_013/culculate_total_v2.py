# 課題の内容
# 商品を購入して、消費税を加えた計算結果を返す関数を記述してください。
# 第1引数に商品の金額、第2引数に消費税（10%）を設定できるようにしてください。

def culculate_total(price,tax_rate=1.1):
  total = price * tax_rate

  print(f'税抜価格 {price}円')
  print(f'消費税 10％加算')
  print(f'税込価格 {total}円')


culculate_total(2000)