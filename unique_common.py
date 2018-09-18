def unique_common(a, b):
    new_list=[]
    for item in a:
        a_item=item
        for item in b:
            if item==a_item:
                new_list.append(item)
    for item in new_list:
        new_list_item=new_list.count(item)
        if new_list_item>1:
            for n in range(new_list_item-1):
                new_list.remove(item)
    new_list.sort()
    if len(new_list)==0:
        return None
    else:
        return new_list
print(unique_common([5, 6, -7, 8, 8, 9, 9, 10], [2, 4, 8, 8, 5, -7]))
print(unique_common([5, 6, 7, 0], [3, 2, 3, 2]))
##proff's
#def _unique_common_elements_sample_ed2_(a, b):
#    common = []
#    for items in a:
#        if items in b:
#            common.append(items)
#    if not common:
#        return None
#    unique = []
#    for items in common[:]:
#        if items not in unique:
#            unique.append(items)
#    return sorted(unique)
