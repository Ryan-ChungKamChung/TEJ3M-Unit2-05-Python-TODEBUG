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
 
