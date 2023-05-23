# Idea here is that we have a WeatherStation that measures Humidity, temperature and Pressure
# WeatherData is a class that pulls the data from the weather station and is responsible for
# updating a number of displays that show current conditions, stats and forecast
# The idea is that new displays may get introduced


from random import uniform


class CurrentConditionsDisplay:
  def update(self, temperature, humidity, pressure):
    print("!!!!!!!!!!!!!!!!!!!!!")
    print("Displaying current conditions:")
    print("Temperature: ", temperature)
    print("Humidity: ", humidity)
    print("Pressure: ", pressure)
    print("!!!!!!!!!!!!!!!!!!!!!")


class StatsDisplay:
  def __init__(self):
    # Private vars start with double underscore
    self.__temperatures = []
    self.__humidities = []
    self.__pressures = []

  def update(self, temperature, humidity, pressure):
    self.__temperatures.append(temperature)
    self.__humidities.append(humidity)
    self.__pressures.append(pressure)

    print("#######################")
    print("Displaying stats:")
    print("Temperature: ", sum(self.__temperatures)/len(self.__temperatures))
    print("Humidity: ", sum(self.__humidities)/len(self.__humidities))
    print("Pressure: ", sum(self.__pressures)/len(self.__pressures))
    print("#######################")


class ForecastDisplay:
  def update(self, temperature, humidity, pressure):
    print("-----------------")
    print("Displaying forecast:")
    print("Temperature: ", (temperature + uniform(-5, +5)))
    print("Humidity: ", (humidity + uniform(-10, +10)))
    print("Pressure: ", pressure)
    print("-----------------")


class WeatherData:

  def __init__(self):
    self.__currentConditionsDisplay = CurrentConditionsDisplay()
    self.__statsDisplay = StatsDisplay()
    self.__forecastDisplay = ForecastDisplay()

  def get_temperature(self):
    return uniform(5, 30)

  def get_humidity(self):
    return uniform(10, 60)
  
  def get_pressure(self):
    return 1013

  def measurementsChanged(self):
    temperature = self.get_temperature()
    humidity = self.get_humidity()
    pressure = self.get_pressure()

    # Update the displays
    self.__currentConditionsDisplay.update(temperature, humidity, pressure)
    self.__statsDisplay.update(temperature, humidity, pressure)
    self.__forecastDisplay.update(temperature, humidity, pressure)


## Main Code ##

weatherData = WeatherData()

for i in range(1):
  weatherData.measurementsChanged()
