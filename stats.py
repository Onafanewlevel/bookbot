def get_word_count(text):
    text_array = text.split()
    text_count = len(text_array)
    return text_count

def get_char_count(text):
    count = {}
    text = text.lower()
    for word in text:
        for char in word:
            if char not in count:
                count[char] = 0
            count[char] += 1
    return count

def sort_by_count(char_count_dict):
    sorted_list = []
    for k, v in char_count_dict.items():
        if not k.isalpha():
            continue
        count_dict = {}
        count_dict["char"] = k
        count_dict["num"] = v
        sorted_list.append(count_dict)
    sorted_list.sort(key=lambda d: d["num"], reverse=True)
    return sorted_list
