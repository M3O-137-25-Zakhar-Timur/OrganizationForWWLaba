from purchase_analyzer import *
path = "data/purchases.txt"
out_path = "report/report.txt"
purchases, error  = read_purchases(path)

write_report(purchases, error, out_path)