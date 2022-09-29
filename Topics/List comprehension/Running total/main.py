li = [int(x) for x in list(input())]
li_of_li = [li[:x + 1] for x in range(len(li))]
print([sum(x) for x in li_of_li])
