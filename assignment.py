"""
COMP1730/6730 assignment template.

Collaborators: <your group's university IDs here>
"""

import csv
import random
import re
import numpy as np

def load_stops(path):
    '''
    Load a csv file with bus stop information.
    The argument should be a string, which is the path to the file.
    The return value is a list of stops, as described in the assignment
    specification.
    '''
    with open(path) as bus_stop_file:
        reader = csv.reader(bus_stop_file)
        next(reader) # skip header
        return [ (int(id_), float(lat), float(lon), name)
                 for id_, lat, lon, name in reader]
    
def load_routes(path):
    '''
    Load a csv file with bus route information.
    The argument should be a string, which is the path to the file.
    The return value is a list of routes, as described in the assignment
    specification.
    '''
    with open(path) as routes_file:
        reader = csv.reader(routes_file)
        return [
            (route[0], [int(stop) for stop in route[1:]])
            for route in reader]

def print_journey(journey):
    '''
    Print a bus journey.
    The argument should be a valid journey data structure, as
    described in the assignment specification.
    The function does not return a value.
    '''
    print('Start at {}.'.format(journey[0][1]))
    for stop_number, (route, stop_a, stop_b) in enumerate(journey):
        print('{}. Take {} from {} to {}.'.format(
            stop_number + 1, route, stop_a, stop_b))
    print('Arrived at {}.'.format(journey[-1][2]))


# Question 1

def southernmost_stop(stops):
    return


def closest_stop_to_csit(stops):
    return


def most_common_number(routes):
    return


def most_stops(routes):
    return


# Question 2

def find_route(stops, routes, stop_a, stop_b):
    return


# Question 3

def random_bus_journey(stops, routes, first_stop, n_repeats):
    return


# Question 4

def find_path(stops, routes, stop_a, stop_b):
    map = {}



# Question 5a

def load_times(path):
    return


# Question 5b

def time_journey(journey, stops, routes, times):
    return


if __name__ == '__main__':
    # You can write any testing of your function that you want to
    # run here. The following is just an example, showing how to
    # use the loading function and the print_journey function.
    
    stops = load_stops('bus_stops.csv')
    routes = load_routes('bus_routes.csv')

    # example_journey = [("10 Denman Prospect", "City West Marcus Clarke St", "Cotter Rd After Streeton Dr"),
    #                    ("10 Denman Prospect", "Cotter Rd After Streeton Dr", "Holborow Av after Greenwood St")]
    # print_journey(example_journey)
    map = {}
    for i in range(len(routes)):
        line = routes[i][1]
        # print(line)
        for j in range(len(line)):
            if j == 0:
                (map.setdefault(line[j], set())).add(line[j+1])
            elif j == len(line)-1:
                # (map.setdefault(line[j], set())).add(line[j-1])
                pass

            else:
                (map.setdefault(line[j], set())).add(line[j+1])
                # (map.setdefault(line[j], set())).add(line[j-1])
    for key, value in map.items():
        print('{key}: {value}'.format(key=key, value=value))




    # Question 1
    # print('southernmost_stop:', southernmost_stop(stops, routes))
    # print('closest_stop_to_csit:', closest_stop_to_csit(stops, routes))
    # print('most_routes:', most_routes(stops, routes))
    # print('most_stops:', most_stops(stops, routes))

    # Question 2
    # print('To get from stop 533 to stop 1070, catch bus',
    #       'find_route(stops, routes, stops[533], stops[1070]))

    # Question 3
    # maeve_journey = random_bus_journey(stops, routes, stops[533], 5)
    # print('Maeve\'s journey:', maeve_journey)

    # Question 4
    # print('The route between City West and the Old Bus Depot Markets is',
    #       find_path(stops, routes,
    #                 stops[533], stops[851]))



    # Question 5a
    # times = load_times('times.csv')

    # Question 5b
    # print('Maeve\'s journey took',
    #       time_journey(maeve_journey, stops, routes, times),
    #       'minutes.')

    # Don't forget that your answers to Question 6 (written individual
    # report) must be provided in a separate file (answers.pdf).
