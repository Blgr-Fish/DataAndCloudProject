import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

df = pd.read_csv("conc/conc.csv")
df["AVG_TIME_S"] = df["AVG_TIME"] / 1000.0

grouped = df.groupby("PARAM")["AVG_TIME"]
means = grouped.mean().values
stds = grouped.std().values
params = grouped.mean().index.tolist()

x = np.arange(len(params))

plt.figure(figsize=(12, 6))

bars = plt.bar(
    x,
    means,
    width=0.6,
    capsize=5,
    color="#4C84D3",
    error_kw={"elinewidth": 0.8, "capthick": 2}
)

plt.xlabel("Nombre d’utilisateurs simultanés")
plt.ylabel("Temps moyen par requête (secondes)")
plt.title("Temps moyen par requête selon la concurrence")

plt.xticks(x, params)

plt.yscale("log")   # Échelle logarithmique

# Forcer l'affichage "normal" (pas scientifique) sur l'axe y
plt.gca().yaxis.set_major_formatter(ScalarFormatter())
plt.gca().yaxis.get_major_formatter().set_scientific(False)

# Ajouter la valeur au-dessus de chaque barre
for xi, val in zip(x, means):
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
plt.savefig("conc/conc.png")
plt.close()
