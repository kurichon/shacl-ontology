<<<<<<< HEAD
from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef
from rdflib.namespace import DC, DCTERMS

# Load your ontology
g = Graph()
g.parse("your_ontology.owl", format="xml")  # or "turtle" for TTL

# Optionally bind common namespaces
g.bind("rdfs", RDFS)
g.bind("owl", OWL)
g.bind("dc", DC)
g.bind("dcterms", DCTERMS)

# List of common annotation properties to check
annotation_props = [RDFS.label, RDFS.comment, OWL.versionInfo, DC.title, DC.creator, DCTERMS.description]

# Collect annotations from ontology
for s, p, o in g:
    if p in annotation_props:
        print(f"Subject: {s}")
        print(f"Property: {p}")
        print(f"Value: {o}")
        print("---")
        
entity = URIRef("http://example.org/circuit#Resistor")

for p in annotation_props:
    for o in g.objects(entity, p):
=======
from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef
from rdflib.namespace import DC, DCTERMS

# Load your ontology
g = Graph()
g.parse("your_ontology.owl", format="xml")  # or "turtle" for TTL

# Optionally bind common namespaces
g.bind("rdfs", RDFS)
g.bind("owl", OWL)
g.bind("dc", DC)
g.bind("dcterms", DCTERMS)

# List of common annotation properties to check
annotation_props = [RDFS.label, RDFS.comment, OWL.versionInfo, DC.title, DC.creator, DCTERMS.description]

# Collect annotations from ontology
for s, p, o in g:
    if p in annotation_props:
        print(f"Subject: {s}")
        print(f"Property: {p}")
        print(f"Value: {o}")
        print("---")
        
entity = URIRef("http://example.org/circuit#Resistor")

for p in annotation_props:
    for o in g.objects(entity, p):
>>>>>>> ef7894841a0b1848d359698b5194b0432c7ec9c4
        print(f"{p.split('#')[-1]}: {o}")