import MySQLdb

import time
db = MySQLdb.connect("localhost","root","","app",autocommit=True)
db.autocommit = True
c=db.cursor()

def create_user(fnam,uname,sex,userid):
    result = ""
    print("Rig----------?",fnam,uname,sex)
    sql = "INSERT INTO `users` (full_name,username,sex,user_id) VALUES (%s,%s,%s,%s)"
    val = (fnam,uname,sex,userid)
    try:
        c.execute(sql,val)
        db.commit()
    except Exception as e:
        print("Somthing wrong", e)
        return False
    return 1
def delete_user(username):
    print("dEL----------?",username)
    return c.execute("DELETE FROM `users` WHERE `username` = %s",(username,))
def find_user(username):
    print("Finding-------?",username)
    sql = "SELECT * FROM users WHERE username = %s"
    val = (username,)
    c.execute(sql,val)
    rec = c.fetchone()
    resul = []
    resul = list(rec)
    return resul
def is_exist(username):
    print("IsEx---------?",username)
    c.execute("SELECT * FROM users WHERE username = %s",(username,))
    return len(c.fetchall())
def get_games():
    sql = "SELECT * FROM games"
    c.execute(sql)
    return c.fetchall()
def set_party(pid,party,user,catg):
    c.execute("SELECT * FROM party WHERE id = %s",(party+user,))
    if c.fetchone() is None:
        sql = "INSERT INTO `party` (`id`,`party`, `user`,`catag`) VALUES (%s,%s,%s,%s)"
        val = (pid,party,user,catg)
        c.execute(sql,val)
        db.commit()
    else:
        print("already checkd") 
def get_catag():
    c.execute("SELECT * FROM catog")
    return c.fetchall()
def update_party(party,suser):
    c.execute("SELECT * FROM `party` WHERE user = %s AND party = %s",(party,"wait"))
    if c.fetchone() is None:
        return 0
    else:
        c.execute("SELECT * FROM `party` WHERE user = %s",(party,))
        result = c.fetchone()
        pid = result[0]
        if(result[2] == suser):
            return -1
        else:
            c.execute("UPDATE party SET party= %s WHERE id = %s",(suser,pid,))
            db.commit()
            return 1
def find_party(username):
    c.execute("SELECT * FROM party WHERE user= %s",(username,))
    return c.fetchone()
def cr_party_rs(pi):
    sql = "INSERT INTO `party_result` (`partyid`,`userresult`, `partyresult`) VALUES (%s,%s,%s)"
    val = (pi,"","")
    c.execute(sql,val)
    db.commit()
def set_current(cat):
    print("Set_current or session function",cat)
    c.execute("INSERT INTO session (`party_user`, `pid`) VALUES (%s, %s)",(cat[1],cat[0]))
    db.commit()
def have_se(username):
    c.execute("SELECT * FROM session WHERE party_user = %s",(username,))
    if c.fetchone() is None:
        return False
    else:
        return True
def delete_session(username):
    c.execute("DELETE FROM `session` WHERE  `party_user`=%s",(username,))
    db.commit()
def session_pid(username):
    c.execute("SELECT * FROM session WHERE party_user = %s",(username,))
    pid = c.fetchone()[1]            
    return pid
def user_cach(username,cach):
    c.execute("INSERT INTO `temp` (`store_by`, `data`) VALUES (%s, %s)",(username,cach))
    db.commit()
def get_cach(username):
    c.execute("SELECT * FROM temp WHERE store_by = %s",(username,))
    return c.fetchone()[1]
def delete_cach(username):
    c.execute("DELETE FROM `temp` WHERE  `store_by`= %s;",(username,))
    db.commit()
def reset(username):
    c.execute("DELETE FROM `party` WHERE party = %s",(username,))
    db.commit()








    


c.execute('commit')