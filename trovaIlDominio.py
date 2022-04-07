import socket
from tkinter import *

def getDomain(ip):
    global output, entryIP
    output.config(state=NORMAL)
    output.delete(1.0, END)
    
    #se l'utente non ha digitato nulla
    if ip == "":
        output.insert(END, "Non hai inserito alcun IP!")
        output.config(state=DISABLED)
        entryIP.delete(0, END)
        return 0

    try:
        domain_list=socket.gethostbyaddr(ip)
    #errori (timeout, errore ip)
    except Exception as e:
        output.insert(END, e)
        output.config(state=DISABLED)
        entryIP.delete(0, END)
        return 0

    #se ci sono più domini
    if(len(domain_list[1]) >0):
        print("Questo ip pare associato a più domini:")
        output.insert(END, domain_list[0])
        
        #stampo altri domini associati
        for elem in domain_list[1]:
            output.insert(END, elem)
        #disabilita la modifica del Text element
        output.config(state=DISABLED)
        entryIP.delete(0, END)
    else:
        output.insert(END, str(domain_list[0]))
        output.config(state=DISABLED)
        entryIP.delete(0, END)

if __name__=="__main__":
    tk=Tk()
    tk.geometry("400x280+1000+50")
    tk.title("Trova il dominio")
    
    ip=StringVar()
    tk.bind("<Return>", lambda event: getDomain(ip.get()))

    titleLabel = Label(tk, text="Indirizzo IP:", font=("Helvetica", 12)).pack(side=TOP, pady=10)
    
    entryIP = Entry(tk, textvariable=ip)
    entryIP.pack()
    
    middleLabel = Label(tk, text="Dominio:", font=("Helvetica", 12)).pack(pady=10)

    output = Text(tk, height=3, width=40, state=DISABLED, bg="LightYellow2")
    output.pack()   

    bottomLabel = Label(tk, text="Software sviluppato da Daniele Carugo - 2022", font=("Helvetica", 8), fg="white").pack(side=BOTTOM, pady=10)

    domainButton = Button(tk, text="Trova dominio", command=lambda:getDomain(ip.get())).pack(pady=10)

    tk.mainloop()

