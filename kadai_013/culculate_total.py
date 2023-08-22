def culculate_total(price,tax_rate):
  tax = price * (tax_rate / 100)
  total = price + tax

  print(f'税抜価格 {price}円')
  print(f'消費税率 {tax_rate}％')
  print(f'税込価格 {total}円')


culculate_total(1000,10)