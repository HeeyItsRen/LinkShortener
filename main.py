import pyshorteners
if __name__ == "__main__":
    BASE_URL = input('URL to shorten: ')
    short = pyshorteners.Shortener()
    print (short.tinyurl.short(BASE_URL))