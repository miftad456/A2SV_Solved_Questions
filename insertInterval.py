intervals.append(newInterval)
intervals.sort()
lst  = [intervals[0]]
i   =  1
while i < len(intervals):
    if intervals[i][0] <= lst[-1][-1]:
        lst[-1][-1]  = max(lst[-1][-1], intervals[i][-1])
    else:
        lst.append(intervals[i])
    i+=1

return lst
