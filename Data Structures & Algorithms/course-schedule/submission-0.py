from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs_left = [set() for _ in range(numCourses)]
        follow_ups = [[] for _ in range(numCourses)]
        for course, preq in prerequisites:
            prereqs_left[course].add(preq)
            follow_ups[preq].append(course)
        
        taken = set()
        q = deque()
        for course, prereqs in enumerate(prereqs_left):
            if len(prereqs) == 0:
                q.append(course)
                taken.add(course)
        
        while q:
            course = q.popleft()

            for next_course in follow_ups[course]:
                if next_course in taken:
                    continue
                
                for prereq in tuple(prereqs_left[next_course]):
                    if prereq in taken:
                        prereqs_left[next_course].remove(prereq)
                if len(prereqs_left[next_course]) == 0:
                    q.append(next_course)
                    taken.add(next_course)
        
        return len(taken) == numCourses


