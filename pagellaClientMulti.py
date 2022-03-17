#nome del file : pagellaClientMulti.py
import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json
import pprint

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225
NUM_WORKERS=4

#Versione 1 
def genera_richieste1(num,address,port):
    start_time_threads=time.time()
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()
        end_time_thread=time.time()
    #1. Generazione casuale:
    #   di uno studente (valori ammessi: 5 cognomi a caso tra cui il tuo cognome)
    #   di una materia (valori ammessi: Matematica, Italiano, inglese, Storia e Geografia)
    #   di un voto (valori ammessi 1 ..10)
    #   delle assenze (valori ammessi 1..5)
    stud=random.randint(1, 5) 
    mat=random.randint(0, 4)
    materia=""
    if (materia==0):
        materia="Matematica"
    elif (materia==1):
        materia="Italiano"
    elif (materia==2):
        materia="Inglese"
    elif (materia==3):
        materia="Storia"
    else:
        materia="Geografia"

    voto=random.randint(1, 10)
    assenza=random.randint(1, 5)
    #2. comporre il messaggio, inviarlo come json
    messaggio={
            'studente' :stud,
            'materia':materia,
            'voto':voto,
            'assenza':assenza,
    }
    print(messaggio)
    #   esempio: {'studente': 'Studente4', 'materia': 'Italiano', 'voto': 2, 'assenze': 3}
    #3. ricevere il risultato come json: {'studente':'Studente4','materia':'italiano','valutazione':'Gravemente insufficiente'}
    messaggio=json.dumps(messaggio)
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024)
    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        # voto < 4 Gravemente insufficiente
        # voto [4..5] Insufficiente
        # voto = 6 Sufficiente
        # voto = 7 Discreto 
        # voto [8..9] Buono
        # voto = 10 Ottimo -> PER CONTROLLO
        #4 stampare la valutazione ricevuta esempio: La valutazione di Studente4 in italiano è Gravemente insufficiente
        s.close()
    end_time_thread=time.time()
    print(f"La valutazione di studente n.{stud} è: {data.decode()}")
    print("Il tempo è: ", end_time_thread-start_time_threads)

#Versione 2 
def genera_richieste2(num,address,port):
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()
  #....
  #   1. Generazione casuale di uno studente(valori ammessi: 5 cognomi a caso scelti da una lista)
    stud=random.randint(0, 5) 
    materia=random.randint(0, 4)
    voto=random.randint(1, 10)
    assenza=random.randint(1, 5)
    messaggio={
            'studente' :stud,
            'materia':materia,
            'voto':voto,
            'assenza':assenza,
    }
    messaggio=json.dumps(messaggio)
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024)
    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        print(f"{threading.current_thread().name}: Studente: {data.decode()}")
    s.close()
  #   Per ognuna delle materie ammesse: Matematica, Italiano, inglese, Storia e Geografia)
  #   generazione di un voto (valori ammessi 1 ..10)
  #   e delle assenze (valori ammessi 1..5) 
  #   esempio: pagella={"Cognome1":[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9.5,3), ("Storia",8,2), ("Geografia",8,1)]}
  #2. comporre il messaggio, inviarlo come json
  #3  ricevere il risultato come json {'studente': 'Cognome1', 'media': 8.0, 'assenze': 8}

#Versione 3
def genera_richieste3(num,address,port):
  #....
  #   1. Per ognuno degli studenti ammessi: 5 cognomi a caso scelti da una lista
  #   Per ognuna delle materie ammesse: Matematica, Italiano, inglese, Storia e Geografia)
  #   generazione di un voto (valori ammessi 1 ..10)
  #   e delle assenze (valori ammessi 1..5) 
  #   esempio: tabellone={"Cognome1":[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9,3), ("Storia",8,2), ("Geografia",8,1)],
  #                       "Cognome2":[("Matematica",7,2), ("Italiano",5,3), ("Inglese",4,12), ("Storia",5,2), ("Geografia",4,1)],
  #                        .....}
  #2. comporre il messaggio, inviarlo come json
  #3  ricevere il risultato come json e stampare l'output come indicato in CONSOLE CLIENT V.3
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()
  #....
  #   1. Generazione casuale di uno studente(valori ammessi: 5 cognomi a caso scelti da una lista)
    stud=random.randint(0, 4) 
    materia=random.randint(0, 4)
    voto=random.randint(1, 10)
    assenza=random.randint(1, 5)
    messaggio={
            'studente' :stud,
            'materia':materia,
            'voto':voto,
            'assenza':assenza
    }
    messaggio=json.dumps(messaggio)
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024)
    data=json.loads
    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        print(f"{threading.current_thread().name}: La valutazione di studente è: {data.decode()}")
    s.close()

if __name__ == '__main__':
    start_time=time.time()
    # PUNTO A) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)
    # alla quale passo i parametri (num,SERVER_ADDRESS, SERVER_PORT)
    for num in range(0, NUM_WORKERS):
        genera_richieste1(num, SERVER_ADDRESS, SERVER_PORT)

    end_time=time.time()
    print("Total SERIAL time=", end_time - start_time)
     
    start_time=time.time()
    threads=[]
    # PUNTO B) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)  
    # tramite l'avvio di un thread al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i thread e attenderne la fine
    for num in range (0, NUM_WORKERS):
        # ad ogni iterazione appendo il thread creato alla lista threads
        threads.append(threading.Thread(target=genera_richieste1, args=(num, SERVER_ADDRESS, SERVER_PORT,)))
        #thread2=threads.append(threading.Thread(target=genera_richieste2, args=(num, SERVER_ADDRESS, SERVER_PORT,)))
        #thread3=threads.append(threading.Thread(target=genera_richieste3, args=(num, SERVER_ADDRESS, SERVER_PORT,)))

    for i in range (len(threads)):
        threads[i].start()
        #thread2[i].start()
        #thread3[i].start()

    for i in range (len(threads)):
        threads[i].join()
        #thread2[i].join()
        #thread3[i].join()
    end_time=time.time()
    print("Total THREADS time= ", end_time - start_time)

    """start_time=time.time()
    process=[]
    # PUNTO C) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3) 
    # tramite l'avvio di un processo al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i processi e attenderne la fine
    for num in range(0, NUM_WORKERS):
        process.append(multiprocessing.Process(target=genera_richieste1, args=(num, SERVER_ADDRESS, SERVER_PORT)))
        process.append(multiprocessing.Process(target=genera_richieste2, args=(num, SERVER_ADDRESS, SERVER_PORT)))
        process.append(multiprocessing.Process(target=genera_richieste3, args=(num, SERVER_ADDRESS, SERVER_PORT)))

    for num in range(0, NUM_WORKERS):
        process[num].start()

    for num in range(0, NUM_WORKERS):
        process[num].join()

    end_time=time.time()
    print("Total PROCESS time= ", end_time - start_time)"""