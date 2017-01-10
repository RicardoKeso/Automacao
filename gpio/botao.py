#!/usr/bin/python2.7

import RPi.GPIO as GPIO
import sqlite3, time

# [0]id, [1]bcm(nome), [2]board(pino), [3]output, [4]status, [5]alterar 

db = '../db/automacao.db'

conn = sqlite3.connect(db)
cursor = conn.cursor()

def alterarGPIO(pino, status):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False) #desabilita os alertas
    GPIO.setup(int(pino), GPIO.OUT)
    GPIO.output(int(pino), int(status))

while True:
    sql = "select count(*) from gpioControl where alterar=1 and output=1;"
    cursor.execute(sql)
    cont = ("%s" % (cursor.fetchone()))
    
    if (cont != "0"):
        sql = "select * from gpioControl where alterar=1 and output=1;"
        cursor.execute(sql)
        
        for linha in cursor.fetchall():
            pino = ("%s" % (linha[2]))
            status = ("%s" % (linha[4]))

            #print str(pino) + (" - ligado" if (status == "1") else " - desligado")
            sql = "UPDATE gpioControl SET alterar=0 WHERE board=" + str(pino) + ";"
            cursor.execute(sql)
            conn.commit()

            alterarGPIO(pino, status)
            time.sleep(0.5)

conn.close()
