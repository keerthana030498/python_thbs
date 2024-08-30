sentence = "To change the overall look your document. To change the look available in the gallery"
new_sentence = sentence.split()
mydict = {}
for words in new_sentence:
    if words in mydict:
        mydict[words] += 1
    else:
        mydict[words] =1
print(mydict)
