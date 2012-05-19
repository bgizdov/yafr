from pysqlite2 import dbapi2 as sqlite

connection = sqlite.connect("./db/yafr.db")
cursor = connection.cursor()

# id | name | type | parent
sql = """CREATE TABLE IF NOT EXISTS folders (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(50)
	 )"""
cursor.execute(sql)
connection.commit()

def addFolder(name):
	sql = "INSERT INTO folders (id, name) VALUES (NULL, '%s')" % (name)
	cursor.execute(sql)
	connection.commit()
	cursor.execute('SELECT id FROM folders ORDER BY id DESC LIMIT 1')
	return cursor.fetchall()[0]

def renameFolder(name, folderId):
	sql = "UPDATE folders SET name = '%s' WHERE id = %s" % (name, folderId)
	cursor.execute(sql)
	connection.commit()
	cursor.execute('SELECT id FROM folders ORDER BY id DESC LIMIT 1')
	return cursor.fetchall()[0]

def delFolder(folderId):
	sql = "DELETE FROM folders WHERE id = " + folderId
	cursor.execute(sql)
	sql = "DELETE FROM feeds WHERE folderId = " + folderId
	cursor.execute(sql)
	connection.commit()
	cursor.execute('SELECT id FROM folders ORDER BY id DESC LIMIT 1')
	return cursor.fetchall()[0]

def getAll():
	sql = "SELECT * FROM folders"
	cursor.execute(sql)
	return cursor.fetchall()



	

