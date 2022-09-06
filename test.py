import json
import requests
urlDep = "https://data.education.gouv.fr/api/v2/catalog/datasets/fr-en-annuaire-education/records?select=count%28%2A%29%20as%20cpt%2C%20%2A&order_by=&group_by=code_departement&limit=10&offset=0"
urlGraphique= "https://data.education.gouv.fr/explore/embed/dataset/fr-en-annuaire-education/analyze/?disjunctive.nom_etablissement&disjunctive.type_etablissement&disjunctive.appartenance_education_prioritaire&disjunctive.type_contrat_prive&disjunctive.code_type_contrat_prive&disjunctive.pial&geofilter.polygon=&q=mail&lang=fr&dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6ImZyLWVuLWFubnVhaXJlLWVkdWNhdGlvbiIsIm9wdGlvbnMiOnsiZGlzanVuY3RpdmUubm9tX2V0YWJsaXNzZW1lbnQiOnRydWUsImRpc2p1bmN0aXZlLnR5cGVfZXRhYmxpc3NlbWVudCI6dHJ1ZSwiZGlzanVuY3RpdmUuYXBwYXJ0ZW5hbmNlX2VkdWNhdGlvbl9wcmlvcml0YWlyZSI6dHJ1ZSwiZGlzanVuY3RpdmUudHlwZV9jb250cmF0X3ByaXZlIjp0cnVlLCJkaXNqdW5jdGl2ZS5jb2RlX3R5cGVfY29udHJhdF9wcml2ZSI6dHJ1ZSwiZGlzanVuY3RpdmUucGlhbCI6dHJ1ZSwiZ2VvZmlsdGVyLnBvbHlnb24iOiIiLCJxIjoibWFpbCIsImxhbmciOiJmciIsImxvY2F0aW9uIjoiMywxOC42NjExNiwtMi43Nzc3MyIsImJhc2VtYXAiOiJqYXdnLnN0cmVldHMifX0sImNoYXJ0cyI6W3siYWxpZ25Nb250aCI6dHJ1ZSwidHlwZSI6ImNvbHVtbiIsImZ1bmMiOiJDT1VOVCIsInlBeGlzIjoiZWNvbGVfbWF0ZXJuZWxsZSIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlLCJjb2xvciI6IiNBRjE5NzQifV0sInhBeGlzIjoiZGF0ZV9vdXZlcnR1cmUiLCJtYXhwb2ludHMiOiIiLCJ0aW1lc2NhbGUiOiJ5ZWFyIiwic29ydCI6IiJ9XSwiZGlzcGxheUxlZ2VuZCI6dHJ1ZSwiYWxpZ25Nb250aCI6dHJ1ZX0%3D&location=3,18.66116,-2.77773&basemap=jawg.streets"

r = requests.get("https://data.education.gouv.fr/api/v2/catalog/datasets/fr-en-annuaire-education?select=2A")
respDep = requests.get(urlDep)
respGraphique = requests.get(urlGraphique)

json_dataDep = json.loads(respDep.text)



def writeIn(r):
    with open("result.json", "w") as f:
        f.write(r.text)
    return open("result1.json", "r") == True

def toJSON(json_dataDep):
    for element in json_dataDep["records"]:
        cpt = element["record"]["fields"]["cpt"]
        dep = element["record"]["fields"]["code_departement"]
        print("Dep: " + str(dep) + "\tCpt: " + str(cpt))
    return True
        
#NOM DE DOMAINE DES MAISL: Fonction Substring inconnue(fonctionne sous SqlServer). Lié a l'ApiKey
#       ==> SUBSTRING(mail,CHARINDEX('@',mail)+1, LEN(mail)) as domaine
#       mail[mail.index('@')+1:len(mail)]
 #Fichier html contenant le graphique   
def stocker():
    with open('graphique.html', 'w') as f:
        f.write("<html><body><iframe src='https://data.education.gouv.fr/explore/embed/dataset/fr-en-annuaire-education/analyze/?disjunctive.nom_etablissement&disjunctive.type_etablissement&disjunctive.appartenance_education_prioritaire&disjunctive.type_contrat_prive&disjunctive.code_type_contrat_prive&disjunctive.pial&geofilter.polygon=&q=mail&lang=fr&dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6ImZyLWVuLWFubnVhaXJlLWVkdWNhdGlvbiIsIm9wdGlvbnMiOnsiZGlzanVuY3RpdmUubm9tX2V0YWJsaXNzZW1lbnQiOnRydWUsImRpc2p1bmN0aXZlLnR5cGVfZXRhYmxpc3NlbWVudCI6dHJ1ZSwiZGlzanVuY3RpdmUuYXBwYXJ0ZW5hbmNlX2VkdWNhdGlvbl9wcmlvcml0YWlyZSI6dHJ1ZSwiZGlzanVuY3RpdmUudHlwZV9jb250cmF0X3ByaXZlIjp0cnVlLCJkaXNqdW5jdGl2ZS5jb2RlX3R5cGVfY29udHJhdF9wcml2ZSI6dHJ1ZSwiZGlzanVuY3RpdmUucGlhbCI6dHJ1ZSwiZ2VvZmlsdGVyLnBvbHlnb24iOiIiLCJxIjoibWFpbCIsImxhbmciOiJmciJ9fSwiY2hhcnRzIjpbeyJhbGlnbk1vbnRoIjp0cnVlLCJ0eXBlIjoiY29sdW1uIiwiZnVuYyI6IkNPVU5UIiwieUF4aXMiOiJlY29sZV9tYXRlcm5lbGxlIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiI0FGMTk3NCJ9XSwieEF4aXMiOiJkYXRlX291dmVydHVyZSIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6InllYXIiLCJzb3J0IjoiIn1dLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlfQ%3D%3D&location=3,18.66116,-2.77773&basemap=jawg.streets&static=false&datasetcard=false' width='400' height='300' frameborder='0'></iframe></body></html>")
        return True
    return False