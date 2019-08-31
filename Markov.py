from janome.tokenizer import Tokenizer
import random
import re
import json

class Markov:

    def save_dict(self, dict):
        f = open("dict.json", "w")
        json.dump(dict, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))

    def to_dict(self, path):
        # テキストファイルを読み込む
        text = open(path, 'rb').read()
        text = text.decode('utf_8')
        
        # テキストを形態素解析読み込みます
        words = Tokenizer().tokenize(text, wakati=True)
        
        # マルコフ連鎖用辞書作成
        dict = {}  # 辞書初期化
        w1, w2 = "", ""
        for word in words:
            # 「\n」や「\u3000」
            if (re.match('\n', word) or re.match('\u3000', word)):
                continue
            
            if w1 and w2:
                if (w1 not in dict):
                    dict[w1] = {}
                if (w1 in dict):
                    if (w2 not in dict[w1]):
                        dict[w1][w2] = []
                dict[w1][w2].append(word)
            w1, w2 = w2, word  # 1単語スライド

        return dict

    def create_text(self, dict, first_word, limit):
        if (first_word not in dict):
            return '「' + first_word + '」は辞書に含まれていません'
        text = first_word
        w1 = first_word
        w2 = ''
        next_word = ''
        for i in range(limit):
            if (w2 == ''):
                w2 = random.choice(list(dict[w1].items()))[0]
                text = text + w2
                continue
            next_word = random.choice(dict[w1][w2])
            text = text + next_word
            w1, w2 = w2, next_word
        return text
