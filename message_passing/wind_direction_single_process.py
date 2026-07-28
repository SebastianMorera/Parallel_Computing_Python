import os

import re
from os.path import join

import time

WIND_REGEX = "\d* METAR.*EGLL \d*Z [A-Z ]*(\d{5}KT|VRB\d{2}KT).*="
WIND_EX_REGEX = "(\d{5}KT|VRB\d{2}KT)"
VARIABLE_WIND_REGEX = ".*VRB\d{2}KT"
VALID_WIND_REGEX = "\d{5}KT"
WIND_DIR_ONLY_REGEX = "(\d{3})\d{2}KT"
TAF_REGEX = ".*TAF.*"
COMMENT_REGEX = "\w*#.*"
METAR_CLOSE_REGEX = ".*="


def parse_to_array(text):
    lines = text.splitlines()
    metar_str = ""
    metars = []
    for line in lines:
        if re.search(TAF_REGEX, line):
            break
        if not re.search(COMMENT_REGEX, line):
            metar_str += line.strip()
        if re.search(METAR_CLOSE_REGEX, line):
            metars.append(metar_str)
            metar_str = ""
    return metars


def extract_wind_direction(metars):
    winds = []
    for metar in metars:
        if re.search(WIND_REGEX, metar):
            for token in metar.split():
                if re.match(WIND_EX_REGEX, token):
                    winds.append(re.match(WIND_EX_REGEX, token).group(1))
    return winds


def mine_wind_distribution(winds, wind_d):
    for wind in winds:
        if re.search(VARIABLE_WIND_REGEX, wind):
            for i in range(8):
                wind_d[i] += 1
        elif re.search(VALID_WIND_REGEX, wind):
            d = int(re.match(WIND_DIR_ONLY_REGEX, wind).group(1))
            dir_index = round(d / 45.0) % 8
            wind_d[dir_index] += 1
    return wind_d


if __name__ == "__main__":
    path_to_files = "../message_passing/metarfiles"
    wind_dist = [0] * 8
    start = time.time()
    for file in os.listdir(path_to_files):
        with open(join(path_to_files, file), "r") as f:
            metars = parse_to_array(f.read())
            winds = extract_wind_direction(metars)
            wind_dist = mine_wind_distribution(winds, wind_dist)

    end = time.time()
    print(f"Done, time taken = {end - start}")
    print(wind_dist)
