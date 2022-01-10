import docx 
def updating(filename):
    doc = docx.Document("C:\\Users\\Root\\To\\Word\\File\\"+filename+".docx")
    fulltext = []
    contentstr = ''
    for para in doc.paragraphs:
        fulltext.append(para.text)
    for word in fulltext:
        contentstr += word
    return contentstr

