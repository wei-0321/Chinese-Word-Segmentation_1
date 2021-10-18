from tkinter import *
from word_segmentation import forward_match, reverse_match

win = Tk() #建立視窗window
win.title('自然語言斷詞系統') #視窗的名字
win.geometry('1480x764') # 設定視窗的大小(長x寬) 
win.config(bg='#4F4F4F') #背景


longest_term = 0
dict_word = {}
#建立詞語字典
with open("lexicon1_raw_nosil.txt", encoding="utf8") as file:
    line = file.readline()
    while line:
        line_list = line.split()
        dict_word.update({line_list[0] : 0})   #詞語 : 出現次數
        if len(line_list[0]) > longest_term:
            longest_term = len(line_list[0])
        line = file.readline()

def getTextInput():
    source_sentence = Text_input.get("1.0","end")#取得文字框的輸入內容 從最初到最末的所有內容
    
    result_forward = forward_match(source_sentence, dict_word, longest_term)

    result_reverse = reverse_match(source_sentence, dict_word, longest_term)
    
    listbox.delete("0", "end")     #點擊前都要先刪除原有的
    for element in result_forward:
        word = source_sentence[element[0] : element[1]+1]
        listbox.insert("end", word)  #一筆一筆加進去
    
    listbox2.delete("0", "end")    #點擊前都要先刪除原有的
    for element in result_reverse:
        word = source_sentence[element[0] : element[1]+1]
        listbox2.insert("end", word)  #一筆一筆加進去
    
    

title = Label(win,text='自然語言斷詞系統',bg='#02578E',fg='#FFFFFF',width=87,font=('微軟正黑體',20,'bold'))#標題

label_intput = Label(win,text='請輸入文章:',bg='#4F4F4F',fg='#FFFFFF',height=3,width=10,font=('微軟正黑體',20,'bold'))
Text_input  = Text(win, height=10) 
Text_input.grid(row=1,column=1,rowspan=2,columnspan=3,ipadx=10,ipady=10,padx=50 ,pady=50)

btn_forward = Button(win,command=getTextInput,text='進行斷詞', width = 10,bg='#02578E',fg='#FFFFFF',font=('微軟正黑體',16,'bold'),relief="flat")#設定搜尋詳細資訊


#正向最長匹配
frame = Frame(win) #讓滾動條和listbox結合
frame.grid(row=7,column=1)
label_forward = Label(frame,text='正向最長匹配',bg='#FFFFFF',fg='#000000',width=20,font=('微軟正黑體',20,'bold')).grid(row=4,column=5)      
listbox = Listbox(frame,width=20,height=20,font=('微軟正黑體',12,'bold'))#設定listbox
listbox.grid(row=5,column=5)#顯示listbox

scb = Scrollbar(frame ,command=listbox.yview) #設定滾動條
listbox.configure(yscroll=scb.set)
scb.grid(row=5,column=4,sticky=NS)#其中N代表北，S代表南，意思是讓這個布局能夠在此格子中及於從南到北的長度


#反向最長匹配
frame2 = Frame(win) #讓滾動條和listbox結合
frame2.grid(row=7,column=3)
label_backward = Label(frame2,text='反向最長匹配',bg='#FFFFFF',fg='#000000',width=20,font=('微軟正黑體',20,'bold')).grid(row=4,column=5)      
listbox2 = Listbox(frame2,width=20,height=20,font=('微軟正黑體',12,'bold'))#設定listbox
listbox2.grid(row=5,column=5)#顯示listbox

scb2 = Scrollbar(frame2 ,command=listbox2.yview) #設定滾動條
listbox2.configure(yscroll=scb2.set)
scb2.grid(row=5,column=4,sticky=NS)#其中N代表北，S代表南，意思是讓這個布局能夠在此格子中及於從南到北的長度


title.grid(row=0,columnspan=10)
label_intput.grid(row=1,column=0,sticky=W+S,padx=50)

btn_forward.grid(row=1,column=5,sticky=S)
          
win.mainloop()