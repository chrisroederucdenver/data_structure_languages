# Data Structures Languages
Exploring and showing how some languages allow you to create a populated structure out of maps/dictionaries, lists and tuples.
Because of how easy it is to read JSON into javascript, our FHIR work being JSON, etc. This works with JSON, not XML. Stay tuned.

This exploration started as a way to understand the motivations for Whistle. Two things come to mind. One is that the paths to the data are a little simple in Whistle, though not overwhelmingly so. The translation between XML and JSON will color the Whistle code, and the translation/load from XML to Python. Second is how you don't have to create the structure before using it. In Perl they call this autovivification.
(as of this writing, I haven't written the Whistle yet, so take that with a grain of salt...) 

## Sample Data
from 	github.com://GoogleCloudPlatform/healthcare-data-harmonization

## Python
Python 3.8.1rc1
Most of the project here is Python

## JavaScript
Nashorn is no longer. Use V8 as part of node.js On mac, brew install node.

This is a small example to show the two ways you can write the paths down into a structure. JS gets a little awkward when accessing files because it's meant to run in a browser. Back ends are written in javascript, I haven't.

## Perl
I started to try and write this in Perl. I stopped because it's been a long time, and I got deep enough to see that while autovivification is cool, the paths are no better.

## Whistle
Google's data harmonization language, written in Java, has the disadvantage that it is a different and rare language, but it has simple paths and autovivification.

