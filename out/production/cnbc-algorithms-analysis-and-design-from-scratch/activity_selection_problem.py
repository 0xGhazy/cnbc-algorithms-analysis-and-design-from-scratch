from typing import List

def greedy_select_activities(activities: List[tuple]) -> List[int]:
    """
    Function that select activities using a greedy approach
    this function runs in O(n) time complexity.
    
    parameters:
        activities: list of activities, each activity is a tuple that contains start and end time.
    
    returns:
        result: list of valid activities indexes
    """
    result = [0]
    # init the 
    i, j = 1, 0
    while i < len(activities):
        # 0 for start time and 1 for end time
        if activities[i][0] >= activities[j][1]:
            result.append(i)
        j = i
        i += 1
    return result


# eash activity tuple is (start, end) time.
activities = [(9,11), (10,11), (11,12), (12,14), (13,15), (15,16)]
print(greedy_select_activities(activities))
