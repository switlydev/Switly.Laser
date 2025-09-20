import csv
import os

class Cards:
    @staticmethod
    def get_spg_id():
        CardSkillsID = []
        base_path = os.path.dirname(__file__)
        csv_path = os.path.abspath(os.path.join(base_path, "../../../LaserData/Assets/csv_logic/cards.csv"))

        with open(csv_path, newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for index, row in enumerate(csv_reader):
                if index < 2:
                    continue
                if row[5] in ('4', '5'):  # zaten string
                    CardSkillsID.append(index - 2)

        return CardSkillsID

    def get_spg_by_brawler_id(self, brawler_id: int, type: int):
        base_path = os.path.dirname(__file__)
        char_path = os.path.abspath(os.path.join(base_path, "../../../LaserData/Assets/csv_logic/characters.csv"))
        cards_path = os.path.abspath(os.path.join(base_path, "../../../LaserData/Assets/csv_logic/cards.csv"))

        with open(char_path, newline='', encoding='utf-8') as char_file:
            char_reader = csv.reader(char_file)
            for index, row in enumerate(char_reader):
                if index < 2:
                    continue
                if index == brawler_id + 2:
                    name = row[0]
                    break
            else:
                return None

        with open(cards_path, newline='', encoding='utf-8') as cards_file:
            cards_reader = csv.reader(cards_file)
            for index, row in enumerate(cards_reader):
                if index < 2:
                    continue
                if row[5] == str(type) and row[3] == name:
                    return index - 2

        return None

    def get_unlocked_spg(self, brawler_id: int):
        base_path = os.path.dirname(__file__)
        char_path = os.path.abspath(os.path.join(base_path, "../../../LaserData/Assets/csv_logic/characters.csv"))
        cards_path = os.path.abspath(os.path.join(base_path, "../../../LaserData/Assets/csv_logic/cards.csv"))
        result_ids = []

        with open(char_path, newline='', encoding='utf-8') as char_file:
            char_reader = csv.reader(char_file)
            for index, row in enumerate(char_reader):
                if index < 2:
                    continue
                if index == brawler_id + 2:
                    name = row[0]
                    break
            else:
                return []

        with open(cards_path, newline='', encoding='utf-8') as cards_file:
            cards_reader = csv.reader(cards_file)
            for index, row in enumerate(cards_reader):
                if index < 2:
                    continue
                if row[3] == name and row[4].lower() != "true" and row[5] in ("4", "5"):
                    result_ids.append(index - 2)

        return result_ids

    @staticmethod
    def get_brawler_unlock():
        CardUnlockID = []
        base_path = os.path.dirname(__file__)
        csv_path = os.path.abspath(os.path.join(base_path, "../../../LaserData/Assets/csv_logic/cards.csv"))

        with open(csv_path, newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            for index, row in enumerate(csv_reader):
                if index < 2:
                    continue
                if row[4] == '0':
                    CardUnlockID.append(index - 2)

        return CardUnlockID
