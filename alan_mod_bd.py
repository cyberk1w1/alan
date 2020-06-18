import sqlite3

def InsertURL(urladdress, protocol, domain, path, query, fragment, params):
    conn = sqlite3.connect('C:\\Users\\anubis\\Desktop\\alan\\alan.db')
    c = conn.cursor()
    bdquery = """INSERT INTO url (urladdress, protocol, domain, path, query, fragment, params) VALUES (?, ?, ?, ?, ?, ?, ?);"""
    data_query = (urladdress, protocol, domain, path, query, fragment, params)
    c.execute(bdquery, data_query)
    #c.execute("INSERT INTO url (urladdress, protocol, domain, path, query, fragment, params) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}', '{6}')".format(urladdress, protocol, domain, path, query, fragment, params))
    conn.commit()
    c.close()

def QueryURL(url):
    conn = sqlite3.connect('alan.db')
    c = conn.cursor()
    urladdress = url
    c.execute("SELECT * FROM URL WHERE urladdress = '%s'" % urladdress)
    conn.close()