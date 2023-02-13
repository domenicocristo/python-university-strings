"""
Un cifrario di Cesare è un metodo di criptazione debole che consiste nel "ruotare" 
ogni lettera di una parola di un dato numero di posti seguendo la sequenza alfabetica, ricominciando 
da capo quando necessario. Ad esempio 'A' ruotata di 3 posti diventa 'D', e 'Z' ruotata di 1 posto diventa 'A'.
Per ruotare una parola si ruota ciascuna delle sue lettere dello stesso numero di posti prefissato.

Scrivete una funzione di nome ruota_parola che richieda una stringa e un intero come parametri,
e che restituisca una nuova stringa che contiene le lettere della stringa di partenza ruotate della 
quantità indicata.
"""

def ruota_parola(stringa, intero):
    nuova_stringa = ""
    for lettera in stringa:
        if lettera.isalpha():
            indice_rotato = (ord(lettera) - ord('a') + intero) % 26 + ord('a')
            nuova_lettera = chr(indice_rotato)
            if lettera.isupper():
                nuova_lettera = nuova_lettera.upper()
            nuova_stringa += nuova_lettera
        else:
            nuova_stringa += lettera
    return nuova_stringa

print(ruota_parola('cheer', 7))