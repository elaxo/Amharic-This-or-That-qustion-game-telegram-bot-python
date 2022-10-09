import telebot
import time
import users as user
import game as ga
import bot_info as binfo
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
TELEGRAM_TOKEN = binfo.Token
bot = telebot.TeleBot(TELEGRAM_TOKEN)

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🧒🏻ወንድ", callback_data="cb_yes"),
               InlineKeyboardButton("👧🏼ሴት", callback_data="cb_no"))
    return markup
def gen_markupI(party,suser,cat):
    print(party,suser,cat)
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🧒🏻ወንድ", callback_data="cb_yesi"),
               InlineKeyboardButton("👧🏼ሴት", callback_data="cb_noi"))
    return markup
def start():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("በድጋሚ ይሞክሩ", callback_data="start"),)
    return markup
def startG():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("----ጀምር-----", callback_data="startG"),)
    return markup
def startGI(cat):
    if user.have_se(cat[1]):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("----ጀምር-----", callback_data="Goback"),)
    else:
        user.set_current(cat)
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("ጀምር", callback_data="StartIG"),)
    return markup
def send_catag(m):
    cat = user.get_catag()
    markup = InlineKeyboardMarkup()
    for i in range(len(cat)):
        if cat[i][0] == 4:
            markup.add(InlineKeyboardButton(str(cat[i][1]), callback_data="back"),)
        else:
            markup.add(InlineKeyboardButton(str(cat[i][1]), callback_data=str(cat[i][0])),)
    return markup
    #bot.send_message(message.chat.id,fullname+" wants to check what is in common with you!",reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("😁 Send 😁", url="https://t.me/share/url?url=🤚🖐Hey! \nYour friend "+fullname+" wants to check what is in common with you! \n👉https://t.me/"+binfo.username+"?start="+username)))


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        if call.from_user.username is None:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="""username ሊኖርዎት ግድ ነዉ! ይህን ስቴፕ በመከተል ያስትካክሉ 
            \nStep 1. Go to the menu "Settings"
            \nStep 2: Click "Edit" button
            \nStep 3. Click on the "username" field
            \nStep 4: Create a username and click "Done" Done! Your username is set.
             \n and come back again!
            """,reply_markup=start())
        else:
            if user.is_exist(call.from_user.username) >=1:
                print("User already exists!")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='ግልጽ እኮ ነው!😁😁')
                time.sleep(0.5)
                start_game(call)
            else:
                user.create_user(call.from_user.first_name,call.from_user.username,"Male",call.from_user.id)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='ተመዝግበዋል!')
                time.sleep(0.5)
                start_game(call)
    elif call.data == "cb_no":
        if call.from_user.username is None:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="""username ሊኖርዎት ግድ ነዉ! ይህን ስቴፕ በመከተል ያስትካክሉ  
            \nStep 1. Go to the menu "Settings"
            \nStep 2: Click "Edit" button
            \nStep 3. Click on the "username" field
            \nStep 4: Create a username and click "Done" Done! Your username is set.
            \n and come back again!
            """,reply_markup=start())
        else:
            if user.is_exist(call.from_user.username) >=1:
                print("User already exists!")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='ግልጽ እኮ ነው!😁😁')
                time.sleep(0.5)
                start_game(call)
            else:
                user.create_user(call.from_user.first_name,call.from_user.username,"Female",call.from_user.id)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='ተመዝግበዋል!')
                time.sleep(0.5)
                start_game(call)
    elif call.data == "cb_yesi":
        if call.from_user.username is None:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="""username ሊኖርዎት ግድ ነዉ! ይህን ስቴፕ በመከተል ያስትካክሉ  
            \nStep 1. Go to the menu "Settings"
            \nStep 2: Click "Edit" button
            \nStep 3. Click on the "username" field
            \nStep 4: Create a username and click "Done" Done! Your username is set.
             \n and come back again!
            """,reply_markup=startI())
        else:
            if user.is_exist(call.from_user.username) >=1:
                print("User already exists!")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='ግልጽ እኮ ነው!😁😁')
                time.sleep(0.5)
                start_gameI(call)
            else:
                user.create_user(call.from_user.first_name,call.from_user.username,"Male",call.from_user.id)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='ተመዝግበዋል!')
                time.sleep(0.5)
                start_gameI(call)
    elif call.data == "cb_noi":
        if call.from_user.username is None:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="""username ሊኖርዎት ግድ ነዉ! ይህን ስቴፕ በመከተል ያስትካክሉ  
            \nStep 1. Go to the menu "Settings"
            \nStep 2: Click "Edit" button
            \nStep 3. Click on the "username" field
            \nStep 4: Create a username and click "Done" Done! Your username is set.
            \n and come back again!
            """,reply_markup=start())
        else:
            if user.is_exist(call.from_user.username) >=1:
                print("User already exists!")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='ግልጽ እኮ ነው!!😁😁')
                time.sleep(0.5)
                start_gameI(call)                
            else:
                user.create_user(call.from_user.first_name,call.from_user.username,"Female",call.from_user.id)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='ተመዝግበዋል!')
                time.sleep(0.5)
                start_gameI(call)
    elif call.data == "start":
        #bot.edit_message_text(call., text=NEW_TEXT, message_id=MESSAGE_TO_EDIT)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= "  እንኳን ወደ ቦታችን በደና መጡ! \n እባክዎ ይመዝገቡ! \n\n  እርስዎ?", reply_markup=gen_markup())
        #bot.edit_message_text(chat_id=call.json.chat.id,text="Welcome \n Register?", message_id=call.json.message.id)
    elif call.data == "startG":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="""
        !ወደ ጨዋታው 👍 \n
        😁በዚ ጨዋታ አንዳንድ ጥያቄወችን ይጠየቃሉ! ጨዋታው እሚሆነዉ ጥያቄወችን መመለስ እና ተመሳሳይ መላሾቸን ማግኘት ነው፡፡
                """)
        time.sleep(2)
        ga.play(bot,call.from_user.username,call)
    elif False:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="""
        !ወደ ጨዋታው 👍 \n
        😁በዚ ጨዋታ አንዳንድ ጥያቄወችን ይጠየቃሉ! ጨዋታው እሚሆነዉ ጥያቄወችን መመለስ እና ተመሳሳይ መላሾቸን ማግኘት ነው፡፡
                """)
        time.sleep(2)
        ga.playI(bot,call.from_user.username,call,0)
        #bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="LOL",reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("LOLIPOP", callback_data="ans1"),InlineKeyboardButton("CANDY", callback_data="ans2")))
    elif call.data == "ans1":
         last = ga.get_last(call.from_user.username)
         
         print(last)
         if last == "NO":
            print("He never been playd")
            ga.set_game(call.from_user.username,1,0)
            ga.play(bot,call.from_user.username,call)
         elif last >= 9:
            ga.endgame(bot,call)
         else:
            ga.update_game(call.from_user.username,1,last+1)
            ga.play(bot,call.from_user.username,call)
    elif call.data == "ans2":
         last = ga.get_last(call.from_user.username)
         print(last)
         if last == "NO":
            print("He never been playd")
            ga.set_game(call.from_user.username,2,0)
            ga.play(bot,call.from_user.username,call)
         else:
            ga.update_game(call.from_user.username,2,last+1)
            ga.play(bot,call.from_user.username,call)
    elif call.data == "0":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="እነዚህን ጥያቄዎቸ በትክክል ይመልስዋቸዉ እና ለጐደኛዎ ያጋሩ እና ልዩነቱን ይምልከቱ! \n ❗️ ያስታዉሱ ከዚ በፊት ለጐደኛዎ የላኩት ሊንክ ካለ ሂደቱ ይቈርጣል ❗️\n    ትንሽ ይጠብቁ.......")        
        if ga.self_isPlay(call.from_user.username):
            ga.self_delete(call.from_user.username)
        ga.self_cplay(bot,call,0)
        ga.self_play(bot,call,0)
    elif call.data == "1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="እነዚህን ጥያቄዎቸ በትክክል ይመልስዋቸዉ እና ለጐደኛዎ ያጋሩ እና ልዩነቱን ይምልከቱ! \n ❗️ ያስታዉሱ ከዚ በፊት ለጐደኛዎ የላኩት ሊንክ ካለ ሂደቱ ይቈርጣል ❗️\n    ትንሽ ይጠብቁ.......")
        if ga.self_isPlay(call.from_user.username):
            ga.self_delete(call.from_user.username)
        ga.self_cplay(bot,call,1)
        ga.self_play(bot,call,1)
    elif call.data == "2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="እነዚህን ጥያቄዎቸ በትክክል ይመልስዋቸዉ እና ለጐደኛዎ ያጋሩ እና ልዩነቱን ይምልከቱ! \n ❗️ ያስታዉሱ ከዚ በፊት ለጐደኛዎ የላኩት ሊንክ ካለ ሂደቱ ይቈርጣል ❗️\n    ትንሽ ይጠብቁ.......")
        if ga.self_isPlay(call.from_user.username):
            ga.self_delete(call.from_user.username)
        ga.self_cplay(bot,call,2)
        ga.self_play(bot,call,2)
    elif call.data == "3":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="እነዚህን ጥያቄዎቸ በትክክል ይመልስዋቸዉ እና ለጐደኛዎ ያጋሩ እና ልዩነቱን ይምልከቱ! \n ❗️ ያስታዉሱ ከዚ በፊት ለጐደኛዎ የላኩት ሊንክ ካለ ሂደቱ ይቈርጣል ❗️\n    ትንሽ ይጠብቁ.......")
        if ga.self_isPlay(call.from_user.username):
            ga.self_delete(call.from_user.username)
        ga.self_cplay(bot,call,3)
        ga.self_play(bot,call,3)
    elif call.data == "ans1s":
        last = ga.get_self_last(call.from_user.username)
        ga.set_self_play(call.from_user.username,1)
        last = last+1
        if last >= 10:
            ga.endgameI(bot,call)
        else:
            ga.set_play_last(call.from_user.username,last)
            ga.update_self_game(bot,call,call.from_user.username,last)
    elif call.data == "ans2s":
        last = ga.get_self_last(call.from_user.username)
        ga.set_self_play(call.from_user.username,2)
        last = last+1
        if last >=10:
            ga.endgameI(bot,call)
        else:
            ga.set_play_last(call.from_user.username,last)
            ga.update_self_game(bot,call,call.from_user.username,last)
    elif call.data == "back":
        ga.endgame(bot,call)
    elif call.data == "Goback":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="😒😒 እባክዎ የጀመሩትን ይጨርሱ! \t ከዚ በፊት የጀመሩትን ይጨርሱ!  😒😒 \n \n \n \n ይጨርሱና ይምልሱ!  ልክ ያልሆነ ነገር ካሉ ይህን ይጫኑ 👉 \Reset")
    elif call.data == "StartIG":
        ga.party_play(bot,call)
    elif call.data == "ans1i":
        last = ga.get_lastparty(call.from_user.username)
        ga.set_party_play(call.from_user.username,1)
        print("Last:",last)
        last = int(last)+1
        print("Ans1 : ",last)
        if last >= 10:
            pid = user.session_pid(call.from_user.username)
            user.delete_session(call.from_user.username)
            ga.endgameParty(bot,call,pid)
        else:
            ga.set_party_last(call.from_user.username,last)
            ga.update_party_game(bot,call,call.from_user.username,last)
    elif call.data == "ans2i":
        last = ga.get_lastparty(call.from_user.username)
        ga.set_party_play(call.from_user.username,2)
        print("Last:",last)
        last = int(last)+1
        print("Ans1 : ",last)
        if last >= 10:
            pid = user.session_pid(call.from_user.username)
            user.delete_session(call.from_user.username)
            ga.endgameParty(bot,call,pid)
        else:
            ga.set_party_last(call.from_user.username,last)
            ga.update_party_game(bot,call,call.from_user.username,last)
    elif call.data == "home":
        ga.endgame(bot,call)




         
@bot.message_handler(commands=['start'])
def message_handler(message):
    if message.from_user.username is None:
        print("NO username")
        bot.send_message(message.chat.id, """username ሊኖርዎት ግድ ነዉ! ይህን ስቴፕ በመከተል ያስትካክሉ  
            \nStep 1. Go to the menu "Settings"
            \nStep 2: Click "Edit" button
            \nStep 3. Click on the "username" field
            \nStep 4: Create a username and click "Done" Done! Your username is set.
             \n and come back again!
            """,reply_markup=start())
    elif len(message.text) > 7:
        party = user.find_user(message.text[8:])
        if user.update_party(party[1],message.from_user.username) == 1:
            user.user_cach(message.from_user.username,party[1])
            bot.send_message(message.chat.id, "እንኳን ደህና ምጡ!,  በዚ ጨዋታ አንዳንድ ጥያቄወችን ይጠየቃሉ! ጨዋታው እሚሆነዉ ጥያቄወችን መመለስ እና ተመሳሳይ መላሾቸን ማግኘት ነው፡፡"+party[0]+" ከእርሶ ጋር የጥያቄ ጨዋታወቺን መጫዎት ይፈልጋሉ፡፡ \n\n መቀጠል ከፈለጉ እባክዎ ይምዝገቡ?\n  እርስዎ?", reply_markup=gen_markupI(party[1],message.from_user.username,message.text[7]))
        elif user.update_party(party[1],message.from_user.username) == -1:
            bot.send_message(message.chat.id, "ይሄ ሊንክ የእርስዎ ነው ለሌላ ሰው ያጋሩ!",reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("Go Back", callback_data="home")))
        else:
            bot.send_message(message.chat.id, "ይሄ ሊንክ ጊዜዉ አልፍዋል",reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("ይመለሱ", callback_data="home")))
    else:
        bot.send_message(message.chat.id, "እንኳን ደህና ምጡ! ? \n\n  እባክዎ ይምዝገቡ?", reply_markup=gen_markup())

@bot.message_handler(commands=['Find'])
def message_handler(message):
        bot.send_message(message.chat.id, "ተመሳሳይዎን በመፈለግ ላይ...........💣")
        ga.find_match(bot,message)

@bot.message_handler(commands=['Reset'])
def message_handler(message):
        bot.send_message(message.chat.id, "ሁሉንም ወደ አዲስ በመቀየር ላይ.......")
        user.reset(message.from_user.username)
        bot.send_message(message.chat.id, "ተሳክትዋል!  ",reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("ይመለሱ", callback_data="home")))



@bot.message_handler(commands=['Check'])
def message_handler(message):
    fullname = str(message.from_user.full_name)
    username = message.from_user.username
    print(fullname)
    bot.send_message(message.chat.id,"ይምርጡ:",reply_markup=send_catag(message))



def start_game(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='ጨዋታዊ ጥያቄዎቺን ይጠየቃሉ! \n ሁሉንም ይመልሱ! \n ሲዘጋጁ ጀምር እሚለውን ይጫኑ! \n\n --😁😁😁😁😁😁😁--',reply_markup=startG())


def start_gameI(call):
    party = user.get_cach(call.from_user.username)
    data = user.find_party(party)
    print("Start_gameI function :",data)
    useri = user.find_user(data[2])
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=useri[0]+'  ከእርሶ ጋር የጥያቄ ጨዋታወቺን መጫዎት ይፈልጋሉ፡፡ \n ሁሉንም ይመልሱ! \n ሲዘጋጁ ጀምር እሚለውን ይጫኑ! \n\n --😁😁😁😁😁😁😁--',reply_markup=startGI(data))
    user.delete_cach(call.from_user.username)





bot.polling()
  
        
