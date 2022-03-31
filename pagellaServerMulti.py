#nome del file : pagellaServerMulti.py

from email import message
from pprint import pprint
import socket
from threading import Thread
import json


SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225

#Versione 1 
def ricevi_comandi1(sock_service,addr_client):
    while True:
        data=sock_service.recv(1024)
        if not data: 
                break
        data=data.decode()
        data=json.loads(data)        
        #1. recuperare dal json studente, materia, voto e assenze
        """students={'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7.5,4),("Storia",7.5,4),("Geografia",5,7)],
                'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9.5,0),("Storia",8,2),("Geografia",8,1)],
                'Nicola Spina':[("Matematica",7.5,2),("Italiano",6,2),("Inglese",4,3),("Storia",8.5,2),("Geografia",8,2)],
                'Edoardo Giamboi':[("Matematica",8,0),("Italiano",9, 2),("Inglese", 7,1),("Storia",9,1),("Geografia",8,1)],
                'Luca Rossi': [("Matematica", 10,2),("Italiano", 9, 1),("Inglese", 8,1),("Storia", 7,2),("Geografia", 8,1)]}"""
        #2. restituire un messaggio in json contenente studente, materia e una valutazione testuale :
        # voto < 4 Gravemente insufficiente
        # voto [4..5] Insufficiente
        # voto = 6 Sufficiente
        # voto = 7 Discreto 
        # voto [8..9] Buono
        # voto = 10 Ottimo
        studente=data['studente']
        materia=data['materia']
        voto=data['voto']
        assenza=data['assenza']
        #uscito=[]
        #uscito.append(students[studente])
        ris=""
        if (voto<4):
            ris="Gravemente Insufficiente"
        elif (voto==4 or voto==5):
            ris="Insufficiente"
        elif (voto==6):
            ris="Sufficiente"
        elif (voto==7):
            ris="Discreto"
        elif (voto==8 or voto==9):
            ris="Buono"
        else:
            ris="Ottimo"
        """for s in uscito:
            if (uscito[materia]==uscito[s]):
                if (uscito[0]<4):
                    messaggio="G.Insufficiente"
                elif (uscito[0]==4 or uscito[0]==5):
                    messaggio="Insufficiente"
                elif (uscito[0]==6):
                    messaggio="Sufficiente"
                elif (uscito[0]==7):
                    messaggio="Discreto"
                elif (uscito[0]==8 or uscito[0]==9):
                    messaggio="Buono"
                else:
                    messaggio="Ottimo"""
    
        messaggio={
            'studente':studente,
            'materia':materia,
            'risultato':ris
        }
        print("Dati inviati al client: ")
        print(messaggio)
        messaggio=json.dumps(messaggio)
        sock_service.sendall(messaggio.encode("UTF-8"))
    sock_service.close()

#Versione 2 
def ricevi_comandi2(sock_service,addr_client):
  #....
  #1.recuperare dal json studente e pagella
  #2. restituire studente, media dei voti e somma delle assenze :
  while True:
        data=sock_service.recv(1024)
        if not data: 
                break
        data=data.decode()
        data=json.loads(data)        
        studente=data['studente']
        pagella=data['pagella']
        assenze=0
        media=0
        for i,p in enumerate(pagella):
            media+=int(p[1])
            assenze+=int(p[2])
        media=media/i
        messaggio={
            'studente':studente,
            'media':media,
            'assenze':assenze,
        }
        print("Dati inviati al client: ")
        print(messaggio)
        messaggio=json.dumps(messaggio)
        sock_service.sendall(messaggio.encode("UTF-8"))
  sock_service.close()

  """voto=data['voto']
    uscito=[]
    uscito.append(pagella[studente])
    messaggio=""
    for studente, voti in pagella.items():
        media=0
        for v in voti:
            media+=v
            media/=len(voti)
                messaggio=media
        somma=0
        for s in uscito:
            somma+=uscito[1]
        messaggio=", "+somma
        messaggio=str(messaggio)
        sock_service.sendall(messaggio.encode("UTF-8"))
        sock_service.close()"""

     
#Versione 3
def ricevi_comandi3(sock_service,addr_client):
  #....
  #1.recuperare dal json il tabellone
  #2. restituire per ogni studente la media dei voti e somma delle assenze :
  while True:
      data=sock_service.recv(1024)
      if not data:
          break
      data=data.decode()
      data=json.loads()
      pp=pprint.PrettyPrinter(indent=4)
      tab=[]
      for stud in data:
          pagel=data[stud]
          assenze=0
          media=0
          for i,p in enumerate(pagel):
            media+=int(p[1])
            assenze+=int(p[2])    
          media=media/i
          mes={
            'studente': stud,
            'media': media,
            'assenze':assenze,
        }
          tab.append(mes)
      print("Dati inviati al client")
      pp.pprint(tab)
      mes=tab
      mes=json.dumps(mes)
      sock_service.sendall(mes.encode("UTF-8"))
  sock_service.close()


def ricevi_connessioni(sock_listen):
    while True:
        sock_service, addr_client = sock_listen.accept()
        print("\nConnessione ricevuta da " + str(addr_client))
        print("\nCreo un thread per servire le richieste ")
        try:
            Thread(target=ricevi_comandi1,args=(sock_service,addr_client)).start()
        except:
            print("il thread non si avvia")
            sock_listen.close()
        
def avvia_server(SERVER_ADDRESS,SERVER_PORT):
    sock_listen=socket.socket()
    sock_listen.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock_listen.bind((SERVER_ADDRESS,SERVER_PORT))
    sock_listen.listen(5)
    print("Server in ascolto su %s." %str((SERVER_ADDRESS,SERVER_PORT)))
    ricevi_connessioni(sock_listen)

if __name__=='__main__':
    avvia_server(SERVER_ADDRESS,SERVER_PORT)