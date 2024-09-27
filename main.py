def get_book_contents(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    
    return file_contents

def get_words_from_book(book_content_str):
    words = book_content_str.split()
    return words

def get_chars_count(book_content_str):
    char_count_dict = {}
    for ch in book_content_str.lower():
        if ch not in char_count_dict:
            char_count_dict[ch] = 0
        char_count_dict[ch] += 1
    return char_count_dict

def conv_dict_name_count_pair(char_count_dict):
    list_dict = []
    for ch in char_count_dict:
        if ch.isalpha():
            list_dict.append({'char_str':ch, 'count':char_count_dict[ch]})
    return list_dict

def sort_on_str_count(str_count_dict):
    return str_count_dict['count']

def main():
    book_path = 'books/frankenstein.txt'
    book_content = get_book_contents(book_path)
    # print(book_content)
    words = get_words_from_book(book_content)
    # print(len(words))
    char_count = get_chars_count(book_content)
    # print(char_count)
    list_char_count = conv_dict_name_count_pair(char_count)
    # print(list_char_count)
    list_char_count.sort(reverse=True, key=sort_on_str_count)
    # print(list_char_count)
    # Book report
    str_bldr = f'--- Begin report of {book_path} ---'
    str_bldr += '\n'
    str_bldr += f'{len(words)} words found in the document'
    str_bldr += '\n'
    str_bldr += '\n'
    str_bldr += '\n'
    list_str_bldr = []
    for l in list_char_count:
        list_str_bldr.append(f"The '{l['char_str']}' character was found {l['count']} times")
    temp_str = '\n'.join(list_str_bldr)
    str_bldr += temp_str
    str_bldr += '\n'
    str_bldr += '--- End report ---'
    print(str_bldr)

main()