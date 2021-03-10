Request-Response Cycle | ch_12_01_assigment.py:

Exploring the HyperText Transport Protocol

You are to retrieve the following document using the HTTP protocol in a way
that you can examine the HTTP Response headers.

http://data.pr4e.org/intro-short.txt
There are three ways that you might retrieve this web page and look
at the response headers:

- Preferred: Modify the socket1.py program to retrieve the above URL and print
out the headers and data. Make sure to change the code to retrieve the above
URL the values are different for each URL.

- Open the URL in a web browser with a developer console or FireBug and manually
  examine the headers that are returned.

Enter the header values in each of the fields below and press "Submit".

#Answers:

Last-Modified: Sat, 13 May 2017 11:22:22 GMT

ETag: "1d3-54f6609240717"

Content-Length: 467

Cache-Control: max-age=0, no-cache, no-store, must-revalidate

Content-Type: text/plain

################################################################################
################################################################################

Scraping HTML Data with BeautifulSoup | ch_12_02_assigment.py:

Scraping Numbers from HTML using BeautifulSoup In this assignment you will write
a Python program similar to http://www.py4e.com/code3/urllink2.py. The program
will use urllib to read the HTML from the data files below, and parse the data,
extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give
you the sum for your testing and the other is the actual data you need to
process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_941921.html (Sum ends with 66)

You do not need to save these files to your folder since your program will read
the data directly from the URL. Note: Each student will have a distinct data
url for the assignment - so only use your own data url for analysis.

Data Format
The file is a table of names and comment counts. You can ignore most of the
data in the file except for lines like the following:

<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

You are to find all the <span> tags in the file and pull out the numbers
from the tag and sum the numbers.

Look at the sample code provided. It shows how to find all of a certain kind
of tag, loop through the tags and extract the various aspects of the tags.

...
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   print 'URL:',tag.get('href', None)
   print 'Contents:',tag.contents[0]
   print 'Attrs:',tag.attrs

You need to adjust this code to look for span tags and pull out the text
content of the span tag, convert them to integers and add them up to
complete the assignment.

Sample Execution:
$ python3 solution.py
Enter - http://py4e-data.dr-chuck.net/comments_42.html
Count 50
Sum 2...

Turning in the Assignment

Enter the sum from the actual data and your Python code below:

#Answer:
Sum: 2066

################################################################################
################################################################################

Following Links with BeautifulSoup | ch_12_03_assigment.py:

Following Links in Python

In this assignment you will write a Python program that expands on
http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the
HTML from the data files below, extract the href= vaues from the anchor tags,
scan for a tag that is in a particular position relative to the first name in
the list, follow that link and repeat the process a number of times and report
the last name you find.

We provide two files for this assignment. One is a sample file where we give you
the name for your testing and the other is the actual data you need to process
for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat
this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah Last name in
sequence: Anayah

Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Shae.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat
this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: A

Strategy
The web pages tweak the height between the links and hide the page after a
few seconds to make it difficult for you to do the assignment without writing
a Python program. But frankly with a little effort and patience you can
overcome these attempts to make it a little harder to complete the assignment
without writing a Python program. But that is not the point. The point is to
write a clever Python program to solve the program.

Sample execution

Here is a sample execution of a solution:

$ python3 solution.py
Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Enter count: 4
Enter position: 3
Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html

The answer to the assignment for this execution is "Anayah".

Turning in the Assignment
Enter the last name retrieved and your Python code below:

#Answer:
Name: Artemis
