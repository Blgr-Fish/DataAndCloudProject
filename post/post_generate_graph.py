import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

# fichiers CSV et labels correspondants
files = ["post/post10.csv", "post/post100.csv", "post/post1000.csv"]
labels = ["10 posts/user", "100 posts/user", "1000 posts/user"]

means_list = []

# calculer moyenne des AVG_LAT_MS pour chaque fichier
for f in files:
    df = pd.read_csv(f)
    mean_ms = df["AVG_LAT_MS"].mean()
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
plt.yscale("log")
plt.ylabel("Temps moyen par requête (secondes)")
plt.title("Temps moyen par requête selon la taille des posts")

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
plt.savefig("post/post.png")
plt.close()
