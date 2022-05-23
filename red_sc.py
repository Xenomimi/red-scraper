import requests

a = input("Podaj link do zdjęcia: ")
nazwa = input("Podaj nazwe pliku")
r = requests.get(a)

f = open(nazwa+".png", "wb")
f.write(r.content)
f.close()
print("Pobrano zdjęcie! :)")
