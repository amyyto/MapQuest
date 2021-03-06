# MapQuest

The following information is provided from the project guide:

This program will describe a trip taken between a sequence of locations, the goal being to travel from the first location to the second, then from the second location to the third, and so on, until reaching the last location. 

The program will not prompt the user in anyway and the user must know the precise input format.

Step 1:
An integer whose value is at least 2, alone on a line, that specifies how many locations the trip will consist of.
If there are n locations, the next n lines of input will each describe one location. Each location can be a city such as Irvine, CA, an address such as 4545 Campus Dr, Irvine, CA, or anything that the Open MapQuest API will accept as a location. (The details of what is acceptable as a location is described here. Your program won't need to validate this input, but you'll need to expect that you might not get a valid response if you use something that MapQuest won't accept; you'll need to experiment with the Open MapQuest API's to see how they respond to invalid locations.)

Step 2:
A positive integer (i.e., whose value is at least 1), alone on a line, that specifies how many outputs will need to be generated.
If there are m outputs, the next m lines of input will each describe one output. Each output can be one of the following:
STEPS for step-by-step directions, meaning a brief description of each maneuver (e.g., a turn, entering or exiting a freeway, etc.) you would have to make to drive from one location to another

Step 3:
TOTALDISTANCE for the total distance traveled if completing the entire trip

TOTALTIME for the total estimated time to complete the entire trip

LATLONG for the latitude and longitude of each of the locations specified in the input

ELEVATION for the elevation, in feet, of each of the locations specified in the input
