# rnapi
Petite API de recherche dans le Répertoire National des Associations (RNA)

## Import des données

psql < import_rna.sql


## Installation de l'API

**Utiliser python 3 !!!**

```
mkvirtualenv rnapi -p /usr/bin/python3
pip install -r requirements.txt
```
## Démarrer l'API

```
gunicorn rnapi:app -b 0.0.0.0:1901
```

## Exemples de recherches

Par nom: http://stmaur.cquest.org:1901/rna?nom=OpenStreetMap

Par nom + code INSEE de commune:

http://stmaur.cquest.org:1901/rna?nom=OpenStreetMap&insee=75102

Par code RNA ou de déclaration:

http://stmaur.cquest.org:1901/rna?rna=W751212517

Par code INSEE de commune:

http://stmaur.cquest.org:1901/rna?insee=89004

Par code SIRET:

http://stmaur.cquest.org:1901/rna?siret=41473595100017
