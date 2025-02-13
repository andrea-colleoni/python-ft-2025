#%% Import
import numpy as np
import sys

print(np.info(np.array, output=sys.stdout))
# %%

#%%
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr)
# %%

#%%
arr_quad = arr ** 2
print(arr_quad)
# %%

#%% matrici
matrice = np.array([[1, 2, 3], [4,  5, 6]])
print(matrice)
matrice = matrice + 2
print(matrice)
# %%

#%%
zeros = np.zeros((2, 3, 4))
ones = np.ones((3, 5))
casuali = np.random.rand(3, 3)
print(zeros)
print(ones)
print(casuali)
# %%

#%% operazioni tra vettori/matrici
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print(a + b)
print(a * b)
print(a / b)
# %%

#%%
print(np.sum(a))
print(np.mean(a))
print(np.max(a))
print(np.min(a))
print(np.std(a))
# %%

#%% index / slice
numeri = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(numeri[1])
print(numeri[1:5:2])
print(numeri[-3:])
# %%

#%% indicizzazione condizionale
print(numeri[numeri > 30])
print(numeri[(numeri > 30) & (numeri <= 80)])
# %%

#%% ordinamenti
valori = np.array([20, 4, 16, 12, 17, 25, 3 , 7])
ordinati = np.sort(valori)
print(ordinati)

c = 20
tabella = np.array([[c, 5], [6, 8], [12, 4]])
print(np.sort(tabella, axis= None))
print(np.sort(tabella, axis= 1))
# %%

#%% iteratori
for n in tabella.flat:
    print(n)

for idx, row in enumerate(tabella):
    print(f"Riga {idx}: {row}")
# %%

#%% salvataggio e caricamento
np.save("valori", valori)
np.savetxt("tabella.txt", tabella, delimiter=', ')

load = np.load("valori.npy")
print(load)
# %%