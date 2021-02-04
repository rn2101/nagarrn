from textblob import TextBlob

text = input("Enter text here=> ")
blob = TextBlob(text)

print("searching language\n", blob.detect_language())

print("Translate to")
print("1. Hindi\t 2. English\t 3. Urdu\t 4. Spanish\t 5. French-:")
to = int(input("Enter your choice=> "))
if 5 < to < 1:
    print("Wrong choice")
    exit()
elif to == 1:
    to = 'en'
elif to == 2:
    to = 'hi'
elif to == 3:
    to = 'ar'
elif to == 4:
    to = 'ur'
else:
    to = 'fr'
print("\nTranslating\n")

print(blob.translate(to=to))
