from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        is_touched = True
        while is_touched:
            is_touched = False
            for _ in range(len(students)):
                student = students.popleft()
                sandwich = sandwiches.popleft()
                if student == sandwich:
                    is_touched = True
                else:
                    students.append(student)
                    sandwiches.appendleft(sandwich)
        return len(sandwiches)


        