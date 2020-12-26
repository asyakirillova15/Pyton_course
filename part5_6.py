def func(value):
    var = '('
    try:
        if var in value:
            return True
    except ValueError:
        return False


total_dict = {}
with open('text_6.txt', 'r', encoding='utf-8') as plan:
    for el in plan.readlines():
        el = el.split()
        key_ = el[0][:-1]
        my_filter = filter(func, el)
        my_filter = list(my_filter)
        sum_hours = 0
        for elem in my_filter:
            num = int(elem[:elem.index("(")])
            sum_hours += num
        dict_base = {key_: sum_hours}
        total_dict.update(dict_base)
    print(total_dict)
