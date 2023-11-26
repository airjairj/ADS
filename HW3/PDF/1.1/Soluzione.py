def calcolo_differenze(valori):

    val_tot = sum(valori)                                           # moneta totale del bottino
    print("valore totale: ",val_tot)

    # Creo l'array                                                  # Così copro tutte le possibili somme
    array = [0] * (val_tot // 2 + 1)                                # dalla somma minima (zero) fino a val_tot // 2 (il target)

    # Riempio l'array
    for moneta in valori:                                           # Per ogni moneta
        for i in range(val_tot // 2, moneta - 1, -1):               # Scorro indietro dal target alla moneta                                              
            array[i] = max(array[i], array[i - moneta] + moneta)    # Memoizzo il max tra il valore salvato,
                                                                    # ed il valore precendente + la nuova moneta

    #
    min_diff = val_tot - 2 * array[val_tot // 2]
    print("array post calcoli:\n",array)

    return min_diff

num_test = int(input("NUMERO DI CASI DI TEST: "))

while num_test > 0:

    val_monete = []
    num_monete = int(input("NUMERO DI MONETE: "))  # 1 / 50

    for _ in range(num_monete):
        val_monete.append(int(input("moneta: ")))  # 1 / 1000

    ris = calcolo_differenze(val_monete)
    print("OUTPUT:", ris)

    num_test -= 1
