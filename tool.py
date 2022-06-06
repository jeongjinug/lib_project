import pandas as pd
from tkinter import *
from tkinter import messagebox, ttk
import datetime


User = pd.read_csv('UserMake_DF.csv', encoding='utf-8-sig')
Book = pd.read_csv('BookMake_DF.csv', encoding='utf-8-sig')

window = Tk()
window.title("도서 관리 프로그램")
window.geometry("800x600")
window.resizable(width = False, height = False)

def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text,"%Y-%m-%d")
        return True
    except ValueError:
        return False

def Member_make() :
    def quit1() :
        toplevel.destroy()

    def register() :
        checkphone = ""
        checkname = ""
        checkbirthday = ""
        checksex = ""
        checkmail= ""
        count = 0
        count2 = 0
        MsgBox = messagebox.askquestion ('등록 확인','등록하시겠습니까??')
        if MsgBox == 'yes':
            if (phonetext.get().replace(" ", "") == "") :
                checkphone = "전화번호"
                count2 = count2 + 1
            if (nametext.get().replace(" ", "") == "") :
                checkname = "이름"
                count2 = count2 + 1
            if (birthdaytext.get().replace(" ", "") == "") :
                checkbirthday = "생일"
                count2 = count2 + 1
            if (sextext.get().replace(" ", "") == "") :
                checksex = "성별"
                count2 = count2 + 1
            if (mailtext.get().replace(" ", "") == "") :
                checkmail = "메일"
                count2 = count2 + 1
            if count2 >= 1 :
                messagebox.showinfo("잘못된 형식", "{} {} {} {} {} 입력이 되지 않았습니다.".format(checkphone,checkname,checkbirthday,checksex,checkmail))
                return
            if (len(phonetext.get().replace(" ", "")) <= 8)  :
                checkphone = "전화번호"
                count = count + 1
            elif (len(phonetext.get().replace(" ", "")) != 13) | (phonetext.get().replace(" ", "").count('-') != 2) | (phonetext.get().replace(" ", "")[:3] != "010") |  (phonetext.get().replace(" ", "")[3] != '-') | (phonetext.get().replace(" ", "")[8] != '-') | (any(eng.isalpha() for eng in phonetext.get().replace(" ", ""))) :
                checkphone = "전화번호"
                count = count + 1
            if nametext.get().replace(" ", "").isalpha() == False :
                checkname = "이름"
                count = count + 1
            if (len(birthdaytext.get().replace(" ", "")) <= 7)  :
                checkbirthday = "생일"
                count = count + 1
            elif len(birthdaytext.get().replace(" ", "")) != 10 | (birthdaytext.get().replace(" ", "").count('-') != 2) | (birthdaytext.get().replace(" ", "")[4] != '-') | (birthdaytext.get().replace(" ", "")[7] != '-') | (any(eng2.isalpha() for eng2 in birthdaytext.get().replace(" ", ""))) | (validate_date(birthdaytext.get().replace(" ", "")) == False) | (int((birthdaytext.get().replace(" ", "")[:4])) > 2017) :
                checkbirthday = "생일"
                count = count + 1
            if (sextext.get().replace(" ", "") != "남") & (sextext.get().replace(" ", "") != "여") :
                checksex = "성별"
                count = count + 1
            if mailtext.get().replace(" ", "").find("@") == -1 :
                checkmail = "메일"
                count = count + 1

            if phonetext.get().replace(" ", "") in User['User_phone'].values.astype(str) :
                messagebox.showinfo("중복", "이미 등록된 전화번호입니다.")
            elif count >= 1 :
                messagebox.showinfo("잘못된 형식", "{} {} {} {} {} 형식이 잘못되었습니다.".format(checkphone,checkname,checkbirthday,checksex,checkmail))
            else : 
                today = datetime.datetime.now()
                today = today.date()
                messagebox.showinfo("등록 완료", "등록이 완료되었습니다.")
                User.loc[phonetext.get().replace(" ", "")] = [phonetext.get().replace(" ", ""), nametext.get().replace(" ", ""), birthdaytext.get().replace(" ", "") ,sextext.get().replace(" ", ""), mailtext.get().replace(" ", ""), today, 'X', 0, 'X']
                User.to_csv('UserMake_DF.csv', mode = 'w', index = False ,header = True, encoding='utf-8-sig')
                toplevel.destroy()
        else:
            messagebox.showinfo("등록 취소", "등록이 취소되었습니다.")
            toplevel.destroy()
        
    def overlapcheck() :
        if (phonetext.get().replace(" ", "") == "")  :
            messagebox.showinfo("잘못된 형식", "전화번호 입력이 되지 않았습니다.")
            return
        if (len(phonetext.get().replace(" ", "")) <= 8) :
            messagebox.showinfo("잘못된 형식", "전화번호 형식이 잘못되었습니다.") 
            return
        elif (len(phonetext.get().replace(" ", "")) != 13) | (phonetext.get().replace(" ", "").count('-') != 2) | (phonetext.get().replace(" ", "")[:3] != "010") | (phonetext.get().replace(" ", "")[3] != '-') | (phonetext.get().replace(" ", "")[8] != '-') | (any(eng.isalpha() for eng in phonetext.get().replace(" ", ""))) :
            messagebox.showinfo("잘못된 형식", "전화번호 형식이 잘못되었습니다.") 
            return

        if phonetext.get().replace(" ", "") in User['User_phone'].values.astype(str) :
            messagebox.showinfo("중복", "이미 등록된 전화번호입니다.")
        else : 
            messagebox.showinfo("사용 가능", "사용 가능한 전화번호입니다.")


    toplevel=Toplevel(window)
    toplevel.geometry("700x500")

    label=Label(toplevel, text="회원등록", font = ("돋움체", 20))
    label.place(x = 290, y = 30)

    phonelabel1 = Label(toplevel, text = "전화번호")
    phonelabel1.place(x = 225, y= 100)
    phonetext = Entry(toplevel, width = 20)
    phonetext.place(x = 325, y= 100)
    phoneform1 = Label(toplevel, text = "EX) 000-0000-0000", font = ("돋움체", 8) ,fg = "red" )
    phoneform1.place(x = 340, y = 120)

    namelabel1 = Label(toplevel, text = "이름")
    namelabel1.place(x = 225, y= 150)
    nametext = Entry(toplevel, width = 20)
    nametext.place(x = 325, y= 150)
    nameform1 = Label(toplevel, text = "EX) 홍길동", font = ("돋움체", 8) ,fg = "red" )
    nameform1.place(x = 365, y = 170)

    birthdaylabel1 = Label(toplevel, text = "생일")
    birthdaylabel1.place(x = 225, y=200 )
    birthdaytext = Entry(toplevel, width = 20)
    birthdaytext.place(x = 325, y= 200)
    birthdayform1 = Label(toplevel, text = "EX) 0000-00-00", font = ("돋움체", 8) ,fg = "red" )
    birthdayform1.place(x = 350, y = 220)

    sexlabel1 = Label(toplevel, text = "성별")
    sexlabel1.place(x = 225, y= 250)
    sextext = Entry(toplevel, width = 20)
    sextext.place(x = 325, y= 250)
    sexform1 = Label(toplevel, text = "남 or 여", font = ("돋움체", 8) ,fg = "red" )
    sexform1.place(x = 370, y = 270)

    maillabel1 = Label(toplevel, text = "메일")
    maillabel1.place(x = 225, y= 300)
    mailtext = Entry(toplevel, width = 20)
    mailtext.place(x = 325, y= 300)
    mailform1 = Label(toplevel, text = "EX) oooo@ooo.oo", font = ("돋움체", 8) ,fg = "red" )
    mailform1.place(x = 350, y = 320)

    clearbutton = Button(toplevel, text = "등록", command = register)
    cancelbutton = Button(toplevel, text = "취소", command = quit1)
    overlapbutton = Button(toplevel, text = "중복 조회", command = overlapcheck ,font =("돋움체", 8),fg= "blue" , width = 10)
    clearbutton.place(x = 275, y = 400)
    cancelbutton.place(x = 375, y = 400)
    overlapbutton.place(x = 480, y =100)

def Member_search() : 
    def search() :
        global treeview
        treeview = ttk.Treeview(toplevel2, column = ["이름", "생년월일", "전화번호", "성별", "탈퇴여부", "대여여부"],
            displaycolumns=["이름", "생년월일", "전화번호", "성별", "탈퇴여부", "대여여부"])
        treeview.place(x= 50, y = 170)
        treeview.column("이름", width = 100, anchor = CENTER)
        treeview.heading("이름", text = "이름", anchor = CENTER)
        treeview.column("생년월일", width = 100, anchor = CENTER)
        treeview.heading("생년월일", text = "생년월일", anchor = CENTER)
        treeview.column("전화번호", width = 100, anchor = CENTER)
        treeview.heading("전화번호", text = "전화번호", anchor = CENTER)
        treeview.column("성별", width = 100, anchor = CENTER)
        treeview.heading("성별", text = "성별", anchor = CENTER)
        treeview.column("탈퇴여부", width = 100, anchor = CENTER)
        treeview.heading("탈퇴여부", text = "탈퇴여부", anchor = CENTER)
        treeview.column("대여여부", width = 100, anchor = CENTER)
        treeview.heading("대여여부", text = "대여여부", anchor = CENTER)
        treeview["show"] = "headings"
        
        if (phonetext2.get() == '') & (nametext2.get() == '') :
            return
        elif phonetext2.get() == '' :
            Search = User[User['User_name'].str.contains(nametext2.get())]
        elif nametext2.get() == '' :
            Search = User[User['User_phone'].str.contains(phonetext2.get())]
        else :
            Search = User[User['User_phone'].str.contains(phonetext2.get()) | User['User_name'].str.contains(nametext2.get())]
        Search = Search[['User_name', 'User_birthday', 'User_phone', 'User_sex', 'User_withdrawcheck', 'User_rentcnt']]
        Search = Search.values.tolist()
        for i in range(len(Search)):
            treeview.insert("", "end", text = "", values=Search[i], iid = i)


        choicebutton = Button(toplevel2, text = "선택")
        choicebutton.bind('<Button>', choice)
        choicebutton.place(x = 325, y = 400)
        treeview.bind('<Double-Button-1>', choice)

    def choice(event) :
        sel = treeview.focus()

        try :
            selectedname = treeview.item(sel).get("values")[0]
            selectedphone = treeview.item(sel).get("values")[2]

        except IndexError :
            messagebox.showinfo("오류", "조회된 정보가 없습니다.")
            return

        Search = User[(User['User_phone'] == selectedphone) | (User['User_name'] == selectedname)]


        toplevel3 =Toplevel(window)
        toplevel3.geometry("700x500")

        label=Label(toplevel3, text="회원 정보 상세 창", font = ("돋움체", 20), anchor = N)
        label.place(x = 225, y = 30)

        phonelabel3 = Label(toplevel3, text = "전화번호")
        phonelabel3.place(x = 225, y= 90)
        phonetext3 = Entry(toplevel3, width = 20)
        phonetext3.insert(0, Search.iloc[0]['User_phone'])
        phonetext3.place(x = 325, y= 90)
        phoneform2 = Label(toplevel3, text = "EX) 000-0000-0000", font = ("돋움체", 8) ,fg = "red" )
        phoneform2.place(x = 340, y = 110)

        namelabel3 = Label(toplevel3, text = "이름")
        namelabel3.place(x = 225, y= 140)
        nametext3 = Entry(toplevel3, width = 20)
        nametext3.insert(0, Search.iloc[0]['User_name'])
        nametext3.place(x = 325, y= 140)
        nameform2 = Label(toplevel3, text = "EX) 홍길동", font = ("돋움체", 8) ,fg = "red" )
        nameform2.place(x = 365, y = 160)

        birthdaylabel3 = Label(toplevel3, text = "생일")
        birthdaylabel3.place(x = 225, y=190 )
        birthdaytext3 = Entry(toplevel3, width = 20)
        birthdaytext3.insert(0, Search.iloc[0]['User_birthday'])
        birthdaytext3.place(x = 325, y= 190)
        birthdayform2 = Label(toplevel3, text = "EX) 0000-00-00", font = ("돋움체", 8) ,fg = "red" )
        birthdayform2.place(x = 350, y = 210)

        sexlabel3 = Label(toplevel3, text = "성별")
        sexlabel3.place(x = 225, y= 240)
        sextext3 = Entry(toplevel3, width = 20)
        sextext3.insert(0, Search.iloc[0]['User_sex'])
        sextext3.place(x = 325, y= 240)
        sexform2 = Label(toplevel3, text = "남 or 여", font = ("돋움체", 8) ,fg = "red" )
        sexform2.place(x = 370, y = 260)

        maillabel3 = Label(toplevel3, text = "메일")
        maillabel3.place(x = 225, y= 290)
        mailtext3 = Entry(toplevel3, width = 20)
        mailtext3.insert(0, Search.iloc[0]['User_mail'])
        mailtext3.place(x = 325, y= 290)
        mailform2 = Label(toplevel3, text = "EX) oooo@ooo.oo", font = ("돋움체", 8) ,fg = "red" )
        mailform2.place(x = 350, y = 310)

        rentlabel = Label(toplevel3, text = "대여 여부")
        rentlabel.place(x = 185, y= 340)
        renttext = Entry(toplevel3, width = 5)
        renttext.insert(0, Search.iloc[0]['User_rentcnt'])
        renttext.place(x = 255, y= 340)

        quitlabel1 = Label(toplevel3, text = "탈퇴 여부")
        quitlabel1.place(x = 385, y= 340)
        quittext = Entry(toplevel3, width = 5)
        quittext.insert(0, Search.iloc[0]['User_withdrawcheck'])
        quittext.place(x = 455, y= 340)

        def modify() :
            checkphone = ""
            checkname = ""
            checkbirthday = ""
            checksex = ""
            checkmail= ""
            count = 0
            count2 = 0
            MsgBox = messagebox.askquestion ('수정 확인','수정하시겠습니까??')
            if MsgBox == 'yes':
                if (phonetext3.get().replace(" ","") == "") :
                    checkphone = "전화번호"
                    count2 = count2 + 1
                if (nametext3.get().replace(" ","") == "") :
                    checkname = "이름"
                    count2 = count2 + 1
                if (birthdaytext3.get().replace(" ","") == "") :
                    checkbirthday = "생일"
                    count2 = count2 + 1
                if count2 >= 1 :
                    messagebox.showinfo("잘못된 형식", "{} {} {} 입력이 되지 않았습니다.".format(checkphone,checkname,checkbirthday))
                    return

                if (len(phonetext3.get().replace(" ", "")) <= 8)  :
                    checkphone = "전화번호"
                    count = count + 1 
                elif (len(phonetext3.get().replace(" ", "")) != 13) | (phonetext3.get().replace(" ", "").count('-') != 2) | (phonetext3.get().replace(" ", "")[:3] != "010") |  (phonetext3.get().replace(" ", "")[3] != '-') | (phonetext3.get().replace(" ", "")[8] != '-') | (any(eng.isalpha() for eng in phonetext3.get().replace(" ", "")))  :
                    checkphone = "전화번호"
                    count = count + 1
                if nametext3.get().replace(" ", "").isalpha() == False :
                    checkname = "이름"
                    count = count + 1
                if (len(birthdaytext3.get().replace(" ", "")) <= 7)  :
                    checkphone = "생일"
                    count = count + 1
                elif len(birthdaytext3.get().replace(" ", "")) != 10 | (birthdaytext3.get().replace(" ", "").count('-') != 2) | (birthdaytext3.get().replace(" ", "")[4] != '-') | (birthdaytext3.get().replace(" ", "")[7] != '-') | (any(eng2.isalpha() for eng2 in birthdaytext3.get().replace(" ", ""))) | (validate_date(birthdaytext3.get().replace(" ", "")) == False) :
                    checkbirthday = "생일"
                    count = count + 1
                if (sextext3.get().replace(" ", "") != "남") & (sextext3.get().replace(" ", "") != "여") :
                    checksex = "성별"
                    count = count + 1
                if mailtext3.get().replace(" ", "").find("@") == -1 :
                    checkmail = "메일"
                    count = count + 1

                if (Search['User_withdrawcheck'] == 'O').any() :
                    messagebox.showinfo("수정 불가능", "이미 탈퇴한 회원은 수정이 불가능합니다.")
                elif (Search['User_rentcnt'] >= 1 ).any() :
                    messagebox.showinfo("수정 불가능", "대여 중인 회원은 수정이 불가능합니다.")
                elif count >= 1 :
                    messagebox.showinfo("잘못된 형식", "{} {} {} {} {} 형식이 잘못되었습니다.".format(checkphone,checkname,checkbirthday,checksex,checkmail))
                else : 
                    if Search.iloc[0]['User_phone'] == phonetext3.get() :
                        messagebox.showinfo("수정 완료", "수정이 완료되었습니다.")
                        User.loc[(User['User_phone'] == selectedphone) | (User['User_name'] == selectedname), ('User_phone', 'User_name', 'User_birthday', 'User_sex', 'User_mail')] = [phonetext3.get().replace(" ", ""), nametext3.get().replace(" ", ""), birthdaytext3.get().replace(" ", "") ,sextext3.get().replace(" ", ""), mailtext3.get().replace(" ", "")]
                        User.to_csv('UserMake_DF.csv', mode = 'w', index = False, header = True, encoding='utf-8-sig')
                        toplevel3.destroy()
                        toplevel2.destroy()
                        
                    elif phonetext3.get() in User['User_phone'].values.astype(str) :
                        messagebox.showinfo("중복", "이미 등록된 전화번호입니다.")
                    

                    else : 
                        messagebox.showinfo("수정 완료", "수정이 완료되었습니다.")
                        User.loc[(User['User_phone'] == selectedphone.get()) | (User['User_name'] == selectedname.get()), ('User_phone', 'User_name', 'User_birthday', 'User_sex', 'User_mail')] = [phonetext3.get(), nametext3.get(), birthdaytext3.get() ,sextext3.get(), mailtext3.get()]
                        User.to_csv('UserMake_DF.csv', mode = 'w', index = False, header = True, encoding='utf-8-sig')
                        toplevel3.destroy()
                        toplevel2.destroy()
                    
            else:
                messagebox.showinfo("수정 취소", "수정이 취소되었습니다.")
                toplevel2.destroy()
        
        def overlapcheck() :
            if Search.iloc[0]['User_phone'] == phonetext3.get() :
                return 
            if (phonetext3.get().replace(" ", "") == "")  :
                messagebox.showinfo("잘못된 형식", "전화번호 입력이 되지 않았습니다.")
                return
            if (len(phonetext3.get().replace(" ", "")) <= 8) :
                messagebox.showinfo("잘못된 형식", "전화번호 형식이 잘못되었습니다.") 
                return
            elif (len(phonetext3.get().replace(" ", "")) != 13) | (phonetext3.get().replace(" ", "").count('-') != 2) | (phonetext3.get().replace(" ", "")[:3] != "010") | (phonetext3.get().replace(" ", "")[3] != '-') | (phonetext3.get().replace(" ", "")[8] != '-') | (any(eng.isalpha() for eng in phonetext3.get().replace(" ", ""))) | (phonetext3.get() == ""):
                messagebox.showinfo("잘못된 형식", "전화번호 형식이 잘못되었습니다.") 
                return
            else : 
                if  phonetext3.get() in User['User_phone'].values.astype(str) :
                    messagebox.showinfo("중복", "이미 등록된 전화번호입니다.")
                else : 
                    messagebox.showinfo("사용 가능", "사용 가능한 전화번호입니다.")

        def out() :
            MsgBox = messagebox.askquestion ('탈퇴 확인','탈퇴하시겠습니까??')
            if MsgBox == 'yes':
                if (Search['User_rentcnt'] >= 1 ).any() :
                    messagebox.showinfo("탈퇴 불가능", "대여 중인 회원은 탈퇴가 불가능합니다.")

                elif (Search['User_withdrawcheck'] == 'O').any() :
                    messagebox.showinfo("탈퇴 불가능", "이미 탈퇴한 회원은 탈퇴가 불가능합니다.")

                elif (Search['User_withdrawcheck'] == 'X').any() :
                    User.loc[(User['User_phone'] == phonetext2.get()) | (User['User_name'] == nametext2.get()), ('User_withdrawcheck')] = "O"
                    User.to_csv('UserMake_DF.csv', mode = 'w', index = False ,header = True, encoding='utf-8-sig')

                    messagebox.showinfo("탈퇴 완료", "탈퇴가 완료되었습니다.")
                    toplevel3.destroy()
                    toplevel2.destroy()
            
            else : 
                messagebox.showinfo("수정 취소", "수정이 취소되었습니다.")

        def cancel() :
            toplevel3.destroy()

        modifybutton = Button(toplevel3, text = "수정", command = modify)
        outbutton = Button(toplevel3, text = "탈퇴", command = out)
        cancelbutton = Button(toplevel3, text = "취소", command = cancel)
        overlapbutton = Button(toplevel3, text = "중복 조회", command = overlapcheck ,font =("돋움체", 8),fg= "blue" , width = 10)
        modifybutton.place(x = 275, y = 400)
        outbutton.place(x = 325, y = 400)
        cancelbutton.place(x = 375, y = 400)
        overlapbutton.place(x = 480, y = 90)

    def quit2() :
        toplevel2.destroy()

    toplevel2=Toplevel(window)
    toplevel2.geometry("700x500")

    label=Label(toplevel2, text="회원조회", font = ("돋움체", 20))
    label.place(x = 290, y = 30)

    phonelabel1 = Label(toplevel2, text = "전화번호")
    phonelabel1.place(x = 225, y= 80)
    phonetext2 = Entry(toplevel2, width = 20)
    phonetext2.place(x = 325, y = 80)

    namelabel2 = Label(toplevel2, text = "이름")
    namelabel2.place(x = 225, y = 130)
    nametext2 = Entry(toplevel2, width = 20)
    nametext2.place(x = 325, y = 130)

    searchbutton = Button(toplevel2, text = "조회", command = search)
    cancelbutton = Button(toplevel2, text = "취소", command = quit2)
    searchbutton.place(x = 275, y = 400)
    cancelbutton.place(x = 375, y = 400)

def book_add() :
    def quit1() :
        toplevel.destroy()

    def register() :
        checkisbn = ""
        checkprice = ""
        checktitle = ""
        checkauthor = ""
        checkpub = ""
        count = 0
        count2 = 0
        MsgBox = messagebox.askquestion ('등록 확인','등록하시겠습니까??')
        if MsgBox == 'yes':
            if (ISBNtext.get().replace(" ", "") == "") :
                checkisbn = "ISBN"
                count2 = count2 + 1
            if (pricetext.get().replace(" ", "") == "") :
                checkprice = "가격"
                count2 = count2 + 1
            if (titletext.get().replace(" ", "") == "") :
                checktitle = "제목"
                count2 = count2 + 1
            if (authortext.get().replace(" ", "") == "") :
                checkauthor = "저자"
                count2 = count2 + 1
            if (pubtext.get().replace(" ", "") == "") :
                checkpub = "출판사"
                count2 = count2 + 1
            if count2 >= 1 :
                messagebox.showinfo("잘못된 형식", "{} {} {} {} {} 입력이 되지 않았습니다.".format(checkisbn, checkprice, checktitle, checkauthor, checkpub))
                return

            if (ISBNtext.get().replace(" ", "").isdigit() == False)  :
                checkisbn = "ISBN"
                count = count + 1
            if (pricetext.get().replace(" ", "").isdigit() == False) :
                checkprice = "가격"
                count = count + 1
            

            if ISBNtext.get() in Book['Book_ISBN'].values.astype(str) :
                messagebox.showinfo("중복", "중복된 ISBN 번호입니다.")   
            elif count >= 1 :
                messagebox.showinfo("잘못된 형식", "{} {} 형식이 잘못되었습니다.".format(checkisbn,checkprice))     
            else :
                messagebox.showinfo("등록 완료", "등록이 완료되었습니다.")
                Book.loc[ISBNtext.get()] = [ISBNtext.get().replace(" ",""), titletext.get(), pubtext.get(), authortext.get().replace(" ",""), pricetext.get().replace(" ",""), linktext.get(), descriptiontext.get(), 'X']
                Book.to_csv('BookMake_DF.csv', mode = 'w', index = False, header = True, encoding='utf-8-sig')
                toplevel.destroy()
        else:
            messagebox.showinfo("등록 취소", "등록이 취소되었습니다.")
            toplevel.destroy()

    def overlapcheck() :
        if (ISBNtext.get().replace(" ", "") == "") :
            messagebox.showinfo("잘못된 형식", "ISBN이 입력이 되지 않았습니다.") 
            return
        elif (ISBNtext.get().replace(" ", "").isdigit() == False) :
            messagebox.showinfo("잘못된 형식", "ISBN 형식이 잘못되었습니다.") 
            return
        if ISBNtext.get() in Book['Book_ISBN'].values.astype(str) :
            messagebox.showinfo("중복", "중복된 ISBN 번호입니다.")
        else :
            messagebox.showinfo("사용 가능", "사용 가능한 ISBN 번호입니다.")

    toplevel=Toplevel(window)
    toplevel.geometry("700x500")

    label=Label(toplevel, text="도서등록", font = ("돋움체", 20))
    label.place(x = 290, y = 30)

    ISBNlabel1 = Label(toplevel, text = "ISBN")
    ISBNlabel1.place(x = 225, y= 95)
    ISBNtext = Entry(toplevel, width = 20)
    ISBNtext.place(x = 325, y= 95)
    ISBNform1 = Label(toplevel, text = "숫자로만 입력", font = ("돋움체", 8) ,fg = "red" )
    ISBNform1.place(x = 355, y = 115)

    titlelabel1 = Label(toplevel, text = "제목")
    titlelabel1.place(x = 225, y= 135)
    titletext = Entry(toplevel, width = 20)
    titletext.place(x = 325, y= 135)

    authorlabel1 = Label(toplevel, text = "저자")
    authorlabel1.place(x = 225, y=175)
    authortext = Entry(toplevel, width = 20)
    authortext.place(x = 325, y= 175)

    publabel1 = Label(toplevel, text = "출판사")
    publabel1.place(x = 225, y= 215)
    pubtext = Entry(toplevel, width = 20)
    pubtext.place(x = 325, y= 215)

    pricelabel1 = Label(toplevel, text = "가격")
    pricelabel1.place(x = 225, y= 255)
    pricetext = Entry(toplevel, width = 20)
    pricetext.place(x = 325, y= 255)
    priceform1 = Label(toplevel, text = "숫자로만 입력", font = ("돋움체", 8) ,fg = "red" )
    priceform1.place(x = 355, y = 275)

    linklabel1 = Label(toplevel, text = "관련 링크")
    linklabel1.place(x = 225, y= 295)
    linktext = Entry(toplevel, width = 20)
    linktext.place(x = 325, y= 295)

    descriptionlabel1 = Label(toplevel, text = "정보")
    descriptionlabel1.place(x = 225, y= 335)
    descriptiontext = Entry(toplevel, width = 20)
    descriptiontext.place(x = 325, y= 335)

    clearbutton = Button(toplevel, text = "등록", command = register)
    cancelbutton = Button(toplevel, text = "취소", command = quit1)
    overlapbutton = Button(toplevel, text = "중복 조회", command = overlapcheck ,font =("돋움체", 8),fg= "blue" , width = 10)
    clearbutton.place(x = 275, y = 395)
    cancelbutton.place(x = 375, y = 395)
    overlapbutton.place(x = 480, y =95)

def book_search() : 
    def search() :
        global treeview
        treeview = ttk.Treeview(toplevel2, column = ["제목", "저자", "ISBN", "가격", "출판사", "대여여부"],
            displaycolumns=["제목", "저자", "ISBN", "가격", "출판사", "대여여부"])
        treeview.place(x= 50, y = 170)
        treeview.column("제목", width = 100, anchor = CENTER)
        treeview.heading("제목", text = "제목", anchor = CENTER)
        treeview.column("저자", width = 100, anchor = CENTER)
        treeview.heading("저자", text = "저자", anchor = CENTER)
        treeview.column("ISBN", width = 100, anchor = CENTER)
        treeview.heading("ISBN", text = "ISBN", anchor = CENTER)
        treeview.column("가격", width = 100, anchor = CENTER)
        treeview.heading("가격", text = "가격", anchor = CENTER)
        treeview.column("출판사", width = 100, anchor = CENTER)
        treeview.heading("출판사", text = "출판사", anchor = CENTER)
        treeview.column("대여여부", width = 100, anchor = CENTER)
        treeview.heading("대여여부", text = "대여여부", anchor = CENTER)
        treeview["show"] = "headings"


        if (ISBNtext2.get() == '') & (titletext2.get() == '') :
            return
        elif ISBNtext2.get() == '' :
            Search = Book[Book['Book_title'].str.contains(titletext2.get())]
        elif titletext2.get() == '' :
            Search = Book[Book['Book_ISBN'].astype(str).str.contains(ISBNtext2.get())]
        else :
            Search = Book[Book['Book_ISBN'].astype(str).str.contains(ISBNtext2.get()) | Book['Book_title'].str.contains(titletext2.get())]
        Search = Search[['Book_title', 'Book_author', 'Book_ISBN', 'Book_price', 'Book_pub', 'Book_rentcheck']]
        Search = Search.values.tolist()
        for i in range(len(Search)):
            treeview.insert("", "end", text = "", values=Search[i], iid = i)

        choicebutton = Button(toplevel2, text = "선택")
        choicebutton.bind('<Button>', choice)
        choicebutton.place(x = 325, y = 400)
        treeview.bind('<Double-Button-1>', choice)

    def choice(event) :
        sel = treeview.focus()
        try :
            selectedISBN = treeview.item(sel).get("values")[2]
            selectedtitle = treeview.item(sel).get("values")[0]
        except IndexError :
            messagebox.showinfo("오류", "조회된 정보가 없습니다.")
            return

        Search = Book[(Book['Book_ISBN'] == selectedISBN) | (Book['Book_title'] == selectedtitle)]
        
        toplevel3 =Toplevel(window)
        toplevel3.geometry("700x500")

        label=Label(toplevel3, text="도서 정보 상세 창", font = ("돋움체", 20), anchor = N)
        label.place(x = 225, y = 30)

        titlelabel3 = Label(toplevel3, text = "제목")
        titlelabel3.place(x = 225, y= 85)
        titletext3 = Entry(toplevel3, width = 20)
        titletext3.insert(0, Search.iloc[0]['Book_title'])
        titletext3.place(x = 325, y= 85)

        authorlabel3 = Label(toplevel3, text = "저자")
        authorlabel3.place(x = 225, y= 120)
        authortext3 = Entry(toplevel3, width = 20)
        authortext3.insert(0, Search.iloc[0]['Book_author'])
        authortext3.place(x = 325, y= 120)

        pricelabel3 = Label(toplevel3, text = "가격")
        pricelabel3.place(x = 225, y=155 )
        pricetext3 = Entry(toplevel3, width = 20)
        pricetext3.insert(0, Search.iloc[0]['Book_price'])
        pricetext3.place(x = 325, y= 155)
        priceform2 = Label(toplevel3, text = "숫자로만 입력", font = ("돋움체", 8) ,fg = "red" )
        priceform2.place(x = 355, y = 175)

        publabel3 = Label(toplevel3, text = "출판사")
        publabel3.place(x = 225, y= 190)
        pubtext3 = Entry(toplevel3, width = 20)
        pubtext3.insert(0, Search.iloc[0]['Book_pub'])
        pubtext3.place(x = 325, y= 190)

        linklabel3 = Label(toplevel3, text = "관련 링크")
        linklabel3.place(x = 225, y= 225)
        linktext3 = Entry(toplevel3, width = 20)
        linktext3.insert(0, Search.iloc[0]['Book_link'])
        linktext3.place(x = 325, y= 225)

        ISBNlabel = Label(toplevel3, text = "ISBN")
        ISBNlabel.place(x = 225, y= 260)
        ISBNtext3 = Entry(toplevel3, width = 20)
        ISBNtext3.insert(0, Search.iloc[0]['Book_ISBN'])
        ISBNtext3.place(x = 325, y= 260)
        ISBNform2 = Label(toplevel3, text = "숫자로만 입력", font = ("돋움체", 8) ,fg = "red" )
        ISBNform2.place(x = 355, y = 280)

        descriptionlabel1 = Label(toplevel3, text = "도서 설명")
        descriptionlabel1.place(x = 225, y= 295)
        descriptiontext3 = Entry(toplevel3, width = 20)
        descriptiontext3.insert(0, Search.iloc[0]['Book_author'])
        descriptiontext3.place(x = 325, y= 295)

        rentlabel1 = Label(toplevel3, text = "대여 여부")
        rentlabel1.place(x = 225, y= 330)
        renttext3 = Entry(toplevel3, width = 20)
        renttext3.insert(0, Search.iloc[0]['Book_rentcheck'])
        renttext3.place(x = 325, y= 330)

        def modify() :
            checkisbn = ""
            checkprice = ""
            checktitle = ""
            checkauthor = ""
            checkpub = ""
            count = 0
            count2 = 0
            MsgBox = messagebox.askquestion("수정 확인", "수정하시겠습니까?")
            if MsgBox == 'yes' :
                if (ISBNtext3.get().replace(" ", "") == "") :
                    checkisbn = "ISBN"
                    count2 = count2 + 1
                if (pricetext3.get().replace(" ", "") == "") :
                    checkprice = "가격"
                    count2 = count2 + 1
                if (titletext3.get().replace(" ", "") == "") :
                    checktitle = "제목"
                    count2 = count2 + 1
                if (authortext3.get().replace(" ", "") == "") :
                    checkauthor = "저자"
                    count2 = count2 + 1
                if (pubtext3.get().replace(" ", "") == "") :
                    checkpub = "출판사"
                    count2 = count2 + 1
                if count2 >= 1 :
                    messagebox.showinfo("잘못된 형식", "{} {} {} {} {} 입력이 되지 않았습니다.".format(checkisbn, checkprice, checktitle, checkauthor, checkpub))
                    return
                
                if (ISBNtext3.get().replace(" ", "").isdigit() == False)  :
                    checkisbn = "ISBN"
                    count = count + 1
                if (pricetext3.get().replace(" ", "").isdigit() == False) :
                    checkprice = "가격"
                    count = count + 1


                if (Search['Book_rentcheck'] == 'O').any() :
                    messagebox.showinfo("수정 불가능", "대여 중인 도서는 수정이 불가능합니다.")
                elif count >= 1 :
                    messagebox.showinfo("잘못된 형식", "{} {} 형식이 잘못되었습니다.".format(checkisbn,checkprice)) 
                else : 
                    if Search.iloc[0]['Book_ISBN'] == ISBNtext3.get() :
                        messagebox.showinfo("수정 완료", "수정이 완료되었습니다.")
                        Book.loc[(Book['Book_ISBN'] == selectedISBN) | (Book['Book_title'] == selectedtitle), ('Book_ISBN', 'Book_title', 'Book_pub', 'Book_author', 'Book_price', 'Book_link', 'Book_description')] = [ISBNtext3.get().replace(" ",""), titletext3.get(), pubtext3.get(),authortext3.get().replace(" ",""), pricetext3.get().replace(" ",""), linktext3.get(), descriptiontext3.get()]
                        Book.to_csv('BookMake_DF.csv', mode = 'w', header = True, index = False, encoding='utf-8-sig')
                        toplevel3.destroy()
                        toplevel2.destroy()

                    elif ISBNtext3.get() in Book['Book_ISBN'].values :
                        messagebox.showinfo("중복", "중복된 ISBN 번호입니다.")

                    else : 
                        messagebox.showinfo("수정 완료", "수정이 완료되었습니다.")
                        Book.loc[(Book['Book_ISBN'] == selectedISBN) | (Book['Book_title'] == selectedtitle), ('Book_ISBN', 'Book_title', 'Book_pub', 'Book_author', 'Book_price', 'Book_link', 'Book_description')] = [ISBNtext3.get().replace(" ",""), titletext3.get(), pubtext3.get() ,authortext3.get().replace(" ",""), pricetext3.get().replace(" ",""), linktext3.get(), descriptiontext3.get()]
                        Book.to_csv('BookMake_DF.csv', mode = 'w', index = False, header = True, encoding='utf-8-sig')
                        toplevel3.destroy()
                        toplevel2.destroy()

            else:
                messagebox.showinfo("수정 취소", "수정이 취소되었습니다.")
                toplevel2.destroy()

        def overlapcheck() :
            if str(Search.iloc[0]['Book_ISBN']) == ISBNtext3.get() :
                return
            if (ISBNtext3.get().replace(" ", "") == "") :
                messagebox.showinfo("잘못된 형식", "ISBN이 입력이 되지 않았습니다.") 
                return
            elif (ISBNtext3.get().replace(" ", "").isdigit() == False) :
                messagebox.showinfo("잘못된 형식", "ISBN 형식이 잘못되었습니다.") 
                return
            else :
                if  ISBNtext3.get() in Book['Book_ISBN'].values.astype(str) :
                    messagebox.showinfo("중복", "중복된 ISBN 번호입니다.")
                else : 
                    messagebox.showinfo("사용 가능", "사용 가능한 ISBN 번호입니다.")

        def delete() :
            MsgBox = messagebox.askquestion ('삭제 확인','삭제하시겠습니까??')
            if MsgBox == 'yes':
                if (Search['Book_rentcheck'] == 'X').any() :
                    Clear = Book[(Book['Book_ISBN'].astype(str) == ISBNtext2.get()) | (Book['Book_title'] == titletext2.get())].index
                    Book.drop(Clear, inplace = True)
                    Book.to_csv('BookMake_DF.csv', mode = 'w', index = False, header = True, encoding='utf-8-sig')
                    messagebox.showinfo("삭제 완료", "삭제가 완료되었습니다.")
                    toplevel3.destroy()
                    toplevel2.destroy()

                elif (Search['Book_rentcheck'] == 'O').any() :
                    messagebox.showinfo("삭제 불가능", "대여 중인 도서는 삭제가 불가능합니다.")

                else : 
                    messagebox.showinfo("수정 취소", "수정이 취소되었습니다.")
        
        def cancel() :
            toplevel3.destroy()

        modifybutton = Button(toplevel3, text = "수정", command = modify)
        outbutton = Button(toplevel3, text = "삭제", command = delete)
        cancelbutton = Button(toplevel3, text = "취소", command = cancel)
        overlapbutton = Button(toplevel3, text = "중복 조회", command = overlapcheck ,font =("돋움체", 8),fg= "blue" , width = 10)
        modifybutton.place(x = 275, y = 400)
        outbutton.place(x = 325, y = 400)
        cancelbutton.place(x = 375, y = 400)
        overlapbutton.place(x = 480, y = 260)

    def quit2() :
        toplevel2.destroy()

    toplevel2=Toplevel(window)
    toplevel2.geometry("700x500")

    label=Label(toplevel2, text="도서조회", font = ("돋움체", 20))
    label.place(x = 290, y = 30)

    ISBNlabel1 = Label(toplevel2, text = "ISBN")
    ISBNlabel1.place(x = 225, y= 80)
    ISBNtext2 = Entry(toplevel2, width = 20)
    ISBNtext2.place(x = 325, y = 80)

    titlelabel2 = Label(toplevel2, text = "제목")
    titlelabel2.place(x = 225, y = 130)
    titletext2 = Entry(toplevel2, width = 20)
    titletext2.place(x = 325, y = 130)

    searchbutton = Button(toplevel2, text = "조회", command = search)
    cancelbutton = Button(toplevel2, text = "취소", command = quit2)
    searchbutton.place(x = 275, y = 400)
    cancelbutton.place(x = 375, y = 400)

def Rent_make() :
    Rent = pd.read_csv('RentMake_DF.csv', encoding='utf-8-sig')

    toplevel_rent=Toplevel(window)
    toplevel_rent.geometry("700x500")

    label=Label(toplevel_rent, text="대여 희망 회원 조회", font = ("돋움체", 20))
    label.place(x = 215, y = 30)

    phonelabel1 = Label(toplevel_rent, text = "전화번호")
    phonelabel1.place(x = 225, y= 80)
    phonetext2 = Entry(toplevel_rent, width = 20)
    phonetext2.place(x = 325, y = 80)

    namelabel2 = Label(toplevel_rent, text = "이름")
    namelabel2.place(x = 225, y = 130)
    nametext2 = Entry(toplevel_rent, width = 20)
    nametext2.place(x = 325, y = 130)

    def search() :
        global treeview

        treeview = ttk.Treeview(toplevel_rent, column = ["이름", "생년월일", "전화번호", "성별", "탈퇴여부", "대여여부"],
            displaycolumns=["이름", "생년월일", "전화번호", "성별", "탈퇴여부", "대여여부"])
        treeview.place(x= 50, y = 170)
        treeview.column("이름", width = 100, anchor = CENTER)
        treeview.heading("이름", text = "이름", anchor = CENTER)
        treeview.column("생년월일", width = 100, anchor = CENTER)
        treeview.heading("생년월일", text = "생년월일", anchor = CENTER)
        treeview.column("전화번호", width = 100, anchor = CENTER)
        treeview.heading("전화번호", text = "전화번호", anchor = CENTER)
        treeview.column("성별", width = 100, anchor = CENTER)
        treeview.heading("성별", text = "성별", anchor = CENTER)
        treeview.column("탈퇴여부", width = 100, anchor = CENTER)
        treeview.heading("탈퇴여부", text = "탈퇴여부", anchor = CENTER)
        treeview.column("대여여부", width = 100, anchor = CENTER)
        treeview.heading("대여여부", text = "대여여부", anchor = CENTER)
        treeview["show"] = "headings"

        if (phonetext2.get() == '') & (nametext2.get() == '') :
            return
        elif phonetext2.get() == '' :
            Search = User[User['User_name'].str.contains(nametext2.get())]
        elif nametext2.get() == '' :
            Search = User[User['User_phone'].str.contains(phonetext2.get())]
        else :
            Search = User[User['User_phone'].str.contains(phonetext2.get()) | User['User_name'].str.contains(nametext2.get())]
        Search = Search[['User_name', 'User_birthday', 'User_phone', 'User_sex', 'User_withdrawcheck', 'User_rentcnt']]
        Search = Search.values.tolist()
        for i in range(len(Search)):
            treeview.insert("", "end", text = "", values=Search[i], iid = i)

        choicebutton = Button(toplevel_rent, text = "선택")
        choicebutton.bind('<Button>', choice)
        choicebutton.place(x = 325, y = 400)
        treeview.bind('<Double-Button-1>', choice)

    def choice(event) :
        sel = treeview.focus()
        
        try :
            selectedname = treeview.item(sel).get("values")[0]
            selectedphone = treeview.item(sel).get("values")[2]
        except IndexError :
            messagebox.showinfo("오류", "조회된 정보가 없습니다.")
            return

        toplevel_rent.destroy()
        toplevel2=Toplevel(window)
        toplevel2.geometry("700x500")

        label=Label(toplevel2, text="대여 희망 도서 조회", font = ("돋움체", 20))
        label.place(x = 215, y = 30)

        ISBNlabel1 = Label(toplevel2, text = "ISBN")
        ISBNlabel1.place(x = 225, y= 80)
        ISBNtext2 = Entry(toplevel2, width = 20)
        ISBNtext2.place(x = 325, y = 80)

        titlelabel2 = Label(toplevel2, text = "제목")
        titlelabel2.place(x = 225, y = 130)
        titletext2 = Entry(toplevel2, width = 20)
        titletext2.place(x = 325, y = 130)


        def search2() :
            global treeview

            treeview = ttk.Treeview(toplevel2, column = ["제목", "저자", "ISBN", "가격", "출판사", "대여여부"],
                displaycolumns=["제목", "저자", "ISBN", "가격", "출판사", "대여여부"])
            treeview.place(x= 50, y = 170)
            treeview.column("제목", width = 100, anchor = CENTER)
            treeview.heading("제목", text = "제목", anchor = CENTER)
            treeview.column("저자", width = 100, anchor = CENTER)
            treeview.heading("저자", text = "저자", anchor = CENTER)
            treeview.column("ISBN", width = 100, anchor = CENTER)
            treeview.heading("ISBN", text = "ISBN", anchor = CENTER)
            treeview.column("가격", width = 100, anchor = CENTER)
            treeview.heading("가격", text = "가격", anchor = CENTER)
            treeview.column("출판사", width = 100, anchor = CENTER)
            treeview.heading("출판사", text = "출판사", anchor = CENTER)
            treeview.column("대여여부", width = 100, anchor = CENTER)
            treeview.heading("대여여부", text = "대여여부", anchor = CENTER)
            treeview["show"] = "headings"

            if (ISBNtext2.get() == '') & (titletext2.get() == '') :
                return
            elif ISBNtext2.get() == '' :
                Search = Book[Book['Book_title'].str.contains(titletext2.get())]
            elif titletext2.get() == '' :
                Search = Book[Book['Book_ISBN'].astype(str).str.contains(ISBNtext2.get())]
            else :
                Search = Book[Book['Book_ISBN'].astype(str).str.contains(ISBNtext2.get()) | Book['Book_title'].str.contains(titletext2.get())]
            Search = Search[['Book_title', 'Book_author', 'Book_ISBN', 'Book_price', 'Book_pub', 'Book_rentcheck']]
            Search = Search.values.tolist()
            for i in range(len(Search)):
                treeview.insert("", "end", text = "", values=Search[i], iid = i)
            
            choicebutton = Button(toplevel2, text = "선택")
            choicebutton.bind('<Button>', choice2)
            choicebutton.place(x = 325, y = 400)
            treeview.bind('<Double-Button-1>', choice2)

        def choice2(event) :
            sel = treeview.focus()
            try :
                selectedISBN = treeview.item(sel).get("values")[2]
                selectedtitle = treeview.item(sel).get("values")[0]
            except IndexError :
                messagebox.showinfo("오류", "조회된 정보가 없습니다.")
                return
        
            Book_Search = Book[(Book['Book_ISBN'] == selectedISBN) | (Book['Book_title'] == selectedtitle)]

            if (Book_Search['Book_rentcheck'] == 'O').any() :
                Rent_Search = Rent[(Rent['Book_ISBN'] == selectedISBN) | (Rent['User_phone'] == selectedphone)]
                User_Search = User[(User['User_phone']) == ",".join(Rent_Search['User_phone'])]
            else :
                User_Search = User[(User['User_phone'] == selectedphone) | (User['User_name'] == selectedname)]

            toplevel2.destroy()
            toplevel3 =Toplevel(window)
            toplevel3.geometry("700x500")

            label=Label(toplevel3, text="대여 정보 상세 창", font = ("돋움체", 20), anchor = N)
            label.place(x = 225, y = 30)

            titlelabel3 = Label(toplevel3, text = "제목")
            titlelabel3.place(x = 50, y= 85)
            titletext2 = Entry(toplevel3, width = 20)
            titletext2.insert(0, Book_Search.iloc[0]['Book_title'])
            titletext2.place(x = 150, y= 85)

            authorlabel3 = Label(toplevel3, text = "저자")
            authorlabel3.place(x = 50, y= 120)
            authortext2 = Entry(toplevel3, width = 20)
            authortext2.insert(0, Book_Search.iloc[0]['Book_author'])
            authortext2.place(x = 150, y= 120)

            pricelabel3 = Label(toplevel3, text = "가격")
            pricelabel3.place(x = 50, y=155 )
            pricetext2 = Entry(toplevel3, width = 20)
            pricetext2.insert(0, Book_Search.iloc[0]['Book_price'])
            pricetext2.place(x = 150, y= 155)

            publabel3 = Label(toplevel3, text = "출판사")
            publabel3.place(x = 50, y= 190)
            pubtext2 = Entry(toplevel3, width = 20)
            pubtext2.insert(0, Book_Search.iloc[0]['Book_pub'])
            pubtext2.place(x = 150, y= 190)

            linklabel3 = Label(toplevel3, text = "관련 링크")
            linklabel3.place(x = 50, y= 225)
            linktext2 = Entry(toplevel3, width = 20)
            linktext2.insert(0, Book_Search.iloc[0]['Book_link'])
            linktext2.place(x = 150, y= 225)

            ISBNlabel = Label(toplevel3, text = "ISBN")
            ISBNlabel.place(x = 50, y= 260)
            ISBNtext = Entry(toplevel3, width = 20)
            ISBNtext.insert(0, Book_Search.iloc[0]['Book_ISBN'])
            ISBNtext.place(x = 150, y= 260)

            descriptionlabel1 = Label(toplevel3, text = "도서 설명")
            descriptionlabel1.place(x = 50, y= 295)
            descriptiontext = Entry(toplevel3, width = 20)
            descriptiontext.insert(0, Book_Search.iloc[0]['Book_description'])
            descriptiontext.place(x = 150, y= 295)

            phonelabel1 = Label(toplevel3, text = "전화번호")
            phonelabel1.place(x = 400, y= 85)
            phonetext = Entry(toplevel3, width = 20)
            phonetext.insert(0, User_Search.iloc[0]['User_phone'])
            phonetext.place(x = 500, y= 85)

            namelabel1 = Label(toplevel3, text = "이름")
            namelabel1.place(x = 400, y= 137)
            nametext = Entry(toplevel3, width = 20)
            nametext.insert(0, User_Search.iloc[0]['User_name'])
            nametext.place(x = 500, y= 137)

            birthdaylabel1 = Label(toplevel3, text = "생일")
            birthdaylabel1.place(x = 400, y=190 )
            birthdaytext = Entry(toplevel3, width = 20)
            birthdaytext.insert(0, User_Search.iloc[0]['User_birthday'])
            birthdaytext.place(x = 500, y= 190)

            sexlabel1 = Label(toplevel3, text = "성별")
            sexlabel1.place(x = 400, y= 242)
            sextext = Entry(toplevel3, width = 20)
            sextext.insert(0, User_Search.iloc[0]['User_sex'])
            sextext.place(x = 500, y= 242)

            maillabel1 = Label(toplevel3, text = "메일")
            maillabel1.place(x = 400, y= 295)
            mailtext = Entry(toplevel3, width = 20)
            mailtext.insert(0, User_Search.iloc[0]['User_mail'])
            mailtext.place(x = 500, y= 295)

            rentlabel1 = Label(toplevel3, text = "대여 여부")
            rentlabel1.place(x = 100, y= 350)
            renttext = Entry(toplevel3, width = 5)
            renttext.insert(0, Book_Search.iloc[0]['Book_rentcheck'])
            renttext.place(x = 170, y= 350)

            rentdatelabel1 = Label(toplevel3, text = "대출 일자")
            rentdatelabel1.place(x = 270, y= 350)
            rentdatetext = Entry(toplevel3, width = 10)
            if (Book_Search['Book_rentcheck'] == 'O').any() :
                rentdatetext.insert(0, Rent_Search.iloc[0]['Rent_Date'])
            rentdatetext.place(x = 340, y= 350)

            returndatelabel1 = Label(toplevel3, text = "반납 예정일")
            returndatelabel1.place(x = 480, y= 350)
            returndatetext = Entry(toplevel3, width = 10)
            if (Book_Search['Book_rentcheck'] == 'O').any() :
                returndatetext.insert(0, Rent_Search.iloc[0]['Rent_returndate'])
            returndatetext.place(x = 550, y= 350)

            def modify() :
                MsgBox = messagebox.askquestion("대여 확인", "대여하시겠습니까?")
                if MsgBox == 'yes' :
                    if (User_Search['User_withdrawcheck'] == 'O').any() :
                        messagebox.showinfo("대여 불가능", "탈퇴한 회원은 대여가 불가능합니다.")
                    elif (Book_Search['Book_rentcheck'] == 'O').any() :
                        messagebox.showinfo("대여 불가능", "이미 대여 중인 도서는 대여가 불가능합니다.")
                    else :
                        today = datetime.datetime.now()
                        today = today.date()
                        returnday = datetime.timedelta(days = 14)
                        messagebox.showinfo("대여 완료", "대여가 완료되었습니다. 반납일은 {} 입니다.".format(today+returnday))
                        seq_max = str(Rent['Rent_seq'].max())
                        if seq_max == 'nan' :
                            Rent.loc[1] = [1, selectedISBN, selectedphone, today, today+returnday, 'O']
                        else :
                            seq_max = Rent['Rent_seq'].max()
                            Rent.loc[seq_max+1] = [seq_max+1, selectedISBN, selectedphone, today, today+returnday, 'O']
                        
                        Book.loc[(Book['Book_ISBN'] == selectedISBN) | (Book['Book_title'] == selectedtitle), ('Book_rentcheck')] = "O"
                        User.loc[(User['User_phone'] == selectedphone) | (User['User_name'] == selectedname), ('User_rentcnt')] += 1
                        
                        Rent.to_csv('RentMake_DF.csv', mode = 'w', index = False ,header = True, encoding='utf-8-sig')
                        Book.to_csv('BookMake_DF.csv', mode = 'w', index = False ,header = True, encoding='utf-8-sig')
                        User.to_csv('UserMake_DF.csv', mode = 'w', index = False ,header = True, encoding='utf-8-sig')

                        toplevel3.destroy()
                        
                    
                else : 
                    messagebox.showinfo("대여 취소", "대여가 취소되었습니다.")
                    toplevel3.destroy()
            
            def cancel() :
                toplevel3.destroy()

            modifybutton = Button(toplevel3, text = "대여", command = modify)
            cancelbutton = Button(toplevel3, text = "취소", command = cancel)
            modifybutton.place(x = 275, y = 400)
            cancelbutton.place(x = 375, y = 400)

        def quit3() :
            toplevel_rent.destroy()
            toplevel2.destroy()


        searchbutton = Button(toplevel2, text = "조회", command = search2)
        cancelbutton = Button(toplevel2, text = "취소", command = quit3)
        searchbutton.place(x = 275, y = 400)
        cancelbutton.place(x = 375, y = 400)

    def quit2() :
        toplevel_rent.destroy()

    searchbutton = Button(toplevel_rent, text = "조회", command = search)
    cancelbutton = Button(toplevel_rent, text = "취소", command = quit2)
    searchbutton.place(x = 275, y = 400)
    cancelbutton.place(x = 375, y = 400)

def Rent_check() :
    Rent = pd.read_csv('RentMake_DF.csv', encoding='utf-8-sig')
    
    toplevel2=Toplevel(window)
    toplevel2.geometry("700x500")

    label=Label(toplevel2, text="대여조회", font = ("돋움체", 20))
    label.place(x = 290, y = 30)

    ISBNlabel1 = Label(toplevel2, text = "ISBN")
    ISBNlabel1.place(x = 225, y= 80)
    ISBNtext2 = Entry(toplevel2, width = 20)
    ISBNtext2.place(x = 325, y = 80)

    titlelabel2 = Label(toplevel2, text = "제목")
    titlelabel2.place(x = 225, y = 130)
    titletext2 = Entry(toplevel2, width = 20)
    titletext2.place(x = 325, y = 130)

    def search() :
        global treeview

        treeview = ttk.Treeview(toplevel2, column = ["제목", "저자", "ISBN", "가격", "출판사", "대여여부"],
            displaycolumns=["제목", "저자", "ISBN", "가격", "출판사", "대여여부"])
        treeview.place(x= 50, y = 170)
        treeview.column("제목", width = 100, anchor = CENTER)
        treeview.heading("제목", text = "제목", anchor = CENTER)
        treeview.column("저자", width = 100, anchor = CENTER)
        treeview.heading("저자", text = "저자", anchor = CENTER)
        treeview.column("ISBN", width = 100, anchor = CENTER)
        treeview.heading("ISBN", text = "ISBN", anchor = CENTER)
        treeview.column("가격", width = 100, anchor = CENTER)
        treeview.heading("가격", text = "가격", anchor = CENTER)
        treeview.column("출판사", width = 100, anchor = CENTER)
        treeview.heading("출판사", text = "출판사", anchor = CENTER)
        treeview.column("대여여부", width = 100, anchor = CENTER)
        treeview.heading("대여여부", text = "대여여부", anchor = CENTER)
        treeview["show"] = "headings"

        if (ISBNtext2.get() == '') & (titletext2.get() == '') :
            return
        elif ISBNtext2.get() == '' :
            Search = Book[Book['Book_title'].str.contains(titletext2.get())]
        elif titletext2.get() == '' :
            Search = Book[Book['Book_ISBN'].astype(str).str.contains(ISBNtext2.get())]
        else :
            Search = Book[Book['Book_ISBN'].astype(str).str.contains(ISBNtext2.get()) | Book['Book_title'].str.contains(titletext2.get())]
        Search = Search[['Book_title', 'Book_author', 'Book_ISBN', 'Book_price', 'Book_pub', 'Book_rentcheck']]
        Search = Search.values.tolist()
        for i in range(len(Search)):
            treeview.insert("", "end", text = "", values=Search[i], iid = i)       
        
        choicebutton = Button(toplevel2, text = "선택")
        choicebutton.bind('<Button>', choice2)
        choicebutton.place(x = 325, y = 400)
        treeview.bind('<Double-Button-1>', choice2)

    def choice2(event) :
        sel = treeview.focus()

        try :
            selectedISBN = treeview.item(sel).get("values")[2]
            selectedtitle = treeview.item(sel).get("values")[0]
        except IndexError :
            messagebox.showinfo("오류", "조회된 정보가 없습니다.")
            return

        Book_Search = Book[(Book['Book_ISBN'] == selectedISBN) | (Book['Book_title'] == selectedtitle)]
        Rent_Search = Rent[(Rent['Book_ISBN']) == selectedISBN]

        if (Book_Search['Book_rentcheck'] == 'O').any() :
            User_Search = User[(User['User_phone']) == ",".join(Rent_Search['User_phone'])]

        toplevel2.destroy()
        toplevel3 =Toplevel(window)
        toplevel3.geometry("700x500")

        label=Label(toplevel3, text="대여 정보 상세 창", font = ("돋움체", 20), anchor = N)
        label.place(x = 225, y = 30)

        titlelabel3 = Label(toplevel3, text = "제목")
        titlelabel3.place(x = 50, y= 85)
        titletext2 = Entry(toplevel3, width = 20)
        titletext2.insert(0, Book_Search.iloc[0]['Book_title'])
        titletext2.place(x = 150, y= 85)

        authorlabel3 = Label(toplevel3, text = "저자")
        authorlabel3.place(x = 50, y= 120)
        authortext2 = Entry(toplevel3, width = 20)
        authortext2.insert(0, Book_Search.iloc[0]['Book_author'])
        authortext2.place(x = 150, y= 120)

        pricelabel3 = Label(toplevel3, text = "가격")
        pricelabel3.place(x = 50, y=155 )
        pricetext2 = Entry(toplevel3, width = 20)
        pricetext2.insert(0, Book_Search.iloc[0]['Book_price'])
        pricetext2.place(x = 150, y= 155)

        publabel3 = Label(toplevel3, text = "출판사")
        publabel3.place(x = 50, y= 190)
        pubtext2 = Entry(toplevel3, width = 20)
        pubtext2.insert(0, Book_Search.iloc[0]['Book_pub'])
        pubtext2.place(x = 150, y= 190)

        linklabel3 = Label(toplevel3, text = "관련 링크")
        linklabel3.place(x = 50, y= 225)
        linktext2 = Entry(toplevel3, width = 20)
        linktext2.insert(0, Book_Search.iloc[0]['Book_link'])
        linktext2.place(x = 150, y= 225)

        ISBNlabel = Label(toplevel3, text = "ISBN")
        ISBNlabel.place(x = 50, y= 260)
        ISBNtext = Entry(toplevel3, width = 20)
        ISBNtext.insert(0, Book_Search.iloc[0]['Book_ISBN'])
        ISBNtext.place(x = 150, y= 260)

        descriptionlabel1 = Label(toplevel3, text = "도서 설명")
        descriptionlabel1.place(x = 50, y= 295)
        descriptiontext = Entry(toplevel3, width = 20)
        descriptiontext.insert(0, Book_Search.iloc[0]['Book_description'])
        descriptiontext.place(x = 150, y= 295)

        phonelabel1 = Label(toplevel3, text = "전화번호")
        phonelabel1.place(x = 400, y= 85)
        phonetext = Entry(toplevel3, width = 20)
        if (Book_Search['Book_rentcheck'] == 'O').any() :
            phonetext.insert(0, User_Search.iloc[0]['User_phone'])
        phonetext.place(x = 500, y= 85)

        namelabel1 = Label(toplevel3, text = "이름")
        namelabel1.place(x = 400, y= 137)
        nametext = Entry(toplevel3, width = 20)
        if (Book_Search['Book_rentcheck'] == 'O').any() :
            nametext.insert(0, User_Search.iloc[0]['User_name'])
        nametext.place(x = 500, y= 137)

        birthdaylabel1 = Label(toplevel3, text = "생일")
        birthdaylabel1.place(x = 400, y=190 )
        birthdaytext = Entry(toplevel3, width = 20)
        if (Book_Search['Book_rentcheck'] == 'O').any() :
            birthdaytext.insert(0, User_Search.iloc[0]['User_birthday'])
        birthdaytext.place(x = 500, y= 190)

        sexlabel1 = Label(toplevel3, text = "성별")
        sexlabel1.place(x = 400, y= 242)
        sextext = Entry(toplevel3, width = 20)
        if (Book_Search['Book_rentcheck'] == 'O').any() :
            sextext.insert(0, User_Search.iloc[0]['User_sex'])
        sextext.place(x = 500, y= 242)

        maillabel1 = Label(toplevel3, text = "메일")
        maillabel1.place(x = 400, y= 295)
        mailtext = Entry(toplevel3, width = 20)
        if (Book_Search['Book_rentcheck'] == 'O').any() :
            mailtext.insert(0, User_Search.iloc[0]['User_mail'])
        mailtext.place(x = 500, y= 295)

        rentlabel1 = Label(toplevel3, text = "대여 여부")
        rentlabel1.place(x = 100, y= 350)
        renttext = Entry(toplevel3, width = 5)
        renttext.insert(0, Book_Search.iloc[0]['Book_rentcheck'])
        renttext.place(x = 170, y= 350)

        rentdatelabel1 = Label(toplevel3, text = "대출 일자")
        rentdatelabel1.place(x = 270, y= 350)
        rentdatetext = Entry(toplevel3, width = 10)
        if (Book_Search['Book_rentcheck'] == 'O').any() :
            rentdatetext.insert(0, Rent_Search.iloc[0]['Rent_Date'])
        rentdatetext.place(x = 340, y= 350)

        returndatelabel1 = Label(toplevel3, text = "반납 예정일")
        returndatelabel1.place(x = 480, y= 350)
        returndatetext = Entry(toplevel3, width = 10)
        if (Book_Search['Book_rentcheck'] == 'O').any() :
            returndatetext.insert(0, Rent_Search.iloc[0]['Rent_returndate'])
        returndatetext.place(x = 550, y= 350)
            

        def modify() :
            MsgBox = messagebox.askquestion("반납 확인", "반납하시겠습니까?")
            if MsgBox == 'yes' :
                if (Book_Search['Book_rentcheck'] == 'X').any() :
                    messagebox.showinfo("반납 불가능", "빌리지 않은 도서는 반납이 불가능합니다.")
                
                else :
                    messagebox.showinfo("반납 완료", "반납이 완료되었습니다.")
                
                    Book.loc[(Book['Book_ISBN'] == selectedISBN) | (Book['Book_title'] == selectedtitle), ('Book_rentcheck')] = "X"
                    User.loc[(User['User_phone']) == ",".join(Rent_Search['User_phone']), ('User_rentcnt')] -= 1

                    Rent.drop(Rent_Search.index, inplace = True)

                    Rent.to_csv('RentMake_DF.csv', mode = 'w', index = False ,header = True, encoding='utf-8-sig')
                    Book.to_csv('BookMake_DF.csv', mode = 'w', index = False ,header = True, encoding='utf-8-sig')
                    User.to_csv('UserMake_DF.csv', mode = 'w', index = False ,header = True, encoding='utf-8-sig')
                    toplevel3.destroy()
            
            else : 
                messagebox.showinfo("반납 취소", "반납이 취소되었습니다.")
                toplevel3.destroy()
        
        def cancel() :
            toplevel3.destroy()

        backbutton = Button(toplevel3, text = "반납", command = modify)
        cancelbutton = Button(toplevel3, text = "취소", command = cancel)
        backbutton.place(x = 275, y = 400)
        cancelbutton.place(x = 375, y = 400)
    
    def quit2() :
        toplevel2.destroy()

    searchbutton = Button(toplevel2, text = "조회", command = search)
    cancelbutton = Button(toplevel2, text = "취소", command = quit2)
    searchbutton.place(x = 275, y = 400)
    cancelbutton.place(x = 375, y = 400)

titlelabel = Label(window, text = "도서 관리 프로그램", font = ("돋움체",30))
titlelabel.place(x = 215, y = 30)

MemberRegi = Button(window, text = "회원 등록",command = Member_make, width = 10, height = 2)
MemberRegi.place(x = 150, y = 150)

MemberSearch = Button(window, text = "회원 조회",command = Member_search, width = 10, height = 2)
MemberSearch.place(x = 150, y = 200)

button1 = Button(window, text = "도서 등록", command= book_add, width = 10, height = 2).place(x= 350, y =150)
button2 = Button(window, text = "도서 조회", command= book_search, width = 10, height = 2).place(x= 350, y =200)

Rent = Button(window, text = "도서 대여",command = Rent_make, width = 10, height = 2).place(x= 550, y =150)
Rentsearch = Button(window, text = "대여 조회", command = Rent_check,width = 10, height = 2).place(x= 550, y =200)

window.mainloop()