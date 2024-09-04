s = "I am keer, how are you"
parts = s.split(",")

firstpart = parts[0].split()
secondpart = parts[1].split()

rev1 = firstpart[::-1]
rev2 = secondpart[::-1]

reverse_Sentence = (" ".join(rev1) + "," + " ".join(rev2))
print(reverse_Sentence)