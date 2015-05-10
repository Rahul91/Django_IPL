import urllib2
from bs4 import BeautifulSoup

url = urllib2.urlopen("http://www.cricbuzz.com/cricket-match/live-scores")
soup = BeautifulSoup(url)

sol = soup.find("div", {"class": "cbz_module_content scag_content"})
#print sol
x=sol.find_all("h3",{"class":"scag_header"})
#print x
#print sol.find_all("h3",{"class":"scag_header"})
p=sol.find_all("div", {"class" : "scag_text1 scag_scores_completed"})
#print p, type(p)
count=len(p)
#print count
#for a in p:
#	n,m=a.find_all("div", {"class":"team_name_completed"}), a.find_all("div", {"class":"teams_scores"})
#	print n.find("div", ) , m

for i in range(count/4):
	s=x[i]
	m,n=p[i], p[i+1]
	print s.text
	a,b=m.find("div", {"class":"team_name_completed"}),m.find("div", {"class":"teams_scores"})
	c,d=n.find("div", {"class":"team_name_completed"}),n.find("div", {"class":"teams_scores"}) 
	print a.text, b.text
	print c.text, d.text
	print ("")	
'''
	for i in range(count/2):
		m=p[i]
		print m
		a,b=m.find("div", {"class":"team_name_completed"}),m.find("div", {"class":"teams_scores"}) 
		print a.text, b.text


x=sol.find_all("h3",{"class":"scag_header"})
	 #,type(sol)
for y in x:
	print y.text'''