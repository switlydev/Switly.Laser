import csv
import os

class Skins:
    @staticmethod
    def get_skins_id():
        SkinsID = []

        # Dosya yolu: src/LaserData/Assets/csv_logic/skins.csv
        base_path = os.path.dirname(__file__)
        csv_path = os.path.abspath(os.path.join(base_path, "../../../LaserData/Assets/csv_logic/skins.csv"))

        # Dosyayı güvenli şekilde aç ve işle
        with open(csv_path, newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            for index, row in enumerate(csv_reader):
                if index < 2:
                    continue
                SkinsID.append(index - 2)

        return SkinsID
