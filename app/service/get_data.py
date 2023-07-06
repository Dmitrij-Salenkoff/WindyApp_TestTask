import asyncio
import struct
from _decimal import Decimal

import aiofiles

from app.schemas import Geo
from app.service.position import get_coord_byte_position
from app.service.utils import find_relevant_timestamps
from app.config.default import settings

from app.schemas import Header

DATA_DIR_PATH = settings.DATA_DIR_PATH
HEADER_SIZE = settings.HEADER_SIZE


async def get_data(from_ts: int, to_ts: int, g: Geo):
    file_names = find_relevant_timestamps(DATA_DIR_PATH, from_ts, to_ts)
    tasks = [get_temp(DATA_DIR_PATH + file_name, g) for file_name in file_names]
    temps = await asyncio.gather(*tasks)
    data = {file_name[:-5]: {"temp": temp} for file_name, temp in zip(file_names, temps)}
    return data


async def get_temp(file_path: str, g: Geo) -> Decimal | None:
    async with aiofiles.open(file_path, "rb") as file:
        bytes_data = await file.read(HEADER_SIZE)
        header_values = Header(*struct.unpack("<7lf", bytes_data))
        try:
            target_position, next_row_byte = get_coord_byte_position(header_values, g)
        except ValueError:
            return
        await file.seek(target_position)
        bytes_temp = await file.read(4)
        temp = struct.unpack("f", bytes_temp)[0]
        if temp == header_values.empty_value:
            return
        return temp
