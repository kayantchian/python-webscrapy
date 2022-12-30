'''
Made by Kayan Tchian
August/14/2022 
'''

import bs4, requests, sys, time
import sys, argparse

class WebScrapy(object):
	def __init__(self):
		parser = argparse.ArgumentParser(
        prog = 'Web Scrapy',
        description='A web scrapy',
        epilog='by kayantchian')
		parser.add_argument('-u', help="specify a site url")
		parser.add_argument('-e', help="grap emails")
		parser.add_argument('-p', help="grap phones")
		parser.add_argument('-c', help="grap cpfs")
		arg = parser.parse_args()
        

	def getHtml(self):
		try:
			response = requests.get(self.url,
						headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
			html = response.text	
			print(f" EMAILs → {patterns.email_get(html)}")
			print(f" PHONEs → {patterns.phone_get(html)}")
			print(f" CPFs → {patterns.cpf_get(html)}")

		except requests.exceptions.HTTPError as errh:
			print ("Http Error:",errh)
			return None
		except requests.exceptions.ConnectionError as errc:
			print ("Error Connecting:",errc)
			return None
		except requests.exceptions.Timeout as errt:
			print ("Timeout Error:",errt)
			return None
		except requests.exceptions.RequestException as err:
			print ("OOps: Something Else",err)
			return None

	def UrlFiles(path):
		try:
			f = open(path, 'r')
			content = f.readlines()
			if content:
				for row in content:
					print(f" EMAILs → {patterns.email_get(row)}")
					print(f" PHONEs → {patterns.phone_get(row)}")
					print(f" CPFs → {patterns.cpf_get(row)}")
			else:
				print("Arquivo vazio")
				return None
		except FileNotFoundError:
			print(f"Sorry, the path '{path}' did not found.\n")
			return None
