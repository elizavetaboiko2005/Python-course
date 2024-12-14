# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Table:
    def __init__(self, материал: str, высота: float, вес: float):
        if материал not in ["дерево", "камень", "пластик"]:
            raise ValueError("Материал должен быть одним из: дерево, камень, пластик.")
        if высота <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        if вес <= 0:
            raise ValueError("Вес должен быть положительным числом.")

        self.материал = материал
        self.высота = высота
        self.вес = вес

    def put_item(self, предмет: str) -> None:
        """
        Добавляет предмет на стол.

        :param предмет: Название предмета, который нужно добавить.

        >>> table = Table("дерево", 1.0, 10.0)
        >>> table.put_item("Книга")
        ...
        """
        ...

    def take_item(self, предмет: str) -> None:
        """
        Убирает предмет со стола.

        :param предмет: Название предмета, который нужно убрать.

        >>> table = Table("дерево", 1.0, 10.0)
        >>> table.take_item("Книга")
        ...
        """
        ...

class Tree:
    def __init__(self, высота: float, возраст_дерева: int):
        if высота <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        if возраст_дерева < 0:
            raise ValueError("Возраст дерева не может быть отрицательным числом.")

        self.высота = высота
        self.возраст_дерева = возраст_дерева

    def increase_age(self, годы: int) -> None:
        """
        Увеличивает возраст дерева.

        :param годы: Количество лет, на которые нужно увеличить возраст.

        >>> tree = Tree(5.0, 10)
        >>> tree.increase_age(2)
        ...
        """
        ...

    def cut_tree(self) -> str:
        """
        Срубает дерево и возвращает его тип.

        :return: Тип дерева.

        >>> tree = Tree(5.0, 10)
        >>> tree.cut_tree()
        ...
        """
        ...

class SocialNetwork:
    def __init__(self, название: str, пользователи: int):
        if not название:
            raise ValueError("Название сети не может быть пустым.")
        if пользователи < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")

        self.название = название
        self.пользователи = пользователи

    def add_user(self, имя: str) -> None:
        """
        Добавляет пользователя в сеть.

        :param имя: Имя пользователя, которого нужно добавить.

        >>> social_network = SocialNetwork("Фейсбук", 100)
        >>> social_network.add_user("Иван")
        ...
        """
        ...

    def delete_user(self, имя: str) -> None:
        """
        Удаляет пользователя из сети.

        :param имя: Имя пользователя, которого нужно удалить.

        >>> social_network = SocialNetwork("Фейсбук", 100)
        >>> social_network.delete_user("Иван")
        ...
        """
        ...

if __name__ == "__main__":
    doctest.testmod() # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
