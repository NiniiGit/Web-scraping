from __future__ import print_function
from lxml.html.diff import htmldiff
import os
import json
import os.path
from os import path
import requests
import bs4
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime


####Variable list######
sender_email = "<add your address>"
receiver_email = "<add your audience>"
password = "<your password>"

message = MIMEMultipart("alternative")
message["Subject"] = "Confluence scraping phase 1"
message["From"] = sender_email
message["To"] = receiver_email
user = '<your mail address>'
apikey = '<generate your api key for target website>'


#######################Fetching of data from confluence site started###############
print('\n Confluence-scraping-start \n')
print('\n Fetching of data from confluence site started \n ')

url = "https://<website-tobe-scraped>"

response = requests.get(url, auth=(user,apikey))

print(response.text)

print('\n Fetching of data from confluence site finished \n ')
#######################Fetching of data from confluence site finished###############

###################start: Eliminate unwanted part and only seperate out html part required further ############

print('\n start to eliminate unwanted part and only seperate out html part required further \n ')

def find_values(id, json_repr):
    results = []

    def _decode_dict(a_dict):
        try:
            results.append(a_dict[id])
        except KeyError:
            pass
        return a_dict

    json.loads(json_repr, object_hook=_decode_dict) # Return value ignored.
    return results

json_repr = response.text
#(find_values('value', json_repr))
valuehtml = (find_values('value', json_repr))
print(valuehtml)


print('\n End to eliminate unwanted part and only seperate out html part required further \n ')
###################End: Eliminate unwanted part and only seperate out html part required further ############

########Converting list type of html into string type##################
print('\n Start of converting list datatype of html into string type \n ')

def listToString(valuehtml):

    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(valuehtml))



newhtmlvalue = listToString(valuehtml)

print("\n newhtmlvalue is \n "+newhtmlvalue)

html = newhtmlvalue



print('\n End of converting list datatype of html into string type \n ')


############New section beginging to compare the old and current confluence page status#####
new_htmlvalue = newhtmlvalue

print("\n Value for new_htmlvalue is : "+new_htmlvalue)
print("\n")
#print(old_htmlvalue)


######## Reading old data from old_htmlvalue and comparing with new data with new_htmlvalue #######

if path.exists("C:/Users/desaind/Desktop/SC team/confluence scraping/old_htmlvalue.txt"):
    pathof_old_content = 'C:/Users/desaind/Desktop/SC team/confluence scraping/old_htmlvalue.txt'
    old_htmlvalue_content = open(pathof_old_content,'r')
    old_htmlvalue = old_htmlvalue_content.read()
    print("\n \n Value inside old_htmlvalue variable is \n\n"+old_htmlvalue)
else :
    print("\n \n file old_htmlvalue.txt does not exist on C:/Users/desaind/Desktop/SC team/confluence scraping/ but will be created ahead \n \n")
    old_htmlvalue = " "
    print("\n Temporary Value of old_htmlvalue is : "+old_htmlvalue+"  but still check as it will change at the end for future reference \n")

###############################################
# First, I removed the split... it is already an array
str1 = old_htmlvalue
print("\n")
str2 = new_htmlvalue


result1 = ''
result2 = ''

#handle the case where one string is longer than the other
maxlen=len(str2) if len(str1)<len(str2) else len(str1)

#loop through the characters
for i in range(maxlen):
  #use a slice rather than index in case one string longer than other
  letter1=str1[i:i+1]
  letter2=str2[i:i+1]

  result1+=letter1
  result2+=letter2

if result1 != result2:
    print('\n \n There is change in content of confluence page \n')
    print('\n Sending email as it seems content part of confluence page has been changed recently')


# Turn these into html MIMEText objects

    part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first

    message.attach(part2)

# Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

    print('\n End of email sending part of script')
    #print('Confluence-scraping-end')

else:
    print('\n Same content as of earlier')

##########################################
######## Storing value into a file for later comparison if confluence content changed or not#######


# Specify the path
path = 'C:/Users/desaind/Desktop/SC team/confluence scraping'

# Specify the file name
file = 'old_htmlvalue.txt'

# Before creating

dir_list = os.listdir(path)
print("\n List of directories and files before creation:")
print(dir_list)
print()

# Creating a file at specified location
with open(os.path.join(path, file), 'w') as fp:
    pass
    # To write data to new file uncomment
    # this
    fp.write(new_htmlvalue)

# After creating
dir_list = os.listdir(path)
print("\nList of directories and files after creation:")
print(dir_list)

######## End: Storing value into a file for later comparison if confluence content changed or not#######





##############END: New section to compate the old and current confluence page ends here   ####################


now = datetime.datetime.now()
print(now)
print(now.hour)
print(now.minute)

check_time = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23 ]

if now.hour in check_time[0 : 23] and now.minute == 34:
    print ('its time to send hourly update as its')
    if result1 == result2:
        print('\nStart of email sending as part of hourly update process \n')


# Turn these into html MIMEText objects
        part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first

        message.attach(part2)

# Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("<smtpaddress>", <port>, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

        print('\n End of email sending part of hourly update process \n')
        print('\n Confluence-scraping-end by sending email \n')

    else :
        print('\n Confluence-scraping-end without sending email\n')
else :
    print ('its not the time for sending hourly update')
