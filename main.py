class StudingError(Exception):
    def __str__(self):
        return f"Стільки часу за день ви можете вчитися "
def check_study(amount_of_study, limit_value):
    if amount_of_studyl>limit_value:
        return "Ви забагато навчаєтесь!"
    else:
        raise StudingError(amount_of_studytime)
studytime=180
check_studytime(studytime,240)