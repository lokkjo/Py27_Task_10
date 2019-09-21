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


if __name__ == '__main__':
    processing_xml('newsafr.xml')