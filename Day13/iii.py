import re

s = "今年是2019是处理90周年"
pattern = r'\d+'
m = re.fullmatch(r'[,\w]+', s)
print(m.grouup())
