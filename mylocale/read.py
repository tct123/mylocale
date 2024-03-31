import csv


def read(
    filepath: str, stringname: str, locale: str, variables: list = []
):  
    with open(file=filepath, newline="", encoding="utf-8") as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=",")



if __name__ == "__main__":
    print(read(filepath="localisation.csv", stringname="stringname", locale="de_de"))
