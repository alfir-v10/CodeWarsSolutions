#### [Delete occurrences of an element if it occurs more than n times](https://www.codewars.com/kata/554ca54ffa7d91b236000023/python)

###### My Solution
``` Python
def delete_nth(order, max_e):
    d = {}
    new_list = []
    for num in order:
        if num not in d.keys():
            d[num] = 1
        else:
            d[num] = d[num] + 1
        if d[num] <= max_e:
            new_list.append(num)
    return new_list
```

###### Best practise
``` Python
def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans
```
