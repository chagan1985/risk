class Country:
    def __init__(self, name: str, continent: str, bordering_countries: list[str]) -> None:
        self._name = name
        self._continent = continent
        self._bordering_countries = bordering_countries

    def get_name(self) -> str:
        return self._name