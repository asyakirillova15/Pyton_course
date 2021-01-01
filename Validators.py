class IntValidator:
    _filtered_value = None
    _raw_value = None
    _handleNegatives = False

    def __init__(self, hint, is_negative=False):
        self._handleNegatives = is_negative
        while True:
            try:
                self._raw_value = input(hint)
                self._filter()
                break
            except ValueError:
                print('Неверное значение, повторите ввод')

    def get_value(self):
        if self._filtered_value is not None:
            return self._filtered_value
        raise ValueError("Не задано значение")

    def _filter(self):
        self._filtered_value = int(self._raw_value)
        if self._handleNegatives and self._filtered_value < 0:
            raise ValueError


class FloatValidator(IntValidator):
    def _filter(self):
        self._filtered_value = float(self._raw_value)
        if self._handleNegatives and self._filtered_value < 0:
            raise ValueError


class NotEmptyValidator(IntValidator):
    def _filter(self):
        if self._raw_value != '':
            self._filtered_value = self._raw_value
        else:
            raise ValueError
