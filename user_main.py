### Amy Vo 29305960 Project 3 Lab 2 ###

#Taken from Project 3 Directions#
#This program will describe a trip taken between a sequence of locations,
#the goal being to travel from the first location to the second, then from
#the second location to the third, and so on, until reaching the last location.
#Based on the user's input, it will show different information about the trip,
#such as turn-by-turn directions, distances and times, etc.


import classes
import mapquest_API

def get_addresses():
    '''Takes in how many addresses and their total'''
    num_addresses = int(input())
    addresses_list = []
    for i in range(num_addresses):
        address = str(input())
        addresses_list.append(address)
    return addresses_list

def get_output_options():
    '''Takes in how many kinds of different options to display information'''
    num_options = int(input())
    outputs_list = []
    for i in range(num_options):
        output = str(input())
        outputs_list.append(output)
    return outputs_list       

def main():
    '''Main function to run functions amd make program run altogether'''
    a = get_addresses()
    g = get_output_options()
    outputs_list2 = []
    search_url = mapquest_API.build_search_url(a)
    json = mapquest_API.get_result(search_url)
  
    
    for output in g:
        if output == 'STEPS':
            mapping = classes.steps(json)
        elif output == 'TOTALDISTANCE':
            mapping = classes.distance(json)
        elif output == 'TOTALTIME':
            mapping = classes.time(json)
        elif output == 'LATLONG':
            mapping = classes.lat_long(json)
        outputs_list2.append(mapping.map_it())
    for i in outputs_list2:
        print(i)

if __name__ == '__main__':
    main()
    print('')
    print('')
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
