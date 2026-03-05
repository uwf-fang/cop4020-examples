# OOP in C language

## **Option 1: Encapsulation in CPP files**
- Public -> in header
    - use `typedef` to hide struct declaration
- Private -> in cpp file

## **Option 2: Struct with function pointer**

- Header file

```c
#include <stdio.h>
#include <stdlib.h>

// Forward declaration of the struct
typedef struct Shape Shape;

// Define the "Interface" / Behavior
struct Shape {
    char* name;
    int width;
    int height;

    // Function pointer: This acts as our "Method"
    void (*display)(Shape* self);
};

```

- C file

```c
void display_shape(Shape* self) {
    printf("Shape: %s | Dimensions: %dx%d\n", self->name, self->width, self->height);
}

// A "Constructor" to initialize the object
Shape* create_shape(char* name, int w, int h) {
    Shape* new_shape = (Shape*)malloc(sizeof(Shape));
    new_shape->name = name;
    new_shape->width = w;
    new_shape->height = h;

    // Linking the function pointer to the implementation
    new_shape->display = display_shape;

    return new_shape;
}

int main() {
    // Instantiate "Objects"
    Shape* rect = create_shape("Rectangle", 10, 20);
    Shape* circle = create_shape("Circle", 5, 5);

    // Call "Methods"
    rect->display(rect);
    circle->display(circle);

    // Clean up (Destructor logic)
    free(rect);
    free(circle);

    return 0;
}

```

---

### Key OOP Principles Applied:

* **Encapsulation:** We grouped data (`width`, `height`) and logic (`display`) together.
* **Abstraction:** The user of `Shape` doesn't need to know how `display` is implemented; they just call the pointer.
* **Polymorphism (Advanced):** You can achieve polymorphism by creating different functions for different shapes and assigning them to the `display` pointer at runtime.

### Summary Table

| OOP Concept | C Implementation |
| --- | --- |
| **Class** | `struct` |
| **Object** | Instance of the `struct` (usually heap-allocated) |
| **Method** | Function pointer within the `struct` |
| **This / Self** | The first argument of the function (`Shape* self`) |
| **Constructor** | A function that `malloc`s and initializes the `struct` |

Would you like me to show you how to implement **Inheritance** in C using struct nesting?