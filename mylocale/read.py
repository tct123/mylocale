import csv


def read(
    fp: str, stringname: str, locale: str, variables: list = []
):  # fp for path to translationfile, locale for wanted locale and variables for eventual variables
    output = "testoutput"
    fields = []
    rows = []
    with open(file=fp, newline="", encoding="utf-8", mode="r") as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
        for field in fields:
            if field == stringname:
                output = f"field index: {field}, {fields.index(field)}"
                return output

    # output = row


if __name__ == "__main__":
    print(read(fp="localisation.csv", stringname="HELLOWORLD", locale="en_EN"))
