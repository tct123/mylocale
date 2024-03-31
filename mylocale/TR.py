import csv


def tr(csv_file, target_key, langcode):
    f = open(csv_file, newline="")
    locale_csv = csv.DictReader(f=f, delimiter=",")
    for item in locale_csv:
        if item["stringname"] == target_key:
            try:
                if item[langcode] == "":
                    return item["en_EN"]
                else:
                    return item[langcode]
            except:
                return item["en_EN"]
