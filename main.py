import Markov

def main():
    # インスタンス生成
    markov = Markov.Markov()

    # テキストファイルのパス
    path = 'data.txt'
    # 最初の単語

    first_word = 'リビング'

    # 連鎖数の上限
    limit = 30

    # 単語ごとの辞書を作成
    dict = markov.to_dict(path)
    markov.save_dict(dict)
    
    # ツイートを１０回生成
    text = markov.create_text(dict, first_word, limit)
    print(text)

if __name__ == '__main__':
    main()