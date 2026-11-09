# Explorateur d'APIs publiques

Page web statique pour chercher et filtrer les APIs du dépôt
[public-apis/public-apis](https://github.com/public-apis/public-apis)
(recherche, catégories, authentification, HTTPS, CORS).

- `index.html` : la page
- `data.js` : les données, générées automatiquement
- `generer.py` / `mettre-a-jour.sh` : téléchargent le README de public-apis et régénèrent `data.js`
- `.github/workflows/maj.yml` : chaque lundi, met à jour les données et redéploie sur GitHub Pages

Mise à jour manuelle en local : `./mettre-a-jour.sh`
