from array import array
from threading import Thread
import time
import threading

import gaugette.rotary_encoder
import gaugette.switch

A_PIN = 7
B_PIN = 9
SW_PIN = 8

TEMPERATURE = 38
TOLERANCE = 0.2  # Wikipedia says 0.3
HEATER_ON = False
LAST_SWITCH_STATE = 0
MOTOR_SPEED = 0
MOTOR_SECONDS = 5

encoder = gaugette.rotary_encoder.RotaryEncoder.Worker(A_PIN, B_PIN)
encoder.start()
switch = gaugette.switch.Switch(SW_PIN)


def change_temperature(value):
    """
    Sets increases or decreases desired temperature
    :param value: temperature delta
    """
    global TEMPERATURE
    if TEMPERATURE + value > 50 or TEMPERATURE - value < 0:
        pass
    else:
        TEMPERATURE += value


def get_temperature():
    """
    Checks temperature sensor
    :return: temperature as float
    """
    # get temperature
    return 38  # placeholder


def heater_on(value):
    """
    Turns heater on or off
    :param value: True for on, False for off
    :return: nothing
    """
    global HEATER_ON
    if HEATER_ON is value:
        pass
    else:
        HEATER_ON = value
        if value:
            # turn heater on
        else:
            # turn heater off


def check_temperature_worker():
    """
    Worker that continuously checks the temperature
    :return: nothing
    """
    temp_array = array('f', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    while 1:
        temp_array.push(get_temperature())
        water_temp = sum(temp_array) / len(temp_array)

        if TEMPERATURE - water_temp > 0:  # because heater maybe still emits heat after being turned off
            heater_on(False)
        elif (TEMPERATURE - water_temp) * -1 > TOLERANCE:
            heater_on(True)



class MotorWorker (Thread):
    """
    Motor worker class that manages motor direction and turning
    """
    def __init__(self):
        """
        Init that sets flag, timestamp and direction
        """
        threading.Thread.__init__(self)
        self.flag = True
        self.timestamp = time.clock()
        self.direction = 1

    def run(self):
        """
        Execution on thread start
        :return: nothing
        """
        self.flag = True
        global MOTOR_SPEED, MOTOR_SECONDS
        self.timestamp = time.clock()
        while self.flag:
            if time.clock() - self.timestamp > 5:
                self.timestamp = time.clock()
                self.direction = self.direction * -1

            motor_speed(MOTOR_SPEED * self.direction)


    def stop(self):
        """
        Stops the thread
        :return: nothing
        """
        self.flag = False


def motor_speed(value):
    """
    Changes motor speed
    :param value: -128/128 for maximum speed in either direction. 0 for off.
    :return:
    """
    global MOTOR_SPEED
    if MOTOR_SPEED is value:
        pass
    else:
        if value > 128:
            MOTOR_SPEED = 128
        elif value < -128:
            MOTOR_SPEED = -128
        else
            MOTOR_SPEED = value
        # set motor speed


temperature_worker = Thread(target=check_temperature_worker, args=())
temperature_worker.start()

motor_worker = MotorWorker()

while 1:
    delta = encoder.get_delta()
    if delta != 0:
        change_temperature(delta)

    sw_state = switch.get_state()
    if sw_state != LAST_SWITCH_STATE:
        LAST_SWITCH_STATE = sw_state
        if LAST_SWITCH_STATE and motor_worker.is_alive():
            motor_worker.stop()
        elif LAST_SWITCH_STATE and not motor_worker.is_alive():
            motor_worker.run()

    # show temperature on display (current and desired)
    # show timer on display after start is pressed
