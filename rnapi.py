#! /usr/bin/python3
import falcon
import psycopg2
import json
import re


class RnaResource(object):
    def getRna(self, req, resp, id=None):
        db = psycopg2.connect("dbname=cquest")
        cur = db.cursor()

        where = '(TRUE)'
        order = ''

        # pagination
        limit = 100
        page = int(req.params.get('page', 1))

        if not id:
            # recherche sur le numéro d'association
            rna = req.params.get('rna', None)
            siret = req.params.get('siret', None)
            if rna:
                where = cur.mogrify("(id=%s OR id_ex=%s)",
                                    (rna, rna)).decode("utf-8")
            elif siret:
                where = cur.mogrify("(siret=%s)", (siret,)).decode("utf-8")
            else:
                # recherche par nom
                nom = req.params.get('nom', None)
                if nom:
                    # on supprime les mots trop courants
                    nom_clean = re.sub('(ASSO[CIATION]*)', '', nom.upper())
                    where = where + cur.mogrify(" AND titre ~ %s",
                                                (nom_clean,)).decode("utf-8")
                    where = where.replace('~', '%')
                    order = cur.mogrify(" ORDER BY titre <-> %s",
                                        (nom,)).decode("utf-8")
                # recherche par code INSEE de commune
                insee = req.params.get('insee', None)
                if insee:
                    where = where + cur.mogrify(" AND adrs_codeinsee=%s",
                                                (insee,)).decode('utf-8')
        else:
            where = cur.mogrify("(id=%s)", (id,)).decode("utf-8")

        query = """SELECT row_to_json(row) FROM (
            SELECT * FROM rna WHERE %s %s LIMIT %s
            ) as row;""" % (where, order, 1000)
        cur.execute(query)

        rna = cur.fetchall()

        resp.status = falcon.HTTP_200
        resp.set_header('X-Powered-By', 'RNApi')
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header("Access-Control-Expose-Headers",
                        "Access-Control-Allow-Origin")
        resp.set_header('Access-Control-Allow-Headers',
                        'Origin, X-Requested-With, Content-Type, Accept')
        resp.body = json.dumps(rna, sort_keys=True)
        db.close()

    def on_get(self, req, resp, id=None):
        self.getRna(req, resp, id)

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
rna = RnaResource()
# things will handle all requests to the matching URL path
app.add_route('/rna', rna)
app.add_route('/rna/{id}', rna)  # handle single event requests
