#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in February 2021
# Rotates servo from 0 to 180 degrees


import time
import board
import pwmio
from adafruit_motor import servo


def main():
 
    pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
    servo = servo.Servo(pwm)
    
    while True:
        for angle in range(0, 180, 5):
            servo.angle = angle
            time.sleep(0.05)
        for angle in range(180, 0, -5):
            servo.angle = angle
            time.sleep(0.05)

 
if __name__ == "__main__":
    main() 
 
