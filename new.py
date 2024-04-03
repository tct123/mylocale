from mylocale.TR import tr

var1 = 1
var2 = 2
var3 = var1 + var2
print(
    tr(
        csv_file="examples/localisation.csv",
        target_key="TEXTVARS",
        varnames=["VAR1", "VAR2", "VAR3"],
        vars=[var1, var2, var3],
    )
)
