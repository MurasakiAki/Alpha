class teacher:
    def __init__(self, title, name, surname, name_shortcut, cabinet_floor, *professions):
        self.title = title or None
        self.name = name
        self.surname = surname
        self.name_shortcut = name_shortcut
        self.cabinet_floor = cabinet_floor
        self.professions = list(professions)
