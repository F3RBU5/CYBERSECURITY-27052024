#include <stdio.h>

void menu ();
void moltiplica ();
void dividi ();
void ins_string();

int main () 
{
	char scelta = {'\0'};/*------------ESSENDO UN CARATTERE PUO' ESSERE SEMPLIFICATA CON ---> char scelta = '\0';---------*/
	menu ();
	scanf ("%d", &scelta);/*-----------ESSENDO SCELTE UN CARATTERE IL FORMATO DEVE ESSERE ---> scanf(" %c", &scelta); L'AGGIUNTA DELLO SPAZIO PRIMA DI C 
										SERVE PER IGNORARE EVENTUALI SPAZIATURE CHE POTREBBERO ARRIVARE DALL'INPUT ES( UNA NUOVA LINEA /n , TABULAZIONI /t) 
							*/

	switch (scelta) /*----POSSIBILE INSERIMENTO DELLA CASISTICA SCELTA NON VALIDA SE LA SCELTA SARA' DIVERSA DA A, B o C
						   -> default: printf("Scelta non valida.\n"); return 1; <-
									INSERITO DOPO ULTIMO BREAK DELLA SCELTA*/
	{
		case 'A':
			moltiplica();
			break;
		case 'B':
            dividi();
             break;
		case 'C':
             ins_string();
             break;
		
	}

return 0;

}


void menu ()
{
	printf ("Benvenuto, sono un assitente digitale, posso aiutarti a sbrigare alcuni compiti\n");
	printf ("Come posso aiutarti?\n");
	printf ("A >> Moltiplicare due numeri\nB >> Dividere due numeri\nC >> Inserire una stringa\n");
}

void moltiplica ()
{
	short int  a,b = 0;
	printf ("Inserisci i due numeri da moltiplicare:");
	scanf ("%f", &a);
	scanf ("%d", &b);

/*--short int a, b = 0;
	scanf ("%hd", &a);
	scanf ("%hd", &b);
--ESSENDO 'a' E 'b' DICHIARATI COME SHORT INT IL FORMATO CORRETTO E' '%hd'-----------*/


	short int prodotto = a * b;

	printf ("Il prodotto tra %d e %d e': %d", a,b,prodotto);
}

void dividi ()
{
        int  a,b = 0;
        printf ("Inserisci il numeratore:");
        scanf ("%d", &a);
	printf ("Inserisci il denumeratore:");
        scanf ("%d", &b);

        int divisione = a % b;	/*FORMATO CORRETTO -> INT divisione = a / b
								SI POTREBBE INSERIRE UN CHECK DI INPUT PER VERIFICARE CHE
								 NUMERATORE E DENOMINATORE SIANO EFFETTIVAMENTE NUMERI INTERI -> 
									printf ("Inserisci il numeratore: "); 
										if (scanf ("%d", &a) != 1)
											{printf("Input non valido.\n");
												return;}
												
												ALLO STESSO MODO POSSIAMO FARE PER IL DENOMINATORE -> 
												 printf ("Inserisci il denominatore: "); if (scanf ("%d", &b) != 1) 
												   { printf("Input non valido.\n"); return; }
											   
											   POSSIAMO ANCHE INSERIRE UN ERRORE PREVISTO COME DIVISIONE PER ZERO, IN QUESTO CASO SE "b" SARA' ZERO
											   IL SISTEMA DARA' ERRORE ->
											   if (b == 0) {printf("Errore: divisione per zero.\n");return;}							   
											   */
											   
								
								

        printf ("La divisione tra %d e %d e': %d", a,b,divisione);
}

void ins_string () 
{
	char stringa[10];
        printf ("Inserisci la stringa:");
        scanf ("%s", &stringa); /*FORMATO CORRETTO -> MODIFICANDO LA SINTASSI NEL MODO CHE SEGUE SAREMO SICURI CHE LO SCANF 
										LEGGERA' UN MASSIMO DI E LI MEMORIZZERA' NELL'ARRAY STRINGA - scanf("%9s", stringa);
								*/
}

