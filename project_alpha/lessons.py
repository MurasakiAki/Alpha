class lesson():
    def __init__(self, name, shortcut, is_practical, need_theoretical):
        self.name = name
        self.shortcut = shortcut
        self.is_practical = is_practical
        self.need_theoretical = need_theoretical

    def set_teacher(self, teacher):
        self.assigned_teacher = teacher
    
    def set_classroom(self, classroom):
        self.assigned_classroom = classroom
    
    def __str__(self):
        return self.shortcut

