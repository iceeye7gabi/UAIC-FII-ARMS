import csv
import random
from operator import itemgetter

anilist_file = open('data.csv', encoding='utf-8')
#anilist_file = open('3000Brrr.csv', encoding='utf-8')
type(anilist_file)

csvreader = csv.reader(anilist_file)


genre = input("Introduceti tipul de anime: ")
random_pick_count = int(input("Introduceti numarul de anime-uri dorite: "))
genre = genre.split(",")

rows = []
for row in csvreader:
    if row:
        isGood = True
        for elem in genre:
            if elem.strip() not in row[5:]:
                isGood = False
        if isGood:
            rows.append(row)

rows = sorted(rows, key=itemgetter(2), reverse=True)

if len(rows) > random_pick_count:
    for _ in range(0,random_pick_count):
        pick = random.choice(rows)
        rows.remove(pick)
        print(pick)
else:
    for _ in rows:
        print(_)
    print(f"Numarul de anime-uri gasite dupa genul {genre}: {len(rows)}")
