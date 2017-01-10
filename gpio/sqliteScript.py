#!/usr/bin/python2.7

import sqlite3

# [0]id, [1]bcm(nome), [2]board(pino), [3]output, [4]status, [5]nome, [6]alterar

db = '../db/automacao.db'

conn = sqlite3.connect(db)
cursor = conn.cursor()

sql = """
CREATE TABLE gpioControl(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    bcm VARCHAR(16) NOT NULL,
    board INT NOT NULL,
    output BOOLEAN NOT NULL,
    status BOOLEAN NOT NULL,
    nome VARCHAR(16) NOT NULL,
    alterar BOOLEAN NOT NULL
    );
"""
cursor.execute(sql)

sql = "INSERT INTO gpioControl (bcm, board, output, status, nome, alterar) VALUES ('GPIO4', 7, 1, 0, 'pin7', 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, nome, alterar) VALUES ('GPIO17', 11, 0, 0, 'pin11', 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, nome, alterar) VALUES ('GPIO18', 12, 1, 0, 'pin12', 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, nome, alterar) VALUES ('GPIO27', 13, 1, 0, 'pin13', 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, nome, alterar) VALUES ('GPIO22', 15, 1, 0, 'pin15', 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, nome, alterar) VALUES ('GPIO23', 16, 1, 0, 'pin16', 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, nome, alterar) VALUES ('GPIO24', 18, 1, 0, 'pin18', 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, nome, alterar) VALUES ('GPIO25', 22, 1, 0, 'pin22', 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, nome, alterar) VALUES ('GPIO5', 29, 1, 0, 'pin29', 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, nome, alterar) VALUES ('GPIO6', 31, 1, 0, 'pin31', 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, nome, alterar) VALUES ('GPIO12', 32, 1, 0, 'pin32', 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, nome, alterar) VALUES ('GPIO13', 33, 1, 0, 'pin33', 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, nome, alterar) VALUES ('GPIO19', 35, 1, 0, 'pin35', 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, nome, alterar) VALUES ('GPIO16', 36, 1, 0, 'pin36', 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, nome, alterar) VALUES ('GPIO26', 37, 1, 0, 'pin37', 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, nome, alterar) VALUES ('GPIO20', 38, 1, 0, 'pin38', 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, nome, alterar) VALUES ('GPIO21', 40, 1, 0, 'pin40', 0);"
cursor.execute(sql)

conn.commit()
conn.close()
