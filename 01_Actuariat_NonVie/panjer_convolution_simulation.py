
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

# Simulation
N_sim = poisson.rvs(lam, size=M)
S_sim = np.array([np.sum(expon.rvs(scale=mu_x, size=n)) if n > 0 else 0 for n in N_sim])

x_grid = np.arange(0, s_max + delta, delta)
f = expon.cdf(x_grid + delta/2, scale=mu_x) - expon.cdf(x_grid - delta/2, scale=mu_x)
f = f / f.sum() 

# Algorithme de panjer
g_panjer = np.zeros(len(x_grid))
g_panjer[0] = np.exp(lam * (f[0] - 1)) 

for k in range(1, len(x_grid)):
    somme = 0
    for j in range(1, k + 1):
        somme += (lam * j / k) * f[j] * g_panjer[k-j]
    g_panjer[k] = somme

# Convulution
# On limite à k_max pour le calcul (99.9% de la distribution de Poisson)
k_max = int(poisson.ppf(0.999, lam))
g_conv = np.zeros(len(x_grid))
f_k = np.array([1.0])

for k in range(k_max + 1):
    pk = poisson.pmf(k, lam)
    term = pk * f_k[:len(x_grid)]
    g_conv[:len(term)] += term
    f_k = convolve(f_k, f)[:len(x_grid)]


plt.figure(figsize=(12, 6))

# Simulation 
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

points_interet = [500, 1000, 1500, 2000]
print(f"{'Montant s':<10} | {'Panjer':<12} | {'Convolution':<12}")
print("-" * 40)

for s in points_interet:
    idx = int(s / delta)
    val_panjer = g_panjer[idx] / delta
    val_conv = g_conv[idx] / delta
    print(f"{s:<10} | {val_panjer:<12.6f} | {val_conv:<12.6f}")


from scipy.stats import gaussian_kde

# Création de l'estimateur KDE basé sur les données simulées (S_sim)
kde = gaussian_kde(S_sim)

# extraction de la valeur de la densité
points_interet = [500, 1000, 1500, 2000]

# Calcul des valeurs de densité estimées
valeurs_kde = kde.evaluate(points_interet)
print(f"{'Montant s':<10} | {'Simulation (KDE)':<18}")
print("-" * 30)
for s, val in zip(points_interet, valeurs_kde):
    print(f"{s:<10} | {val:<18.6f}")

###QUESTION 3 

#  Espérance Théorique
e_theorique = lam * mu_x

#  Espérance Simulation
e_sim = np.mean(S_sim)

# Espérance Panjer
e_panjer = np.sum(x_grid * g_panjer)

print(f"\n--- Question 3 : Espérances ---")
print(f"Espérance Théorique : {e_theorique:.2f}")
print(f"Espérance Simulation : {e_sim:.2f}")
print(f"Espérance Panjer     : {e_panjer:.2f}")

###QUESTION 4 

# Quantile par Simulation
q05_sim = np.quantile(S_sim, 0.05)

# Quantile par Panjer
cdf_panjer = np.cumsum(g_panjer)
# On cherche l'indice où la CDF dépasse 0.05
idx_q05 = np.where(cdf_panjer >= 0.05)[0][0]
q05_panjer = x_grid[idx_q05]

print(f"\n--- Question 4 : Quantile d'ordre 0.05 ---")
print(f"Quantile 0.05 (Simulation) : {q05_sim:.2f}")
print(f"Quantile 0.05 (Panjer)     : {q05_panjer:.2f}")
print(f"Écart absolu               : {abs(q05_sim - q05_panjer):.2f}")


###QUESTION 5

# VaR par Simulation 
var5_sim = np.quantile(S_sim, 0.95)

# VaR par Panjer
idx_var5 = np.where(cdf_panjer >= 0.95)[0][0]
var5_panjer = x_grid[idx_var5]

print(f"\n--- Question 5 : Value-at-Risk 5% ---")
print(f"VaR 5% (Simulation) : {var5_sim:.2f}")
print(f"VaR 5% (Panjer)     : {var5_panjer:.2f}")
print(f"Écart relatif        : {abs(var5_sim - var5_panjer)/var5_sim:.4%}")


