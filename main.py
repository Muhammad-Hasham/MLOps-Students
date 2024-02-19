# main.py
class StudentsInMLOps:
    def __init__(self):
        self.total_strength = 0
        self.class_name = "MLOps"

    def enrollStudents(self, count):
        self.total_strength += count

    def dropStudents(self, count):
        self.total_strength -= count

    def getTotalStrength(self):
        return self.total_strength

    def getClassName(self):
        return self.class_name
