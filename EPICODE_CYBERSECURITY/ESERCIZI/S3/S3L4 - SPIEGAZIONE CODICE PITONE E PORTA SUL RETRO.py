
##########IMPORTAZIONE MODULI 'SOCKET', 'PLATFORM' E 'OS'.########################################### 
#####################################################################################################

#---'SOCKET' È UTILIZZATO PER LA COMUNICAZIONE DI RETE,
#---PLATFORM PER OTTENERE INFORMAZIONI SUL SISTEMA OPERATIVO E OS PER INTERAGIRE CON IL FILE SYSTEM.

import socket, platform, os 

###########################DEFINIZIONE DEGLI INDIRIZZI DEL SERVER####################################
#####################################################################################################

#---'SRV_ADDR' E 'SRV_PORT' DEFINISCONO L'INDIRIZZO IP E LA PORTA SU CUI IL SERVER ASCOLTA.
#---SRV_ADDR È VUOTO, INDICANDO CHE IL SERVER ASCOLTERÀ SU TUTTE LE INTERFACCE DI RETE DISPONIBILI.

SRV_ADDR = ""
SRV_PORT = 1234

###########################CREAZIONE DEL SOCKET######################################################
#####################################################################################################

#---SOCKET.SOCKET(SOCKET.AF_INET, SOCKET.SOCK_STREAM) CREA UN SOCKET UTILIZZANDO IPV4 (AF_INET) E TCP (SOCK_STREAM).

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

###########################BINDING DEL SOCKET########################################################
#####################################################################################################

#---S.BIND((SRV_ADDR, SRV_PORT)) ASSOCIA IL SOCKET ALL'INDIRIZZO E ALLA PORTA SPECIFICATI.

s.bind((SRV_ADDR, SRV_PORT))

###########################ASCOLTO DELLE CONNESSIONI#################################################
#####################################################################################################

#---S.LISTEN(1) METTE IL SOCKET IN MODALITÀ DI ASCOLTO PER UNA CONNESSIONE IN ENTRATA.

s.listen(1)

###########################ACCETTAZIONE DI UNA CONNESSIONE#################################################
###########################################################################################################

#---IL SERVER ACCETTA UNA CONNESSIONE IN ENTRATA CON S.ACCEPT(), CHE RESTITUISCE UN NUOVO SOCKET PER LA COMUNICAZIONE CON IL CLIENT E
#---L'INDIRIZZO DEL CLIENT. STAMPA POI L'INDIRIZZO DEL CLIENT CONNESSO.

connection, address = s.accept()

print("client connected: ", address)

###########################LOOP PRINCIPALE DEL SERVER######################################################
###########################################################################################################

#---LOOP INFINITO-> WHILE 1 CREA UN LOOP INFINITO.
#---RICEZIONE DEI DATI -> CONNECTION.RECV(1024) LEGGE FINO A 1024 BYTE DI DATI DAL CLIENT.
#---GESTIONE DELLE ECCEZIONI -> SE SI VERIFICA UN'ECCEZIONE DURANTE LA RICEZIONE DEI DATI, IL SERVER CONTINUA IL LOOP SENZA INTERROMPERSI.

while 1:
    try:
        data = connection.recv(1024)
    except:
        continue

###########################GESTIONE DEI COMANDI DEL CLIENT######################################################
###########################################################################################################

#---COMANDO '1'-> INFORMAZIONI SULLA PIATTAFORMA PYTHON

#---SE IL SERVER RICEVE '1', CONCATENA LE INFORMAZIONI SULLA PIATTAFORMA E SULL'ARCHITETTURA DELLA MACCHINA 
#---(PLATFORM.PLATFORM() E PLATFORM.MACHINE()) E LE INVIA AL CLIENT.

    if(data.decode('utf-8') == '1'):
        tosend = platform.platform() + platform.machine()
        connection.sendall(tosend.encode())

#---COMANDO '2': LISTA DEI FILE PYTHON

#---RICEZIONE DEL PERCORSO: SE IL SERVER RICEVE '2', LEGGE UN ULTERIORE MESSAGGIO DAL CLIENT CHE CONTIENE UN PERCORSO DI DIRECTORY.
#---LISTARE I FILE: TENTA DI LISTARE I FILE NELLA DIRECTORY SPECIFICATA (OS.LISTDIR(DATA.DECODE('UTF-8'))).
#---CREAZIONE DELLA STRINGA DI RISPOSTA: CREA UNA STRINGA CON I NOMI DEI FILE SEPARATI DA VIRGOLE.
#---GESTIONE DEGLI ERRORI: SE LA DIRECTORY NON ESISTE O NON È ACCESSIBILE, INVIA "WRONG PATH" AL CLIENT.
#---INVIO DELLA RISPOSTA: INVIA LA STRINGA DI RISPOSTA AL CLIENT.

    elif(data.decode('utf-8') == '2'):
        data = connection.recv(1024)
        try:
            filelist = os.listdir(data.decode('utf-8'))
            tosend = ""
            for x in filelist:
                tosend += "," + x
        except:
            tosend = "Wrong path"
        connection.sendall(tosend.encode())

#---COMANDO '0': CHIUDERE LA CONNESSIONE

#---SE IL SERVER RICEVE '0', CHIUDE LA CONNESSIONE CORRENTE E NE ACCETTA UNA NUOVA.

    elif(data.decode('utf-8') == '0'):
        connection.close()
        connection, address = s.accept()


##RIASSUMENDO; QUESTO CODICE IMPLEMENTA UN SEMPLICE SERVER TCP CHE PUÒ RISPONDERE A TRE COMANDI SPECIFICI:

#---'1': INVIA INFORMAZIONI SULLA PIATTAFORMA E SULL'ARCHITETTURA DELLA MACCHINA.
#---'2': INVIA UNA LISTA DEI FILE IN UNA DIRECTORY SPECIFICATA DAL CLIENT.
#---'0': CHIUDE LA CONNESSIONE CORRENTE E NE ACCETTA UNA NUOVA---