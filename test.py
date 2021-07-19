block_size = {"width": 0.3, "height": 0.2, "length": 0.6}

wall_height = 3
wall_length = 10
print(
    "Общая длина 1 стены:",
    wall_length,
    "\nКоличество блоков на 1 ряд:",
    wall_length / block_size["length"],
    "\nРядов нужно:",
    wall_height / block_size["height"],
    "\nБлоков на 1 стену:",
    ((wall_length / block_size["length"]) * (wall_height / block_size["height"])) * 2,
    "\nСредняя цена блока:",
    80,
    "\nЦена за стену:",
    80
    * ((wall_length / block_size["length"]) * (wall_height / block_size["height"]))
    * 2,
)
