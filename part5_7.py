import json

profit = 0
count = 0
average_profit = 0
key = ''
total_dict = {}
av_profit_dict = {}
with open('text_7.txt', 'r', encoding='utf-8') as firm_list:
    for i_str in firm_list.readlines():
        i_str = i_str.split()
        key = i_str[0]
        profit = int(i_str[2]) - int(i_str[3])
        base_dict = {key: profit}
        total_dict.update(base_dict)
        if profit > 0:
            average_profit += profit
            count += 1
    av_profit_dict = {"average_profit": average_profit / count}
    total_list = [total_dict, av_profit_dict]
    print(total_list)
    with open('text_7_1.json', 'w', encoding='utf-8') as write_json:
        json.dump(total_list, write_json, ensure_ascii=False, indent=4)
