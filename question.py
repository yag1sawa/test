age = input("あなたは何歳ですか？")

with open("/Users/yagisawayuji/practice/first.txt", "w", encoding="utf8") as f:
    f.write(age)

with open("/Users/yagisawayuji/practice/first.txt", "r", encoding="utf8") as f:
    print(f.read())