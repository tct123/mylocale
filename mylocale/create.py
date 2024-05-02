import click

@click.command()
def create():
    string = "stringname,en_EN\nHELLOWORLD,Hello World"
    with open(file="localisation.csv", mode="w") as f:
        f.write(string)

if __name__=="__main__":
    create()
