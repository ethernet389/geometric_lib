# Math Formulas

|             Figure              |          Area          |     Perimeter      |                                     Definition                                     |
| :-----------------------------: | :--------------------: | :----------------: | :--------------------------------------------------------------------------------: |
|  _circle_ :large_blue_circle:   |       $\pi R^2$        |     $2 \pi R$      |                             $R$ - radius of the circle                             |
|        _rectangle_ :de:         |      $a \times b$      | $2 \times (a + b)$ |                          $a, b$ - rectangle side lengths                           |
| _square_ :large_orange_diamond: |         $a^2$          |        $4a$        |                              $a$ - square side length                              |
| _triangle_ :small_red_triangle: | $a \times \frac{h}{2}$ |    $a + b + c$     | $a, b, c$ - triangle side lengths <br/> $h$ - perpendicular length to the side $a$ |

These formulas are used to calculate the areas and perimeters of various shapes.

<br/><br/>

# Functions

### Main Information

|        File        |    Function Signature    |                             Parameters (type)                              |  Return value (type)  |                      Description                       |
| :----------------: | :----------------------: | :------------------------------------------------------------------------: | :-------------------: | :----------------------------------------------------: |
|  **_circle.py_**   |      `def area(r)`       |                          `r` - radius (**float**)                          |   area (**float**)    |         _Take_ radius. <br/> _Calculate_ area.         |
|                    |    `def perimeter(r)`    |                          `r` - radius (**float**)                          | perimeter (**float**) |      _Take_ radius. <br/> _Calculate_ perimeter.       |
|                    |
| **_rectangle.py_** |     `def area(a, b)`     |                     `a, b` - side lengths (**float**)                      |   area (**float**)    |         _Take_ sides. <br/> _Calculate_ area.          |
|                    |  `def perimeter(a, b)`   |                     `a, b` - side lengths (**float**)                      | perimeter (**float**) |       _Take_ sides. <br/> _Calculate_ perimeter.       |
|                    |
|  **_square.py_**   |      `def area(a)`       |                       `a` - side length (**float**)                        |   area (**float**)    |          _Take_ side. <br/> _Calculate_ area.          |
|                    |    `def perimeter(a)`    |                       `a` - side length (**float**)                        | perimeter (**float**) |       _Take_ side. <br/> _Calculate_ perimeter.        |
|                    |
| **_triangle.py_**  |     `def area(a, h)`     | `a` - side length (**float**) <br/> `h` - perpendicular length (**float**) |   area (**float**)    | _Take_ side and perpendicular. <br/> _Calculate_ area. |
|                    | `def perimeter(a, b, c)` |                    `a, b, c` - side lengths (**float**)                    | perimeter (**float**) |       _Take_ sides. <br/> _Calculate_ perimeter.       |

### Usage Examples

---

#### Print area and perimeter of **circle**.

```python
import circle

r = 100
area = circle.area(r)
perimeter = circle.perimter(r)
print(area, perimeter)

# 31415.92653589 268.31853071
```

---

#### Print area and perimter of **rectangle**.

```python
import rectangle as rect

a, b = 100, 200
area = rect.area(a, b)
perimeter = rect.perimeter(a, b)
print(area, perimeter)

# 20000 600
```

---

#### Print area and perimeter of **square**.

```python
import square

a = 100
area = square.area(a)
perimeter = square.perimeter(a)
print(area, perimeter)

# 10000 400
```

---

#### Print area and perimeter of **triangle**.

```python
import square

a, b, c = 100, 140, 50
hc = 70.42016757
area = square.area(c, hc)
perimeter = square.perimeter(a, b, c)
print(area, perimeter)

# 1760.50418925 290
```

<br/><br/>

# [Testing](tests.md)

# Commit History

## 04.03.2021

### L-03: Circle and square added

- **Hash**: 8ba9aeb
- **Branch**: main
- **Time**: 14:54:08 +0300
- **Author**: smartiqa \<info@smartiqa.ru\>
- **Created files**:
  - circle.py
  - square.py

### L-03: Docs added

- **Hash**: d078c8d
- **Branch**: main
- **Time**: 14:55:29 +0300
- **Author**: smartiqa \<info@smartiqa.ru\>
- **Created files**:
  - docs/
  - docs/README.md

## 26.03.2021

### L-04: Triangle added

- **Hash**: d080c78
- **Branch**: develop
- **Time**: 14:48:39 +0300
- **Author**: smartiqa \<info@smartiqa.ru\>
- **Created files**:
  - triangle.py

### L-04: Doc updated for triangle

- **Hash**: 51c40eb
- **Branch**: develop
- **Time**: 14:52:26 +0300
- **Author**: smartiqa \<info@smartiqa.ru\>
- **Updated files**:
  - docs/README.md

## 30.03.2021

### L-04: Add calculate.py

- **Hash**: d76db2a
- **Branch**: develop
- **Time**: 17:57:42 +0300
- **Author**: Daniil.K \<dlkay@yandex.ru\>
- **Created files**:
  - calculate.py

### L-04: Update docs for calculate.py

- **Hash**: b5b0fae
- **Branch**: develop
- **Time**: 18:02:23 +0300
- **Author**: Daniil.K \<dlkay@yandex.ru\>
- **Updated files**:
  - docs/README.md

### L-04: Add rectangle.py

- **Hash**: 3049431
- **Branch**: feature
- **Time**: 17:36:09 +0300
- **Author**: Daniil.K \<dlkay@yandex.ru\>
- **Created files**:
  - rectangle.py

## 19.04.2021

### L-05: Add user agreement

- **Hash**: 438b89a
- **Branch**: release
- **Time**: 15:12:19 +0300
- **Author**: Danny \<bublikplushka@yandex.ru\>
- **Updated files**:
  - docs/README.md
- **Created files**:
  - user_agreement.txt

### L-05: Update Docs. Add user agreement info

- **Hash**: 86edb1c
- **Branch**: release
- **Time**: 15:15:14 +0300
- **Author**: Danny \<bublikplushka@yandex.ru\>
- **Updated files**:
  - docs/README.md

## 07.09.2024

### Add rectangle.py

- **Hash**: 367c5c8
- **Branch**: new_features_467462
- **Time**: 22:25:28 +0300
- **Author**: Gleb Simakov \<ethernet389@gmail.com\>
- **Created files**:
  - rectangle.py

### Fix calculation error in rectanlge.py

- **Hash**: ba2a970
- **Branch**: new_features_467462
- **Time**: 22:28:30 +0300
- **Author**: Gleb Simakov \<ethernet389@gmail.com\>
- **Updated files**:
  - rectangle.py
- **Created files**:
  - triangle.py

### docs(\*.py): Add docs to geometric functions

- **Hash**: f0ab236
- **Branch**: new_features_467462
- **Time**: 22:39:28 +0300
- **Author**: Gleb Simakov \<ethernet389@gmail.com\>
- **Updated files**:
  - circle.py
  - rectangle.py
  - square.py
  - triangle.py

## 08.09.2024

### docs(docs/README.md): Update README.md

- **Hash**: 1bed148
- **Branch**: new_features_467462
- **Time**: 03:56:28 +0300
- **Author**: Gleb Simakov \<ethernet389@gmail.com\>
- **Updated files**:
  - docs/README.md

### docs(docs/README.md): Update README.md

- **Hash**: dd97337
- **Branch**: new_features_467462
- **Time**: 17:59:06 +0300
- **Author**: Gleb Simakov \<ethernet389@gmail.com\>
- **Updated files**:
  - docs/README.md


## 04.10.2024

### refactor(): Add .gitignore
- **Hash**: 48d5eed
- **Branch**: new_features_467462
- **Time**: 21:46:00 +0300
- **Author**: Gleb Simakov \<ethernet389@gmail.com\>
- **Created files**:
  - .gitignore

### refactor(): Add test.py and add rectangle commutativity test
- **Hash**: f816da6
- **Branch**: new_features_467462
- **Time**: 21:46:42 +0300
- **Author**: Gleb Simakov \<ethernet389@gmail.com\>
- **Created files**:
  - test.py
  
### refactor(test.py): Add same values test for rectangle
- **Hash**: 96d789d
- **Branch**: new_features_467462
- **Time**: 22:12:01 +0300
- **Author**: Gleb Simakov \<ethernet389@gmail.com\>
- **Updated files**:
  - test.py

## 08.10.2024

### refactor(test.py): refactor(test.py): Add tests to circle and square
- **Hash**: c92e364
- **Branch**: new_features_467462
- **Time**: 16:15:17 +0300
- **Author**: Gleb Simakov \<ethernet389@gmail.com\>
- **Updated files**:
  - test.py

### refactor(test.py): Add tests to triangle
- **Hash**: 401ba5c
- **Branch**: new_features_467462
- **Time**: 17:20:42 +0300
- **Author**: Gleb Simakov \<ethernet389@gmail.com\>
- **Updated files**:
  - test.py

### docs(docs/*): Create tests.md and update README.md
- **Hash**: b1120f9
- **Branch**: new_features_467462
- **Time**: 19:45:54 +0300
- **Author**: Gleb Simakov \<ethernet389@gmail.com\>
- **Updated files**:
  - docs/README.md
- **Created files**:
  - docs/tests.md

### docs(docs/tests.md): Add level of testing
- **Hash**: fe6138f
- **Branch**: new_features_467462
- **Time**: 17:20:42 +0300
- **Author**: Gleb Simakov \<ethernet389@gmail.com\>
- **Updated files**:
  - docs/tests.md

### docs+fix(docs/tests.md): Replace H2 with H3
- **Hash**: 9a1d72c
- **Branch**: new_features_467462
- **Time**: 19:54:29 +0300
- **Author**: Gleb Simakov \<ethernet389@gmail.com\>
- **Updated files**:
  - docs/tests.md