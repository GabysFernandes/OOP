class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def to_file_line(self):
        return f"{self.student_id} | {self.name} | {self.course}"

    @classmethod
    def from_file_line(cls,line):
        parts = line.strip().split("|")

        if len(parts) != 3:
            return None

        student_id = parts[0].strip()
        name = parts[1].strip()
        course = parts[2].strip()

        if not student_id or not name or not course:
            return None
        return cls(student_id, name, course)

    def __str__(self):
        return f"{self.student_id}: {self.name} | ({self.course})"