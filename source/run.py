from array import array
from threading import Thread

import gaugette.rotary_encoder
import gaugette.switch

A_PIN = 7
B_PIN = 9
SW_PIN = 8

TEMPERATURE = 38
TOLERANCE = 0.2  # Wikipedia says 0.3
HEATER_ON = False
LAST_SWITCH_STATE = 0
MOTOR_ON = False

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


def motor_on(value):
    """
    Turns motor on or off
    :param value: True for motor on, False for motor off
    :return:
    """
    global MOTOR_ON
    if MOTOR_ON is value:
        pass
    else:
        MOTOR_ON = value
        if value:
            # turn motor on
        else:
            # turn motor of


temperature_worker = Thread(target=check_temperature_worker, args=())
temperature_worker.start()

while 1:
    delta = encoder.get_delta()
    if delta != 0:
        change_temperature(delta)

    sw_state = switch.get_state()
    if sw_state != LAST_SWITCH_STATE:
        LAST_SWITCH_STATE = sw_state
        if LAST_SWITCH_STATE and MOTOR_ON:
            motor_on(False)
        elif LAST_SWITCH_STATE and not MOTOR_ON:
            motor_on(True)

    # show temperature on display (current and desired)
    # show timer on display after start is pressed
