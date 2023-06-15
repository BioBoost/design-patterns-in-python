# Consider an IoT device class we've build that has a complex
# constructor which takes in quite a lot of arguments to get
# the device initialized.
# There are situations where we connect via WiFi and MQTT,
# while in other situations we may connect it to LoRaWAN.

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



### Some demo code

soilSensor = IotDevice("None", None, None, None, None, "XX:XX:....", "1234567", "000000", 3)
p1Sensor = IotDevice("secret", "secret", "broker", "john", "****", None, None, None, 1)

