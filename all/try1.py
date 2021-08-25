import mysql.connector
query="select * from registration where fname=%s"
try:
    con1 = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='1235',
        port=3306,
        database='login_registration')
    print(con1)
    cur1 = con1.cursor()
    print(cur1)
    cur1.execute(query,('kaushal',))
    print(cur1)
    row1 = cur1.fetchone()
    print(row1)
    con1.close()
except:
    print('error')
    pass