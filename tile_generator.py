import random
from enum import Enum
from typing import List


class WallType(Enum):
    WALL = 0
    DOOR = 1


class Tile:
    n: WallType
    s: WallType
    e: WallType
    w: WallType

    def __init__(self, n: WallType, s: WallType, e: WallType, w: WallType):
        for var in [n, s, e, w]:
            if var not in WallType:
                raise Exception("Undefined WallType.")
        self.n = n
        self.s = s
        self.e = e
        self.w = w


class Dungeon:
    __map: List[List[Tile]]

    def __init__(self, border_x, border_y):
        self.__map = []  # create empty map of dungeon
        self.border_x = border_x
        self.border_y = border_y

    def add_tile(self, tile: Tile):
        tile = self.__add_borders(tile)  # add borders to dungeon
        self.__map[-1].append(tile)  # add new tile to current row

    def __add_borders(self, tile: Tile):
        if len(self.__map) == 1:  # when current tile is first row
            tile.n = WallType.WALL
        if len(self.__map) == self.border_y:  # when current tile is last row
            tile.s = WallType.WALL

        if len(self.__map[-1]) == 0:  # when current tile in current row is first column
            tile.w = WallType.WALL
        if len(self.__map[-1]) == self.border_x - 1:  # when current tile in current row is last column
            tile.e = WallType.WALL
        return tile

    def add_row(self):
        self.__map.append([])  # create new row

    def generate_random(self):  # create grid of tiles with random WallTypes
        for row in range(self.border_y):
            self.add_row()
            for col in range(self.border_x):
                args = []
                for _ in range(4):
                    # args.append(WallType.DOOR)
                    args.append(random.choice(list(WallType)))
                tile = Tile(*args)
                self.add_tile(tile)
        return self.__map


class UglyPrinter:  # ugly way of implementing visualisation of dungeon
    tile_map: List[List[Tile]]

    def __init__(self, tile_map):
        self.tile_map = tile_map

    def print(self):
        i = 0
        for row in self.tile_map:
            top_string = ""
            mid_string = ""
            low_string = ""
            for tile in row:
                #  get ascii chars for walls
                left = self.ascii_e_w(tile.w)
                right = self.ascii_e_w(tile.e)
                up = self.ascii_n(tile.n)
                down = self.ascii_s(tile.s)

                i += 1
                top_string += f"  {up}{up}   "
                mid_string += f" {left}{str(i).zfill(2)}{right}  "
                low_string += f"  {down}{down}   "
            print(top_string)
            print(mid_string)
            print(low_string)

    @staticmethod
    def ascii_e_w(wall_type: WallType):
        if wall_type == WallType.WALL:
            return "|"
        return ":"

    @staticmethod
    def ascii_n(wall_type: WallType):
        if wall_type == WallType.WALL:
            return "_"
        return "."

    @staticmethod
    def ascii_s(wall_type: WallType):
        if wall_type == WallType.WALL:
            return "‾"
        return "'"


def main():
    dungeon = Dungeon(5, 5)
    tile_map = dungeon.generate_random()
    UglyPrinter(tile_map).print()

    print("Done")


if __name__ == "__main__":
    main()
