class ConverterError(Exception):
    def __init__(self, txt):
        self.txt = txt


class ValidationError(Exception):
    def __init__(self, txt):
        self.txt = txt


class DateError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date:
    def __init__(self, date):
        try:
            self.date = Date.converter(date)
            print(f"Сегодняшняя дата: {self.date}")
        except ConverterError as err:
            raise DateError(f"Ошибка конвертации: {err}")
        except ValidationError as err:
            raise DateError(f"Ошибка валидации: {err}")

    @classmethod
    def converter(cls, date):
        try:
            day, month, year = map(int, date.split('-'))
            if cls.validation(day, month, year):
                return date

        except ValueError:
            raise ConverterError("Некорректная дата")

    @staticmethod
    def validation(day, month, year):
        if 1900 < year < 2022:
            if 0 < month <= 12:
                if month == 2:
                    if year % 4 == 0:
                        if year % 100 == 0:
                            if year % 400 == 0:
                                if 0 < day <= 29:
                                    return True
                                else:
                                    raise ValidationError(f"Неверно указан день {day}")
                        if 0 < day <= 29:
                            return True
                        else:
                            raise ValidationError(f"Неверно указан день {day}")
                    else:
                        if 0 < day <= 28:
                            return True
                        else:
                            raise ValidationError(f"Неверно указан день {day}")

                elif month in [1, 3, 5, 7, 8, 10, 12]:
                    if 0 < day <= 31:
                        return True
                    else:
                        raise ValidationError(f"Неверно указан день {day}")
                elif month in [4, 6, 9, 11]:
                    if 0 < day <= 30:
                        return True
                    else:
                        raise ValidationError(f"Неверно указан день {day}")
            else:
                raise ValidationError(f"Неверно указан месяц {month}")
        else:
            raise ValidationError(f"Неверно указан год {year}")


today = Date("21-01-2021")
