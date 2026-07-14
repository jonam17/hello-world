"""TRANSMISSION 07 // RASPBERRY PI — the signal leaves the screen.

Blinks an LED on GPIO 17: hardware saying hello back.
Wiring: GPIO17 -> 330 ohm resistor -> LED -> GND
"""

from time import sleep

try:
    from gpiozero import LED
except ImportError:  # not on a Pi — simulate the heartbeat
    class LED:
        def __init__(self, pin): self.pin = pin
        def on(self):  print(f"[GPIO {self.pin}] * blink *")
        def off(self): pass

led = LED(17)

for _ in range(3):  # three pulses: H-W in a heartbeat
    led.on(); sleep(0.2)
    led.off(); sleep(0.2)

print("[NODE 00] Hello, World :: hardware online")
