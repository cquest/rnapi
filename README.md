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

http://localhost:1901/rna?nom=FNACA
