from ObserverDp.Subject.subject import Subject

class WeatherStation(Subject):

    def __init__(self):
        super().__init__()
        self.temp = 0
        self.hum = 0

    def updateWeather(self, temp, hum):
        self.temp = temp
        self.hum = hum
        self.notify(self.temp, self.hum)
