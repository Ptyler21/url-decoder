import urllib
from urllib import parse


def decode_me(encoded_url):

    decodedString = urllib.parse.unquote(encoded_url)
    print(decodedString)