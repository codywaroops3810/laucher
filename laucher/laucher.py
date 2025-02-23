import tkinter as tk
import webbrowser
import threading


# links para butoes
def tkviewslink(url1):
    webbrowser.open(url1)
    
def btcminerlink(url2):
    webbrowser.open(url2)
    
def curso_pythonlink(url3):
    webbrowser.open(url3)
    
def serverdiscordlink(url4):
    webbrowser.open(url4)
    
def nossalojalink(url5):
    webbrowser.open(url5)

# função abrir link pelo botão
def open_link1(url1):
    webbrowser.open(url1, new=0, autoraise=False)

def open_link2(url2):
    webbrowser.open(url2, new=0, autoraise=False)
    
def open_link3(url3):
    webbrowser.open(url3, new=0, autoraise=False)  
    
def open_link4(url4):
    webbrowser.open(url4, new=0, autoraise=False)
    
def open_link5(url5):
    webbrowser.open(url5, new=0, autoraise=False)  

# abrir em 2º plano  
def open_link12p(url1):
    thread = threading.Thread(target=open_link1, args=(url1,))
    thread.start()

def open_link22p(url2):
    thread = threading.Thread(target=btcminerlink, args=(url2,))
    thread.start()
    
def open_link32p(url3):
    thread = threading.Thread(target=open_link3, args=(url3,))
    thread.start()
    
def open_link42p(url4):
    thread = threading.Thread(target=serverdiscordlink, args=(url4,))
    thread.start()
    
def open_link52p(url5):
    thread = threading.Thread(target=nossalojalink, args=(url5,))
    thread.start()   
    
# links
url1 = "https://download947.mediafire.com/rtnwycza8mag6Ac3pg_nklrC_xbMq_KyUXt217k0Hh3OSp37HuUa5mOw64OmOaT0XWq53O7Y0sJ4dsjMbNzMZ68BtPuUyXiK_A-3r3Q7hYXTMDH6WLRAooLAVorkoGQIbqxQM-y4Jxwc4MUcAoBXQq_kI3YJfqpqe0ll03JvnqtYRbs/d0o0acs27yz1yht/tkviews.rar"
url2 = "https://download1530.mediafire.com/t924vmyy85lgHWUBmWpBOYNZJMjx3myqrlrbanGjKGAY9-OTrDApd7XK-tBrHcSCUnSrEj_ltLNHojk4vTqRpk4JkJQ3yB1Z0NHCF3S0T-7lHF0XWUHV9952zBEVmUP9PBoGm3haYrLa9_Nb-qrqw78qfqQdQ_QXZr4c4VIAGkIWG6I/bn3o53r81gvpy4w/btcminer.rar"
url3 = "https://download1580.mediafire.com/x3x88sivcgqgo9F8KaWMek4E_0HaxV4F1zsbIrHRwspeg9Wt1NlzbVXMel1Yir8fu_7bBHPKnHkrsUOen7eXqWfGec7QbauO4OqIL6hnevVE56J8MVZqTocTAvv-DZOm0f2ldxSvPs47vnZuPd2z1xRqqmV32pjP3fNQ6QiXbu4n14M/xm7ehcbnzvpsebp/curso_aprende+tudo+que+precisas+na+linguagem+python+e+ganha+dinheiro.pdf"
url4 = "https://discord.gg/NEWh8spP"
url5 = "https://codyexpress155.myshopify.com"

def main():
    root = tk.Tk()
    root.title("laucher by codywaroops")
    root.geometry("600x400")  # Dimensões maiores para a janela

    label = tk.Label(root, text="Bem-vindo ao Laucher!", font=("Arial", 14))
    label.pack(pady=20)
    
    
     # Adiciona um ícone personalizado (o arquivo deve ser .ico)
    try:
        root.iconbitmap(r"C:\Users\bomba\Desktop\projeto\laucher\assets\laucher.ico")  # Substitua "icon.ico" pelo caminho do seu arquivo de ícone
    except Exception as e:
        print(f"[ERROR] Failed to load icon: {e}")
        
    # Cria um frame utilizando grid para posicionar os botões
    buttons_frame = tk.Frame(root)
    buttons_frame.pack(pady=5)
    
    # Primeira linha: botões "curso python", "tkviews" e "btcminer"
    button1 = tk.Button(buttons_frame, text="curso python", font=("Arial", 12), width=20, height=3, command=lambda: open_link32p(url3))
    button1.grid(row=0, column=0, padx=5, pady=5)
    
    button2 = tk.Button(buttons_frame, text="tkviews", font=("Arial", 12), width=20, height=3, command=lambda: open_link12p(url1))
    button2.grid(row=0, column=1, padx=5, pady=5)
    
    button3 = tk.Button(buttons_frame, text="btcminer", font=("Arial", 12), width=20, height=3, command=lambda: open_link22p(url2))
    button3.grid(row=0, column=2, padx=5, pady=5)
    
    # Segunda linha: "server discord" abaixo de "curso python" e "nossa loja" abaixo de "tkviews"
    button4 = tk.Button(buttons_frame, text="server discord", font=("Arial", 12), width=20, height=3, command=lambda: open_link42p(url4))
    button4.grid(row=1, column=0, padx=5, pady=5)
    
    button5 = tk.Button(buttons_frame, text="nossa loja", font=("Arial", 12), width=20, height=3, command=lambda: open_link52p(url5))
    button5.grid(row=1, column=1, padx=5, pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    main()