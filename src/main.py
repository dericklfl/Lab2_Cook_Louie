'''! @file      main.py
                This file runs a step response on the motor for two seconds each time a key is pressed. 
    @author     Michael Cook
    @author     Derick Louie
    @date       January 31, 2022
    @copyright  (c) 2022 by Michael Cook, Derick Louie, and released under GNU Public License v3
'''

from closedloop import ClosedLoop
from encoder import Encoder
from motordriver import MotorDriver
import pyb
import time


def main():
    '''! 
    Runs a step response on motor for two seconds when a key is pressed. 
    '''
    
    ## Encoder object using pins PB6 and PB7
    enc = Encoder(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    
    ## Closed loop object with a setpoint of 10000 ticks and kP of 0.03
    closedloop = ClosedLoop(10000, 0.03)
    
    ## Motor object using pins PB4 and PB5
    motor = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)

    
    while True:
        print('Press key and return to begin step response')
        if input():
            #print('Running step response for 2 seconds')
            starttime=time.ticks_ms()
            timeelapsed=0
            
            while(timeelapsed < 2000):
                timeelapsed=time.ticks_ms()-starttime
                enc.update()
                pwm = list(closedloop.run(enc.read()))
                motor.set_duty_cycle(pwm[0])
                time.sleep_ms(10)
                
            closedloop.results(pwm[1], pwm[2])
            enc.zero()
        
    
if __name__ == '__main__':
    main()   