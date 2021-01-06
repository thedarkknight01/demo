import requests
import bs4
from datetime import datetime

url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=Graphic%20Card%20In%20Stock.%20Order%20Soon%21&language=english&route=p&numbers=7358143043"
headers = {
'authorization': "4R38MVT5PGCHvc2oOe6xmjbk9rLIDBstEYfZphWiJAqFQXK7yu31sD78yKPF9AidI4nlN2TfoHh0ROjv",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}

print("Script started at time ", datetime.now())
res = requests.get('https://rptechindia.in/nvidia-geforce-rtx-3070.html')
soup = bs4.BeautifulSoup(res.text, 'lxml')
stock = soup.select('button')
stock_text = stock[1].getText()

print("******************")
print(stock)
print("******************")
print("Stock Status:")
if 'Add to Wishlist' in stock_text:
	print("Out of Stock")
elif 'Add to Cart' in stock_text:
	print("In Stock")
	response = requests.request("POST", url, data=payload, headers=headers)
	print(response.text)

print("******************")
print("Script ended at time ", datetime.now())
print("\n")
