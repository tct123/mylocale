from mylocale import TR
import locale

langcode = locale.getlocale()[0].split("_")[0]
var1 = 1
var2 = 2
var3 = var1 + var2
tr = TR()
x = tr(
    csv_file="examples/localisation.csv", target_key="TEXTVARS", langcode=langcode
).format(var1=var1, var2=var2, var3=var3)
print(x)
