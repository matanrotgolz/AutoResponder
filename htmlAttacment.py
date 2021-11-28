
import updatingContent
def dayone(name):
    subject = "Why it can be Hard to Lose Weight"
    dayoneText ="   <p> Hi there, "+str.title(name)+", this is Gidon. <br>"+updatingContent.updating('updatecontentday1')+".</p>"
            
    return dayoneText,subject

def daytwo(name):
    subject = "  Targeting the Root Cause of Gaining Weight!"
    dayTowtext= " Hi there, "+str.title(name)+",<p> "+updatingContent.updating('updatingcontentday2')+".</p>"
                 
    return dayTowtext,subject


def daythree(name):
    subject = "  Foods and Herbs to Lose Weight! "
    dayThreeText = "  <p>Hi there, "+str.title(name)+","+updatingContent.updating('updatingcontentday3')+".</p>"
                     
    return dayThreeText,subject

def dayfour(name ):
    subject = "Spices and Fruits to Lose Weight! "
    dayFourText = "  <p>Hi there ,"+str.title(name)+",</p>"+"<br><br><p>"+updatingContent.updating('updatingcontentday4')+".</p>"
    return dayFourText,subject
