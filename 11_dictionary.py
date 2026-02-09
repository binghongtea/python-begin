popular_dict = {
    'apple': '苹果',
    'banana': '香蕉',
    'orange': '橘子',
    ('apple',10) : '苹果10个',
}
print(popular_dict[('apple',10)])
popular_dict['lemon'] = '柠檬'
popular_dict['pizza'] = '披萨'
popular_dict['pear'] = '梨'
popular_dict['sharpener'] = '笔锋'

search_input = input("请输入你要查询的词语: ")

if search_input in popular_dict:
    # print("你要查询的词语是: %s" % popular_dict[search_input])
    print(f"你要查询的词语是: {popular_dict[search_input]}")
else :
    print("没有这个词语")
    print(f"词库内总共有：{len(popular_dict)}个词语")