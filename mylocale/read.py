import csv
def read(fp: str, stringname: str, variables:list=[]):
    with open(file=fp, mode="r") as f:
        content = f.read()
    return content


if __name__ == "__main__":
    print(read(fp="localisation.csv",))
