import csv


def read(
    fp: str, stringname: str, locale: str, variables: list = []
):  # fp for path to translationfile, locale for wanted locale and variables for eventual variables
    mylistforindex = []
    with open(file=fp, newline="", encoding="utf-8", mode="r") as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=",")
        for item in csvreader:
            mylistforindex.append(item[stringname])
            

        return mylistforindex
        



if __name__ == "__main__":
    print(read(fp="localisation.csv", stringname="stringname", locale="en_EN"))
