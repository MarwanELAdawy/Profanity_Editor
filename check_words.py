import urllib
def read_text():
    quotes = open("C:\Users\Marwan El-Adawy\Desktop\movie_qoutes.txt")
    contents_file = quotes.read()
    #print (contents_file)
    quotes.close()
    check_profanity(contents_file)
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print (output)
    connection.close()
    if "true" in output:
        print ("Profanilty Alert!!")
    elif "false" in output:
        print ("This Document has no curse words!")
    else:
        print ("Could not scan the document properly.")

read_text()
