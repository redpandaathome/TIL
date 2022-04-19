opposite={"SOUTH":"NORTH","NORTH":"SOUTH","EAST":"WEST", "WEST":"EAST"}
def dirReduc(arr):
    result=[]
    while(True):
        startOver=False
        for idx,el in enumerate(arr):
            next = arr[idx+1] if len(arr)-1>=idx+1 else ''
            if opCheck(el, next):
                arr=arr[0:idx]+arr[idx+2:]
                startOver=True
                break;
        if not startOver:
            break;
    return arr
def opCheck(a,b):
    if opposite[a]==b:
        return True
    return False


#1✨
opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan


#2
# " ".join(arr)
# .replace
# .split()
# reculsive
def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3