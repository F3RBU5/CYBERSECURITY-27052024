#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Funzione per presentare l'introduzione del gioco
void presentazione() {
    printf("Benvenuto nel gioco di domande e risposte!\n");
    printf("Rispondi alle domande e accumula punteggio.\n");
}

// Funzione per presentare il menu e ricevere la scelta dell'utente
char menu() {
    char scelta;
    printf("\nMenu:\n");
    printf("A) Iniziare una nuova partita\n");
    printf("B) Uscire dal gioco\n");
    printf("Scelta: ");
    scanf(" %c", &scelta);
    return scelta;
}

// Funzione per iniziare una nuova partita
void nuova_partita() {
    char nome[50];
    int punteggio = 0;
    
    printf("\nInserisci il tuo nome: ");
    scanf("%s", nome);
    printf("\nCiao, %s! Cominciamo la partita!\n", nome);
    
    // Array di domande e risposte
    char domande[][100] = {
        "Qual è la capitale dell'Italia?",
        "Chi ha scritto 'La Divina Commedia'?",
        "Quale pianeta è più vicino al Sole?"
    };
    
    char risposte[][3][50] = {
        {"A) Roma", "B) Milano", "C) Napoli"},
        {"A) Dante Alighieri", "B) Giovanni Boccaccio", "C) Francesco Petrarca"},
        {"A) Mercurio", "B) Venere", "C) Marte"}
    };
    
    char risposta_utente[10];
    
    // Ciclo per ogni domanda
    for(int i = 0; i < 3; i++) {
        printf("\nDomanda %d: %s\n", i+1, domande[i]);
        for(int j = 0; j < 3; j++) {
            printf("%s\n", risposte[i][j]);
        }
        printf("Risposta: ");
        scanf("%s", risposta_utente);
        
        // Valutazione della risposta
        if(strcmp(risposta_utente, "A") == 0 || strcmp(risposta_utente, "a") == 0) {
            if(i == 0) // Risposta alla prima domanda
                punteggio += 10;
        }
        else if(strcmp(risposta_utente, "B") == 0 || strcmp(risposta_utente, "b") == 0) {
            if(i == 1) // Risposta alla seconda domanda
                punteggio += 10;
        }
        else if(strcmp(risposta_utente, "C") == 0 || strcmp(risposta_utente, "c") == 0) {
            if(i == 2) // Risposta alla terza domanda
                punteggio += 10;
        }
    }
    
    // Stampiamo il punteggio finale
    printf("\nIl tuo punteggio finale è: %d\n", punteggio);
}

int main() {
    char scelta;
    
    presentazione();
    
    do {
        scelta = menu();
        
        switch(scelta) {
            case 'A':
            case 'a':
                nuova_partita();
                break;
            case 'B':
            case 'b':
                printf("\nArrivederci!\n");
                break;
            default:
                printf("\nScelta non valida. Riprova.\n");
        }
    } while(scelta != 'B' && scelta != 'b');

    return 0;
}
