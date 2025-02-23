if __name__ == "__main__":
    class Vehicle:
        """
        Базовый класс для транспортных средств.
        """

        def __init__(self, make: str, model: str, year: int) -> None:
            """
            Инициализация транспортного средства.

            :param make: Производитель транспортного средства.
            :param model: Модель транспортного средства.
            :param year: Год выпуска транспортного средства.
            """
            self._make = make  # Непубличный атрибут, чтобы защитить данные о производителе
            self._model = model  # Непубличный атрибут, чтобы защитить данные о модели
            self.year = year

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта Vehicle.

            :return: Строка с информацией о транспортном средстве.
            """
            return f"Vehicle(make={self._make}, model={self._model}, year={self.year})"

        def start_engine(self) -> str:
            """
            Запускает двигатель транспортного средства.

            :return: Сообщение о запуске двигателя.
            """
            return f"The engine of {self._make} {self._model} is now running."


    class Car(Vehicle):
        """
        Класс для легковых автомобилей, наследующий от Vehicle.
        """

        def __init__(self, make: str, model: str, year: int, doors: int) -> None:
            """
            Инициализация легкового автомобиля.

            :param make: Производитель легкового автомобиля.
            :param model: Модель легкового автомобиля.
            :param year: Год выпуска легкового автомобиля.
            :param doors: Количество дверей в легковом автомобиле.
            """
            super().__init__(make, model, year)  # Вызов конструктора базового класса
            self.doors = doors  # Публичный атрибут, количество дверей

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта Car.

            :return: Строка с информацией о легковом автомобиле.
            """
            return f"Car(make={self._make}, model={self._model}, year={self.year}, doors={self.doors})"

        def start_engine(self) -> str:
            """
            Запускает двигатель легкового автомобиля.

            Переопределяет метод базового класса, чтобы добавить специфичное сообщение для легкового автомобиля.

            :return: Сообщение о запуске двигателя легкового автомобиля.
            """
            return f"The engine of the car {self._make} {self._model} is now running with a smooth sound."


    class Truck(Vehicle):
        """
        Класс для грузовых автомобилей, наследующий от Vehicle.
        """

        def __init__(self, make: str, model: str, year: int, capacity: float) -> None:
            """
            Инициализация грузового автомобиля.

            :param make: Производитель грузового автомобиля.
            :param model: Модель грузового автомобиля.
            :param year: Год выпуска грузового автомобиля.
            :param capacity: Грузоподъемность грузового автомобиля в тоннах.
            """
            super().__init__(make, model, year)  # Вызов конструктора базового класса
            self._capacity = capacity  # Непубличный атрибут, чтобы защитить данные о грузоподъемности

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта Truck.

            :return: Строка с информацией о грузовом автомобиле.
            """
            return f"Truck(make={self._make}, model={self._model}, year={self.year}, capacity={self._capacity})"

        def start_engine(self) -> str:
            """
            Запускает двигатель грузового автомобиля.

            Переопределяет метод базового класса, чтобы добавить специфичное сообщение для грузового автомобиля.

            :return: Сообщение о запуске двигателя грузового автомобиля.
            """
            return f"The engine of the truck {self._make} {self._model} is now running with a powerful roar."

    pass
