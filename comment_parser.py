import sys, getopt
import urllib
import urllib2
from bs4 import BeautifulSoup
from bs4 import Comment
from pyfiglet import Figlet

custom_fig = Figlet(font='big', width=150)
print(custom_fig.renderText('COMMENT EXTRACTOR').rstrip())
print('\n\t\t\t\t\tAUTHOR: BHARAT THAPA')

print("\n\n")
# DEAULT values
urlFlag = 0
outputFlag = 0
# GET ALL ARFUMENTS
arguments = sys.argv
# SAVE ALL ARGUMENTS EXCEPT FOR FIRST WHICH IS SCRIPT name
arguments_list = arguments[1:]

# DEFINING WHICH SWITCH ARE VALID AND WHICH ARE NOT FOR getopt
short_options = "hu:vo:"
long_options = ["help","url=","verbose","output="]

try:
    arguments, values = getopt.getopt(arguments_list, short_options, long_options)
except getopt.error as err:
    # Output error, and return with an error code
    print (str(err))
    sys.exit(2)

# Evaluate given options
for current_argument, current_value in arguments:
    if current_argument in ("-v", "--verbose"):
        print ("Enabling verbose mode")
        verboseFlag = 1
    elif current_argument in ("-h", "--help"):
        print ("comment_parser.py -u [url]\n")
        print ("comment_parser.py -u [url] -o outputFileName\n")
        print ("comment_parser.py -u [url] --output=outputFileName\n")
        print ("comment_parser.py --url=[url]")
    elif current_argument in ("-u", "--url"):
        urlFlag = 1
        url = current_value
    elif current_argument in ("-o", "--output"):
        outputFlag = 1
        outputValue = current_value

if urlFlag == 1:
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = {'User-Agent': user_agent}

    req = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(req)
    the_page = response.read()
    # print(the_page)
    soup = BeautifulSoup(the_page,'html.parser')
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    if current_argument in ("-o","--output"):
        outputFlag = 1
    for c in comments:
        if outputFlag == 1:
            with open(outputValue+".txt","a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0 :
                    file_object.write("\n")
                file_object.write("\n")
                file_object.write("<!-- "+c+ " -->")
                file_object.write("\n\n")
                file_object.write("==============================================")
        print("<!-- "+c+ " -->")
        print("==============================================")


    # url = sys.argv[1]
    # # comments = re.findall("^<!-- -->$",soup)
    #
    # print(soup.prettify())
    # print(soup.title)
    # print(soup.title.name)
    # print(soup.title.string)
    # # print(soup.find_all('a'))
    # for link in soup.find_all('a'):
    #     print(link.get('href'))
    # print(soup.b.string)
