class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        ## courses -> set of courses we want to pass
        ## done_courses -> set of courses we passed
        ##                 all courses with no prerequisites will
        ##                 be added here
        ## course_rules -> creates a relation between courses
        ##                 eg. {7: {1, 2, 3}}
        ##                 means that for course 7 we need to pass
        ##                 the courses 1, 2 and 3
        courses = set(range(1, n+1))
        done_courses = set(range(1, n+1))
        course_rules = {}
        
        for x, y in relations:
            
            ## if course has a prerequesite
            ## then it can't be taken in the first semester
            if y in done_courses:
                done_courses.remove(y)
            
            ## setup the relations
            if y in course_rules:
                course_rules[y].add(x)
            else:
                course_rules[y] = {x}
        
        
        ## this condition covers the case where
        ## we don't have any courses to take in
        ## the first semester, which means we
        ## won't be able to take any courses at all
        if not done_courses:
            return -1
        
        count_semesters = 1
        courses = courses - done_courses
        
        while courses: 
            
            next_semester = set()
            
            for cr in course_rules:
                
                ## do we have the prerequisites for cr
                ## in our set done_courses?
                if course_rules[cr].issubset(done_courses):
                    if cr in courses:
                        next_semester.add(cr)
            
            
            if not next_semester:
                break
                
            count_semesters += 1
            courses -= next_semester
            done_courses |= next_semester

        if not courses:
            return count_semesters
        else:
            return -1
