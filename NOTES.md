## PERSONAL NOTES
I have never used Python or Flask in an application, nor have I worked with XML data before. I pivoted several times to find a XML to HTML or XML to JSON module package that would work for me.

## GOALS REMAINING (see below)
1. Add the address to database front to back - can delete but not add with mysql.connection.commit() - expanded thoughts below
2. Working search - no errors but does not parse data to the page. Code works in Python shell

## WHAT WORKED
1. USPSApi extension for Python - prints correct address to shell (used childhood address as a test)
2. mySQL database - was able to create table and add dummy data through MySQL Workbench & connect to flask

## WHAT WAS WORKING - AND THEN WASN'T
1. Was able to add to database from localhost at one point - but stopped being able to and cannot figure out why address will not commit to the database. Have re-typed code several times from docs, StackOverflow and various online sources and data will not commit to database. However can delete with the same syntax.

## WHAT DIDN'T WORK
1. 'name' is a reserved item with mySQL so had to change to 'surname'
2. zipcode_ext (extra 4 digits) made the content look cluttered - removed as an option from database and code

## NEEDS TO BE FIXED
1. Database connection needs to be in it's own file (has username and password - security issue)
2. USPSAPI username needs to be in it's own file as well (security issues)
2. Figure out why the search will not return any errors but works in shell??
3. Figure out why the database is only running one way (back to front)
4. Tighten up the CSS

## NEEDS TO BE ADDRESSED LATER
1. Log in & authentication as address book may be considered private data. Also required so name (Jasmine) isn't hard coded
2. Making address book address drop downs or modals - show name or address_1 and the rest in a drop down or modal
3. Making addresses sortable by name or state
4. Allow addresses to be edited (button is on page, but disabled)

## QUESTIONS
1. mysql.connection.commit() works to delete an address but will not add to database - why? I have come across nearly the exact same code in several places online and what I have should work
2. I am missing an extra step in the API search going from Python shell to the app - what is it?