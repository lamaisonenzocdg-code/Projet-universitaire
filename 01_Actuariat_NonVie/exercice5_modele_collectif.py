# -*- coding: utf-8 -*-
"""
Created on Fri Dec 26 17:04:53 2025

@author: lamai
"""
import numpy as np
from scipy.stats import poisson, gamma
import matplotlib.pyplot as plt

def f_S_exercice5(s, lam=10, beta=1/100, max_k=60):
    """
    Détermine la fonction de probabilité de S (Q1)
    Logique : somme pondérée des densités Gamma (TD5 Ex3 Q2)
    """
    # 1. Masse de probabilité en s=0 (P(N=0))
    if s == 0:
        return np.exp(-lam)
    
    # 2. Densité pour s > 0
    # On calcule la somme f_k(s) * P(N=k)
    densite_continue = 0
    for k in range(1, max_k):
        # Probabilité P(N=k)
        prob_N = poisson.pmf(k, lam)
        # Densité f_k(s) de la loi Gamma(k, 1/100)
        densite_gamma = gamma.pdf(s, a=k, scale=1/beta)
        
        densite_continue += densite_gamma * prob_N
        
    return densite_continue

# --- Visualisation pour vérification ---
s_points = np.linspace(0.1, 3000, 500)
f_vals = [f_S_exercice5(x) for x in s_points]

plt.figure(figsize=(10, 5))
plt.plot(s_points, f_vals, label="f_S(s) : Poisson(10) composée Exp(1/100)")
plt.title("Fonction de probabilité de S (Question 1)")
plt.xlabel("Montant s")
plt.ylabel("Densité")
plt.legend()
plt.grid(True)
plt.show()

print(f"Probabilité ponctuelle P(S=0) = {f_S_exercice5(0):.6f}")

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, expon
from scipy.signal import convolve

# Paramètres
lam = 10
mu_x = 100 # car beta = 1/100
M = 100000 # Nombre de simulations
delta = 5  # Pas de discrétisation pour Panjer/Convolution
s_max = 3000

# --- 1. SIMULATION ---
N_sim = poisson.rvs(lam, size=M)
S_sim = np.array([np.sum(expon.rvs(scale=mu_x, size=n)) if n > 0 else 0 for n in N_sim])

# --- 2. PREPARATION DISCRETISATION (pour Panjer et Convolution) ---
x_grid = np.arange(0, s_max + delta, delta)
# Discrétisation de l'exponentielle (méthode de l'intégrale locale)
f = expon.cdf(x_grid + delta/2, scale=mu_x) - expon.cdf(x_grid - delta/2, scale=mu_x)
f = f / f.sum() # Normalisation

# --- 3. ALGORITHME DE PANJER ---
# Pour Poisson(lam) : a = 0, b = lam
g_panjer = np.zeros(len(x_grid))
g_panjer[0] = np.exp(lam * (f[0] - 1)) # g0 = P(N=0) si f0=0, sinon P(S=0)

for k in range(1, len(x_grid)):
    somme = 0
    for j in range(1, k + 1):
        somme += (lam * j / k) * f[j] * g_panjer[k-j]
    g_panjer[k] = somme

# --- 4. CONVOLUTION ---
# On limite à k_max pour le calcul (99.9% de la distribution de Poisson)
k_max = int(poisson.ppf(0.999, lam))
g_conv = np.zeros(len(x_grid))
f_k = np.array([1.0]) # Loi de la somme pour k=0 (masse en 0)

for k in range(k_max + 1):
    pk = poisson.pmf(k, lam)
    # On ajoute la contribution de P(N=k)*f^{*k}
    term = pk * f_k[:len(x_grid)]
    g_conv[:len(term)] += term
    # Calcul de la convolution suivante f^{*(k+1)}
    f_k = convolve(f_k, f)[:len(x_grid)]

# --- GRAPHIQUE COMPARATIF ---
plt.figure(figsize=(12, 6))

# Simulation (Histogramme)
plt.hist(S_sim, bins=100, density=True, alpha=0.3, label="Simulation (Monte-Carlo)", color='gray')

# Panjer
plt.plot(x_grid, g_panjer/delta, label="Algorithme de Panjer", linewidth=2, color='blue')

# Convolution
plt.plot(x_grid, g_conv/delta, label="Convolution numérique", linestyle='--', color='red')

plt.title("Comparaison des fonctions de probabilité de S (Question 2)")
plt.xlabel("Montant de la charge totale S")
plt.ylabel("Densité")
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, s_max)
plt.show()