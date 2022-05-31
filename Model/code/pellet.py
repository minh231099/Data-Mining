from re import sub
from owlready2 import *

f = open("OWL_REASONING.txt", "w")

onto = get_ontology("../owl/FamilyTree.owl").load()


def createDictIndividuals(properties, individuals):
    dic = {}
    for property in properties:
        relations = property.get_relations()
        for relation in relations:
            if not relation[0].name in dic:
                dic[relation[0].name] = []
            if relation[0].name != relation[1].name:
                dic[relation[0].name].append((property.name, relation[1].name))

    for individual in individuals:
        if individual.name not in dic:
            dic[individual.name] = []

    return dic


# Get list of class
f.write("List Class: \n")
classNames = [x.name for x in (list(onto.classes()))]
classNames.sort()
f.write("[")
for i in range(0, len(classNames)):
    if (i != 0):
        f.write(", ")
    f.write(classNames[i])
f.write("]")
f.write('\n\n')

properties = [x for x in onto.object_properties()]  # Get all object properties
individuals = [x for x in onto.individuals()]  # Get all individual

dic = createDictIndividuals(properties, individuals)

f.write("Properties:\n")
for property in properties:
    f.write(property.name + ", ")
f.write('\n\n')

for individual in individuals:
    if individual.name not in dic:
        dic[individual.name] = []

f.write("Individuals Before Reasoning:\n")
for individual in dic.keys():
    f.write(individual + ':\n')
    obj = individual
    for relation in dic[obj]:
        predict = relation[0]
        subj = relation[1]
        f.write('\t' + predict + ' ' + subj + '\n')
    f.write('\n')

with onto:
    sync_reasoner_pellet(infer_property_values=True)
    dic = createDictIndividuals(properties, individuals)
    f.write('\n\n')
    f.write("Individuals After Reasoning:\n")

    for individual in dic.keys():
        f.write(individual + ':\n')
        obj = individual
        for relation in dic[obj]:
            predict = relation[0]
            subj = relation[1]
            f.write('\t' + predict + ' ' + subj + '\n')
        f.write('\n')
f.close()
