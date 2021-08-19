from sqlite3 import connect

date = 0 # TIMESTAMP времени с которого считать игроков

if len(date) == 10: date = str(date) + '000'
elif len(date) == 13: pass
else: raise 'date не в формате TIMESTAMP'

con = connect('authme.db')
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
        WHERE regdate >= %s;
    """ % date)

con.commit()
con.close()
