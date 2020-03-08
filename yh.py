from requests import Session
import re,os


def login(email):
	s = Session()
	r = s.get("https://login.yahoo.com")
	acc = re.search(r'\<input type\=\"hidden\"\ name\=\"acrumb\"\ value\=\"(.*?)\"\ \/\>',r.text).group(1)
	sess = re.search(r'\<input\ type\=\"hidden\"\ name\=\"sessionIndex\"\ value\=\"(.*?)\"\ \/\>',r.text).group(1)
	data = {
		"acrumb":acc,
		"sessionIndex":sess,
		"username":email,
		"passwd":"",
		"signin":"Berikutnya"
	}
	
	x = s.post("https://login.yahoo.com",data=data)
	if "messages.ERROR_INVALID_IDENTIFIER" in x.text:
		print(email," invalid")
	else:
		print(email, " valid")
	
if __name__=='__main__':
	login("karjok@yahoo.com")