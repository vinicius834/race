

from src import import_data, process_data, models

if __name__ == '__main__':
    race = import_data.read_race_log()
    process_data.race_result(race, process_data.get_pilots(race))