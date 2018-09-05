pip3 install bs4

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_string)

# css 选择器器语法,,不怎么好用
r = soup.select("")
r[0].text

# attr

# decode

# node.node.node
quote.span.attrs
tag.tag.attrs

# 另一种,还行.. 
r2 = soup.find_all('div',id="search")

