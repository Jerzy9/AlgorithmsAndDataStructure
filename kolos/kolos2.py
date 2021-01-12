def wczytaj_text():
    text = ""

    try:
        file = open("zadanie2.txt")
        text = file.read()

    except FileNotFoundError:
        print("nieznaleziono pliku")

    return text


def szyfrowanie_kolumnowe(text, n):
    text = text.replace(" ", "")
    res = ""
    for i in range(n):
        for j in range(i, len(text), n):
           res += text[j]

    return res


# text = "ALGORYTMY I STRUKTURY DANYCH"
n = 5
text = wczytaj_text()
print(text)
print(szyfrowanie_kolumnowe(text, n))