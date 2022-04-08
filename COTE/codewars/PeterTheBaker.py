#https://www.codewars.com/kata/525c65e51bf619685c000059/solutions/python
# 💖💖💖

# Infinity? math.inf
# math.floor()
# key check in dict -> key in dict
# terminary operator a if a else b
# min? not math.min but min(num, num2)
import math
def cakes(recipe, available):
    minResult = math.inf
    for el in recipe:
        temp = math.floor(available[el]//recipe[el]) if el in available and el in recipe else 0
        minResult= min(minResult, temp)
        
    return minResult

# improved
# dictionary get method... dict.get(key, ifNotExisting->val) https://www.w3schools.com/python/ref_dictionary_get.asp
def cakes(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)


# improved2
def cakes(recipe, available):
    try:
        return min([available[a]/recipe[a] for a in recipe])
    except:
        return 0