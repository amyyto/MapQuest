### #Amy Vo 29305960 Project 3 Lab 2 ###

#This module contains the classes that will carry out the
#different options that the user wishes for their information to be displayed.

#This class will return step by step directions
class steps:
    def __init__(self,x):
        self._x = x
    def map_it(self):
        directions = '\nDIRECTIONS\n'
        for i in self._x['route']['legs']:
            for w in i['maneuvers']:
                directions += str(w['narrative']) + '\n'
        return directions
    
#This class will return the total distance        
class distance:
    def __init__(self,x):
        self._x = x
    def map_it(self):
        y = self._x['route']['distance']
        distance = str(round(y))
        return('Total Distance: ' + distance + ' miles\n')

#This class will return the total time        
class time:
    def __init__(self,x):
        self._x = x
    def map_it(self):
        seconds = self._x['route']['time']
        minutes = str(round(seconds/60))
        return ('Total Time: ' + minutes + ' minutes\n')

#This class will return the longtitude and latitude        
class lat_long:
    def __init__(self,x):
        self._x = x
    def map_it(self):
        lat_and_long = ''

        for i in self._x['route']['locations']:
            y = i['latLng']['lat']
            if y > 0:
                latitude = str(round(y, 2)) + 'N'           
            else:
                latitude = str(round(abs(y), 2)) + 'S'
            z = i['latLng']['lng']
            if z < 0:
                longtitude = str(round(abs(z), 2)) + 'W'
            else:
                longtitude = str(round(z, 2)) + 'E'
            lat_and_long += latitude + ' ' + longtitude + '\n'
        return lat_and_long
            
    
