import xml.etree.ElementTree as ET

def processing_xml(file: str):
  tree = ET.parse(file)
  root = tree.getroot()
  news_text_list = []
  xml_items = root.findall('channel/item')
  words_list = []
  for item in xml_items:
    news_text_list += item.find('description').text.split()
  for word in news_text_list:
    if len(word) > 6:
      words_list.append(word)
  words_list = sorted(list(set(words_list)),
                        key=lambda x: news_text_list.count(x),
                        reverse=True)
  for count, word in enumerate(words_list[0:10], 1):
    print(f'{count}. Слово «{word}» найдено '
          f'{news_text_list.count(word)} раз')


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
    words_set = sorted(list(set(words)), key=lambda x: words.count(x), reverse=True)
    for count, word in enumerate(words_set[0:10], 1):
      print(f'{count}. Слово «{word}» найдено '
            f'{words.count(word)} раз')


if __name__ == '__main__':
  print('\nTesting XML\n')
  processing_xml('newsafr.xml')
  print('\nTesting json\n')
  processing_json('newsafr.json')