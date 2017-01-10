#!/usr/bin/python2.7

import RPi.GPIO as GPIO
import sys
import os

pino = int(sys.argv[1])
estado = ""

caminhoPino = os.path.expanduser("../pinos/" + str(pino))

if os.path.exists(caminhoPino):
    arq = open(caminhoPino, "r")
    estado = arq.read()
    arq.close()
else:
    arq = open(caminhoPino, "w")
    arq.close()
    estado = 0

if estado != "0" and estado != "1":
    estado = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) #desabilita os alertas
GPIO.setup(pino, GPIO.OUT)
GPIO.output(pino, int(estado))

arq = open(str(caminhoPino), "w")
arq.write(str(int(not(int(estado)))))
arq.close()
