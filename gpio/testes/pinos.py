#!/usr/bin/python2.7

import RPi.GPIO as GPIO
import sys, os

while True:
    caminho = os.path.expanduser("mudarEstado/") 
    mudarEstados = os.listdir(caminho)


    if len(mudarEstados) != 0:
        for pino in mudarEstados:

            caminhoPino = os.path.expanduser("pinos/" + str(pino))

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

            estado = str(int(not(int(estado))))

            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False) #desabilita os alertas
            GPIO.setup(int(pino), GPIO.OUT)
            GPIO.output(int(pino), int(estado))

            arq = open(str(caminhoPino), "w")
            arq.write(estado)
            arq.close()

            os.remove(caminho + str(pino))
