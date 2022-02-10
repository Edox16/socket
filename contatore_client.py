import socket
import json

#Dichiaro una porta e gli assegno un valore (127.0.0.1) e dopo una porta (65433)
HOST="127.0.0.1"
PORT=22009

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        stri=input('Inserire i dati, "KO" per uscire: ')
        messaggio={
            'Stringa' : stri
        }
        messaggio=json.dumps(messaggio) 
        s.sendall(messaggio.encode("UTF-8"))
        data=s.recv(1024)
        if stri=="KO":
            print(data.decode())
            break
        else:
            print("Stringa modificata: ", data.decode())