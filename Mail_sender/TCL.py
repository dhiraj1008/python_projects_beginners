#By TCL
# sending mail with your own client not with gmail client ..i,e by python.. 
"""
steps  :-
       1)In gmail app we need to set up below mentioned things.
         we are using this service from gmail account and non-gmail application..!,
         so by default gmail will block it because gmail is very secure ..we need to 
         enable it. go to ->security tab
                          ->2 step verification 
                          ->turn on!
       2)go to App password and fill the details(select spp -> other ,select device -> anyname u want) to generate password(16 character)..!  
       3)do code in python file:               
"""
#A package for parsing, handling, and generating email messages.(for email meaage formate)
from email.message import EmailMessage
#SMTP -> simple mail transfer protocol(set of rules defined to send a mail)..
#for reciving mail we use pop .
import smtplib
#import your password from where it is defined ..!
import password
#we need to create a server ..
server = smtplib.SMTP("smtp.gmail.com",587)
#we need to create secure connection ..TLS(transport layer security),SSL(secure socket layer)...!
server.starttls()
sender="dhirajalate92@gmail.com"
#genereated through 'temp emal' (even u can type 'temp email' in google or other serch engine)..
reciver="gejoxe1610@gpipes.com"

#for login in to gmail
server.login(sender,password.password)

#create instance 
em = EmailMessage()
em['from']=sender
em['To']=reciver
em['subject']="adopt zoo animals"
body="""
     adopt zoo animals if we able to do plz contact us on 9987654432
     - animzoo
"""
em.set_content(body)

#send mail..

server.sendmail(sender,reciver,em.as_string())

print("Mail sent")