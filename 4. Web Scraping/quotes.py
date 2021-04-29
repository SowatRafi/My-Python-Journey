from urllib.request import urlopen as UReq
from bs4 import BeautifulSoup as Bsoup


def Printing():
    print()
    for quote in quotes:
        fav_quote = quote.findAll("p", {"class": "aquote"})
        aquote = f'{fav_quote[0].text.strip().capitalize()}'

        fav_authors = quote.findAll("p", {"class": "author"})
        author = f"- {fav_authors[0].text.strip().upper()}\n"
        print(aquote)
        print(author)


def SAVE_AS_TXT(quote, author):
    with open("Quotes.txt", 'a', encoding="utf-8") as f:
        f.write(f"{quote}\n")
        f.write(f"{author}\n")


quotes_page = 'https://bluelimelearning.github.io/my-fav-quotes/'
UClient = UReq(quotes_page)
page_html = UClient.read()
UClient.close()

page_soup = Bsoup(page_html, "html.parser")
quotes = page_soup.findAll("div", {"class": "quotes"})
print(len(quotes))
# print(quotes[1])
# print(page_soup.h1.text.strip())

ask1 = str(input("Do you want to save all of these in a text?\n- (Yes/y) "))
if ask1.lower().strip() == "yes" or ask1.upper().strip() == "Y":
    keyAuthor = []
    values = []
    for quote in quotes:
        fav_quote = quote.findAll("p", {"class": "aquote"})
        aquote = f'{fav_quote[0].text.strip().capitalize()}'

        fav_authors = quote.findAll("p", {"class": "author"})
        author = f"- {fav_authors[0].text.strip().upper()}\n"
        print(aquote)
        print(author)
        keyAuthor.append(author)
        values.append(aquote)
    zipObj = zip(keyAuthor, values)
    dictOf = dict(zipObj)

    for key, value in dictOf.items():
        SAVE_AS_TXT(quote=value, author=key)

else:
    print("Okay your wish.\n")
    ask1 = str(input("Do you want to save `line by line` in a text?\n- (Yes/y) "))
    if ask1.lower().strip() == "yes" or ask1.upper().strip() == "Y":
        for quote in quotes:
            fav_quote = quote.findAll("p", {"class": "aquote"})
            aquote = f'{fav_quote[0].text.strip().capitalize()}'

            fav_authors = quote.findAll("p", {"class": "author"})
            author = f"- {fav_authors[0].text.strip().upper()}\n"
            print(aquote)
            print(author)
            ask3 = str(input("Do you want to save this line in a text?\n- (Yes/y) "))
            if ask3.lower().strip() == "yes" or ask3.upper().strip() == "Y":
                SAVE_AS_TXT(quote=aquote, author=author)

    else:
        Printing()

# !python3 quotes.py > Quotes.txt
