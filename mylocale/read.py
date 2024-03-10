import csv
def read(fp: str, stringname: str, locale:str, variables:list=[]): # fp for path to translationfile, locale for wanted locale and variables for eventual variables
    with open(file=fp, mode="r") as f:
        content = f.read()
    return content


if __name__ == "__main__":
    print(read(fp="localisation.csv",))
