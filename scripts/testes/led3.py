#!/usr/bin/python2.7

import RPi.GPIO as gpio
import time, os

botao = 11
pino = 7
status = 0
caminho = os.path.expanduser("mudarEstado/" + str(pino))
 
gpio.setmode(gpio.BOARD) 
gpio.setwarnings(False);                          
gpio.cleanup()

gpio.setup(botao, gpio.IN)
 
def action_press_button(gpio_pin):
    global status

    print "Tratando o botao no pino que foi pressionado"
    status = not status
    
    arq = open(caminho, "w")
    arq.close()
    


gpio.add_event_detect(botao, gpio.BOTH, callback=action_press_button ,bouncetime=300)

while True:
    time.sleep(1)
