class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

def getMenu(self):
    sql = '''SELEC * FROM mainmenu'''
    try:
        self.__cur.execute(sql)
        res = self.__cur.frtchall()
        if res: return res
    except:
        print("bd reading error")
    return []





