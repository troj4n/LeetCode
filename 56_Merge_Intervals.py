from collections import deque
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        def merge_graph(intervals,visited,i):
            #print ("-----")
            q=deque()
            q.append((intervals[i][0],intervals[i][1]))
            visited.add(i)
            temp_result=[]
            #temp_result.append(intervals[i][0])
            start_lim=sys.maxsize
            end_lim=-sys.maxsize
            while q:
                #print (q)
                left,right=q.popleft()
                start_lim=min(start_lim,left)
                end_lim=max(end_lim,right)
                for j in range(len(intervals)):
                    if j not in visited and right>=intervals[j][0] and left<=intervals[j][1]:
                        visited.add(j)
                        q.append((intervals[j][0],intervals[j][1]))
            temp_result.append(start_lim)
            temp_result.append(end_lim)
            return (temp_result)
        n=len(intervals)
        visited=[0]*(n+1)
        #intervals.sort()
        merged_intervals=[]
        visited=set()
        for i in range(n):
            if i not in visited:
                merged_intervals.append(merge_graph(intervals,visited,i))
        return (merged_intervals)
