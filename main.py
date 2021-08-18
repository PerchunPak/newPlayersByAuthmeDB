import sqlite3

con = sqlite3.connect('authme.db')
cur = con.cursor()

cur.execute("""
        CREATE TABLE afterDay (
        username varchar(255),
        password varchar(255),
        ip varchar(40),
        regip varchar(255),
        regdate TIMESTAMP
        );
    """)
cur.execute("""
        INSERT INTO afterDay (username, password, ip, regip, regdate)
        SELECT realname, password, ip, regip, regdate FROM authme
        WHERE regdate >= 1623963600000;
    """)

con.commit()
con.close()
