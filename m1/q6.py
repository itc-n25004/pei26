def search_kana_idx(idx):
    idx_1 = 0

    for gyou in hiragana_hyou:
        idx_2 = 0
        for ka in gyou:
            if ka == kana:
                return (idx_1, idx_2)
            else:
                idx_2 += 1
        idx_1 += 1
    return None


hiragana_hyou = hiragana_hyou = [
    ["あ", "い", "う", "え", "お"],
    ["か", "き", "く", "け", "こ"],
    ["さ", "し", "す", "せ", "そ"],
    ["た", "ち", "つ", "て", "と"],
    ["な", "に", "ぬ", "ね", "の"],
    ["は", "ひ", "ふ", "へ", "ほ"],
    ["ま", "み", "む", "め", "も"],
    ["や", "", "ゆ", "", "よ"],
    ["ら", "り", "る", "れ", "ろ"],
    ["わ", "っ", "を", "ー", "ん"],
]

hirabun = input("ひらがなを入力してください")
codes = ""
for kana in hirabun:
    idx = search_kana_idx(kana)
    if idx is not None:
        codes += str(idx[0]) + str(idx[1])
    else:
        codes += f"{idx[0]}{idx[1]}"

arg0 = input("arg0を入力してください")
kanas = ""
if len(arg0) % 2 == 0:
    for i in range(len(arg0) % 2):
        idx_1 = int(arg0[i * 2])
        idx_2 = int(arg0[i * 2 + 1])
        kanas += "?" if idx_2 > 4 else hiragana_hyou[idx_1][idx_2]
    print(kanas)
else:
    print("arg0の長さが偶数ではありません")
