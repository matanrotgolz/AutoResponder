
import updatingContent
def dayone(name):
    subject = "Subject Example1"
    dayoneText ="   <p> Hi there, "+str.title(name)+", this is Gidon. <br>"+updatingContent.updating('updatecontentday1')+".</p>"
            
    return dayoneText,subject

def daytwo(name):
    subject = "Subject Example2"
    dayTowtext= " Hi there, "+str.title(name)+",<p> "+updatingContent.updating('updatingcontentday2')+".</p>"
                 
    return dayTowtext,subject


def daythree(name):
    subject = " Subject Example3 "
    dayThreeText = "  <p>Hi there, "+str.title(name)+","+updatingContent.updating('updatingcontentday3')+".</p>"
                     
    return dayThreeText,subject

def dayfour(name):
    subject = "Subject Example4 "
    dayFourText = "  <p>Hi there ,"+str.title(name)+",</p>"+"<br><br><p>"+updatingContent.updating('updatingcontentday4')+".</p>"
    return dayFourText,subject
