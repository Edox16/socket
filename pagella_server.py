#Importo il socket ed il json
import socket
import json
import pprint

HOST='127.0.0.1'
PORT=65434

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("[*] In ascolto su %s:%d "%(HOST, PORT))
    #conversione del client    
    students={'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7.5,4),("Storia",7.5,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9.5,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7.5,2),("Italiano",6,2),("Inglese",4,3),("Storia",8.5,2),("Geografia",8,2)]}
    while True:
        cs, address=s.accept()#accetta la conversione
        print("Connessione a ", address)
        while True:
            data=cs.recv(1024)
            data=data.decode()
            data=data.strip()
            data=json.loads(data)
            comando=data['Comando']
            print ("[*] Received: %s" % data)
            #list : per vedere i voti inseriti
            #set /nomestudente : per inserire uno studente
            #put /nomestudente/materia/voto/ore : per aggiungere i voti della materia allo studente
            #get /nomestudente : per richiedere i voti di uno studente
            #exit : per chiudere solo il client
            #close : per chiudere sia client sia server
            #Digita il comando list; dizionario studenti eccetera.
            if comando=="#list":
                serialized_dict = json.dumps(students)
                cs.sendall(serialized_dict.encode())
            elif comando.find('#set')!=-1:
                
                

                print(students[nomeStudente])
                


            elif comando.find('#put')!=-1:#Da finire il put
                nomeStud=print("Inserire il nome di uno studente ")
            elif comando=='#close':#Da finire il close
                 print('Ricevuto "KO" dal server. Chiudo la connessione con il client.')
            print (cs.getpeername())
            pp=pprint.PrettyPrinter(indent=4)
            pp.pprint(students)

        cs.close()
            

        
        
        
        
        
        
        
          
    
                        
                    
    
      