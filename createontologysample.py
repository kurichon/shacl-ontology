#pip install rdflib

from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef, Literal, XSD

# Initialize graph
g = Graph()

# Define namespaces
EX = Namespace("http://example.org/circuit#")
g.bind("ex", EX)
g.bind("rdf", RDF)
g.bind("rdfs", RDFS)
g.bind("owl", OWL)

# Declare classes
g.add((EX.Resistor, RDF.type, OWL.Class))
g.add((EX.Capacitor, RDF.type, OWL.Class))
g.add((EX.Circuit, RDF.type, OWL.Class))

# Object Property: hasPart
g.add((EX.hasPart, RDF.type, OWL.ObjectProperty))
g.add((EX.hasPart, RDFS.domain, EX.Circuit))
g.add((EX.hasPart, RDFS.range, EX.Component))  # Assume Component is superclass

# Data Property: hasResistance
g.add((EX.hasResistance, RDF.type, OWL.DatatypeProperty))
g.add((EX.hasResistance, RDFS.domain, EX.Resistor))
g.add((EX.hasResistance, RDFS.range, XSD.float))

# Create individuals
r1 = EX.R1
c1 = EX.C1
ckt = EX.MyCircuit

g.add((r1, RDF.type, EX.Resistor))
g.add((c1, RDF.type, EX.Capacitor))
g.add((ckt, RDF.type, EX.Circuit))

# MyCircuit hasPart R1 and C1
g.add((ckt, EX.hasPart, r1))
g.add((ckt, EX.hasPart, c1))


#Assign data properties
g.add((r1, EX.hasResistance, Literal(1000, datatype=XSD.float)))

#Save to TTL
g.serialize(destination="circuit.ttl", format="turtle")