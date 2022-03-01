

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
time.sleep(0.5)

rvr.sensor_start()
time.sleep(0.5)

print("starting up")
setpoint = 40.0
MAX_SPEED = 50

rvr.update_sensors()
print("1")

error = 0
tolerance = 3
k = 2.6
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

rvr.setMotors(160, 160)
time.sleep(0.5)
rvr.setMotors(160, 160)


time.sleep(0.2)
#Algorithm 1: Go to orange boxes
start_time = time.monotonic()
elapsed_time = time.monotonic() - start_time

print("3")
while(elapsed_time < 5.5):

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
        rvr.set_all_leds(255,0,0) #set leds to red
        time.sleep(0.1)
        rvr.set_all_leds(0,255,0) #set leds to green
        time.sleep(0.1)
        pass
    time.sleep(0.2)
print("4")

set_heading = 90
tolerance_heading = 3
output_heading = 150

start_time = time.monotonic()
elapsed_time = time.monotonic() - start_time

#Algorithm 2: Turn until wanted heading
#rvr.drive_to_position_si(0.5, rvr.get_x(), rvr.get_y(), 0.1)

rvr.drive(50, 90)
time.sleep(3)
rvr.stop()
    
rvr.update_sensors()
gap_coordinates = [rvr.get_x(), rvr.get_y()]

time.sleep(0.5)

rvr.drive(70, 45)
time.sleep(4)
rvr.stop()

#Algorithm 3: Drive until purple box touches side
start_time = time.monotonic()
elapsed_time = time.monotonic() - start_time

setpoint = 280
k2 = 0.05
while(elapsed_time < 2.5):

    elapsed_time = time.monotonic() - start_time

    try:

        # Add your proportional control code here.
        error = setpoint -  rvr.get_y()
        output = error*k2
        
        
        rvr.setMotors(output, output) #set the power of the motors for both the left and right track
            # Read the Sphero RVR library file to find the rvr.setMotors(left,right) command.
            # Use this command in the next line to send the output of your proportional
            # control to both the left and right motors.

    except RuntimeError:
        print("Retrying!")
        rvr.set_all_leds(255,0,0) #set leds to red
        time.sleep(0.1)
        rvr.set_all_leds(0,255,0) #set leds to green
        time.sleep(0.1)
        pass
    time.sleep(0.2)



'''
time.sleep(0.5)

rvr.drive(-100, 45)
time.sleep(8)
rvr.stop()
'''

'''
while(elapsed_time < 6.0):
    elapsed_time = time.monotonic() - start_time
    rvr.update_sensors()
    rvr.set_all_leds(0,0,255) #set leds to blue
    time.sleep(0.1) #turn off
    
    print(rvr.get_heading())
    heading = rvr.get_heading()
    error = set_heading - heading
    
    if(error > 0):
        rvr.setMotors(output_heading, output_heading*-1)
    elif(error < 0):
        rvr.setMotors(output_heading*-1, output_heading)

    time.sleep(0.2)
'''
print("5")
    
    
'''

    
'''
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
