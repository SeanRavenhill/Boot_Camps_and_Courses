Extracting Data from XML | ch_13_01_assignment.py:
--------------------------------------------------------------------------------

In this assignment you will write a Python program somewhat similar to
http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read
the XML data from that URL using urllib and then parse and extract the comment
counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give
you the sum for your testing and the other is the actual data you need to
process for the assignment.

- Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
- Actual data: http://py4e-data.dr-chuck.net/comments_941923.xml (Sum ends with 14)

You do not need to save these files to your folder since your program will read
the data directly from the URL. Note: Each student will have a distinct data url
for the assignment - so only use your own data url for analysis.

Data Format and Approach
The data consists of a number of names and comment counts in XML as follows:

<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>

You are to look through all the <comment> tags and find the <count> values
sum the numbers. The closest sample code that shows how to parse XML is
geoxml.py(https://bit.ly/3bcrqP0). But since the nesting of the elements
in our data is different than the data we are parsing in that sample code
you will have to make real changes to the code.

To make the code a little simpler, you can use an XPath selector string
to look through the entire tree of XML for any tag named 'count' with the
following line of code:

counts = tree.findall('.//count')

Take a look at the Python ElementTree documentation and look for the supported
XPath syntax for details. You could also work from the top of the XML down to
the comments node and then loop through the child nodes of the comments node.

Sample Execution

$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
Retrieved 4189 characters
Count: 50
Sum: 2...

Turning in the Assignment

Enter the sum from the actual data and your Python code below:

Sum: (ends with 14)

#Answer:
Sum: 2614

################################################################################
################################################################################

Extracting Data from JSON | ch_13_02_assigment.py:
--------------------------------------------------------------------------------

In this assignment you will write a Python program somewhat similar to
http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read
the JSON data from that URL using urllib and then parse and extract the comment
counts from the JSON data, compute the sum of the numbers in the file and enter
the sum below:

We provide two files for this assignment. One is a sample file where we give
you the sum for your testing and the other is the actual data you need to
process for the assignment.

- Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
- Actual data: http://py4e-data.dr-chuck.net/comments_941924.json (Sum ends with 65)

You do not need to save these files to your folder since your program will read
the data directly from the URL. Note: Each student will have a distinct data url
for the assignment - so only use your own data url for analysis.

Data Format
The data consists of a number of names and comment counts in JSON as follows:

{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}

The closest sample code that shows how to parse JSON and extract a list is
json2.py(https://bit.ly/3baLam7). You might also want to look at
geoxml.py(https://bit.ly/3kG1tub) to see how to prompt for a URL and retrieve
data from a URL.

Sample Execution

$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...

Turning in the Assignment

Enter the sum from the actual data and your Python code below:

Sum:(ends with 65)

#Answer:
Sum: 2665

################################################################################
################################################################################

Calling a JSON API | ch_13_03_assigment.py:
--------------------------------------------------------------------------------

In this assignment you will write a Python program somewhat similar to
http://www.py4e.com/code3/geojson.py. The program will prompt for a location,
contact a web service and retrieve JSON for the web service and parse that data,
and retrieve the first place_id from the JSON. A place ID is a textual
identifier that uniquely identifies a place as within Google Maps.

API End Points

To complete this assignment, you should use this API endpoint that has a
static subset of the Google Data:

http://py4e-data.dr-chuck.net/json?

This API uses the same parameter (address) as the Google API. This API also has
no rate limit so you can test as often as you like. If you visit the URL with
no parameters, you get "No address..." response.

To call the API, you need to include a key= parameter and provide the address
that you are requesting as the address= parameter that is properly URL encoded
using the urllib.parse.urlencode() function as shown
in http://www.py4e.com/code3/geojson.py

Make sure to check that your code is using the API endpoint is as shown above.
You will get different results from the geojson and json endpoints so make
sure you are using the same end point as this autograder is using.

Test Data / Sample Execution

You can test to see if your program is working with a location of
"South Federal University" which will have a place_id
of "ChIJ1Z9sheJZkFQRDePQqQebCdg".

$ python3 solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 2275 characters
Place id ChIJ1Z9sheJZkFQRDePQqQebCdg

Turn In

Please run your program to find the place_id for this location:

Washington State University

Make sure to enter the name and case exactly as above and enter the place_id
and your Python code below. Hint: The first seven characters of the place_id
are "ChIJb6h ..."

Make sure to retreive the data from the URL specified above and not the
normal Google API. Your program should work with the Google API -
but the place_id may not match for this assignment.

#Answer:
place_id: ChIJb6hIyAWHn1QR23BXtaTyZfQ
