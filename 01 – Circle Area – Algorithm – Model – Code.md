
## Task 01: Parallelogram Area
Write the parallelogram area algorithm, draw the flowchart, and write algorithm code.

`area = b * h` where (b) for base and (h) for height

#### Algorithm
- Read the `base` and `height` from ths user
- calcuate the `area` where ares is `height` * `base`
- Print the result on screen

#### Flowchart

<dev align="center">

![parallelogram](https://user-images.githubusercontent.com/60070427/232834521-ec47488b-1dcc-490f-922e-c32031307b58.png)

</dev>

### Code in Python

```python
def parallelogram_area(b: float, h: float) -> float:
    a = b * h
    return a

# read base and height
b = float(input("Enter base: "))
h = float(input("Enter height: "))
print(parallelogram_area(b, h))
```

## Task 02: Trapezoid  Area
Write the Trapezoid area algorithm, draw the flowchart, and write algorithm code.

`area = (b1+b2)h/2` where b1, b2 for base1 and base2 and (h) for height

#### Algorithm
- Read the `base1`, `base2` and `height` from ths user
- calcuate the `area` where ares is (`base1` + `base2`)* `height` / 2
- Print the result on screen

#### Flowchart

<dev align="center">

![tarea](https://user-images.githubusercontent.com/60070427/232847157-744c6434-9c5a-487a-b77a-2b1a9086b497.png)

</dev>

### Code in Python

```python
def trapezoid_area(b1: float, b2: float, h: float) -> float:
    a = (b1 + b2)* h/2
    return a

# read base and height
b1 = float(input("Enter base1: "))
b2 = float(input("Enter base2: "))
h = float(input("Enter height: "))
print(trapezoid_area(b1, b2, h))
```