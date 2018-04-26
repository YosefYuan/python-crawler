
import requests, bs4
#https://www1.miele.de/iinet/cn/callassistance/sa/ca.aspx?searchProd=e5
#https://www1.miele.de/iinet/cn/callassistance/ca_2745.aspx

# a=["0000000","0000000","0000000","0000000","0000000","0000000","0000000","0000000","0000000","0000000","0000000","0000000","0000000","0000000","0000000",]


a=["ca_3137","ca_3740","ca_3159","ca_3151","ca_3147","ca_3746","ca_3153","ca_3744","ca_3739"]


pageId = "rollerWash-others"
ind = ""
i=1
for v in a: 
	link = 'https://www1.miele.de/iinet/cn/callassistance/'+v+'.aspx'
	#print (link) 
	if (i > 9):
		ind = str(i)
	else:
		ind = "0" + str(i)
	res2 = requests. get(link)
	res2. raise_for_status()
	soup2 = bs4.BeautifulSoup(res2.text,"html.parser")
	#detail2 = soup2. select('.scrolling div[style="margin:10px 0px"]') 

	detail2 = soup2. select('#c_sf_title')
	detail3 = soup2. select('#c_sf_title + div')
	print('{') 
	print("  quespdpid: `" + pageId + "-"+ind+"`,") 
	i=i+1
	print("  quesTitle: `<div>"+ str(detail2[0]) + str(detail3[0]) +"</div>`")
	print('},') 
	 


 