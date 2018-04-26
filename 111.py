
import requests, bs4
#https://www.miele.cn/domestic/trouble-shooting-guide-391.htm
baseurl = 'https://www1.miele.de/';
res = requests. get('https://www1.miele.de/iinet/cn/callassistance/sa/ca.aspx') 
res. raise_for_status() 
soup = bs4.BeautifulSoup(res.text,"html.parser")
catenames = soup. select('#productLinks b') 
for catename in catenames: 
	print (catename.getText()) 
print ('===============')
cateimgs = soup. select('#productLinks img') 
for cateimg in cateimgs: 
	print (baseurl+cateimg.get('src')) 
print ('===============')
catelinks = soup. select('#productLinks a') 
#https://www1.miele.de/iinet/cn/callassistance/sa/ca.aspx?searchProd=e7
catelinkurl = 'https://www1.miele.de/iinet/cn/callassistance/sa/ca.aspx'
for catelink in catelinks: 
	listlink = catelinkurl+catelink.get('href')
	print (listlink) 

	res = requests. get(listlink) 
	res. raise_for_status() 
	soup = bs4.BeautifulSoup(res.text,"html.parser")
	details = soup. select('#result a') 
	#https://www1.miele.de/iinet/cn/callassistance/ca_3577.aspx
	for detail in details: 
		#listlink = catelinkurl+catelink.get('href')
		print (detail.getText()) 
		detaillink = 'https://www1.miele.de/'+detail.get('href')
		print (detaillink+'----------')
		res2 = requests. get(detaillink) 
		res2. raise_for_status() 
		soup2 = bs4.BeautifulSoup(res2.text,"html.parser")
		detail2 = soup2. select('.scrolling div[style="margin:10px 0px"]') 
		print (detail2)

        
     

	print ('===============')
	 

print ('===============')
print ('===============')
print ('===============')


 





 