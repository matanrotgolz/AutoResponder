
from os import read
import time
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes
import htmlAttacment
def send_email(day1content,day1subject,reciverEmail,username):
        sender_address = 'info@livbhealthy.com'
        sender_pass = 'Sabasafta40!'
        receiver_address = reciverEmail
        client = username
        #Setup the MIME
        msg = EmailMessage()
        # generic email headers
        msg['Subject'] = day1subject
        msg['From'] = sender_address
        msg['To'] = receiver_address

        # set the plain text body
        msg.set_content('LiveBHealthy')

        # now create a Content-ID for the image
        image_cid = make_msgid(domain='xyz.com')
        # if `domain` argument isn't provided, it will 
        # use your computer's name
        # set an alternative html body
        msg.add_alternative("""\
        <html>
            <heade>
                <style>
                        p{
                         color:black;
                        }
                        img{
                                border-radius:50%
                        }
                </style>
            </head>    
            <body>
             """+day1content+""" 
            </body>
            <br>
            <footer>
                <img src="cid:{image_cid}"><br><br>
                <h3>If you want, Contact us:</h3>
                <p><strong><img src="https://img.icons8.com/office/16/000000/facebook-new.png"/> :</strong></P>
                <p><strong><img src="https://img.icons8.com/external-flatart-icons-lineal-color-flatarticons/64/000000/external-email-contact-us-flatart-icons-lineal-color-flatarticons-7.png"/>: info@livbhealthy.com</strong></p>
            </footer>
        </html>
        """.format(image_cid=image_cid[1:-1]), subtype='html')
        # image_cid looks like <long.random.number@xyz.com>
        # to use it as the img src, we don't need `<` or `>`
        # so we use [1:-1] to strip them off

        with open('resources\Images\logo.png', 'rb') as img:

                # know the Content-Type of the image
                maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

                # attach it
                msg.get_payload()[1].add_related(img.read(), 
                                         maintype=maintype, 
                                         subtype=subtype, 
                                         cid=image_cid)      
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_address, sender_pass)
                server.sendmail(sender_address,receiver_address,bytes(msg))

def readAndSend(reciverEmail,username,counter):
    emailManagmentFile = open("emailManagmentFile","w")
    print("Starting the proccess...")
    if (counter == 0):
            day1content , day1subject = htmlAttacment.dayone(username)
            send_email(day1content,day1subject,reciverEmail,username)
            emailManagmentFile.write("email has been sent to "+str(reciverEmail))
            print("email has been sent to "+str(reciverEmail))
            emailManagmentFile.close()
    elif(counter == 1):
            day2Content,day2Subject = htmlAttacment.daytwo(username)
            send_email(day2Content,day2Subject,reciverEmail,username)
            emailManagmentFile = open("emailManagmentFile","w")
            emailManagmentFile.write("email has been sent to "+str(reciverEmail))
            print("email has been sent to "+str(reciverEmail))
            emailManagmentFile.close()
    elif(counter ==2):
            day3Content,day3Subject = htmlAttacment.daythree(username)
            send_email(day3Content,day3Subject,reciverEmail,username)
            emailManagmentFile = open("emailManagmentFile","w")
            emailManagmentFile.write("email has been sent to "+str(reciverEmail))
            print("email has been sent to "+str(reciverEmail))
            emailManagmentFile.close()
    elif(counter ==3):
            day4Content,day4Subject = htmlAttacment.dayfour(username)
            send_email(day4Content,day4Subject,reciverEmail,username)
            emailManagmentFile = open("emailManagmentFile","w")
            emailManagmentFile.write("email has been sent to "+str(reciverEmail))
            print("email has been sent to "+str(reciverEmail))
            emailManagmentFile.close()
    elif(counter > 3):
            emailManagmentFile = open("emailManagmentFile","w")
            emailManagmentFile.write("The following costumer: "+reciverEmail+" has finished all his videos! moving him to a new table")

    print("mail proccess has been finished!")