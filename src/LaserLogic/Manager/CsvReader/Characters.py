import csv
import os

class Characters:

    @staticmethod
    def get_brawlers_id():
        BrawlersID = []

        base_path = os.path.dirname(__file__)
        csv_path = os.path.join(base_path, "../../../LaserData/Assets/csv_logic/characters.csv")
        csv_path = os.path.abspath(csv_path)

        with open(csv_path, newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count < 2:
                    line_count += 1
                    continue
                if row[20] == 'Hero' and row[2].lower() != 'true' and row[1].lower() != 'true':
                    BrawlersID.append(line_count - 2)
                line_count += 1

        return BrawlersID

    def get_brawler_by_skin_id(self, skin_id):
        base_path = os.path.dirname(__file__)

        # characskinsters.csv dosyası
        skin_csv = os.path.abspath(os.path.join(base_path, "../../../LaserData/Assets/csv_logic/characskinsters.csv"))
        with open(skin_csv, newline='', encoding='utf-8') as skins_file:
            csv_reader = csv.reader(skins_file)
            line_count = 0

            for row in csv_reader:
                if line_count < 2:
                    line_count += 1
                    continue

                if line_count == skin_id + 2:
                    conf = row[1]
                    break
                line_count += 1
            else:
                return None  # bulunamadı

        # skin_confs.csv dosyası
        skin_conf_csv = os.path.abspath(os.path.join(base_path, "../../../LaserData/Assets/csv_logic/skin_confs.csv"))
        with open(skin_conf_csv, newline='', encoding='utf-8') as sconf_file:
            csv_reader = csv.reader(sconf_file)
            for row in csv_reader:
                if row[0] == conf:
                    brawler_conf = row[1]
                    break
            else:
                return None

        # characters.csv dosyası
        char_csv = os.path.abspath(os.path.join(base_path, "../../../LaserData/Assets/csv_logic/characters.csv"))
        with open(char_csv, newline='', encoding='utf-8') as char_file:
            csv_reader = csv.reader(char_file)
            line_count = 0
            for row in csv_reader:
                if line_count < 2:
                    line_count += 1
                    continue
                if row[0] == brawler_conf:
                    return line_count - 2
                line_count += 1

        return None
