import copy
import sys

TOTAL_DISKS = 5  # Чем больше дисков тем сложнее головоломка

# Изначально все диски находятся на стержне А:
SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))

def main():
    """ Проводит одну игру Ханойская башня """
    print(
        """THE TOWER OF HANOI, by Al Sweigart al@inventwithpython.com
        
        Move the tower of dicks, one disk at a time, to another tower. Large
        disks connot rest on top of a smaller disk.
        
        More info at htpps://en.wikipedia.org/wiki/Towel_of_Hanoi
        """
    )

    """Словарь towers содержит ключи "A", "B" и "C", и значения - списки,
    предсталяющие стопку дисков. Список содержит целые числа, предсавляющие
    диски разных размеров, а начало списка представляет низ башни. Для игры
    с 5 дисками список [5,4,3,2,1] представляет заполненную башню. Пустой
    список list [] представляет башню без дисков. В списке [1, 3] большой диск
    находится на меньшем диске, такая конфигурация не допустима. Список [3, 1]
    допустим, так как меньшие диски могут размещаться на больших."""

    towers = {"A": copy.copy(SOLVED_TOWER), "B": [], "C": []}

    while True:  # Один ход для каждой итерации цикла.
        # Вывести башни и диски
        displayTowers(towers)

        # Запросить ход у пользователя
        fromTower, toTower = getPlayerMove(towers)

        # Переместить верхний диск с fromTower на to Tower:
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        # Проверить, решена ли головоломка
        if SOLVED_TOWER in (towers["B"], towers["C"]):
            displayTowers(towers) # Вывести башни в последний раз
            print("You have solved the puzzle! Well done!")
            sys.exit


def getPlayerMove(towers):
    """Запрашивает ход у пользователяю Возвращает fromTower, toTower"""

    while True:  # Пока пользователь не введет допустимый ход.
        print('Enter the letters of "from" and "to" towers, or QUIT.')
        print("(e.g., AB to moves a disk from tower A to tower B.)")
        print()
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        # Убедится в том, что пользователь ввел допустирое обозначение башен:
        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("Enter one of AB, AC, BA, BC, CA or CB")
            continue  # Снова запросить ход.
        
        # Более содержательные имена переменных:
        fromTower, toTower = response[0], response[1]

        if len(towers[fromTower]) == 0:
            # Башня fromTower не может быть пустой:
            print("You selected a tower with no disks.")
            continue

        elif len(towers[toTower]) == 0:
            # На пустую башню можно переместить любой диск.
            return fromTower, toTower

        elif towers[toTower][-1] < towers[fromTower][-1]:
            print("Can't put larger disks on top of smaller ones.")
            continue

        else:
            # Допустимый ход, вернуть выбранные башни:
            return fromTower, toTower

def displayTowers(towers):
    """ Выводит три башни с дисками """


    # Вывести три башни:
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                displayDisk(0)  # Вывести пустой стержень без диска
            else:
                displayDisk(tower[level])  # Вывести диск
        print()
    
    # вывести обозначение башен A, B и С:
    emptySpace = " " * (TOTAL_DISKS)
    print("{0}A{0}{0}B{0}{0}C\n".format(emptySpace))

def displayDisk(width):
    """ Вывлодит диск заданной ширины, Ширина 0 означает отсудствие диска."""
    emptySpace = " " * (TOTAL_DISKS - width)


    if width == 0:
        print(f"{emptySpace}||{emptySpace}", end="")
    else:
        disk = "@" * width
        numLabel = str(width).rjust(2, "_")
        print(f"{emptySpace}{disk}{numLabel}{disk}{emptySpace}", end="")

if __name__ == "__main__":
    main()
