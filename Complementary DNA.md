
[Complementary DNA](https://www.codewars.com/kata/554e4a2f232cdd87d9000038/python)

###### My solution
``` Python
def DNA_strand(dna):
    d = {'A': 'T', 'T': 'A', 'C':'G', 'G':'C'}
    return ''.join([d[k] for k in dna])
```

###### Best Practise
``` Python
import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))
```
