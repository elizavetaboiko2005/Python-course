if __name__ == "__main__":
    # Write your solution here
    class SocialNetwork:
        """Базовый класс для социальных сетей."""

        def __init__(self, name: str, users_count: int) -> None:
            """Инициализация атрибутов социальной сети."""
            self.__name = name  # название социальной сети (инкапсулированный атрибут)
            self.__users_count = users_count  # количество пользователей (инкапсулированный атрибут)

        def __str__(self) -> str:
            """Возвращает строковое представление социальной сети."""
            return f"{self.__name} с {self.__users_count} пользователей"

        def __repr__(self) -> str:
            """Возвращает формальное представление социальной сети."""
            return f"SocialNetwork(name='{self.__name}', users_count={self.__users_count})"

        def add_user(self) -> None:
            """Добавляет пользователя в социальную сеть."""
            self.__users_count += 1


    class VK(SocialNetwork):
        """Дочерний класс для социальной сети ВКонтакте."""

        def __init__(self, users_count: int, groups_count: int) -> None:
            """Инициализация атрибутов ВКонтакте."""
            super().__init__("VK", users_count)  # вызываем конструктор базового класса
            self.__groups_count = groups_count  # количество групп (инкапсулированный атрибут)

        def __str__(self) -> str:
            """Возвращает строковое представление ВКонтакте."""
            return f"{super().__str__()} и {self.__groups_count} групп"

        def __repr__(self) -> str:
            """Возвращает формальное представление ВКонтакте."""
            return f"VK(users_count={self._SocialNetwork__users_count}, groups_count={self.__groups_count})"

        def add_user(self) -> None:
            """Добавляет пользователя в ВКонтакте и выводит сообщение о добавлении."""
            super().add_user()  # вызываем метод родительского класса для увеличения счетчика пользователей
            print("Пользователь добавлен в ВКонтакте.")


    # Пример использования классов
    if __name__ == "__main__":
        social_network = SocialNetwork("Facebook", 200000)
        print(social_network)  # вывод: Facebook с 200000 пользователей
        print(repr(social_network))  # вывод: SocialNetwork(name='Facebook', users_count=200000)

        vk = VK(100000, 5000)
        print(vk)  # вывод: VK с 100000 пользователей и 5000 групп
        print(repr(vk))  # вывод: VK(users_count=100000, groups_count=5000)
        vk.add_user()  # вывод: Пользователь добавлен в ВКонтакте.
        print(vk)  # вывод: VK с 100001 пользователей и 5000 групп
    pass
