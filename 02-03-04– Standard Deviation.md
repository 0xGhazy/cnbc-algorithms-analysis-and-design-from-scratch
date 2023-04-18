## Task 01: Write algorithm for correlation with flowchart and code.

#### Algorithm
- initialize our variables `x`, `y`, `sumx`, `sumy`, `sumxy`, `sumx2`, `sumy2`, and `n`
- reading the `x[]` and `y[]`.
- calculate `n` = length of `x[]` or `y[]`.
- calculate each of `x[i]`, `y[i]`, `xy`, `sumx`, `sumy`, `sumx2`, and `sumy2`.
- calculate the numerator = `n(sumxy) - sumx * sumy`
- calculate the denominator = `sqrt(n * sumx2 - sqr(sumx)) * sqrt(n * sumy2 - sqr(sumy))`
- calculate the correlation by dividing the `numerator` by the `denominator`.
- display the correlation on the screen.


#### Flowchart
<dev align="center">

![Correlation](https://user-images.githubusercontent.com/60070427/232887968-5bd1989d-acdb-4dee-a4c6-a7a212d9e6c1.png)

</dev>

### Code in Python

```python
from typing import List
from math import sqrt

def calculate_correlation(x: List[int], y: List[int]) -> float:
    sumx = sumy = sumxy = sumx2 = sumy2 = numerator = denominator = 0
    n = len(x)
    for i in range(0, n):
        sumx+= x[i]
        sumy+= y[i]
        sumxy += x[i] * y[i]
        sumx2 += x[i] ** 2
        sumy2 += y[i] ** 2
    # Numerator = n(sumxy) - sumx * sumy
    numerator = n * sumxy - (sumx * sumy)
    # Denominator = sqrt(n * sumx2 - sqr(sumx)) * sqrt(n * sumy2 - sqr(sumy))
    denominator = sqrt(n * sumx2 - sumx ** 2) * sqrt(n * sumy2 - sumy ** 2)
    result = numerator / denominator
    return result

# read base and height
x = [43,21,25,42,57,59]
y = [99,65,79,75,87,81]
print(calculate_correlation(x, y))
```

# References
- [Maths Is Fun - Correlation](https://www.mathsisfun.com/data/correlation.html)
- [Statistics How To - Correlation Coefficient: Simple Definition, Formula, Easy Steps
](https://www.statisticshowto.com/probability-and-statistics/correlation-coefficient-formula/)