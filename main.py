text = input("Ievadiet tekstu: ")
def delete (text):
  if text.count("e")>0:
   text = text.replace("e"," ")
   print(text.upper())
  else:
   text - "TEKSTS NESATUR VAJADZIGO BURTU."
  return text
delete(text)
