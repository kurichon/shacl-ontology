from rdflib import Graph, Namespace, RDF, RDFS, URIRef, Literal
from collections import defaultdict
import csv, itertools

onto_file   = "your_ontology.owl"      # TTL works too
onto_fmt    = "xml"                    # "turtle" if TTL

g = Graph().parse(onto_file, format=onto_fmt)

# Set the namespace(s) you use for categories
EX = Namespace("http://example.org/circuit#")
g.bind("ex", EX)

# ------------------------------------------------------------------
#   TRACE the inheritance chain for every datatype property
#     category = *top‑level* super‑property (the one that has no
#     further rdfs:subPropertyOf parent).  Configure as needed.
# ------------------------------------------------------------------
def top_superprop(prop):
    """Return the highest super‑property in the rdfs:subPropertyOf chain."""
    visited = set()
    while True:
        parents = [p for p in g.objects(prop, RDFS.subPropertyOf) if p not in visited]
        if not parents:
            return prop                  # reached the top
        visited.add(prop)
        prop = parents[0]                # follow first path (simple tree)

# Build a map:  datatype‑property  →  category (top super‑property)
CATEGORY_OF = {}
for p in g.subjects(RDF.type, RDF.Property):
    if (p, RDF.type, URIRef("http://www.w3.org/2002/07/owl#DatatypeProperty")) in g:
        CATEGORY_OF[p] = top_superprop(p)
