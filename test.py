
data_dic = {d: len([nbr for nbr in graph.neighbors(d)]) for d in domains}
sorted_data = sorted(data_dic, key=data_dic.get, reverse=True)
length = list(data_dic.values())
size = length.size()
print(max(length), min(length))
print(length[size*0.62:])