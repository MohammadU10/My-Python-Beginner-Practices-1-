
# A Search Engine Function that Finds a Specific Character Or Word in the Given Text :
def search(txt, wd):
    """ You are working on a Search Engine. Watch your back Google!
    The given code takes a text and a word as input and passes them to a function called search().
    The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not. """
    
    if wd in txt:
        return "Word found"
    else:
        return "Word not found"


text = input("Enter Your Text: ")
word = input("Enter a Word: ")

print(search(text, word))


# Also Link to My Course Certificate: "https://www.sololearn.com/certificates/CC-AZDSOA4W"