String = "Tutor Joes Computer Educations"
rev = ""
words = String.split()
for word in words:
    rev = word +" " + rev
print(rev)