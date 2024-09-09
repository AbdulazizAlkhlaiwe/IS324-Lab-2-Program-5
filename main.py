def remove_words(main_list, remove_list):
    result_list = []

    for i in main_list:
        words = i.split(' ')
        filtered_sentence = ""

        for w in words:
            for r in remove_list:
                w = w.replace(r, '')


            filtered_sentence += w + " "


        result_list.append(filtered_sentence.strip())

    return result_list



main_list = ['Blue color', 'Red#', 'Purple', 'Red %', 'Black']
remove_list = ['%', 'color', '#']


result = remove_words(main_list, remove_list)


print("String list:", main_list)
print("Remove list:", remove_list)
print("Result list:", result)