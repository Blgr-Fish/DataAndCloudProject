# DataAndCloudProject — Résultats du benchmark TinyInsta

Lien de la webapp : [tiny-insta](https://tinyinsta-benchmark.ew.r.appspot.com/) 

Présentation des résultats CSV présents dans le dossier `out/`. Pour chaque expérience
 :
- Un tableau reprenant les lignes du CSV correspondant aux valeurs en provenance de  `out/`),
- L'image du graphe associé.

**Remarque** : j'ai utilisé `hey` (heybenchmark) au lieu d'ApacheBench (`ab`) parce que `ab` provoquait des timeouts sur mes tests. J'ai aussi modifié sur mon `google cloud console` le fichier `seed.py` pour qu'il insère plus rapidement dans les tables. Pour finir, le fichier `reset_tables.py` a été utilisé pour vider les tables `Post` et `User`.

## Concurrence (`out/conc.csv`)

Paramètres CSV :

| PARAM | AVG_TIME | RUN | FAILED |
|---:|---:|---:|---:|
| 1 | 70.1 | 1 | 0 |
| 1 | 55.6 | 2 | 0 |
| 1 | 51.7 | 3 | 0 |
| 10 | 113.0 | 1 | 0 |
| 10 | 120.8 | 2 | 0 |
| 10 | 118.8 | 3 | 0 |
| 20 | 157.8 | 1 | 0 |
| 20 | 159.3 | 2 | 0 |
| 20 | 147.2 | 3 | 0 |
| 50 | 255.6 | 1 | 0 |
| 50 | 257.3 | 2 | 0 |
| 50 | 215.6 | 3 | 0 |
| 100 | 425.7 | 1 | 0 |
| 100 | 435.2 | 2 | 0 |
| 100 | 463.5 | 3 | 0 |
| 1000 | 4952.8 | 1 | 0 |
| 1000 | 5608.8 | 2 | 0 |
| 1000 | 7354.7 | 3 | 0 |

Graphe associé :

![Concurrence](out/conc.png)

## Taille des posts (`out/post.csv`)

Paramètres CSV :

| PARAM | AVG_TIME | RUN | FAILED |
|---:|---:|---:|---:|
| 50 | 270.9 | 1 | 0 |
| 50 | 249.9 | 2 | 0 |
| 50 | 228.7 | 3 | 0 |
| 50 | 268.0 | 1 | 0 |
| 50 | 226.1 | 2 | 0 |
| 50 | 194.1 | 3 | 0 |
| 50 | 6260.8 | 1 | 0 |
| 50 | 5776.5 | 2 | 0 |
| 50 | 6125.2 | 3 | 0 |

Graphe associé :

![Taille des posts](out/post.png)

## Fanout / followees (`out/fanout.csv`)

 Paramètres CSV :

| PARAM | AVG_TIME | RUN | FAILED |
|---:|---:|---:|---:|
| 50 | 376.5 | 1 | 0 |
| 50 | 340.5 | 2 | 0 |
| 50 | 326.7 | 3 | 0 |
| 50 | 449.8 | 1 | 0 |
| 50 | 437.8 | 2 | 0 |
| 50 | 443.2 | 3 | 0 |
| 50 | 7440.0 | 1 | 0 |
| 50 | 8385.2 | 2 | 0 |
| 50 | 12858.6 | 3 | 0 |

Graphe associé :

![Fanout](out/fanout.png)

## Conclusion

On constate qu'avec ce benchmark, que le fanout et la concurrence impactent beaucoup les performances, et qu'au contraire le nombre de posts est négligeable malgré l'énorme quantité de posts que l'on a insérée pour l'expérience.

Cela démontre donc que ce programme `tiny-insta` est en **Fanout-Read** : Lorsque l'on affiche la timeline d'un utilisateur, on récupère tous ses followees, puis on trie lesquels on va afficher et enfin on les renvoie. 

#### Remarque :

Lors du benchmark, il y a eu beaucoup de soucis liés aux temps d'exécution ; parfois ils étaient anormalement longs, j'ai donc dû par moment vider l'ensemble des tables, et retirer les index, puis remettre le tout en ordre. De plus, avec seulement 3 runs par barplot, la quantité de données peut ne pas être suffisante pour représenter fidèlement les temps d'exécution, en d'autres termes, certaines valeurs ne sont peut-être pas représentatives des vraies performances associées à la webapp.