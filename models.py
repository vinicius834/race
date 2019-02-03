class Pilot(object):
    def __init__(self, pilot_cod, pilot_name):
        self.pilot_cod = pilot_cod
        self.pilot_name = pilot_name

class Race(object):
    def __init__(self, hour, pilot_cod, pilot_name, lap_number, lap_time, average_lap_speed):
        self.hour = hour
        self.pilot_cod = pilot_cod
        self.pilot_name = pilot_name
        self.lap_number = lap_number
        self.lap_time = lap_time
        self.average_lap_speed = average_lap_speed

    def __str__(self):
        return "{0} - {1} - {2} - {3}".format(self.pilot_cod, self.pilot_name, self.lap_number, self.lap_time)

class Result(object):
    def __init__(self, final_position, pilot_cod, pilot_name, total_laps, total_race_time, best_lap_time, average_speed, time_after_winner):
        self.final_position = final_position
        self.pilot_cod = pilot_cod
        self.pilot_name = pilot_name
        self.total_laps = total_laps
        self.total_race_time = total_race_time
        self.best_lap_time = best_lap_time
        self.average_speed = average_speed
        self.time_after_winner = time_after_winner
