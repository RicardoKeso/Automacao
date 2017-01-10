#!/usr/bin/python2.7

import sqlite3

# [0]id, [1]bcm(nome), [2]board(pino), [3]output, [4]status, [5]alterar

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
    alterar BOOLEAN NOT NULL
    );
"""
cursor.execute(sql)

sql = "INSERT INTO gpioControl (bcm, board, output, status, alterar) VALUES ('GPIO4', 7, 1, 0, 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, alterar) VALUES ('GPIO17', 11, 0, 0, 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, alterar) VALUES ('GPIO18', 12, 1, 0, 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, alterar) VALUES ('GPIO27', 13, 1, 0, 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, alterar) VALUES ('GPIO22', 15, 1, 0, 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, alterar) VALUES ('GPIO23', 16, 1, 0, 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, alterar) VALUES ('GPIO24', 18, 1, 0, 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, alterar) VALUES ('GPIO25', 22, 1, 0, 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, alterar) VALUES ('GPIO5', 29, 1, 0, 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, alterar) VALUES ('GPIO6', 31, 1, 0, 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, alterar) VALUES ('GPIO12', 32, 1, 0, 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, alterar) VALUES ('GPIO13', 33, 1, 0, 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, alterar) VALUES ('GPIO19', 35, 1, 0, 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, alterar) VALUES ('GPIO16', 36, 1, 0, 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, alterar) VALUES ('GPIO26', 37, 1, 0, 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, alterar) VALUES ('GPIO20', 38, 1, 0, 0);"
cursor.execute(sql)
sql = "INSERT INTO gpioControl (bcm, board, output, status, alterar) VALUES ('GPIO21', 40, 1, 0, 0);"
cursor.execute(sql)

conn.commit()
conn.close()
