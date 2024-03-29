def sort_by_count(dict_lst):
    return dict_lst['count']

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        letter_dict = {}
        for word in words:
            word = word.lower()
            for char in word:
                if char not in letter_dict and char.isalpha():
                    letter_dict[char] = 1
                elif char.isalpha():
                    letter_dict[char] += 1
        
        letter_lst = []
        
        for key in letter_dict:
            entry = {'name': key, "count": letter_dict[key]}
            letter_lst.append(entry)
        
        letter_lst.sort(reverse=True, key=sort_by_count)            
        print("-- Begin report of books/frankenstein.txt --")
        print(f"{len(words)} words found in the document\n")
        for letter in letter_lst:
            print(f"The {letter['name']} character was found {letter['count']} times")
        print("\n-- End report --")
main()