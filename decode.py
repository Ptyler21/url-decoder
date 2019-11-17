import urllib
from urllib import parse

decoded_url = "https://github.com/Ptyler21/url-decoder"

encoded_url = "https%3A%2F%2Fgithub.com%2FPtyler21%2Furl-decoder"


decodedString = urllib.parse.unquote(encoded_url)

print(decodedString)