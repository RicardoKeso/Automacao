#!/usr/bin/python2.7

import RPi.GPIO as gpio
import time, os, sqlite3
from datetime import datetime

botao = 11
pino = 7
caminho = os.path.expanduser("mudarEstado/" + str(pino))
 
gpio.setmode(gpio.BOARD) 
gpio.setwarnings(False);                          
gpio.setup(botao, gpio.IN)

def atualizarStatus(pino):
    conn = sqlite3.connect('../db/automacao.db')
    cursor = conn.cursor()
    status = 0;

    sql = "select status from automacao where pino=?"
    cursor.execute(sql, [(pino)])

    for linha in cursor.fetchone():
        status = linha

    status = 0 if (status == 1) else 1

    sql = "UPDATE Automacao SET status = " + str(status) + " WHERE pino == " + str(pino) + ";"
    cursor.execute(sql)

    conn.close()

 
def action_press_button(gpio_pin):
    print "pino do botao " + str(gpio_pin) + " - " + str(datetime.now())

    atualizarStatus(pino)

    arq = open(caminho, "w")
    arq.close()


gpio.add_event_detect(botao, gpio.BOTH, callback=action_press_button ,bouncetime=500) # padrao 300



while True:
    time.sleep(1)
