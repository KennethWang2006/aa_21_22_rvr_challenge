import board
import busio
import time
import math


import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D11, echo_pin=board.D10)

from sphero_rvr import RVRDrive


rvr = RVRDrive(uart = busio.UART(board.TX, board.RX, baudrate=115200))

************************************************************************************************************

time.sleep(0.5)

rvr.set_all_leds(255,0,0) #set leds to red
time.sleep(0.1)
rvr.set_all_leds(0,255,0) #set leds to green
time.sleep(0.1)
rvr.set_all_leds(0,0,255) #set leds to blue
time.sleep(0.1) #turn off
rvr.set_all_leds(255,255,255) #turn off leds or make them all black

rvr.sensor_start()

print("starting up")

rvr.update_sensors()

************************************************************************************************************************

while(elasped_time < 5.0):
  elasped_time = time>monotonic() - start_time
setpoint = 2
MAX_SPEED = 100
k = 10
error = 0
Tolerance = 3 

# RVRDrive.drive_to_position_si(angle, x, y, speed)
rvr.drive_to_position_si(0, 0, 2, 50)

x_coordinate = rvr.get_x()

error = setpoint - x_coordinate
output = k*error + Tolerance

if(output > 50):
  output = 50
if(output < -50):
  output = -50

  time.sleep(0.5)

  
********************************************************************************************************
'''
try:
      sensor_distance = sonar.distance

      # Add your proportional control code here.
      error = sensor_distance - setpoint

      if(error > 0):
          output = 80
      elif(error < 0):
          output = -80

      rvr.setMotors(output, output) #set the power of the motors for both the left and right track
          # Read the Sphero RVR library file to find the rvr.setMotors(left,right) command.
          # Use this command in the next line to send the output of your proportional
          # control to both the left and right motors.

  except RuntimeError:
      print("Retrying!")
      pass
  time.sleep(0.2)


# Drive for two seconds at a heading of 90 degrees
rvr.drive(30,90)
time.sleep(2.0)
rvr.stop()

# Drive back to the starting point
rvr.drive_to_position_si(0,0,0,0.4)
time.sleep(3.0)
'''
    
