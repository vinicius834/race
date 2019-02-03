from models import *
from datetime import timedelta, datetime as dt
from decimal import *

PILOT_COD_LITERAL = 'pilot_cod'
TOTAL_LAPS_LITERAL = 'total_laps'
TOTAL_TIME_LITERAL = 'total_time'
BEST_LAP_TIME_LITERAL = 'best_lap_time'

def sort_by_laps_number(race):
    race.sort(key=lambda x: x.lap_number)
    return race

def get_pilots(race):
    pilots = list({(item.pilot_cod, item.pilot_name) for item in race})
    pilots = [Pilot(item[0], item[1]) for item in pilots]
    return pilots

def get_pilots_cod(race):
    return set([item.pilot_cod for item in get_pilots(race)])

def get_positions(race):
    pilots_cod = get_pilots_cod(race)
    results = list(map(lambda pilot_cod: get_total_time_and_laps_number_by_pilot(race, pilot_cod), pilots_cod))
    return calc_final_position(results)

def get_total_time_and_laps_number_by_pilot(race, pilot_cod):
    total_time = timedelta(hours=0,minutes=0, seconds=0, microseconds=0)
    laps = 0
    best_lap_time = dt.strptime("00:00.000", "%M:%S.%f").time()
    for race_item in race:
        if race_item.pilot_cod == pilot_cod:
            lap_time = dt.strptime(race_item.lap_time, "%M:%S.%f").time()
            best_lap_time = get_best_lap_by_pilot(lap_time, best_lap_time)
            total_time += timedelta(minutes=lap_time.minute, seconds=lap_time.second, microseconds=lap_time.microsecond)
            laps = int(race_item.lap_number)

    return {PILOT_COD_LITERAL: pilot_cod, TOTAL_TIME_LITERAL: total_time, TOTAL_LAPS_LITERAL: laps, BEST_LAP_TIME_LITERAL: best_lap_time}

def get_best_lap_by_pilot(lap_time, best_lap_time):
    aux = dt.strptime("00:00.000", "%M:%S.%f").time()
    if aux == best_lap_time or best_lap_time > lap_time:
        return lap_time
    else:
        return best_lap_time

def get_best_race_lap(race):
    best_lap_time = dt.strptime("00:00.000", "%M:%S.%f").time()
    for race_item in race:
        lap_time = dt.strptime(race_item.lap_time, "%M:%S.%f").time()
        best_lap_time = get_best_lap_by_pilot(lap_time, best_lap_time)
    return best_lap_time

def get_average_speed_by_pilot(race, pilot_cod):
    race_items = list(filter(lambda race_item: race_item.pilot_cod == pilot_cod, race))
    average_speed = 0
    for race_item in race_items:
        average_speed += Decimal(race_item.average_lap_speed.replace(',', '.'))
    return round(average_speed/len(race_items), 3)

def calc_final_position(results):
    results.sort(key=lambda individual_result: (individual_result['total_time']))
    results.sort(key=lambda individual_result: (individual_result['total_laps']), reverse=True)
    return results

def race_result(race, pilots):
    positions = get_positions(race)
    index = 1
    final_result = []
    time_winner = positions[0][TOTAL_TIME_LITERAL]
    for position in positions:
        pilot = list(filter(lambda pilot: (pilot.pilot_cod == position[PILOT_COD_LITERAL]), pilots))[0]
        time_after_winner = position[TOTAL_TIME_LITERAL] - time_winner
        result = Result(index, pilot.pilot_cod, pilot.pilot_name, position[TOTAL_LAPS_LITERAL], position[TOTAL_TIME_LITERAL], position[BEST_LAP_TIME_LITERAL], get_average_speed_by_pilot(race, pilot.pilot_cod), time_after_winner)
        final_result.append(result)
        index += 1
    best_race_lap = get_best_race_lap(race)
    report(final_result, best_race_lap)

def report(final_result, best_lap_race):
    print('{:<20} {:<20} {:<16} {:<18} {:<18} {:<18} {}'.format('Final Position', 'Pilot Cod', 'Pilot Name', 'Completed Laps', 'Total Race Time', 'Best Lap', 'Average Speed'))
    for result in final_result:
        print('{:<20} {:<20} {:<16} {:<18} {:<18} {:<18} {:<18} +({})'
                         .format(str(result.final_position) + '°', result.pilot_cod, result.pilot_name, result.total_laps, str(result.total_race_time), str(result.best_lap_time), result.average_speed, str(result.time_after_winner)))

    print('\nBest Race Lap: {best_lap_race}'.format(best_lap_race=best_lap_race))


