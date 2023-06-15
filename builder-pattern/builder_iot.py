# Using the builder pattern we can create a builder for each situation
# and abstract away the construction of the more complex IoT device.

# The Builder interface
class Builder:

  def reset(self) -> None:
    """Overrides Builder.reset()"""
    pass
  
  def add_wifi() -> None:
    """Overrides Builder.add_wifi()"""
    pass

  def setup_mqtt() -> None:
    """Overrides Builder.setup_mqtt()"""
    pass

  def add_lorawan() -> None:
    """Overrides Builder.add_lorawan()"""
    pass

  def set_sensor_pin() -> None:
    """Overrides Builder.set_sensor_pin()"""
    pass


class IotDevice:
  def __init__(self,
                wifi_pass: str,
                wifi_ssid: str,
                mqtt_broker: str,
                mqtt_username: str,
                mqtt_password: str,
                lorawan_dev_eui: str,
                lorawan_app_eui: str,
                lorawan_app_key: str,
                sensor_pin: int
                ) -> None:

    print("Creating a complex IoT device")
    # We actually do nothing here ! Its an example remember


class IoTDeviceBuilder(Builder):
  
  def reset(self) -> None:
    print("Resetting builder ....")

  def add_wifi(self,
                wifi_pass: str,
                wifi_ssid: str
                ) -> None:
    print("Adding wifi")

  def setup_mqtt(self,
                mqtt_broker: str,
                mqtt_username: str,
                mqtt_password: str
                ) -> None:
    print("Setting up MQTT")

  def add_lorawan(self,
                lorawan_dev_eui: str,
                lorawan_app_eui: str,
                lorawan_app_key: str
                ) -> None:
    print("Setting up LoRaWAN")

  def set_sensor_pin(self,
                pin: int
                ) -> None:
    print("Setting up sensor pin")

  def get_device(self) -> IotDevice:
    # Return fake device which would be constructed device
    # in reality
    return IotDevice("","","","","","","","",0)


class DeviceDirector:
  # static method (no self)
  def create_soil_sensor(builder: IoTDeviceBuilder) -> IotDevice:
    builder.reset()
    builder.add_lorawan("XX:XX:....", "1234567", "000000")
    builder.set_sensor_pin(3)
    return builder.get_device()
    
  def create_p1_sensor(builder: IoTDeviceBuilder) -> IotDevice:
    builder.reset()
    builder.add_wifi("secret", "secret")
    builder.setup_mqtt("broker", "john", "****")
    builder.set_sensor_pin(1)
    return builder.get_device()




### Some demo code

builder = IoTDeviceBuilder()

soilSensor = DeviceDirector.create_soil_sensor(builder)
p1Sensor = DeviceDirector.create_p1_sensor(builder)

