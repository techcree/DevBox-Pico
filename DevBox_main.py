#by 838375 V4.1 - Temperaturmessung und Anzeige mit Display und RGB LEDs
import machine 
import utime
import picodisplay
from machine import ADC #Mainboard Sensor
from machine import Pin
import picodisplay as display # Pico Display boilerplate
import time, random

# Display Setting
width = display.get_width()
height = display.get_height()
display_buffer = bytearray(width * height * 2)
display.init(display_buffer)
display.set_backlight(0.5)
# Setup Temperaturmessung und Konvertierung
sensor_temp = machine.ADC(4) 
conversion_factor = 3.3 / (65535) 
display.set_backlight(0.5)

#Messung und LED Logig
while True:
    h = 0
    o = 0
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = round(27 - (reading - 0.706) / 0.001721)
    tempa=temperature
    display.set_pen(0, 0, 139)
    display.rectangle(0, 0, 300, 140)
    display.set_pen(255, 255, 255)
    display.text("Temperatur:", 10, 40, 0, 3)
    display.text("  " + "{:.0f}".format(temperature) + "." + "c", 10, 30, 0, 7) 
    display.update()
    utime.sleep(3)
#LED zeigen Temperaturbereiche an    
    if tempa > 25:
        print ("HEISS")
        print (tempa)
        picodisplay.set_led(255, 0, 0)
        
    elif ((tempa>= 20) and (tempa<= 25)):    
        print ("WARM")
        print (tempa)
        picodisplay.set_led(0, 255, 0)
    elif tempa < 20:
        print ("KALT")
        print (tempa)
        picodisplay.set_led(0, 0, 255)
        
    utime.sleep(0.5)
    picodisplay.set_led(0, 0, 0)
    utime.sleep(3)
