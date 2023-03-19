#!/usr/bin/python3

from gpiozero import LED
import piclap

light = LED(17)

class Config(piclap.Settings):
    def __init__(self):
        super().__init__()
        self.chunk_size = 512
        self.wait = 0.5
        self.method.value = 600

    def on2Claps(self):
        light.toggle()
        print(f"Light Toggled at GPIO: {light.pin}")

    def on4Claps(self):
        pass


listener = piclap.Listener(Config(), calibrate=False)
listener.start()