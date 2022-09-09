import threading
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
must = [False,False]
conn_pool ={}
addr = ("localhost",7000)
server.bind(addr)
def recv_form():
       conn1 = conn_pool.get("first","Not")
       if conn1 != "Not":
           fform = conn1.recv(1024).decode("utf-8")
           print(f"fform: {fform}")
           must[0]=True
       else:
          print("No Connection")
def recv_formsc():
       conn2 = conn_pool.get("second","Not")
       if conn2 != "Not":
          sform = conn2.recv(1024).decode('utf-8')
          print(f"sform: {sform}")
          must[1]=True
       else:
         print("No connection")
thr2 = threading.Thread(target=recv_form)
thr22 = threading.Thread(target=recv_formsc)
def to_listen():
    i = 1
    while i <= 2:
       key = "first" if i == 1 else "second"
       server.listen()
       i+=1
       print(f"[LISTENING] on {addr}")
       conn,add = server.accept()
       print(f"[CONNECTED] with {addr}")
       conn_pool[key]=conn
       if key == "first":
            thr2.start()
       elif key == "second":
            thr22.start()

def recv_send(key):
    while True:
        print(key)
        print(conn_pool)
        msg = conn_pool.get(key).recv(1024)
        if key == "first":
           conn_pool.get("second").send(msg)
        elif key == "second":
           conn_pool.get("first").send(msg)


thr1 = threading.Thread(target=to_listen)
thr2 = threading.Thread(target=recv_form)
thr3 = threading.Thread(target=recv_send,args=("first",))
thr4 = threading.Thread(target=recv_send,args=("second",))
thr1.start()
thr1.join()
while True:
    if must[0] == True and must[1] == True:
         thr3.start()
         thr4.start()
         break
    else:
        continue
