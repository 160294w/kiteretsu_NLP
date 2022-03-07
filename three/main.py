import csv
np_dic = {}
fp = open("pn.csv", "rt", encoding="utf-8")
reader = csv.reader(fp, delimiter='\t')
for i, row in enumerate(reader):
    name = row[0]
    result = row[1]
    np_dic[name] = result
    if i % 1000 == 0: print(i)
print("OK")

print(np_dic["激怒"])
print(np_dic["苦情"])
print(np_dic["糞"])
print(np_dic["喜び"])
print(np_dic["勝利"])
print(np_dic["上品"])
print(np_dic["商品"])
print(np_dic["奔走"])
print(np_dic["時間"])

