import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

# fichiers CSV et labels correspondants
files = ["fanout/fanout10.csv", "fanout/fanout50.csv", "fanout/fanout100.csv"]
labels = ["10 followee/user", "50 followee/user", "100 followee/user"]

means_list = []

# calculer moyenne des AVG_TIME pour chaque fichier
for f in files:
    df = pd.read_csv(f)
    mean_ms = df["AVG_TIME"].mean()
    means_list.append(mean_ms / 1000.0)  # conversion en secondes

# préparer les positions des barres
x = np.arange(len(files))

plt.figure(figsize=(10, 6))
bars = plt.bar(
    x,
    means_list,
    width=0.6,
    color="#4C84D3",
    capsize=5
)



plt.xticks(x, labels)
plt.yscale("log")   # Échelle logarithmique
plt.ylabel("Temps moyen par requête (secondes)")
plt.title("Temps moyen par requête selon le nombre de followees (200 requêtes, 50 concurrentes)")

# Forcer affichage normal (pas scientifique) sur y
plt.gca().yaxis.set_major_formatter(ScalarFormatter())
plt.gca().yaxis.get_major_formatter().set_scientific(False)


# Ajouter la valeur au-dessus de chaque barre
for xi, val in zip(x, means_list):
    plt.annotate(
        f"{val:.2f}s",
        xy=(xi, val),
        xytext=(0, 6),
        textcoords="offset points",
        ha="center",
        va="bottom",
        fontsize=10,
        color="black"
    )

plt.tight_layout()
plt.savefig("fanout/fanout.png")
plt.close()
