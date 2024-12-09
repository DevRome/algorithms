# Creazione di una hash table (dizionario)
hash_table = {}

# Inserimento di chiavi e valori
hash_table["nome"] = "Alice"
hash_table["età"] = 25
hash_table["città"] = "Roma"

# Accesso ai valori
print("Nome:", hash_table["nome"])  # Output: Nome: Alice

# Modifica di un valore
hash_table["età"] = 26
print("Età aggiornata:", hash_table["età"])  # Output: Età aggiornata: 26

# Rimozione di una chiave
del hash_table["città"]

# Controllo della presenza di una chiave
print("Città presente?", "città" in hash_table)  # Output: Città presente? False

# Iterazione su chiavi e valori
for chiave, valore in hash_table.items():
    print(chiave, ":", valore)
