# Future proof solution where new displays can be added with ease

from random import uniform

class DisplayElement:
  def display(self):
    """Overrides DisplayElement.display()"""
    pass


class Observer:
  def update(self, temperature, humidity, pressure):
    """Overrides Observer.update()"""
    pass


class CurrentConditionsDisplay(Observer):

  def __init__(self):
    # Private vars start with double underscore
    self.__temperature = 0
    self.__humidity = 0
    self.__pressure = 0

  def update(self, temperature, humidity, pressure):
    self.__temperature = temperature
    self.__humidity = humidity
    self.__pressure = pressure
    self.display()

  def display(self):
    print("!!!!!!!!!!!!!!!!!!!!!")
    print("Displaying current conditions:")
    print("Temperature: ", self.__temperature)
    print("Humidity: ", self.__humidity)
    print("Pressure: ", self.__pressure)
    print("!!!!!!!!!!!!!!!!!!!!!")


class StatsDisplay(Observer):
  def __init__(self):
    self.__temperatures = [0]
    self.__humidities = [0]
    self.__pressures = [0]

  def update(self, temperature, humidity, pressure):
    self.__temperatures.append(temperature)
    self.__humidities.append(humidity)
    self.__pressures.append(pressure)
    self.display()

  def display(self):
    print("#######################")
    print("Displaying stats:")
    print("Temperature: ", sum(self.__temperatures)/len(self.__temperatures))
    print("Humidity: ", sum(self.__humidities)/len(self.__humidities))
    print("Pressure: ", sum(self.__pressures)/len(self.__pressures))
    print("#######################")


class ForecastDisplay(Observer):

  def __init__(self):
    self.__temperature = 0
    self.__humidity = 0
    self.__pressure = 0

  def update(self, temperature, humidity, pressure):
    self.__temperature = temperature + uniform(-5, +5)
    self.__humidity = humidity + uniform(-10, +10)
    self.__pressure = pressure
    self.display()

  def display(self):
    print("-----------------")
    print("Displaying forecast:")
    print("Temperature: ", self.__temperature)
    print("Humidity: ", self.__humidity)
    print("Pressure: ", self.__pressure)
    print("-----------------")


class WeatherData:

  def __init__(self):
    self.__observers = []

    self.__temperature = 0
    self.__humidity = 0
    self.__pressure = 0

  def subscribe(self, observer):
    self.__observers.append(observer)

  def notify_subscribers(self):
    for o in self.__observers:
      o.update(self.__temperature, self.__humidity, self.__pressure)

  def get_temperature(self):
    return uniform(5, 30)

  def get_humidity(self):
    return uniform(10, 60)
  
  def get_pressure(self):
    return 1013

  def measurementsChanged(self):
    # Main business logic
    self.__temperature = self.get_temperature()
    self.__humidity = self.get_humidity()
    self.__pressure = self.get_pressure()

    # Update the observers
    self.notify_subscribers()


## Main Code ##

weatherData = WeatherData()

weatherData.subscribe(CurrentConditionsDisplay())
weatherData.subscribe(StatsDisplay())
weatherData.subscribe(ForecastDisplay())

for i in range(1):
  weatherData.measurementsChanged()
