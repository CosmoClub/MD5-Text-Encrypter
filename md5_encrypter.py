import hashlib
print("Enter text to be encrypted: ")
text=input()
print("Text: ",text)
encrypt=hashlib.md5(text.encode())
print("The encrypted text is: ",encrypt.hexdigest())


