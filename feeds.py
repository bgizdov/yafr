from pysqlite2 import dbapi2 as sqlite
import feedparser
import datetime

connection = sqlite.connect("./db/yafr.db")
cursor = connection.cursor()

sql = """CREATE TABLE IF NOT EXISTS feeds (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	folderId INTEGER,
	url VARCHAR(200),
	name VARCHAR(100)
	 )"""

cursor.execute(sql)
connection.commit()

sql = """CREATE TABLE IF NOT EXISTS articles (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	feedId INTEGER,
	folderId INTEGER,
	title VARCHAR(200),
	link VARCHAR(200),
	date DATE,
	summary TEXT,
	status INTEGER
	 )"""

cursor.execute(sql)
connection.commit()

def parseName(feedurl):
	print 'parseName'
	d = feedparser.parse(feedurl)
	print d.feed
	return d.feed.title.replace("'", '')

def addFeed(feedurl, folderId):
	print 'Add feeed '
	print folderId
	name = parseName(feedurl)
	sql = "INSERT INTO feeds (id, url, name, folderId) VALUES (NULL, '%s', '%s', %s)" % (feedurl, name, folderId)
	print sql
	cursor.execute(sql)
	connection.commit()
	cursor.execute('SELECT id, name FROM feeds ORDER BY id DESC LIMIT 1')
	d = cursor.fetchall()
	return (str(d[0][0]), d[0][1])

def delFeed(feedId):
	sql = "DELETE FROM feeds WHERE id = " + feedId
	cursor.execute(sql)
	connection.commit()

def getFeeds(folderId):
	print 'Get feeds'
	sql = 'SELECT id, url, name FROM feeds WHERE folderId=' + folderId
	cursor.execute(sql)
	return cursor.fetchall()

def getUnreadCount(feedId):
	print 'Get unreaded count'
	sql = 'SELECT COUNT(*) FROM articles WHERE (status = 0 OR status = 1) AND feedId=' + feedId
	cursor.execute(sql)
	return cursor.fetchall()[0][0]

def escape(s):
	return s.replace("'", "").replace(':', '') #FIXME

def isArticleExist(link):
	sql = "SELECT COUNT(*) FROM articles WHERE link='%s'" % (link)
	cursor.execute(sql)
	return cursor.fetchall()[0][0] > 0

def fetchFeed(feedId, folderId):
	print 'Fetching feeds'
	sql = 'SELECT url FROM feeds WHERE id=' + feedId
	cursor.execute(sql)
	url = cursor.fetchall()[0][0]
	data = feedparser.parse(url)
	for entry in data.entries:
		try:
			title = escape(unicode(entry.title))
			link = escape(unicode(entry.link))
			if isArticleExist(link):
				continue
			try:
				upd = entry.updated_parsed
				date = datetime.datetime(upd[0], upd[1], upd[2], upd[3], upd[4], upd[5])
				updated = "'" + date.isoformat().replace('T', ' ') + "'"
			except:
				updated = 'NOW()'
			
			summary = escape(unicode(entry.summary))
			sql = """INSERT INTO articles (id, feedId, folderId, title, link, date, summary, status)
				VALUES (NULL, %s, %s, '%s', '%s', %s, '%s', 0)""" % (feedId, folderId, title, link, updated, summary)
			#print sql
			cursor.execute(sql)
			connection.commit()
		except:
			print 'except'
	
def searchArticles(feedId, status, search):
	print '* Get articles'
	if status == -1:
		filteradd = ''
	else:
		filteradd = ' AND status=' + str(status)
	sql = """SELECT title, date, name, articles.id, status
		FROM articles
		LEFT JOIN feeds ON articles.feedId = feeds.id
		WHERE status <> 4 """ + filteradd + "  AND feedId=" + feedId + " AND title LIKE '%" + search + "%'"
	
	cursor.execute(sql)
	return cursor.fetchall()

def getArticlesFeed(feedId, status):
	print '* Get articles'
	if status == -1:
		filteradd = ''
	else:
		filteradd = ' AND status=' + str(status)
	sql = """SELECT title, date, name, articles.id, status
		FROM articles
		LEFT JOIN feeds ON articles.feedId = feeds.id
		WHERE status <> 4 """ + filteradd + "  AND feedId=" + feedId
	
	cursor.execute(sql)
	return cursor.fetchall()

def getArticlesFolder(folderId, status):
	print '* Get articles'
	if status == -1:
		filteradd = ''
	else:
		filteradd = ' AND status=' + str(status)
	sql = """SELECT title, date, name, articles.id, status
		FROM articles
		LEFT JOIN feeds ON articles.feedId = feeds.id
		WHERE status <> 4 """ + filteradd + "  AND folderId=" + folderId
	cursor.execute(sql)
	return cursor.fetchall()

def markReadImp(articleId):
	sql = 'UPDATE articles SET status = 2 WHERE status <> 3 AND id=' + articleId
	cursor.execute(sql)
	connection.commit()

def markArticle(articleId, status):
	sql = 'UPDATE articles SET status = ' + status + ' WHERE id=' + articleId
	cursor.execute(sql)
	connection.commit()

def markNew(articleId):
	markArticle(articleId, '0')
	
def markUnread(articleId):
	markArticle(articleId, '1')
	
def markRead(articleId):
	markArticle(articleId, '2')

def markImportant(articleId):
	markArticle(articleId, '3')
	
def markDel(articleId):
	markArticle(articleId, '4')
	
def getArticle(articleId):
	print '* Get articles'
	sql = """SELECT articles.id, title, link, date, summary, name
		FROM articles
		LEFT JOIN feeds ON articles.feedId = feeds.id
		WHERE articles.id=""" + articleId
	print sql
	cursor.execute(sql)
	data = cursor.fetchall()
	markReadImp(articleId)
	return data

def markFeedRead(feedId):
	sql = """UPDATE articles SET status = 2 WHERE feedId =""" + feedId
	print sql
	cursor.execute(sql)
	connection.commit()
	
def markAllRead(feedId):
	sql = """UPDATE articles SET status = 2"""
	print sql
	cursor.execute(sql)
	connection.commit()
	
	
	
	
	
	
	
	
	
	
	
	
	
	