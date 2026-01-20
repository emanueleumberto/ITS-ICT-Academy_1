# Commento a singola riga

# Python NON è un linguaggio tipizzato
# String testo = "Questa è una stringa"

testo = "Questa è una stringa"
# print(testo, type(testo))

testo = 89
# print(testo, type(testo))

testo = True
# print(testo, type(testo))

# Nomenclatura di una variabile
# CamelCase | PascalCase | SnakeCase
nomeDatoVariabile = 0 # -> CamelCase
NomeDatoVariabile = 0 # -> PascalCase
nome_dato_variabile = 0 # -> SnakeCase
nomedatovariabile = 0
NOME_DATO_COSTANTE = 0 # -> Costante

# Assegnazione di una variabile -> =
x = 1
y = 2
z = 3
# Assegnazioni multiple
x,y,z = 1,2,3
x = y = z = 1

""" v = 'testo'
v = "testo"

v = "un'qualcosa"
v = 'Python "NON" è un linguaggio tipizzato'
v = 'Python "NON" è un\'linguaggio tipizzato' """

# Tipi di dato primitivi in python
# -> int    -> 5
# -> float  -> 5.5
# -> string -> 'testo'
# -> bool   -> True | False
# -> None   -> None

# Funzioni primitive predefinite in python
# print(param)  -> Funzione che stampa nel terminale il valore di "param"
# type(param)   -> Funzione che restituisce il tipo di dato di una variabile passata come parametro
# input(param)  -> Funzione che permette di inserire un valore da terminale
# len(param)    -> Funzione che restituisce la lunghezza di una stringa
# help(function)-> Restituisce la documentazione della funzione passata come parametro

""" print("Registrazione utente:")
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
citta = input("Inserisci la tua città: ")
eta = input("inserisci la tua età: ")

pensione = 67 - int(eta)

print("Ciao " + nome + " " + cognome + " (" + citta + ") " + eta + " anni")
print("Anni mancanti alla pensione", pensione)
print("Fine") """


# Funzioni primitive predefinite di casting
# int(param)    -> funzione che restituisce il paramentro inserito nel tipo int
# float(param)  -> funzione che restituisce il paramentro inserito nel tipo float
# str(param)    -> funzione che restituisce il paramentro inserito nel tipo string
# bool(param)  -> funzione che restituisce il paramentro inserito nel tipo boolean
#   bool(0) | bool('') | bool([]) | bool(()) | bool({}) -> False

n = '50'
print(n, type(n))
n = int(n)
print(n, type(n))
n = float(n)
print(n, type(n))
n = bool(n)
print(n, type(n))
n = str(n)
print(n, type(n))

