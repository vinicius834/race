from race.process_data import *
from race.import_data import *
import unittest

class TestImportData(unittest.TestCase):
    def test_read_race_log(self):
        self.assertTrue(len(read_race_log()) > 0)

class TestProcessData(unittest.TestCase):
    def setUp(self):
        self.race = read_race_log()

    def test_get_pilots(self):
        pilots = get_pilots(self.race)
        self.assertTrue(len(pilots) > 0)
        self.assertTrue(pilots[0].pilot_name)

    def test_get_pilots_cod(self):
        expected_pilot_cod = "038"
        pilots_cod = get_pilots_cod(self.race)
        self.assertTrue(len(pilots_cod) > 0)
        self.assertIn(expected_pilot_cod,pilots_cod)

    def test_get_total_time_and_laps_number_by_pilot(self):
        pilot_cod = "038"
        total_race_laps = 4
        data = get_total_time_and_laps_number_by_pilot(self.race, pilot_cod)
        self.assertEqual(pilot_cod, data[PILOT_COD_LITERAL])
        self.assertEqual(total_race_laps, data[TOTAL_LAPS_LITERAL])

    def test_get_best_lap_by_pilot_first_lap(self):
        pilot_cod = "038"
        race_item = [item for item in self.race if pilot_cod == item.pilot_cod][0]
        best_lap_time = dt.strptime("00:00.000", "%M:%S.%f").time()
        lap_time = dt.strptime(race_item.lap_time, "%M:%S.%f").time()
        result_best_lap = get_best_lap_by_pilot(lap_time, best_lap_time)
        self.assertEqual(lap_time, result_best_lap)

    def test_get_best_lap_by_pilot(self):
        pilot_cod = "038"
        race_item = [item for item in self.race if pilot_cod == item.pilot_cod][0]
        best_lap_time = dt.strptime("01:00.000", "%M:%S.%f").time()
        lap_time = dt.strptime(race_item.lap_time, "%M:%S.%f").time()
        result_best_lap = get_best_lap_by_pilot(lap_time, best_lap_time)
        self.assertEqual(best_lap_time, result_best_lap)

    def test_best_race_lap(self):
        race = self.get_race()
        expected_best_race_lap = dt.strptime(race[0].lap_time, "%M:%S.%f").time()
        best_race_lap = get_best_race_lap(race)
        self.assertEqual(expected_best_race_lap, best_race_lap)

    def test_get_positions(self):
        race = self.get_race()
        result = get_positions(race)
        self.assertEqual(race[0].pilot_cod, result[0][PILOT_COD_LITERAL])

    def get_race(self):
        race1 = Race('23:49:08.277', '038', 'F. MASSA', 1, '1:02.852', '44,275')
        race2 = Race('23:49:10.858', '033', 'R.BARRICHELLO', 1, '1:04.352', '43,243')
        race3 = Race('23:49:11.075', '002', 'K.RAIKKONEN', 1, '1:04.108', '43,408')
        return [race1, race2, race3]

if __name__ == '__main__':
    unittest.main()