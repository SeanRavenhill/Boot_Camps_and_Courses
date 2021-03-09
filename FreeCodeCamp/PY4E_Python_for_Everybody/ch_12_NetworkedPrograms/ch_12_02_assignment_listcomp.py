# See README.md for assignment briefs.
# Wanted to see if I could write a version using redaction
# and list comprehension.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')

total = sum([int(i.contents[0]) for i in tags])

print(total)

# Could also have redacted down to the below commented out line of code
# and not stored the result in a variable. 

# print(sum([int(i.contents[0]) for i in tags]))
