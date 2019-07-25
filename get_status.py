import cognitive_face as CF
from global_variables import personGroupId

Key = '1cb27881e27d42628ab2d61fcc5b14b2'
CF.Key.set(Key)

res = CF.person_group.get_status(personGroupId)
print res
