'''
Made by Kayan Tchian
August/14/2022 
'''

import bs4, requests, sys, time
import patterns

def getHtml(url):
	try:
		response = requests.get("https://evaldowolkers.wordpress.com/sobre",
		              headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
		html = response.text	
		print(f" EMAILs → {patterns.email_get(html)}")
		print(f" EMAILs → {patterns.phone_get(html)}")
		print(f" EMAILs → {patterns.cpf_get(html)}")

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
				print(f" EMAILs → {patterns.phone_get(row)}")
				print(f" EMAILs → {patterns.cpf_get(row)}")
		else:
			print("Arquivo vazio")
			return None
	except FileNotFoundError:
		print(f"Sorry, the path '{path}' did not found.\n")
		return None

logo = '''

$$\      $$\ $$$$$$$$\ $$$$$$$\         $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$$\ $$\     $$\ 
$$ | $\  $$ |$$  _____|$$  __$$\       $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\\$$\   $$  |
$$ |$$$\ $$ |$$ |      $$ |  $$ |      $$ /  \__|$$ /  \__|$$ |  $$ |$$ /  $$ |$$ |  $$ |\$$\ $$  / 
$$ $$ $$\$$ |$$$$$\    $$$$$$$\ |      \$$$$$$\  $$ |      $$$$$$$  |$$$$$$$$ |$$$$$$$  | \$$$$  /  
$$$$  _$$$$ |$$  __|   $$  __$$\        \____$$\ $$ |      $$  __$$< $$  __$$ |$$  ____/   \$$  /   
$$$  / \$$$ |$$ |      $$ |  $$ |      $$\   $$ |$$ |  $$\ $$ |  $$ |$$ |  $$ |$$ |         $$ |    
$$  /   \$$ |$$$$$$$$\ $$$$$$$  |      \$$$$$$  |\$$$$$$  |$$ |  $$ |$$ |  $$ |$$ |         $$ |    
\__/     \__|\________|\_______/        \______/  \______/ \__|  \__|\__|  \__|\__|         \__|    
                                                                                                    
       '''
try:
	print(f" {logo} \n[1] URL\n[2] Files with URLs\n[3] Exit ")
	while True:
		option = int(input("\n>> "))
		if(option == 1):
			website	 = input("\nURL: ")
			getHtml(website)
		elif(option == 2):
			path = input("\nPath file: ")
			UrlFiles(path)
		elif(option == 3):
			print("Turning off...")
			time.sleep(3)
			sys.exit(0)
		else:
			print("\nInvalid Option.")

except ValueError:
	print("\nPlease only use integers numbers.")
	sys.exit(0)
