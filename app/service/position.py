from math import floor

from app.schemas import Header, Geo


def get_coord_byte_position(h: Header, g: Geo):
    lat_mul = g.lat * h.multiplier
    lon_mul = g.lon * h.multiplier

    if not (h.min_y <= lat_mul <= h.max_y and h.min_x <= lon_mul <= h.max_x):
        raise ValueError("Provided coordinates are out of bounds")

    # Вычисление размерности сетки
    num_rows = floor((h.max_y - h.min_y) / h.dy) + 1
    num_columns = floor((h.max_x - h.min_x) / h.dx) + 1

    # Вычисление позиции значения в плоском массиве
    target_row = floor((lat_mul - h.min_y) / h.dy)
    target_column = floor((lon_mul - h.min_x) / h.dx)

    target_position = target_row * num_columns + target_column

    # Вычисление позиции байта в файле
    header_size = 8 * 4  # Размер заголовка в байтах
    byte_position = header_size + target_position * 4

    return byte_position, num_columns * 4
