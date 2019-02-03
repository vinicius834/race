from process_data import get_pilots, race_result
from import_data import *

if __name__ == '__main__':
    race = read_race_log()
    race_result(race, get_pilots(race))