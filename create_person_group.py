import cognitive_face as CF
from global_variables import personGroupId
import sys

Key = '1cb27881e27d42628ab2d61fcc5b14b2'
CF.Key.set(Key)

personGroups = CF.person_group.lists()
for personGroup in personGroups:
    if personGroupId == personGroup['personGroupId']:
        print personGroupId + " already exists."
        sys.exit()

res = CF.person_group.create(personGroupId)
print res
