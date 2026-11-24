# Turtle Art

Generative art made with Python's built-in `turtle` module. This repo contains two projects:

1. **Spirograph** (`beauty_cycle.py`): circles in random colours, rotated to form a spirograph pattern
2. **Hirst-style dot painting** (`random_dot.py`): a 10 × 10 grid of coloured dots inspired by Damien Hirst's spot paintings

---

## How to run

You need Python 3 with tkinter (the library `turtle` uses to draw its window).

```bash
python beauty_cycle.py
python random_dot.py
```

Click on the window to close it when the drawing is finished.

> **Mac + Homebrew Python:** if you get `ModuleNotFoundError: No module named '_tkinter'`, install tkinter with:
> ```bash
> brew install python-tk@3.14
> ```

---

## 1. Spirograph (`beauty_cycle.py`)

Draws 100 circles with a radius of 100. Each circle gets a random colour, and the turtle turns 10° before drawing the next one, which builds up the spirograph pattern.

### How it works

```python
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
```

- `screen.colormode(255)` lets turtle use RGB colours from 0 to 255.
- `random_color()` returns a **tuple** of three random numbers: one for red, one for green, one for blue.

```python
for i in range(100):
    tim.color(random_color())
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)
```

- `tim.heading()` gets the direction the turtle is facing.
- `tim.setheading(...)` turns it 10° further before drawing the next circle.

---

## 2. Hirst-style dot painting (`random_dot.py`)

Recreates the style of Damien Hirst's spot paintings: rows of evenly spaced dots, each in a colour picked at random from a palette.

### Step 1: Getting the colours

The colour palette was taken from a reference image with the [`colorgram.py`](https://pypi.org/project/colorgram.py/) package:

```python
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

print(rgb_colors)
```

The printed list was copied into the code as `color_list`, so the painting runs without needing the image or `colorgram`. (The extraction code is left commented out at the top of the file for reference. The source image isn't included in this repo.)

### Step 2: Moving to the starting point

```python
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
```

- `penup()` stops the turtle from drawing lines between dots.
- Heading 225° points down-left, so moving forward 250 takes the turtle to the bottom-left corner where the grid starts.
- `setheading(0)` faces it right, ready to draw the first row.

### Step 3: Drawing the grid

```python
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
```

- Each dot is 20 pixels wide, with 50 pixels between dots.
- `random.choice(color_list)` picks a random colour from the palette.
- `dot_count % 10 == 0` is true after every 10th dot. When that happens, the turtle moves up one row and back to the left to start the next row.
- 100 dots = 10 rows × 10 dots.

---

## Note: centring the window on Mac

On newer Python versions on macOS, the turtle's starting point `(0, 0)` can appear off-centre. Both scripts fix this by setting the window and drawing area to the same size:

```python
screen.setup(width=800, height=600)
screen.screensize(800, 600)
```

---

## What I learned

- Using the `turtle` module to draw shapes and patterns
- RGB colours and **tuples**
- The `random` module: `randint()` and `choice()`
- Installing and using an external package (`colorgram.py`)
- Controlling movement with `heading()`, `setheading()`, `penup()` and `goto()`
- Using loops and the `%` (modulo) operator to build a grid