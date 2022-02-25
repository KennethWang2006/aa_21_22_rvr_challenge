

# Write your code here :-)
import board, busio, time, math, digitalio, adafruit_hcsr04

from sphero_rvr import RVRDrive
from ssis_rvr   import pin

rvr   = RVRDrive(uart = busio.UART(pin.TX, pin.RX, baudrate=115200))
sonar = adafruit_hcsr04.HCSR04(trigger_pin=pin.TRIGGER, echo_pin=pin.ECHO)


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
setpoint = 40.0
MAX_SPEED = 50

rvr.update_sensors()
print("1")

error = 0
tolerance = 3
k = 3
start_time = time.monotonic()
elapsed_time = time.monotonic() - start_time

print("2")

#def moveControlled(v_time, v_setpoint):
#    while(elapsed_time < v_time):

#    elapsed_time = time.monotonic() - start_time

#    try:
#        sensor_distance = sonar.distance

#        # Add your proportional control code here.
#        error = sensor_distance - v_setpoint
#        output = error*k
#        
#        
#        rvr.setMotors(output, output) #set the power of the motors for both the left and right track
#            # Read the Sphero RVR library file to find the rvr.setMotors(left,right) command.
#            # Use this command in the next line to send the output of your proportional
#            # control to both the left and right motors.

#    except RuntimeError:
 #       print("Retrying!")
#        pass
#    time.sleep(0.2)

#-------------------------------------------------------------------------
#Algorithm 1: Go to orange boxes
print("3")
while(elapsed_time < 6.0):

    elapsed_time = time.monotonic() - start_time

    try:
        sensor_distance = sonar.distance

        # Add your proportional control code here.
        error = sensor_distance - setpoint
        output = error*k
        
        
        rvr.setMotors(output, output) #set the power of the motors for both the left and right track
            # Read the Sphero RVR library file to find the rvr.setMotors(left,right) command.
            # Use this command in the next line to send the output of your proportional
            # control to both the left and right motors.

    except RuntimeError:
        print("Retrying!")
        pass
    time.sleep(0.2)
print("4")

set_heading = 90
tolerance_heading = 3
output_heading = 20

#Algorithm 2: Turn until wanted heading
while(elapsed_time < 6.0):
    elapsed_time = time.monotonic() - start_time
    
    try:
        print(rvr.get_heading())
        heading = rvr.get_heading()
        error = set_heading - heading
        
        if abs(error) < tolerance_heading:
            rvr.setMotors(output, output_heading*-1)
        
    







    
#Turn 90 degrees clockwise and move drive through the gap (could change with an algorithm but could be repetitive which the function moveControlled could solve)
#turn 90 degrees clockwise using motor forward and motor backward
#rvr.drive_to_position_si(0,1,0,SPEED) #turn 0 degrees after moving, to these x,y, coordinates at SPEED
    
#Algorithm 2: move to location of upper green box

#Algorithm 3: push upper green box and move back to "green box" line

#Algorithm 4: move to location of lower green box

#move inbetween green boxes

#Algorithm 5/6: push both green boxes to the wall



#Finish
rvr.stop()
