import telebot
import MySQLdb
import users as user
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import bot_info as binfo
import random
import time
db = MySQLdb.connect("localhost","root","","app",autocommit=True)
db.autocommit = True
c=db.cursor()




def party_play(bot,call):
    c.execute("SELECT * FROM session WHERE party_user = %s",(call.from_user.username,))
    pid = c.fetchone()[1]
    c.execute("SELECT * FROM party WHERE id = %s",(pid,))
    party = c.fetchone()
    c.execute("SELECT * FROM game_test WHERE catg = %s",(party[3]))
    games = c.fetchall()
    bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=games[0][2],reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(games[0][3], callback_data="ans1i"),InlineKeyboardButton(games[0][4], callback_data="ans2i")))
def get_lastparty(username):
    c.execute("SELECT * FROM session WHERE party_user = %s",(username,))
    pid = c.fetchone()[1]
    c.execute("SELECT * FROM party_result WHERE partyid = %s",(pid,))
    user_res = c.fetchone()
    if user_res[2] is None or user_res[2] == '':
        return 0
    else:
        return user_res[4]
def set_party_play(username,ans):
    c.execute("SELECT * FROM session WHERE party_user = %s",(username,))
    pid = c.fetchone()[1]
    c.execute("SELECT * FROM party_result WHERE partyid = %s",(pid,))
    user_res = c.fetchone()
    val = (str(user_res[2])+str(ans),pid)
    c.execute("UPDATE party_result SET partyresult = %s WHERE partyid = %s",val)
def set_party_last(username,last):
    c.execute("SELECT * FROM session WHERE party_user = %s",(username,))
    pid = c.fetchone()[1]
    val = (last,pid)
    print("Set_party_last",val)
    try:
        c.execute("UPDATE party_result SET partylast = %s WHERE partyid = %s",val)
        db.commit()
    except Exception as e:
        print(e)
def update_party_game(bot,call,username,last):
    c.execute("SELECT * FROM session WHERE party_user = %s",(username,))
    pid = c.fetchone()[1]
    c.execute("SELECT * FROM `party` WHERE `id` = %s",(pid,))
    cat = c.fetchone()[3]
    print("Keep playing")
    c.execute("SELECT * FROM game_test WHERE catg = %s",(cat,))
    games = c.fetchall()
    print(games[last][2])
    bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=games[last][2],reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(games[last][3], callback_data="ans1i"),InlineKeyboardButton(games[last][4], callback_data="ans2i")))
def endgameParty(bot,call,pid):
    c.execute("SELECT * FROM party_result WHERE partyid = %s",(pid,))
    result = c.fetchone()
    print(result)
    bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="✨✨✨✨✨✨✨✨✨✨ \n ስለመለሱ እናመሰግናለን! \n ዉጤቱን እንመልከት! \n ይጠብቁን.......")
    time.sleep(0.5)
    party = result[2]
    user = result[1]
    cnt = 0
    match = []
    prc = 0
    for p in party:
        if p == user[cnt]:
            match.append({"test":cnt,"ans":p})
            prc = prc + 10
        print(p)
        print("User",user[cnt])
        cnt = cnt +1
    c.execute("SELECT * FROM party WHERE id = %s",(result[0],))
    cat = c.fetchone()[3]
    c.execute("SELECT * FROM game_test WHERE catg = %s",(cat,))
    games = c.fetchall()
    rmsg = ""
    for m in match:
        print(games[int(m["test"])][2]," ሁለታቺሁም የመለሳቺሁት ",games[int(m["test"])][int(m['ans'])+2])
        rmsg = rmsg + "☑️"+games[int(m["test"])][2]+" ሁለታቺሁም የመለሳቺሁት "+games[int(m["test"])][int(m['ans'])+2]+"\n"
    bot.send_message(call.message.chat.id, "✨✨✨✨✨✨✨✨✨✨ \n result \n"+rmsg+" \n የመመሳሰል ደረጃ = "+str(prc)+"% \nClick share ", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("😁 Send 😁", url="https://t.me/share/url?url=🤚🖐Hey! \n "+rmsg+" \n የመመሳሰል ደረጃ = "+str(prc)+" ፐርሰንት \n ይሄ የኛ ዉጤት ነዉ!")))
    
    



    











def play(bot,username,call):
    sql = "SELECT * FROM `game_result` WHERE username = %s"
    val = (username,)
    c.execute(sql,val)
    user_res = c.fetchone()
    if user_res is None:
        print("Never played")
        c.execute("SELECT * FROM games")
        games = c.fetchall()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=games[0][1],reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(games[0][2], callback_data="ans1"),InlineKeyboardButton(games[0][3], callback_data="ans2")))
    else:
        last = get_last(call.from_user.username)
        last = last+1
        if last >= 10:
            endgame(bot,call)
        else:
            c.execute("SELECT * FROM games")
            games = c.fetchall()
            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=games[last][1],reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(games[last][2], callback_data="ans1"),InlineKeyboardButton(games[last][3], callback_data="ans2")))        
def self_play(bot,call,cat):
    username = call.from_user.username
    c.execute("SELECT * FROM `party` WHERE `user` = %s",(username,))
    pid = c.fetchone()[0]
    print("Self play function :",c.fetchone())    
    c.execute("SELECT * FROM party_result WHERE partyid = %s",(pid,))
    user_res = c.fetchone()
    print(user_res)
    if user_res[1] == "":
        print("Never played")
        c.execute("SELECT * FROM game_test WHERE catg = %s",(cat,))
        games = c.fetchall()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=games[0][2],reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(games[0][3], callback_data="ans1s"),InlineKeyboardButton(games[0][4], callback_data="ans2s")))
    # else:
    #     last = get_last(call.from_user.username)
    #     last = last+1
    #     if last >= 10:
    #         endgame(bot,call)
    #     else:
    #         c.execute("SELECT * FROM games")
    #         games = c.fetchall()
    #         bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=games[last][1],reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(games[last][2], callback_data="ans1"),InlineKeyboardButton(games[last][3], callback_data="ans2")))        
def self_cplay(bot,call,cat):
    pid = int(random.random()*100000000)
    print("Self cplay function creating :",str(pid))
    user.set_party(pid,"wait",call.from_user.username,cat)
    user.cr_party_rs(pid)
    return pid

def self_delete(username):
    c.execute("SELECT * FROM `party` WHERE `user` = %s",(username,))
    pid = c.fetchone()[0]
    c.execute("DELETE FROM party WHERE  id= %s",(pid,))
    db.commit()
    c.execute("DELETE FROM party_result WHERE  `partyid` = %s",(pid,))
    db.commit()
    return True
def self_isPlay(username):
    c.execute("SELECT * FROM `party` WHERE `user` = %s",(username,))
    if c.fetchone() is None:
        return False
    else:
        return True
    



def set_play_last(username,last):
    c.execute("SELECT * FROM `party` WHERE `user` = %s",(username,))
    pid = c.fetchone()[0]
    val = (last,pid)
    c.execute("UPDATE party_result SET userlast = %s WHERE partyid = %s",val)
    db.commit()
    print(pid)
    
def get_self_last(username):
    c.execute("SELECT * FROM `party` WHERE `user` = %s",(username,))
    pid = c.fetchone()[0]
    c.execute("SELECT * FROM party_result WHERE partyid = %s",(pid,))
    user_res = c.fetchone()
    if user_res[3] is None:
        return 0
    else:
        return user_res[3]
def set_self_play(username,ans):
    c.execute("SELECT * FROM `party` WHERE `user` = %s",(username,))
    pid = c.fetchone()[0]
    c.execute("SELECT * FROM party_result WHERE partyid = %s",(pid,))
    user_res = c.fetchone()
    print(pid)
    val = (str(user_res[1])+str(ans),pid)
    c.execute("UPDATE party_result SET userresult = %s WHERE partyid = %s",val)
def update_self_game(bot,call,username,last):
    c.execute("SELECT * FROM `party` WHERE `user` = %s",(username,))
    cat = c.fetchone()[3]
    print("Keep playing")
    c.execute("SELECT * FROM game_test WHERE catg = %s",(cat,))
    games = c.fetchall()
    bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=games[last][2],reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(games[last][3], callback_data="ans1s"),InlineKeyboardButton(games[last][4], callback_data="ans2s")))

def endgameI(bot,call):
    url = "https://t.me/share/url?url=🤚🖐ሰላም! \n የእርሶ ጐዋደኛ "+call.from_user.full_name+" ከእርስዎ ጋር የጥያቄ ጨዋታወቺን መጫዎት ይፈልጋለ! \n መቀጠል ከፈልጉ ይሄን ሊንክ በመንካት ያስጀምሩ \n 👉https://t.me/"+binfo.username+"?start=0"+call.from_user.username
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=" ✨✨✨✨✨✨✨✨✨✨ \n  መልካም 👏 \n \n \n \n ይሄን ለጐዋደኛዎ ያጋሩ! \n \n \n ላክ እሚለዉን በመጫን ያጋሩ! \n \n",reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("➡️ ላክ ⬅️", url=url)))        

def get_last(username):
    sql = "SELECT * FROM `game_result` WHERE username = %s"
    val = (username,)
    c.execute(sql,val)
    user_res = c.fetchone()
    if user_res is None:
        return "NO"
    else:
        return user_res[2]
def set_game(username,ans,last):
    sql = "INSERT INTO `game_result` (`username`, `result`, `last`) VALUES (%s,%s,%s)"
    val = (username,ans,last)
    c.execute(sql,val)
    db.commit()
def update_game(username,ans,last):
    sql = "UPDATE game_result SET result = %s, last = %s WHERE username = %s"
    rsql = c.execute("SELECT * FROM game_result WHERE username = %s",(username,))
    pres = c.fetchone()
    val = ((str(pres[1])+str(ans)),last,username)
    c.execute(sql,val)
    db.commit()
def endgame(bot,call):
    bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="""
    Meeting your soulmate is one of the best experiences in the world!
    \n/start 👈 ጥያቄዎቺን ለማስጀመር 
    \n/Find  👈 ከ እረሶ ጋር ተመሳሳይ መልስ ያላችዉን ሰዎች ለማየት፡፡
    \n/Check 👈 ከ ጐደኛዋ ጋር የጥያቄ ጌሞቺን ለመጫዎት እና ልዩነትዎቺን ለማየት፡፡
    \n/Reset 👈 እንዳዲስ ለማስጀመረ.
    \n \n ➖➖➖➖➖➖➖➖➖➖
    """)        
def find_match(bot,msg):
    c.execute("SELECT result FROM game_result WHERE username = %s",(msg.from_user.username,))
    user_result = str(c.fetchone()[0])
    c.execute("SELECT * FROM game_result")
    allres = c.fetchall()
    matchs = []
    lists = ""
    for i in range(len(allres)):
        k = 0
        level = 0
        for j in str(allres[i][1]):
            if user_result[k] == j:
                level = level+10
            else:
                print("Unmatch")
            k+=1
        if level >=60:
            if allres[i][0] == msg.from_user.username:
                print("You")
            else:
                matchs.append((allres[i][0],level))
    for m in range(len(matchs)):
        print()
        lists = lists+ "\n "+user.find_user(matchs[m][0])[0]+" \t \t @"+matchs[m][0]+" \t "+user.find_user(matchs[m][0])[2]+" \t "+str(matchs[m][1])+"% \n"
    if len(matchs) == 0:
            bot.send_message(msg.chat.id,"""
    የእርሶ ተመሳሳይ ዝርዝር:
    ➖➖➖➖➖➖➖➖➖➖➖➖
            😔ለጊዜዉ ምንም ተመሳሳይ የለዎትም😔
            \n ከትንሽ ጊዜ በህዋላ ይመለሱ  👉 /Find
    \n\n  ➖➖➖➖➖➖➖➖➖➖➖➖
    """,reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("↪️ ይመለሱ", callback_data="ans1")))
    else:
        bot.send_message(msg.chat.id,"""
    የእርሶ ተመሳሳይ ዝርዝር:
    ➖➖➖➖➖➖➖➖➖➖➖➖
    \n Full Name \t User Name \t Sex \t Matching 
    """+lists+""" 

    \n\n  ➖➖➖➖➖➖➖➖➖➖➖➖
    """,reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("↪️ ይመለሱ", callback_data="ans1")))



