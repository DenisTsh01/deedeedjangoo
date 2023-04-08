import json

dict = {}
information_list = {}


def append_dict(subject, information):
    dict[subject] = information
    with open('short_mem_information.json', 'w') as income_data:
        json.dump(dict, income_data)
        income_data.close()
    print(dict)


def append_main_dict():
    with open('information.json', 'a') as fp:
        json.dump(dict, fp)
    # with open('short_mem_information.json', 'r') as data:
    #     income_data = json.load(data)
    #     del data

def get_information():
    with open('information.json', 'r') as info:
        for dictionaries in info:
            print(dictionaries)
