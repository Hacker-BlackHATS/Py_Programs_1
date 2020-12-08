from random import sample
from time import time


def test_kana(opt, kana):
    mac_ch = sample((list(kana)), k=(len(list(kana))))
    result_dict = {"correct": 0, "incorrect": 0, "total_time": 0.00, "average_time": 0.00}
    for i in range(len(mac_ch)):
        inp = ""
        if opt == "1" or opt == "4":
            start_time = time()
            inp = (input(f"{kana[mac_ch[i]]} -> ")).lower().strip()
            finish_time = time() - start_time
            result_dict["total_time"] += finish_time
        elif opt == "2" or opt == "5":
            start_time = time()
            inp = input(f"{mac_ch[i]} -> ")
            finish_time = time() - start_time
            result_dict["total_time"] += finish_time
        if (inp == mac_ch[i] and (opt == "1" or opt == "4")) or (
                inp == kana[mac_ch[i]] and (opt == "2" or opt == "5")):
            result_dict["correct"] += 1
        elif (inp != mac_ch[i] and (opt == "1" or opt == "4")) or (
                inp != kana[mac_ch[i]] and (opt == "2" or opt == "5")):
            result_dict["incorrect"] += 1
        if len(kana) > 1:
            result_dict["average_time"] = result_dict["total_time"] / len(kana)
        elif len(kana) == 1:
            result_dict["average_time"] = result_dict["total_time"]
    return result_dict


def results(r):
    print("Your result ::")
    print(f'Correct answers = {r["correct"]}')
    print(f'Incorrect answers = {r["incorrect"]}')
    print(f'Total Time Taken = {r["total_time"]} seconds')
    print(f'Average Time Taken = {r["average_time"]} seconds')


def word_check(word_dict):
    mac_ch = sample((list(word_dict.keys())), k=(len(word_dict.keys())))
    result_dict = {"correct": 0, "incorrect": 0, "total_time": 0.00, "average_time": 0.00}
    for i in range(len(mac_ch)):
        print(f"{mac_ch[i]}")
        start_time = time()
        inp_rom = (input(f"\tIN RŌMAJI -> ")).lower().strip()
        inp_eng = (input(f"\tIN ENGLISH -> ")).lower().strip()
        finish_time = time() - start_time
        result_dict["total_time"] += finish_time
        print()
        if (inp_rom == word_dict[mac_ch[i]]["Rōmaji"]) and (inp_eng in word_dict[mac_ch[i]]["English"]):
            result_dict["correct"] += 1
        elif (inp_rom != word_dict[mac_ch[i]]["Rōmaji"]) or (inp_eng not in word_dict[mac_ch[i]]["English"]):
            result_dict["incorrect"] += 1
        if len(word_dict) > 1:
            result_dict["average_time"] = result_dict["total_time"] / len(word_dict)
        elif len(word_dict) == 1:
            result_dict["average_time"] = result_dict["total_time"]
    return result_dict


class Japanese:
    def __init__(self):
        self.hiragana = {
            "a": "あ ", "i": "い", "u": "う", "e": "え", "o": "お",
            "ka": "か", "ki": "き", "ku": "く", "ke": "け", "ko": "こ",
            "sa": "さ", "shi": "し", "su": "す", "se": "せ", "so": "そ",
            "ta": "た", "chi": "ち", "tsu": "つ", "te": "て", "to": "と",
            "na": "な", "ni": "に", "nu": "ぬ", "ne": "ね", "no": "の",
            "ha": "は", "hi": "ひ", "fu": "ふ", "he": "へ", "ho": "ほ",
            "ma": "ま", "mi": "み", "mu": "む", "me": "め", "mo": "も",
            "ya": "や", "yu": "ゆ", "yo": "よ",
            "ra": "ら", "ri": "り", "ru": "る", "re": "れ", "ro": "ろ",
            "wa": "わ", "wo": "を",
            "n": "ん",
        }
        self.hiragana_example_words = {
            "あき": {"Rōmaji": "aki", "English": ["autumn", "fall"]},
            "あり": {"Rōmaji": "ari", "English": ["ant"]},
            "あい": {"Rōmaji": "ai", "English": ["love"]},
            "あし": {"Rōmaji": "ashi", "English": ["foot", "leg"]},
            "いし": {"Rōmaji": "ishi", "English": ["stone"]},
            "いるか": {"Rōmaji": "iruka", "English": ["dolphin"]},
            # "いぬ": {"Rōmaji": "inu", "English": ["dog"]},
            # "いす": {"Rōmaji": "isu", "English": ["chair"]},
            # "うし": {"Rōmaji": "ushi", "English": ["cow"]},
            # "うま": {"Rōmaji": "uma", "English": ["horse"]},
            # "うさぎ": {"Rōmaji": "usagi", "English": ["rabbit"]},
            # "うみ": {"Rōmaji": "umi", "English": ["ocean"]},
            # "え": {"Rōmaji": "e", "English": ["picture"]},
            # "えび": {"Rōmaji": "ebi", "English": ["shrimp"]},
            # "えさ": {"Rōmaji": "esa", "English": ["pet food"]},
            # "えいが": {"Rōmaji": "eiga", "English": ["movie"]},
            # "おに": {"Rōmaji": "oni", "English": ["demon"]},
            # "およぐ": {"Rōmaji": "oyogu", "English": ["to swim"]},
            # "おちゃ": {"Rōmaji": "ocha", "English": ["tea"]},
            # "おりがみ": {"Rōmaji": "origami", "English": ["origami"]},
            # "かい": {"Rōmaji": "kai", "English": ["shell"]},
            # "かえる": {"Rōmaji": "kaeru", "English": ["frog"]},
            # "かさ": {"Rōmaji": "kasa", "English": ["umbrella"]},
            # "がっこう": {"Rōmaji": "gakkō", "English": ["school"]},
            # "きのこ": {"Rōmaji": "kinoko", "English": ["mushroom"]},
            # "きつね": {"Rōmaji": "kitsune", "English": ["fox"]},
            # "ぎんこう": {"Rōmaji": "ginkō", "English": ["bank"]},
            # "ぎゅうにゅう": {"Rōmaji": "gyūnyū", "English": ["milk"]},
            # "くま": {"Rōmaji": "kuma", "English": ["bear"]},
            # "くも": {"Rōmaji": "kumo", "English": ["spider"]},
            # "くるま": {"Rōmaji": "kuruma", "English": ["car"]},
            # "ぐん": {"Rōmaji": "gun", "English": ["military"]},
            # "けん": {"Rōmaji": "ken", "English": ["sword"]},
            # "けしごむ": {"Rōmaji": "keshigomu", "English": ["eraser"]},
            # "けいさつ": {"Rōmaji": "keisatsu", "English": ["police"]},
            # "げいしゃ": {"Rōmaji": "geisha", "English": ["geisha"]},
            # "こうえん": {"Rōmaji": "kōen", "English": ["park"]},
            # "こい": {"Rōmaji": "koi", "English": ["romantic love"]},
            # "ごみ": {"Rōmaji": "gomi", "English": ["garbage", "trash"]},
            # "ごきぶり": {"Rōmaji": "gokiburi", "English": ["cockroach"]},
        }
        self.katakana = {
            "a": "ア", "i": "イ", "u": "ウ", "e": "エ", "o": "オ",
            "ka": "カ", "ki": "キ", "ku": "ク", "ke": "ケ", "ko": "コ",
            "sa": "サ", "shi": "シ", "su": "ス", "se": "セ", "so": "ソ",
            "ta": "タ", "chi": "チ", "tsu": "ツ", "te": "テ", "to": "ト",
            "na": "ナ", "ni": "ニ", "nu": "ヌ", "ne": "ネ", "no": "ノ",
            "ha": "ハ", "hi": "ヒ", "fu": "フ", "he": "ヘ", "ho": "ホ",
            "ma": "マ", "mi": "ミ", "mu": "ム", "me": "メ", "mo": "モ",
            "ya": "ヤ", "yu": "ユ", "yo": "ヨ",
            "ra": "ラ", "ri": "リ", "ru": "ル", "re": "レ", "ro": "ロ",
            "wa": "ワ", "wo": "ヲ",
            "n": "ン"
        }
        self.katakana_example_words = {
            "あき": {"Rōmaji": "aki", "English": ["autumn", "fall"]},
            "あり": {"Rōmaji": "ari", "English": ["ant"]},
            "あい": {"Rōmaji": "ai", "English": ["love"]},
            "あし": {"Rōmaji": "ashi", "English": ["foot", "leg"]},
            "いし": {"Rōmaji": "ishi", "English": ["stone"]},
            "いるか": {"Rōmaji": "iruka", "English": ["dolphin"]},
            "いぬ": {"Rōmaji": "inu", "English": ["dog"]},
            "いす": {"Rōmaji": "isu", "English": ["chair"]},
            "うし": {"Rōmaji": "ushi", "English": ["cow"]},
            "うま": {"Rōmaji": "uma", "English": ["horse"]},
            "うさぎ": {"Rōmaji": "usagi", "English": ["rabbit"]},
            "うみ": {"Rōmaji": "umi", "English": ["ocean"]},
            "え": {"Rōmaji": "e", "English": ["picture"]},
            "えび": {"Rōmaji": "ebi", "English": ["shrimp"]},
            "えさ": {"Rōmaji": "esa", "English": ["pet food"]},
            "えいが": {"Rōmaji": "eiga", "English": ["movie"]},
            "おに": {"Rōmaji": "oni", "English": ["demon"]},
            "およぐ": {"Rōmaji": "oyogu", "English": ["to swim"]},
            "おちゃ": {"Rōmaji": "ocha", "English": ["tea"]},
            "おりがみ": {"Rōmaji": "origami", "English": ["origami"]},
            "かい": {"Rōmaji": "kai", "English": ["shell"]},
            "かえる": {"Rōmaji": "kaeru", "English": ["frog"]},
            "かさ": {"Rōmaji": "kasa", "English": ["umbrella"]},
            "がっこう": {"Rōmaji": "gakkō", "English": ["school"]},
            "きのこ": {"Rōmaji": "kinoko", "English": ["mushroom"]},
            "きつね": {"Rōmaji": "kitsune", "English": ["fox"]},
            "ぎんこう": {"Rōmaji": "ginkō", "English": ["bank"]},
            "ぎゅうにゅう": {"Rōmaji": "gyūnyū", "English": ["milk"]},
            "くま": {"Rōmaji": "kuma", "English": ["bear"]},
            "くも": {"Rōmaji": "kumo", "English": ["spider"]},
            "くるま": {"Rōmaji": "kuruma", "English": ["car"]},
            "ぐん": {"Rōmaji": "gun", "English": ["military"]},
            "けん": {"Rōmaji": "ken", "English": ["sword"]},
            "けしごむ": {"Rōmaji": "keshigomu", "English": ["eraser"]},
            "けいさつ": {"Rōmaji": "keisatsu", "English": ["police"]},
            "げいしゃ": {"Rōmaji": "geisha", "English": ["geisha"]},
            "こうえん": {"Rōmaji": "kōen", "English": ["park"]},
            "こい": {"Rōmaji": "koi", "English": ["romantic love"]},
            "ごみ": {"Rōmaji": "gomi", "English": ["garbage", "trash"]},
            "ごきぶり": {"Rōmaji": "gokiburi", "English": ["cockroach"]},
        }

    def menu(self):
        while True:
            print()
            print("_" * 101)
            print("Choose any one of the following options ::")
            print("1-> Test_1 : Rōmaji for Hiragana\n2-> Test_2 : Hiragana for Rōmaji"
                  "\n3-> Test_3 : Hiragana words\n4-> Test_4 : Rōmaji for Katakana"
                  "\n5-> Test_5 : Katakana for Rōmaji\n6-> Test_6 : Katakana words"
                  "\n7-> Exit")
            opt = input(">>>  ")
            if opt == "1":
                results(test_kana("1", self.hiragana))
            elif opt == "2":
                results(test_kana("2", self.hiragana))
            elif opt == "3":
                results(word_check(self.hiragana_example_words))
            elif opt == "4":
                results(test_kana("4", self.katakana))
            elif opt == "5":
                results(test_kana("5", self.katakana))
            elif opt == "6":
                results(word_check(self.katakana_example_words))
            elif opt == "7":
                print("Thank you for playing!!!\nSEE YOU SOON......")
                exit(0)
            else:
                print("Please enter a valid option!!!")
                self.menu()


if __name__ == "__main__":
    obj = Japanese()
    obj.menu()
