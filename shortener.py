#made by kingbob
#credit me
#!/usr/bin/python3
import urllib.request


#mui
print("[+] TinyURL Link Shortener by kingbobPy")
print("[+] Github : https://github.com/kingbobPy")
print("[+] Usage : python3 shortener.py")
linkurl = input("[>] URL > ")
print('\n')

def tiny_url(url):
    apiurl = "http://tinyurl.com/api-create.php?url="
    tinyurl = urllib.request.urlopen(apiurl + url).read()
    return tinyurl.decode("utf-8")

print(tiny_url(linkurl))