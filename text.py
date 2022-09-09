from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.metrics import sp,dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.popup import Popup
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
import socket
import threading
addr = ("localhost",7000)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def Cconnect(addr):
    try:
        client.connect(addr)
        print("connected")
    except:
        print("Error accured in Cconnect")

def send_form(data):
    try:
       data = data.encode("utf-8")
       client.send(data)
       print("Form sent")
    except:
         print("Error accured in send_form")


class account(BoxLayout):
    def __init__(self,**kwd):  
        super().__init__(**kwd) 
        self.grid = GridLayout(cols=2, spacing=(dp(10),dp(10)),pos_hint={'x':.8,'right':.1})
        self.box = BoxLayout(orientation='vertical',size_hint=(.8,.8),padding=(0,0,0,dp(15)))
        self.lebname = Label(text="Name:",font_size=sp(30),size_hint=(1,None),height=dp(90)) 
        self.lebage = Label(text="Age:",font_size=sp(30),size_hint=(1,None),height=dp(90))
        self.lebpass = Label(text="New Password:",font_size=sp(30),size_hint=(1,None),height=dp(90)) 
        self.txtname = TextInput(hint_text="Name",font_size=sp(30),size_hint=(1,None),height=dp(90)) 
        self.txtage = TextInput(hint_text="Age",font_size=sp(30),size_hint=(1,None),height=dp(90))
        self.txtpass = TextInput(hint_text="password",font_size=sp(30), password=True,size_hint=(1,None),height=dp(90))
        self.grid.add_widget(self.lebname)   
        self.grid.add_widget(self.txtname)
        self.grid.add_widget(self.lebage)
        self.grid.add_widget(self.txtage)
        self.grid.add_widget(self.lebpass)
        self.grid.add_widget(self.txtpass)
        self.btn = Button(text="Submit",font_size=sp(25),size_hint=(.4,None), height=dp(70),pos_hint={'x':.3,'top':.2})
        self.box.add_widget(self.grid)
        self.box.add_widget(self.btn)
        self.add_widget(self.box)

class message_place(BoxLayout):
    def __init__(self,**kwd):
        super().__init__(**kwd)
        self.scv = ScrollView()
        self.msg_btn = Label(text="Hi Love",font_size=sp(25),size_hint=(None,None),size=(dp(200),dp(70)))
        self.msg_btn2 = Label(text="Hy hailse me",font_size=sp(25),size_hint=(None,None),size=(dp(200),dp(70)))
#        self.msg_btn.background_color=(1,1,1,1)
        self.orientation = "vertical"
        self.msg = AnchorLayout(anchor_x="left",anchor_y="top")
        self.msg2 = AnchorLayout(anchor_x="right",anchor_y="top")
        self.box = BoxLayout(orientation="horizontal",size_hint=(1,None))
        self.box.height = self.box.minimum_height
        self.msg.add_widget(self.msg_btn)
        self.msg2.add_widget(self.msg_btn2)
        self.box.add_widget(self.msg)
        self.box.add_widget(self.msg2)
        self.box2 = BoxLayout(orientation="horizontal",size_hint=(1,None),height=dp(110))
        self.btn = Button(text="Send",size_hint=(None,None),size=(dp(60),dp(50)))
        self.txt = TextInput(hint_text="Enter Message",font_size=sp(30))
        self.box2.add_widget(self.txt)
        self.box2.add_widget(self.btn)
        self.scv.add_widget(self.box)
        self.add_widget(self.scv)
        self.add_widget(self.box2)


class name(AnchorLayout):
      def __init__(self,**kwd):
        super(name,self).__init__(**kwd)
        self.anchor_x="center"
        self.anchor_y="top"
        self.padding=(0,dp(40),0,0)
        self.box2 = BoxLayout(size_hint=(.5,.5), spacing=dp(20),orientation='vertical')
        self.txt = TextInput(font_size=sp(25),size_hint=(1,None),height=dp(60))
        self.lab = Label(text="chat with",font_size=sp(30),size_hint=(1,None),height=dp(60))
        self.btn = Button(text="Submit",font_size=sp(25),background_color=(.5,.8,.7,.9),size_hint=(1,None),height=dp(75))
        self.box = BoxLayout(orientation='horizontal')
        self.box.add_widget(self.lab)
        self.box.add_widget(self.txt)
        self.box2.add_widget(self.box)
        self.box2.add_widget(self.btn)
        self.add_widget(self.box2)


class maininter(FloatLayout):
    def __init__(self,**kwd):
        super(maininter,self).__init__(**kwd)
        self.grid = GridLayout(cols=2,size_hint=(1,.6),spacing=(dp(7),dp(20)),padding=(0,dp(10),0,0))
        self.box2 = BoxLayout(orientation="vertical")
        self.popup = Popup(title="Form", separator_color=(0,1,0,1),title_size=dp(30),size_hint=(.6,.8))
        self.box = BoxLayout(size_hint=(1,.3), orientation="vertical",padding=dp(10))
        self.lab1 = Label(text="Name: ",color=(0,0,0,1),bold=True,font_size=sp(35),size_hint=(1,None),height=dp(65))
        self.lab2 = Label(text="Password: ",color=(0,0,0,1),bold=True,font_size=sp(35),size_hint=(1,None),height=dp(65))
        self.btn = Button(text="Login", background_color=(0,0,1,1),size_hint=(.8,.4),color=(0,0,0,1),pos_hint={'x':.1},font_size=sp(25))
        self.btn2 = Button(text="Create account", background_color=(1,0,0,1),font_size=sp(25),size_hint=(.6,.3),color=(0,0,0,1),pos_hint={'center_x':.2,'x':.3})
        self.txt1 = TextInput(size_hint=(1,None),height=dp(65), multiline=False,font_size=sp(25))
        self.txt2 = TextInput(size_hint=(1,None),height=dp(65),password=True, multiline= False,font_size=sp(25))
        self.btn3 = Button(text="Login", background_color=(1,0,0,1),font_size=sp(20),size_hint=(None,None),size=(dp(160),dp(80)),color=(0,0,0,1),pos_hint={'x':.4,'top':.5})
        self.grid.add_widget(self.lab1)
        self.grid.add_widget(self.txt1)
        self.grid.add_widget(self.lab2)
        self.grid.add_widget(self.txt2)
        self.box.add_widget(self.btn)
        self.box.spacing = dp(10)
        self.box.add_widget(self.btn2)
        self.box2.add_widget(self.grid)
        self.box2.add_widget(self.box)
        self.popup.content = self.box2
        self.add_widget(self.btn3)
        self.btn3.bind(on_press=self.loginpopup)
    def loginpopup(self,btnobj):
         self.popup.open()
         thr1 = threading.Thread(target=Cconnect,args=(addr,))
         thr1.start()
class MainApp(App):
    def build(self):
        self.obj = maininter()
        self.obj.btn.bind(on_press=self.loginresp)
        self.sm = ScreenManager()
        self.login = Screen(name="login")
        self.login.add_widget(self.obj)
        self.cr_ac = Screen(name="account")
        self.acc = account()
        self.msg = message_place()
        self.msg.btn.bind(on_press=self.for_send)
        self.msg_sc = Screen(name="msg")
        self.msg_sc.add_widget(self.msg)
        self.sm.add_widget(self.msg_sc)
        self.acc.btn.bind(on_press=self.accsubmit)
        self.cr_ac.add_widget(self.acc)
        self.sm.add_widget(self.login)
        self.sm.add_widget(self.cr_ac)
        self.sm.current="login"
        self.obj.btn2.bind(on_press=self.chsc)
        return self.sm
    def loginresp(self,btn):
        line = f"Name :{self.obj.txt1.text} Password: {self.obj.txt2.text}"
        print(f"Form Result {line}")
        self.sm.current = "msg"
        self.obj.popup.dismiss()
        thr2 = threading.Thread(target=send_form,args=(line,))
        thrlog = threading.Thread(target=self.recv_msg)
        thr2.start()
        thr2.join()
        thrlog.start()
    def chsc(self,btn):
        print("[CHANGING] Screen Changed")
        self.sm.current =  "account"
        self.obj.popup.dismiss()
    def accsubmit(self,btn):
        line = f"Name: {self.acc.txtname.text} Age: {self.acc.txtage.text} Password: {self.acc.txtpass.text}"
        print(line)
        self.sm.current = "login"
        thr3 = threading.Thread(target=send_form,args=(line,))
        thr3.start()
        thr4 = threading.Thread(target=self.recv_msg)
        thr3.join()
        thr4.start()
        print("thr4 started")
    def send_msg(self):
        msg = self.msg.txt.text.encode('utf-8')
       
        print(msg)
        client.send(msg)
        print("message sent")
        self.msg.msg_btn2.text = msg.decode()
        self.msg.txt.text=""
    def for_send(self,btn):
       thr5 = threading.Thread(target=self.send_msg)
       thr5.start()
#       self.msg.btn2.text = self.sent_msg

    def recv_msg(self):
        try:
            print("inside recv_msg")
            while client:
               data = client.recv(1024).decode("utf-8")
               print("data receved")
               self.msg.msg_btn.text = data
        except:
           print("Error in recv_msg")


if __name__ == "__main__":
    MainApp().run()

