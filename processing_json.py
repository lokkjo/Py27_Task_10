import json

def processing_json(file: str):
    with open(file, encoding='utf-8') as news_file:
        news = json.load(news_file)
        descriptions = []
        words = []
        for item in news['rss']['channel']['items']:
            descriptions.append(item['description'].split(' '))
        for news_text in descriptions:
            for word in news_text:
                if len(word) > 6:
                    words.append(word)
        words = sorted(list(set(words)),
                       key=lambda x: descriptions.count(x),
                       reverse=True)
        for count, word in enumerate(words[0:10], 1):
            print(f'{count}. Слово «{word}» найдено '
                  f'{descriptions.count(word)} раз')

if __name__ == '__main__':
    processing_json('newsafr.json')