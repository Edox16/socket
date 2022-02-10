#Importo il socket ed il json
import socket
import json

#Dichiaro una porta e gli assegno un valore (127.0.0.1) e dopo una porta (65433)
HOST="127.0.0.1"
PORT=22009

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    cont=1
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST,PORT))
    s.listen()
    print("[*] In ascolto con %s:%d"%(HOST,PORT))
    clientsocket, address = s.accept()
    with clientsocket as cs:
        print("Connessione da ", address)
        while True:
            data=cs.recv(1024)
            if not data:
                break
            data=data.decode()
            data=json.loads(data)
            stri=data['Stringa']
            if stri != "KO":
                risposta="Numero del messaggio: " + str(cont) + "; " + stri
                cont += 1
            else:
                risposta='KO ricevuto dal server. Chiudo la connessione con il client.'
            cs.sendall(risposta.encode("UTF-8"))






