import pandas as pd
from tkinter import *
from tkinter import messagebox, ttk
import datetime

User = pd.read_csv('UserMake_DF.csv', encoding='utf-8-sig')
Book = pd.read_csv('BookMake_DF.csv', encoding='utf-8-sig')
Rent = pd.read_csv('RentMake_DF.csv', encoding='utf-8-sig')


window = Tk()
window.title("도서 관리 프로그램")
window.geometry("800x600")
window.resizable(width = False, height = False)

def Member_make() :
    def quit1() :
        toplevel.destroy()

    def register() :
        MsgBox = messagebox.askquestion ('등록 확인','등록하시겠습니까??')
        if MsgBox == 'yes':
            if phonetext.get() in User['User_phone'].values.astype(str) :
                messagebox.showinfo("중복", "이미 등록된 전화번호입니다.")
            else : 
                today = datetime.datetime.now()
                today = today.date()
                messagebox.showinfo("등록 완료", "등록이 완료되었습니다.")
                User.loc[phonetext.get()] = [phonetext.get(), nametext.get(), birthdaytext.get() ,sextext.get(), mailtext.get(), today, 'X', 0, 'X']
                User.to_csv('UserMake_DF.csv', mode = 'w', index = False ,header = True, encoding='utf-8-sig')
                toplevel.destroy()
        else:
            messagebox.showinfo("등록 취소", "등록이 취소되었습니다.")
            toplevel.destroy()
        
    def overlapcheck() :
        if phonetext.get() in User['User_phone'].values.astype(str) :
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

    namelabel1 = Label(toplevel, text = "이름")
    namelabel1.place(x = 225, y= 150)
    nametext = Entry(toplevel, width = 20)
    nametext.place(x = 325, y= 150)

    birthdaylabel1 = Label(toplevel, text = "생일")
    birthdaylabel1.place(x = 225, y=200 )
    birthdaytext = Entry(toplevel, width = 20)
    birthdaytext.place(x = 325, y= 200)

    sexlabel1 = Label(toplevel, text = "성별")
    sexlabel1.place(x = 225, y= 250)
    sextext = Entry(toplevel, width = 20)
    sextext.place(x = 325, y= 250)

    maillabel1 = Label(toplevel, text = "메일")
    maillabel1.place(x = 225, y= 300)
    mailtext = Entry(toplevel, width = 20)
    mailtext.place(x = 325, y= 300)

    clearbutton = Button(toplevel, text = "등록", command = register)
    cancelbutton = Button(toplevel, text = "취소", command = quit1)
    overlapbutton = Button(toplevel, text = "중복 조회", command = overlapcheck ,font =("돋움체", 8),fg= "red" , width = 10)
    clearbutton.place(x = 275, y = 400)
    cancelbutton.place(x = 375, y = 400)
    overlapbutton.place(x = 480, y =100)

def Member_search() : 
    def search() :
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
        
        Search = User[(User['User_phone'] == phonetext2.get()) | (User['User_name'] == nametext2.get())]
        Search = Search[['User_name', 'User_birthday', 'User_phone', 'User_sex', 'User_withdrawcheck', 'User_rentcnt']]
        Search = Search.values.tolist()
        for i in range(len(Search)):
            treeview.insert("", "end", text = "", values=Search[i], iid = i)


        treeview.bind('<Double-Button-1>', choice)

    def choice(event) :
        Search = User[(User['User_phone'] == phonetext2.get()) | (User['User_name'] == nametext2.get())]
        toplevel3 =Toplevel(window)
        toplevel3.geometry("700x500")

        label=Label(toplevel3, text="회원 정보 상세 창", font = ("돋움체", 20), anchor = N)
        label.place(x = 225, y = 30)

        phonelabel3 = Label(toplevel3, text = "전화번호")
        phonelabel3.place(x = 225, y= 90)
        phonetext3 = Entry(toplevel3, width = 20)
        phonetext3.insert(0, Search.iloc[0]['User_phone'])
        phonetext3.place(x = 325, y= 90)

        namelabel3 = Label(toplevel3, text = "이름")
        namelabel3.place(x = 225, y= 140)
        nametext3 = Entry(toplevel3, width = 20)
        nametext3.insert(0, Search.iloc[0]['User_name'])
        nametext3.place(x = 325, y= 140)

        birthdaylabel3 = Label(toplevel3, text = "생일")
        birthdaylabel3.place(x = 225, y=190 )
        birthdaytext3 = Entry(toplevel3, width = 20)
        birthdaytext3.insert(0, Search.iloc[0]['User_birthday'])
        birthdaytext3.place(x = 325, y= 190)

        sexlabel3 = Label(toplevel3, text = "성별")
        sexlabel3.place(x = 225, y= 240)
        sextext3 = Entry(toplevel3, width = 20)
        sextext3.insert(0, Search.iloc[0]['User_sex'])
        sextext3.place(x = 325, y= 240)

        maillabel3 = Label(toplevel3, text = "메일")
        maillabel3.place(x = 225, y= 290)
        mailtext3 = Entry(toplevel3, width = 20)
        mailtext3.insert(0, Search.iloc[0]['User_mail'])
        mailtext3.place(x = 325, y= 290)

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
            MsgBox = messagebox.askquestion ('수정 확인','수정하시겠습니까??')
            if MsgBox == 'yes':
                if (Search['User_withdrawcheck'] == 'O').any() :
                    messagebox.showinfo("수정 불가능", "이미 탈퇴한 회원은 수정이 불가능합니다.")
                else : 
                    if Search.iloc[0]['User_phone'] == phonetext3.get() :
                        messagebox.showinfo("수정 완료", "수정이 완료되었습니다.")
                        User.loc[(User['User_phone'] == phonetext2.get()) | (User['User_name'] == nametext2.get()), ('User_phone', 'User_name', 'User_birthday', 'User_sex', 'User_mail')] = [phonetext3.get(), nametext3.get(), birthdaytext3.get() ,sextext3.get(), mailtext3.get()]
                        User.to_csv('UserMake_DF.csv', mode = 'w',header = True, encoding='utf-8-sig')
                        toplevel3.destroy()
                        toplevel2.destroy()
                        
                    elif phonetext3.get() in User['User_phone'].values.astype(str) :
                        messagebox.showinfo("중복", "이미 등록된 전화번호입니다.")
                    

                    else : 
                        messagebox.showinfo("수정 완료", "수정이 완료되었습니다.")
                        User.loc[(User['User_phone'] == phonetext2.get()) | (User['User_name'] == nametext2.get()), ('User_phone', 'User_name', 'User_birthday', 'User_sex', 'User_mail')] = [phonetext3.get(), nametext3.get(), birthdaytext3.get() ,sextext3.get(), mailtext3.get()]
                        User.to_csv('UserMake_DF.csv', mode = 'w', header = True, encoding='utf-8-sig')
                        toplevel3.destroy()
                        toplevel2.destroy()
                    
            else:
                messagebox.showinfo("수정 취소", "수정이 취소되었습니다.")
                toplevel2.destroy()
        
        def overlapcheck() :
            if Search.iloc[0]['User_phone'] == phonetext3.get() :
                return 
            else : 
                if  phonetext3.get() in User['User_phone'].values.astype(str) :
                    messagebox.showinfo("중복", "이미 등록된 전화번호입니다.")
                else : 
                    messagebox.showinfo("사용 가능", "사용 가능한 전화번호입니다.")

        def out() :
            MsgBox = messagebox.askquestion ('탈퇴 확인','탈퇴하시겠습니까??')
            if MsgBox == 'yes':
                if (Search['User_withdrawcheck'] == 'X').any() :
                    User.loc[(User['User_phone'] == phonetext2.get()) | (User['User_name'] == nametext2.get()), ('User_withdrawcheck')] = "O"
                    User.to_csv('UserMake_DF.csv', mode = 'w',header = True, encoding='utf-8-sig')
                    messagebox.showinfo("탈퇴 완료", "탈퇴가 완료되었습니다.")
                    toplevel3.destroy()
                    toplevel2.destroy()

                elif (Search['User_rentcnt'] >= 1 ).any() :
                    messagebox.showinfo("탈퇴 불가능", "대여 중인 회원은 탈퇴가 불가능합니다.")

                elif (Search['User_withdrawcheck'] == 'O').any() :
                    messagebox.showinfo("탈퇴 불가능", "이미 탈퇴한 회원은 탈퇴가 불가능합니다.")
            
            else : 
                messagebox.showinfo("수정 취소", "수정이 취소되었습니다.")

        def cancel() :
            toplevel3.destroy()

        modifybutton = Button(toplevel3, text = "수정", command = modify)
        outbutton = Button(toplevel3, text = "탈퇴", command = out)
        cancelbutton = Button(toplevel3, text = "취소", command = cancel)
        overlapbutton = Button(toplevel3, text = "중복 조회", command = overlapcheck ,font =("돋움체", 8),fg= "red" , width = 10)
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
    choicebutton = Button(toplevel2, text = "선택")
    choicebutton.bind('<Button>', choice)
    cancelbutton = Button(toplevel2, text = "취소", command = quit2)
    searchbutton.place(x = 275, y = 400)
    choicebutton.place(x = 325, y = 400)
    cancelbutton.place(x = 375, y = 400)

def book_add() :
    def quit1() :
        toplevel.destroy()

    def register() :
        MsgBox = messagebox.askquestion ('등록 확인','등록하시겠습니까??')
        if MsgBox == 'yes':
            messagebox.showinfo("등록 완료", "등록이 완료되었습니다.")
            toplevel.destroy()
        else:
            messagebox.showinfo("등록 취소", "등록이 취소되었습니다.")
            toplevel.destroy()

    toplevel=Toplevel(window)
    toplevel.geometry("700x500")

    label=Label(toplevel, text="도서등록", font = ("돋움체", 20))
    label.place(x = 290, y = 30)

    ISBNlabel1 = Label(toplevel, text = "ISBN")
    ISBNlabel1.place(x = 225, y= 95)
    ISBNtext = Entry(toplevel, width = 20)
    ISBNtext.place(x = 325, y= 95)

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
    clearbutton.place(x = 275, y = 395)
    cancelbutton.place(x = 375, y = 395)

def book_search() : 
    def search() :
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

    def choice() :
        toplevel3 =Toplevel(window)
        toplevel3.geometry("700x500")

        label=Label(toplevel3, text="도서 정보 상세 창", font = ("돋움체", 20), anchor = N)
        label.place(x = 225, y = 30)

        titlelabel3 = Label(toplevel3, text = "제목")
        titlelabel3.place(x = 225, y= 85)
        titletext2 = Entry(toplevel3, width = 20)
        titletext2.place(x = 325, y= 85)

        authorlabel3 = Label(toplevel3, text = "저자")
        authorlabel3.place(x = 225, y= 120)
        authortext2 = Entry(toplevel3, width = 20)
        authortext2.place(x = 325, y= 120)

        pricelabel3 = Label(toplevel3, text = "가격")
        pricelabel3.place(x = 225, y=155 )
        pricetext2 = Entry(toplevel3, width = 20)
        pricetext2.place(x = 325, y= 155)

        publabel3 = Label(toplevel3, text = "출판사")
        publabel3.place(x = 225, y= 190)
        pubtext2 = Entry(toplevel3, width = 20)
        pubtext2.place(x = 325, y= 190)

        linklabel3 = Label(toplevel3, text = "관련 링크")
        linklabel3.place(x = 225, y= 225)
        linktext2 = Entry(toplevel3, width = 20)
        linktext2.place(x = 325, y= 225)

        ISBNlabel = Label(toplevel3, text = "ISBN")
        ISBNlabel.place(x = 225, y= 260)
        ISBNtext = Entry(toplevel3, width = 20)
        ISBNtext.place(x = 325, y= 260)

        descriptionlabel1 = Label(toplevel3, text = "도서 설명")
        descriptionlabel1.place(x = 225, y= 295)
        descriptiontext = Entry(toplevel3, width = 20)
        descriptiontext.place(x = 325, y= 295)

        rentlabel1 = Label(toplevel3, text = "대여 여부")
        rentlabel1.place(x = 225, y= 330)
        renttext = Entry(toplevel3, width = 20)
        renttext.place(x = 325, y= 330)

        def modify() :
            messagebox.showinfo("수정 완료", "수정이 완료되었습니다.")
            toplevel3.destroy()
            toplevel2.destroy()

        def delete() :
            messagebox.showinfo("삭제 완료", "삭제가 완료되었습니다.")
            toplevel3.destroy()
            toplevel2.destroy()
        
        def cancel() :
            toplevel3.destroy()

        modifybutton = Button(toplevel3, text = "수정", command = modify)
        outbutton = Button(toplevel3, text = "삭제", command = delete)
        cancelbutton = Button(toplevel3, text = "취소", command = cancel)
        modifybutton.place(x = 275, y = 400)
        outbutton.place(x = 325, y = 400)
        cancelbutton.place(x = 375, y = 400)

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
    choicebutton = Button(toplevel2, text = "선택", command = choice)
    cancelbutton = Button(toplevel2, text = "취소", command = quit2)
    searchbutton.place(x = 275, y = 400)
    choicebutton.place(x = 325, y = 400)
    cancelbutton.place(x = 375, y = 400)

def Rent() :
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

    def choice() :
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

        def choice2() :
            toplevel2.destroy()
            toplevel3 =Toplevel(window)
            toplevel3.geometry("700x500")

            label=Label(toplevel3, text="대여 정보 상세 창", font = ("돋움체", 20), anchor = N)
            label.place(x = 225, y = 30)

            titlelabel3 = Label(toplevel3, text = "제목")
            titlelabel3.place(x = 50, y= 85)
            titletext2 = Entry(toplevel3, width = 20)
            titletext2.place(x = 150, y= 85)

            authorlabel3 = Label(toplevel3, text = "저자")
            authorlabel3.place(x = 50, y= 120)
            authortext2 = Entry(toplevel3, width = 20)
            authortext2.place(x = 150, y= 120)

            pricelabel3 = Label(toplevel3, text = "가격")
            pricelabel3.place(x = 50, y=155 )
            pricetext2 = Entry(toplevel3, width = 20)
            pricetext2.place(x = 150, y= 155)

            publabel3 = Label(toplevel3, text = "출판사")
            publabel3.place(x = 50, y= 190)
            pubtext2 = Entry(toplevel3, width = 20)
            pubtext2.place(x = 150, y= 190)

            linklabel3 = Label(toplevel3, text = "관련 링크")
            linklabel3.place(x = 50, y= 225)
            linktext2 = Entry(toplevel3, width = 20)
            linktext2.place(x = 150, y= 225)

            ISBNlabel = Label(toplevel3, text = "ISBN")
            ISBNlabel.place(x = 50, y= 260)
            ISBNtext = Entry(toplevel3, width = 20)
            ISBNtext.place(x = 150, y= 260)

            descriptionlabel1 = Label(toplevel3, text = "도서 설명")
            descriptionlabel1.place(x = 50, y= 295)
            descriptiontext = Entry(toplevel3, width = 20)
            descriptiontext.place(x = 150, y= 295)

            phonelabel1 = Label(toplevel3, text = "전화번호")
            phonelabel1.place(x = 400, y= 85)
            phonetext = Entry(toplevel3, width = 20)
            phonetext.place(x = 500, y= 85)

            namelabel1 = Label(toplevel3, text = "이름")
            namelabel1.place(x = 400, y= 137)
            nametext = Entry(toplevel3, width = 20)
            nametext.place(x = 500, y= 137)

            birthdaylabel1 = Label(toplevel3, text = "생일")
            birthdaylabel1.place(x = 400, y=190 )
            birthdaytext = Entry(toplevel3, width = 20)
            birthdaytext.place(x = 500, y= 190)

            sexlabel1 = Label(toplevel3, text = "성별")
            sexlabel1.place(x = 400, y= 242)
            sextext = Entry(toplevel3, width = 20)
            sextext.place(x = 500, y= 242)

            maillabel1 = Label(toplevel3, text = "메일")
            maillabel1.place(x = 400, y= 295)
            mailtext = Entry(toplevel3, width = 20)
            mailtext.place(x = 500, y= 295)

            rentlabel1 = Label(toplevel3, text = "대여 여부")
            rentlabel1.place(x = 100, y= 350)
            renttext = Entry(toplevel3, width = 5)
            renttext.place(x = 170, y= 350)

            rentlabel1 = Label(toplevel3, text = "대출 일자")
            rentlabel1.place(x = 270, y= 350)
            renttext = Entry(toplevel3, width = 10)
            renttext.place(x = 340, y= 350)

            rentlabel1 = Label(toplevel3, text = "반납 예정일")
            rentlabel1.place(x = 480, y= 350)
            renttext = Entry(toplevel3, width = 10)
            renttext.place(x = 550, y= 350)

            def modify() :
                messagebox.showinfo("대여 완료", "대여가 완료되었습니다.")
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
        choicebutton = Button(toplevel2, text = "선택", command = choice2)
        cancelbutton = Button(toplevel2, text = "취소", command = quit3)
        searchbutton.place(x = 275, y = 400)
        choicebutton.place(x = 325, y = 400)
        cancelbutton.place(x = 375, y = 400)

    def quit2() :
        toplevel_rent.destroy()

    searchbutton = Button(toplevel_rent, text = "조회", command = search)
    choicebutton = Button(toplevel_rent, text = "선택", command = choice)
    cancelbutton = Button(toplevel_rent, text = "취소", command = quit2)
    searchbutton.place(x = 275, y = 400)
    choicebutton.place(x = 325, y = 400)
    cancelbutton.place(x = 375, y = 400)

def Rent_check() :
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

    def search() :
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

    def choice2() :
        toplevel2.destroy()
        toplevel3 =Toplevel(window)
        toplevel3.geometry("700x500")

        label=Label(toplevel3, text="대여 정보 상세 창", font = ("돋움체", 20), anchor = N)
        label.place(x = 225, y = 30)

        titlelabel3 = Label(toplevel3, text = "제목")
        titlelabel3.place(x = 50, y= 85)
        titletext2 = Entry(toplevel3, width = 20)
        titletext2.place(x = 150, y= 85)

        authorlabel3 = Label(toplevel3, text = "저자")
        authorlabel3.place(x = 50, y= 120)
        authortext2 = Entry(toplevel3, width = 20)
        authortext2.place(x = 150, y= 120)

        pricelabel3 = Label(toplevel3, text = "가격")
        pricelabel3.place(x = 50, y=155 )
        pricetext2 = Entry(toplevel3, width = 20)
        pricetext2.place(x = 150, y= 155)

        publabel3 = Label(toplevel3, text = "출판사")
        publabel3.place(x = 50, y= 190)
        pubtext2 = Entry(toplevel3, width = 20)
        pubtext2.place(x = 150, y= 190)

        linklabel3 = Label(toplevel3, text = "관련 링크")
        linklabel3.place(x = 50, y= 225)
        linktext2 = Entry(toplevel3, width = 20)
        linktext2.place(x = 150, y= 225)

        ISBNlabel = Label(toplevel3, text = "ISBN")
        ISBNlabel.place(x = 50, y= 260)
        ISBNtext = Entry(toplevel3, width = 20)
        ISBNtext.place(x = 150, y= 260)

        descriptionlabel1 = Label(toplevel3, text = "도서 설명")
        descriptionlabel1.place(x = 50, y= 295)
        descriptiontext = Entry(toplevel3, width = 20)
        descriptiontext.place(x = 150, y= 295)

        phonelabel1 = Label(toplevel3, text = "전화번호")
        phonelabel1.place(x = 400, y= 85)
        phonetext = Entry(toplevel3, width = 20)
        phonetext.place(x = 500, y= 85)

        namelabel1 = Label(toplevel3, text = "이름")
        namelabel1.place(x = 400, y= 137)
        nametext = Entry(toplevel3, width = 20)
        nametext.place(x = 500, y= 137)

        birthdaylabel1 = Label(toplevel3, text = "생일")
        birthdaylabel1.place(x = 400, y=190 )
        birthdaytext = Entry(toplevel3, width = 20)
        birthdaytext.place(x = 500, y= 190)

        sexlabel1 = Label(toplevel3, text = "성별")
        sexlabel1.place(x = 400, y= 242)
        sextext = Entry(toplevel3, width = 20)
        sextext.place(x = 500, y= 242)

        maillabel1 = Label(toplevel3, text = "메일")
        maillabel1.place(x = 400, y= 295)
        mailtext = Entry(toplevel3, width = 20)
        mailtext.place(x = 500, y= 295)

        rentlabel1 = Label(toplevel3, text = "대여 여부")
        rentlabel1.place(x = 100, y= 350)
        renttext = Entry(toplevel3, width = 5)
        renttext.place(x = 170, y= 350)

        rentlabel1 = Label(toplevel3, text = "대출 일자")
        rentlabel1.place(x = 270, y= 350)
        renttext = Entry(toplevel3, width = 10)
        renttext.place(x = 340, y= 350)

        rentlabel1 = Label(toplevel3, text = "반납 예정일")
        rentlabel1.place(x = 480, y= 350)
        renttext = Entry(toplevel3, width = 10)
        renttext.place(x = 550, y= 350)

        def modify() :
            messagebox.showinfo("반납 완료", "반납이 완료되었습니다.")
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
    choicebutton = Button(toplevel2, text = "선택", command = choice2)
    cancelbutton = Button(toplevel2, text = "취소", command = quit2)
    searchbutton.place(x = 275, y = 400)
    choicebutton.place(x = 325, y = 400)
    cancelbutton.place(x = 375, y = 400)

titlelabel = Label(window, text = "도서 관리 프로그램", font = ("돋움체",30))
titlelabel.place(x = 215, y = 30)

MemberRegi = Button(window, text = "회원 등록",command = Member_make, width = 10, height = 2)
MemberRegi.place(x = 150, y = 150)

MemberSearch = Button(window, text = "회원 조회",command = Member_search, width = 10, height = 2)
MemberSearch.place(x = 150, y = 200)

button1 = Button(window, text = "도서 등록", command= book_add, width = 10, height = 2).place(x= 350, y =150)
button2 = Button(window, text = "도서 조회", command= book_search, width = 10, height = 2).place(x= 350, y =200)

Rent = Button(window, text = "도서 대여",command = Rent, width = 10, height = 2).place(x= 550, y =150)
Rentsearch = Button(window, text = "대여 조회", command = Rent_check,width = 10, height = 2).place(x= 550, y =200)

window.mainloop()