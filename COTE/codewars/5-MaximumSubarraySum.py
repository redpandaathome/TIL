def max_sequence(arr):
    local_max=0
    global_max=0
    for i in arr:
        local_max=max(i, i+local_max)
        global_max=max(global_max, local_max)
    return global_max


#
def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max