#!/usr/bin/python2.7

import RPi.GPIO as gpio
import time

PIN=11
  
def action_press_button_loop(gpio_pin):
    print "O botao no pino foi pressionado"
    print "Saindo.."
         
def action_press_button(gpio_pin):
    print "Tratando o botao no pino que foi pressionado"
               
gpio.setmode(gpio.BOARD) 
                
gpio.setup(PIN, gpio.IN, pull_up_down = gpio.PUD_DOWN)
                
gpio.add_event_detect(PIN, gpio.RISING, callback=action_press_button)
                  
while True:
    print "Polling..."

    if gpio.event_detected(PIN):
        action_press_button_loop(PIN)
        break
                             
    time.sleep(5)
                              
gpio.cleanup()
exit()
