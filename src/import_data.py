from .models import *

def read_race_log():
    race_data = {}
    race_list = []
    with open('race_log.txt', 'r') as log_file:
        read_data = log_file.readlines()
        for row in read_data:
            r = row.split()
            r.remove('–')
            race_data['hour'], race_data['pilot_cod'], race_data['pilot_name'], race_data['lap_number'], race_data['lap_time'], race_data['average_lap_speed'] = r
            race_list.append(Race(race_data['hour'], race_data['pilot_cod'], race_data['pilot_name'], race_data['lap_number'], race_data['lap_time'], race_data['average_lap_speed']))
    return race_list