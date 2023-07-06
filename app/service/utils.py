import os


def find_relevant_timestamps(directory: str, from_ts: int, to_ts: int) -> list[str]:
    """
    Search for timestamp that are fit in range of from_ts to to_ts
    :param directory: Path to data directory
    :param from_ts: left end of interval
    :param to_ts: right end of interval
    :return: list of file names that are fit in
    """
    res = []
    for file_name in os.listdir(directory):
        timestamp, ext = file_name.split(".")
        if ext != "wgf4":
            continue
        try:
            timestamp = int(timestamp)
        except ValueError:
            continue
        if to_ts >= timestamp >= from_ts:
            res.append(file_name)
    return res
