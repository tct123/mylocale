from mylocale import TR
import locale

langcode = locale.getlocale()[0].split("_")[0]
var1 = 1
var2 = 2
var3 = var1 + var2
tr = TR(csv_file="examples/localisation.csv", langcode=langcode)
x = tr.tr(target_key="TEXTVARS", langcode=langcode).format(
    var1=var1, var2=var2, var3=var3
)
y = tr.tr(target_key="TEXTVARS2", langcode=langcode).format(
    var1=var1, var2=var2, var3=var3
)
print(x)
print("Right to left: {rtl_support}".format(rtl_support=tr.check_rtl()))
