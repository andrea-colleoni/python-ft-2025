#%% Liste
numeri = [1, 2, 3, 4, 5]
vari = ["ciao", 1, 2.5, True]
con_vuoti = [1, 2, None, 4]

print(numeri)
vari.append("nuovo")
con_vuoti[2] = 3 # ripempio l'elemento vuoto

# %%

#%% Stampa liste
print(vari)
print(con_vuoti)
# %%

#%% Dizionari
persona = {
    "nome": "Mario",
    "cognome": "Rossi",
    "eta": 30
}
persona["eta"] = 31
print(persona)
print(persona["nome"])
# %%

#%% Controllo di flusso
if persona["eta"] < 18:
    print("Minorenne")
    print("Non puoi guidare")
elif persona["eta"] < 30:
    print("Giovane")
    print("Puoi guidare")
else:    
    print("Adulto")
    print("Puoi guidare")
print("Fine")
# %%

#%% Cicli
for i in range(5):
    print(i)

for v in vari:
    print(v)
# %%

#%% Funzioni
def saluta(nome):
    print("Ciao", nome)

saluta("Mario")
# %%