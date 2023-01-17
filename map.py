import csv


class DungeonMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [
            [
                {"type": "floor", "locked": False, "x": x, "y": y}
                for x in range(width)
            ]
            for y in range(height)
        ]

    def set_cell(self, x, y, cell_type, locked=False):
        self.grid[y][x] = {"type": cell_type, "locked": locked, "x": x, "y": y}

    def is_passable(self, x, y):
        cell = self.grid[y][x]
        if cell["type"] == "floor":
            return True
        elif cell["type"] == "door" and not cell["locked"]:
            return True
        else:
            return False

    def output_section(self, start_x, start_y, end_x, end_y, options={}):
        section = ""
        floor = options.get("floor", " ")
        wall = options.get("wall", "█")
        door = options.get("door", "O")
        for y in range(start_y, end_y + 1):
            for x in range(start_x, end_x + 1):
                cell = self.grid[y][x]
                if cell["type"] == "floor":
                    section += floor
                elif cell["type"] == "wall":
                    section += wall
                elif cell["type"] == "door":
                    section += door
            section += "\n"
        return section

    def parse_csv(self, file_path):
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for y, row in enumerate(reader):
                for x, cell_type in enumerate(row):
                    if cell_type == "floor":
                        self.set_cell(x, y, "floor")
                    elif cell_type == "wall":
                        self.set_cell(x, y, "wall")
                    elif cell_type == "door":
                        self.set_cell(x, y, "door", locked=True)
