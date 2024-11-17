import re

def input_string_with_backspaces() -> str:
    string_to_return = input("Enter a string - words separated backspaces: ")
    return string_to_return

def revert(current_word) -> str:
    reverted_word = ""
    for char in current_word[::-1]:
        reverted_word = reverted_word + char
    return reverted_word

def create_list_of_reverted_strings(input_: str) -> list :
    reverted_words_list = []
    pattern_= r'^[A-Za-zА-Яа-яЁё]+( [A-Za-zА-Яа-яЁё]+)*'
    if re.fullmatch(pattern_, input_):
       current_word = ""
       for i in range (len(input_)):
              if input_[i] != " ":
                current_word = current_word + input_[i]

              if i+1 ==len(input_) or input_[i+1] == " ":
                reverted_word =  revert(current_word)
                current_word = ""
                reverted_words_list.append(reverted_word)
    else:
        string_ = input_string_with_backspaces()
        reverted_words_list = create_list_of_reverted_strings(string_)
    return reverted_words_list

if __name__ == '__main__':
    string = input_string_with_backspaces()
    list__ = create_list_of_reverted_strings(string)
    list__.sort()
    print(list__)