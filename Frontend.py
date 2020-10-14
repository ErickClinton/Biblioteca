from tkinter import *
import backend

def get_selected(event):
    global selected_tipo
    index=list1.curselection()[0]
    selected_tipo=list1.get(index)
    print(selected_tipo)
    e1.delete(0,END)
    e1.insert(END,selected_tipo[1])
    e2.delete(0,END)
    e2.insert(END,selected_tipo[2])
    e3.delete(0,END)
    e3.insert(END,selected_tipo[3])
    e4.delete(0,END)
    e4.insert(END,selected_tipo[4])

def ver_comando():
    list1.delete(0,END)
    for achado in backend.Ver():
        list1.insert(END,achado)

def procurar_comando():
    list1.delete(0,END)
    for palavra in backend.procurar(livro_text.get(),recomenda_text.get(),end_text.get(),nota_text.get()):
        list1.insert(END,palavra)

def adicionar_comando():
    backend.insert(livro_text.get(),recomenda_text.get(),end_text.get(),nota_text.get())
    list1.delete(0,END)
    list1.insert(END,(livro_text.get(),recomenda_text.get(),end_text.get(),nota_text.get()))

def deletar_comando():
    backend.deletar(selected_tipo[0])

def update_comando():
    backend.update(selected_tipo[0],livro_text.get(),recomenda_text.get(),end_text.get(),nota_text.get())


window=Tk()


window.wm_title("Livros Lidos")


#dando nome para as barras
l1=Label(window,text="Livro")
l1.grid(row=0,column=0)

l2=Label(window,text="Recomenda")
l2.grid(row=0,column=2)

l3=Label(window,text="End")
l3.grid(row=1,column=0)

l4=Label(window,text="Nota")
l4.grid(row=1,column=2)

#Criando as barras
livro_text=StringVar()
e1=Entry(window,textvariable=livro_text)
e1.grid(row=0,column=1)

recomenda_text=StringVar()
e2=Entry(window,textvariable=recomenda_text)
e2.grid(row=0,column=3)

end_text=StringVar()
e3=Entry(window,textvariable=end_text)
e3.grid(row=1,column=1)

nota_text=StringVar()
e4=Entry(window,textvariable=nota_text)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=1,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected)


#criando os botoes
b1=Button(window,text = "Ver all",width=12,command=ver_comando)
b1.grid(row=2,column=3)

b2=Button(window,text = "Procurar",width=12,command=procurar_comando)
b2.grid(row=3,column=3)

b3=Button(window,text = "Adicionar",width=12,command=adicionar_comando)
b3.grid(row=4,column=3)

b4=Button(window,text = "update",width=12,command=update_comando)
b4.grid(row=5,column=3)

b5=Button(window,text = "delete",width=12,command=deletar_comando)
b5.grid(row=6,column=3)


window.mainloop()
