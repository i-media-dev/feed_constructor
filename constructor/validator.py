from constructor.exceptions import RequiredFieldsError


class Validator:

    def __init__(self, required_fields: tuple[str]):
        self.required_fields = required_fields

    def _get_by_path(self, data, path: str):
        parts = path.replace('[]', '').split('.')
        value = data

        for part in parts:
            if isinstance(value, list):
                if not value:
                    return None
                value = value[0]

            if not isinstance(value, dict):
                return None

            value = value.get(part)
            if value in (None, '', [], {}):
                return None

        return value

    def validate(self, data: dict):
        missing = []

        for path in self.required_fields:
            if self._get_by_path(data, path) is None:
                missing.append(path)

        if missing:
            raise RequiredFieldsError(
                f'Отсутствуют обязательные поля: {", ".join(missing)}'
            )
