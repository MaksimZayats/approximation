# approximation
Approximation of points by a polynomial of arbitrary power


## Usage

## Main functions:
1. `approximate`
    * #### Arguments:
        1. `x: list` — coordinates of points on the x-axis
        2. `y: list` — coordinates of points on the x-axis
        3. `p: int` — power of the polynomial
    * #### Returns:
        1. `polynomial_coefficients: list` <br/>
        The obtained coefficients are from the smallest to the largest power.<br/>
        Example:<br/>
            If you get these coefficients:
            `[2.0, 3.0, 4.0]`<br/>
            This means that the polynom will look like this:  
            `2x^0 + 3x^1 + 4x^2`<br/>
    * #### Notes:
        1. `len(x) == len(y)` must be True.<br/>
            Else you will get an error!
2. `create_polynom`
    * #### Argument:
        1. `polynomial_coefficients: list` coefficients of the polynom. <br/>
        *Obtained from the `approximate`*
    * #### Returns:
        1. A polynom.<br/>
        Example: `4x^2 + 3x^1 + 2`
#### Code Example:
```python
from approximation import create_polynom, approximate


if __name__ == "__main__":
    print("Some example cases:")

    x = [1, 2, 3]
    y = [2, 5, 10]
    p = 2
    print(f"\nCase 1:\nx = {x},\ny = {y},\np = {p}\nPolynom: {create_polynom( approximate(x, y, p) )}")

    x = [-2, -1, 0, 1, 2]
    y = [0, 5, 0, 10, 4]
    p = 4
    print(f"\nCase 2:\nx = {x},\ny = {y},\np = {p}\nPolynom: {create_polynom( approximate(x, y, p) )}")

    x = [-3, -2, -1, 0, 1, 2]
    y = [-10, 0, 5, 0, 10, 4]
    p = 5
    print(f"\nCase 3:\nx = {x},\ny = {y},\np = {p}\nPolynom: {create_polynom( approximate(x, y, p) )}")
```
