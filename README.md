# Python OOP: Circle Class Implementation

A clean, beginner-friendly implementation of Object-Oriented Programming (OOP) in Python demonstrating the creation of a `Circle` class with methods to calculate its area and perimeter (circumference).

---

## 📌 Problem Overview

**Problem Definition:**  
Create a Python class named `Circle` that accepts a `radius` upon initialization. The class must provide methods to compute and return both the area and perimeter (circumference) of the circle.

### Requirements:
1. **Constructor (`__init__`):** Accept and store the `radius` value as an instance attribute (`self.radius`).
2. **`area()` Method:** Compute and return the area using the formula:
   $$\text{Area} = \pi \cdot \text{radius}^2$$
3. **`perimeter()` Method:** Compute and return the circumference using the formula:
   $$\text{Perimeter} = 2 \cdot \pi \cdot \text{radius}$$
4. **Execution & Formatting:** Instantiate a `Circle` object with a radius value, call both methods, and format the output rounded to **two decimal places** (`:.2f`).

---

## 🚀 Code Implementation

```python
import math


class Circle:
  """A class representing a geometric circle.

  Attributes:
      radius (float): The radius of the circle.
  """

  def __init__(self, radius: float):
    # Store radius into the instance attribute (self.radius)
    self.radius = radius

  def area(self) -> float:
    """Calculate and return the area of the circle: π * r^2"""
    return math.pi * (self.radius**2)

  def perimeter(self) -> float:
    """Calculate and return the perimeter (circumference) of the circle: 2 * π * r"""
    return 2 * math.pi * self.radius


if __name__ == "__main__":
  # Hardcoded test value as required
  radius = 5.0

  # Instantiate Circle object
  c1 = Circle(radius)

  # Display calculated results formatted to 2 decimal places
  print(f"Area: {c1.area():.2f}")
  print(f"Perimeter: {c1.perimeter():.2f}")
```

---

## 🧪 Expected Output

For `radius = 5.0`:

```text
Area: 78.54
Perimeter: 31.42
```

---

## 💡 Key Concepts Explained

### 1. `self.radius` vs. Parameter `radius`
* **Parameter `radius` in `__init__(self, radius)`:** A temporary local variable passed from outside during object creation. It disappears once `__init__` finishes execution.
* **Instance attribute `self.radius`:** A permanent variable attached directly to the object (`c1`). Any method inside the class (`area`, `perimeter`) accesses this value using `self.radius`.

### 2. Exponentiation Operator (`**`)
In Python:
* `self.radius * 2` multiplies the radius by 2 (used for perimeter).
* `self.radius ** 2` raises the radius to the power of 2 ($r^2$, used for area).

### 3. Formatting with `:.2f`
* `:` introduces formatting specifiers in an f-string.
* `.2` specifies two digits after the decimal point.
* `f` formats the number as a fixed-point float (automatically rounds mathematically).

---

## 🛠️ How to Run Locally

1. Clone or download this repository.
2. Open your terminal in the project directory.
3. Run the script using Python 3:

```bash
python circle.py
```
