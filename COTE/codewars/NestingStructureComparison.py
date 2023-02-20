def same_structure_as(original,other):
    if not isinstance(original,list) or not isinstance(other,list):
        return False
    
    if len(original)==len(other):
        for el,other in zip(original, other):
            if isinstance(el, list) and isinstance(other, list):
                return same_structure_as(el, other)
            elif isinstance(el, list)!=isinstance(other, list):
                return False
        return True
    else:
        return False


#
def same_structure_as(original,other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2): return False
        else: return True
    else: return not isinstance(original, list) and not isinstance(other, list)