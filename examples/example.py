from mylocale import TR
import locale

langcode = locale.getlocale()[0].split("_")[0]
csv_file = "examples/localisation.csv"
target_key = "HELLOWORLD"
print(tr(csv_file=csv_file, target_key=target_key, langcode=langcode))
