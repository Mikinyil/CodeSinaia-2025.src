import ast

###
# Loads a data set of mountains from the disk
# The "mountains_db.tsv" contains one mountain per line, each line containing
# several fields separated by TAB: mountain name, elevantion, country where it is located and
# the ISO3 code of that country.
# The method returns two values:
# - the map associating each country to the list of mountains it contains
# - the total count of mountains in the database
def load_mountains(mountains_file):
    mountains_map = {}
    count = 0
    with open(mountains_file, "r", encoding="utf-8-sig") as data_file:
        for line in data_file.readlines():
            line_parts = line.split("\t")
            mountain_name = line_parts[0]
            mountain_elevation = ast.literal_eval(line_parts[1]) if line_parts[1] != "NULL" else None
            country_name = line_parts[2]
            country_iso = line_parts[3]
            if not country_name in mountains_map:
                mountains_map[country_name] = []
            mountains_map[country_name].append(mountain_name)
            count += 1
    return mountains_map, count

if __name__ == "__main__":
    mountains_map, count = load_mountains("IntroToPy/mountains_db.tsv")
    print(f"Loaded {count} mountains from {len(mountains_map.keys())} countries.")
