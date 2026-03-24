# Contare le occorrenze di un elemento (Ricorsione)
import logging

logging.basicConfig(level=logging.DEBUG)

def conta_elemento(lista, valore):
    # utilizzando la ricorsione
    # restituisce il numero di volte in cui valore compare nella lista
    logging.debug(f'Lista corrente: {lista}')
    if len(lista) == 0: # not lista
        # Caso base: lista vuota → ritorna 0
        logging.debug('Caso base: lista vuota → ritorna 0')
        return 0
    
    # Caso ricorsivo: se il primo elemento è uguale a valore → +1 
    # poi continua con il resto della lista escluso il primo elemento
    if lista[0] == valore:
        logging.debug(f'Valore: {lista[0]} = {valore} conta +1')
        return 1 + conta_elemento(lista[1:], valore)
    else:
        logging.debug(f'Non fare nulla')
        return conta_elemento(lista[1:], valore)


print(conta_elemento([1, 2, 2, 3, 2], 2))

#  conta_elemento([1, 2, 2, 3], 2) ->
#  conta_elemento([2, 2, 3], 2) -> 1
#  conta_elemento([2, 3], 2) -> 1
#  conta_elemento([3], 2) -> 
#  conta_elemento([], 2) -> 0
