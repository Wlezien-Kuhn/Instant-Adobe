import MySQLdb


#helper methods to access database


def getAllTemplates(cursor):

    cursor.execute("SELECT * from templates")

    return cursor.fetchall()

def getTemplateWithUuid(cursor,uuid):

    cursor.execute("SELECT * from templates where UUID = %(uuid)s",{"uuid":uuid})

    return cursor.fetchone()

def getTemplateWithAep(cursor,aep_path):

    cursor.execute("SELECT * from templates where Aep = %(aep_path)s",{"aep_path":aep_path})

    return cursor.fetchone()

def getTemplateWithMov(cursor,mov_path):

    cursor.execute("SELECT * from templates where Mov = %(mov_path)s",{"mov_path":mov_path})

    return cursor.fetchone()

def getTemplateWithPoster(cursor,poster_path):

    cursor.execute("SELECT * from templates where Poster = %(poster_path)s",{"poster_path":poster_path})

    return cursor.fetchone()

def getTemplateWithTitle(cursor,title):

    cursor.execute("SELECT * from templates where Title = %(title)s",{"title":title})

    return cursor.fetchone()
