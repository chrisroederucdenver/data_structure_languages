# Data Structures Languages

Exploring and showing how some languages allow you to create a populated structure out of maps/dictionaries, lists and tuples, deeply, in the syntax of the language. The most obvious examle is JSON and JavaScript. LISPs have a similar idea. It's pretty easy to read JSON into structures of other languages like Python. The other side of the project here is what it looks like to build a path to an attribute deep in a structure like that and do it in the differen lanagues. Again this is straight forward in JS, also in Python and Perl. 

XML makes things a little different. One option is to read the XML into native language structures, and another is XPath. Xpath is compelling for one of the projects here, CCDA, because the standards are written in XPath.

This exploration started as a way to understand the motivations for Whistle when converting FHIR data, especically when compared to Python. Two things come to mind. One is that the paths to the data are a little more simple in Whistle. Second is how you don't have to create the structure before using it. In Perl they call this autovivification. You don't see this when reading in JSON, but you do when writing to a destination structure.


## CCDA, XML and Xpath Python 

## JSON
### Sample Data
from 	github.com://GoogleCloudPlatform/healthcare-data-harmonization


### Python
Python 3.8.1rc1
Most of the project here is Python

### JavaScript
Nashorn is no longer. Use V8 as part of node.js On mac, brew install node.

This is a small example to show the two ways you can write the paths down into a structure. JS gets a little awkward when accessing files because it's meant to run in a browser. Back ends are written in javascript, I haven't.

### Perl
I started to try and write this in Perl. I stopped because it's been a long time, and I got deep enough to see that while autovivification is cool, the paths are no better.

### Whistle
Google's data harmonization language, written in Java, has the disadvantage that it is a different and rare language, but it has simple paths and autovivification.
- Java 11, (fails with Java 21 and Gradle 8)
- Gradle 7 
- git@github.com:GoogleCloudPlatform/healthcare-data-harmonization.git



