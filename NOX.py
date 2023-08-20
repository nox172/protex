import os
import pyfiglet

def download_sqlmap():
# Download SQLMap tool or any other command you desire
	os.system("git clone https://github.com/sqlmapproject/sqlmap.git")

def open_youtube_video(video_url):
# Open the YouTube video in the default browser
	os.system("start " + video_url)

a = '\033[31m'
b = '\033[32m'
c = '\033[33m'
d = '\033[34m'
e = '\033[35m'
f = '\033[36m'
g = '\033[90m'
h = '\033[39m'

# Title
os.system('clear')
logo = pyfiglet.figlet_format("Web Hacking")
print(c+logo)
print(g+"Developed By NOX\n")
# Screen choice
print(c+"\n\t["+a+"00"+c+"] "+h+"About us")
print(c+"\t["+a+"01"+c+"] "+h+"Install SQLmap")
print(c+"\t["+a+"02"+c+"] "+h+"Course for SQLmap\n")
choice = input(b+"Choose an option:"+h+"$ ")
# Work
if choice == "0" or choice == "00":
	print(c+'\n╭'+'─'*39+'╮')
	print(c+"│"+b+" Telegram:"+h+"  @Noxform\t\t"+c+"\t│")
	print(c+'╰'+'─'*39+'╯')
elif choice == "1" or choice == "01":
	download_sqlmap()
	print("SQLmap tool downloaded successfully")
elif choice == "2" or choice == "02":
	print(c+"\n\t["+a+"01"+c+"] "+h+"Part 1")
	print(c+"\t["+a+"02"+c+"] "+h+"Part 2")
	print(c+"\t["+a+"03"+c+"] "+h+"Part 3")
	print(c+"\t["+a+"04"+c+"] "+h+"Part 4")
	option = input(b+"\nChoose an option:"+h+"$ ")
	if option == "1" or option == "01":
		print(c+"\n\t["+a+"!"+c+"] "+h+"Copy link of the course")
		print(c+'╭'+'─'*39+'╮')
		print(c+"│"+f+"\thttps://youtu.be/NNzXxyxjFcE\t"+c+"│")
		print(c+'╰'+'─'*39+'╯')
	elif option == "2" or option == "02":
		print(c+"\n\t["+a+"!"+c+"] "+h+"Copy link of the course")
		print(c+'╭'+'─'*39+'╮')
		print(c+"│"+f+"\thttps://youtu.be/33fPZCiidfs\t"+c+"│")
		print(c+'╰'+'─'*39+'╯')
	elif option == "3" or option == "03":
		print(c+"\n\t["+a+"!"+c+"] "+h+"Copy link of the course")
		print(c+'╭'+'─'*39+'╮')
		print(c+"│"+f+"\thttps://youtu.be/hoAr26LgfIw\t"+c+"│")
		print(c+'╰'+'─'*39+'╯')
	elif option == "4" or option == "04":
		print(c+"\n\t["+a+"!"+c+"] "+h+"Copy link of the course")
		print(c+'╭'+'─'*39+'╮')
		print(c+"│"+f+"\thttps://youtu.be/URjuesLQSnE\t"+c+"│")
		print(c+'╰'+'─'*39+'╯')
	else:
		print(a+"\nSyntax error!:"+h+" Pleas try again")
else:
		print(a+"\nSyntax error!:"+h+" Pleas try again")
