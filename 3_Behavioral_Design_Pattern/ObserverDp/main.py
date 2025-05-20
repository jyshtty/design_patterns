import time

from ObserverDp.Observer.zomato import Zomato
from ObserverDp.Observer.display import Display
from ObserverDp.Subject.weatherStation import WeatherStation

if __name__ == "__main__":
    zomato = Zomato()
    display = Display()

    ws = WeatherStation()

    zomato.subscribeToSubject(ws)
    display.subscribeToSubject(ws)

    ws.updateWeather(10, 50)
    time.sleep(2)
    ws.updateWeather(20, 100)
    time.sleep(2)

    ws.updateWeather(5, 60)
    time.sleep(2)

    zomato.unsubscribeToSubject(ws)

    ws.updateWeather(60, 10)
    time.sleep(2)

    ws.updateWeather(10, 10)
    time.sleep(2)

    ws.updateWeather(10, 160)




