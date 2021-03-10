Single Table SQL | ch_15_01_assignment.py:
--------------------------------------------------------------------------------

Instructions:

If you don't already have it, install the SQLite Browser
from http://sqlitebrowser.org/.

Then, create a SQLITE database or use an existing database and create a table
in the database called "Ages":

CREATE TABLE Ages (
  name VARCHAR(128),
  age INTEGER
)

Then make sure the table is empty by deleting any rows that you previously
inserted, and insert these rows and only these rows with the
following commands:

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Tyson', 24);
INSERT INTO Ages (name, age) VALUES ('Elliot', 15);
INSERT INTO Ages (name, age) VALUES ('Munachi', 33);
INSERT INTO Ages (name, age) VALUES ('Makenna', 21);
INSERT INTO Ages (name, age) VALUES ('Lennan', 33);

Once the inserts are done, run the following SQL command:

SELECT hex(name || age) AS X FROM Ages ORDER BY X

Find the first row in the resulting record set and enter the long string
that looks like 53656C696E613333.

Note: This assignment must be done using SQLite - in particular,
the SELECT query above will not work in any other database.
So you cannot use MySQL or Oracle for this assignment.

--------------------------------------------------------------------------------

To get credit for this assignment, perform the instructions below and
enter the code you get here: *(See files ch_15_01_assigment.sqlite, ch_15_01_assigment.sqbpro)*

(Hint: starts with 456)

#Answer:
Code is: 456C6C696F743135

################################################################################
################################################################################

Counting Email in a Database | ch_15_02_assignment.py:
--------------------------------------------------------------------------------

Counting Organizations

This application will read the mailbox data (mbox.txt) and count the number of
email messages per organization (i.e. domain name of the email address) using
a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)

When you have run the program on mbox.txt upload the resulting database file
above for grading.

If you run the program multiple times in testing or with dfferent files,
make sure to empty out the data before each run.

You can use this code as a starting point for your application:
http://www.py4e.com/code3/emaildb.py.

The data file for this application is the same as in previous assignments:
http://www.py4e.com/code3/mbox.txt.

Because the sample code is using an UPDATE statement and committing the results
to the database as each record is read in the loop, it might take as long as a
few minutes to process all the data. The commit insists on completely writing
all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside
of the loop. In any database program, there is a balance between the number
of operations you execute between commits and the importance of not losing the
results of operations that have not yet been committed.

--------------------------------------------------------------------------------

To get credit for this assignment, perform the instructions below and
upload your SQLite3 database here: *(See file ch_15_02_assignment.sqlite)*

Hint: The top organizational count is 536.

You do not need to export or convert the database - simply upload the .sqlite
file that your program creates. See the example code for the use of the
connect() statement.

#-------------------------------#
for row in cur.execute(sqlstr):
    #print(str(row[0]), row[1])
#-------------------------------#
Print Results of above line of code from assignment program:

iupui.edu 536
umich.edu 491
indiana.edu 178
caret.cam.ac.uk 157
vt.edu 110
uct.ac.za 96
media.berkeley.edu 56
ufp.pt 28
gmail.com 25
et.gatech.edu 17

################################################################################
################################################################################

Multi-Table Database - Tracks | ch_15_03_assignment.py:
--------------------------------------------------------------------------------

This application will read an iTunes export file in XML and produce a
properly normalized database with this structure:

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);

If you run the program multiple times in testing or with different files,
make sure to empty out the data before each run.

You can use this code as a starting point for your application:
http://www.py4e.com/code3/tracks.zip. The ZIP file contains the Library.xml
file to be used for this assignment. You can export your own tracks from
iTunes and create a database, but for the database that you turn in for this
assignment, only use the Library.xml data that is provided.

To grade this assignment, the program will run a query like this on your
uploaded database and look for the data it expects to see:

SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3

The expected result of the modified query on your database is:
(shown here as a simple HTML table with titles)

Track                                  |  Artist  |   Album      |  Genre
Chase the Ace	                         |  AC/DC	  | Who Made Who |  Rock
D.T.	                                 |  AC/DC	  | Who Made Who |  Rock
For Those About To Rock (We Salute You)|  AC/DC	  | Who Made Who |	Rock

--------------------------------------------------------------------------------

To get credit for this assignment, perform the instructions and upload your
SQLite3 database here: *(See files ch_15_03_assignment.sqlite, ch_15_03_assignment.sqbpro)*

You do not need to export or convert the database - simply upload the .sqlite
file that your program creates. See the example code for the use of the
connect() statement.

################################################################################
################################################################################

Many Students in Many Courses - Tracks | ch_15_04_assignment.py:
--------------------------------------------------------------------------------

This application will read roster data in JSON format, parse the file,
and then produce an SQLite database that contains a User, Course,
and Member table and populate the tables from the data file.

You can base your solution on this code:
http://www.py4e.com/code3/roster/roster.py - this code is incomplete as you
need to modify the program to store the role column in the Member table to
complete the assignment.

Each student gets their own file for the assignment. Download this file and
save it as roster_data.json. Move the downloaded file into the same folder
as your roster.py program.

Once you have made the necessary changes to the program and it has been run
successfully reading the above JSON data, run the following SQL command:

SELECT User.name,Course.title, Member.role FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;

The output should look as follows:

Ziyaan|si334|0
Zidane|si364|0

Once that query gives the correct data, run this query:

SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;

You should get one row with a string that looks like XYZZY53656C696E613333.

--------------------------------------------------------------------------------

To get credit for this assignment, perform the instructions below and enter
the code you get here: (Hint: starts with XYZZY41616)

*(See files ch_15_04_assignment.sqlite, ch_15_04_assignment.sqbpro)*

#Answer:
Code: XYZZY41616D6E61736934323230
