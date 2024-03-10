import csv


def read(
    fp: str, stringname: str, locale: str, variables: list = []
):  # fp for path to translationfile, locale for wanted locale and variables for eventual variables
    mylist = []
    with open(file=fp, newline="", encoding="utf-8", mode="r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            mylist.append(row)
    print(mylist)


if __name__ == "__main__":
    import os
    read(fp=f"{os.getcwd()}/localisation.csv", stringname="HELLOWORLD", locale="en_EN")
