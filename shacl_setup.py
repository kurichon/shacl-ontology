# Re-create the example SHACL shape file and ontology data in Turtle format

# Example ontology data (circuit-data.ttl)
ontology_data = r"""
@prefix ex: <http://example.org/ontology#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:Resistor1 a ex:Resistor ;
    ex:hasResistanceValue "-5.0"^^xsd:float ;
    ex:hasVoltageRating "12.0"^^xsd:float .

ex:Capacitor1 a ex:Capacitor ;
    ex:hasCapacitanceValue "22.0"^^xsd:float .
"""

# Example SHACL shape file (resistor-shape.ttl)
shacl_shapes = r"""
@prefix ex: <http://example.org/ontology#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:ResistorShape
  a sh:NodeShape ;
  sh:targetClass ex:Resistor ;
  sh:property [
    sh:path ex:hasResistanceValue ;
    sh:datatype xsd:float ;
    sh:minInclusive 0 ;
    sh:message "Resistance must be greater than or equal to 0." ;
  ] .

ex:CapacitorShape
  a sh:NodeShape ;
  sh:targetClass ex:Capacitor ;
  sh:property [
    sh:path ex:hasCapacitanceValue ;
    sh:datatype xsd:float ;
    sh:minInclusive 0 ;
    sh:maxInclusive 100 ;
    sh:message "Capacitance must be between 0 and 100 µF." ;
  ] .
"""
import os
# Save to files
ontology_path = os.getcwd() + "/data/circuit-data.ttl"
shacl_path = os.getcwd() + "/data/resistor-shape.ttl"
try:
    print(os.getcwd())
    os.makedirs(os.getcwd()+ "/data/")
except FileExistsError:
    # directory already exists
    pass
with open(ontology_path, "w") as f:
    f.write(ontology_data)

with open(shacl_path, "w",encoding='utf8') as f:
    f.write(shacl_shapes)

ontology_path, shacl_path
# pip install pyshacl
# pyshacl -d .\data\circuit-data.ttl -s .\data\resistor-shape.ttl
#Results in:
"""
Validation Report
Conforms: False
Results (1):
Constraint Violation in MinInclusiveConstraintComponent (http://www.w3.org/ns/shacl#MinInclusiveConstraintComponent):
        Severity: sh:Violation
        Source Shape: [ sh:datatype xsd:float ; sh:message Literal("Resistance must be greater than or equal to 0.") ; sh:minInclusive Literal("0", datatype=xsd:integer) ; sh:path ex:hasResistanceValue ]
        Focus Node: ex:Resistor1
        Value Node: Literal("-5.0", datatype=xsd:float)
        Result Path: ex:hasResistanceValue
        Message: Resistance must be greater than or equal to 0.
"""