from machine import Pin
from utime import sleep

# Define the GPIO pins for each LED
red_led = Pin(15, Pin.OUT)    # GPIO 15 : Pin 20
yellow_led = Pin(14, Pin.OUT)  # GPIO 14 : Pin 19
green_led = Pin(2, Pin.OUT)   # GPIO 2 : Pin 4
pico_led = Pin("LED", Pin.OUT)  # Onboard LED

def setup_leds():
    # Initialize all LEDs to OFF
    red_led.off()
    yellow_led.off()
    green_led.off()
    pico_led.on()  # Turn on Pico's LED to show the program is running

def traffic_light():
    # Green light for 4.5 seconds
    green_led.on()
    yellow_led.off()
    red_led.off()
    sleep(0.5)
    
    # Yellow light for 1.5 seconds
    green_led.off()
    yellow_led.on()
    red_led.off()
    sleep(0.5)
    
    # Red light for 4.5 seconds
    green_led.off()
    yellow_led.off()
    red_led.on()
    sleep(0.5)

print("Traffic light starting...")
setup_leds()

while True:
    try:
        traffic_light()
    except KeyboardInterrupt:
        # Turn off all LEDs when stopping
        red_led.off()
        yellow_led.off()
        green_led.off()
        break

print("Traffic light stopped.")
