# OOP in C language

## **Option 1: Encapsulation in CPP files**
- Public -> in header
    - use `typedef` to hide struct declaration
- Private -> in cpp file

## **Option 2: Struct with function pointer (encapsulated)**

- Header file

```c
#ifndef SHAPE_H
#define SHAPE_H

// Opaque type: callers cannot see fields
typedef struct Shape Shape;

// Public API
Shape* create_shape(const char* name, int w, int h);
void destroy_shape(Shape* self);
void shape_display(const Shape* self);

#endif

```

- C file

```c
#include "shape.h"
#include <stdio.h>
#include <stdlib.h>

struct Shape {
    const char* name;
    int width;
    int height;

    // Internal method pointer (private to this .c file)
    void (*display)(const Shape* self);
};

static void display_shape_impl(const Shape* self) {
    if (!self) {
        return;
    }
    printf("Shape: %s | Dimensions: %dx%d\n", self->name, self->width, self->height);
}

Shape* create_shape(const char* name, int w, int h) {
    Shape* new_shape = malloc(sizeof(*new_shape));
    if (!new_shape) {
        return NULL;
    }

    new_shape->name = name;
    new_shape->width = w;
    new_shape->height = h;
    new_shape->display = display_shape_impl;

    return new_shape;
}

void shape_display(const Shape* self) {
    if (self && self->display) {
        self->display(self);
    }
}

void destroy_shape(Shape* self) {
    free(self);
}

```

- Usage

```c
#include <stdio.h>
#include "shape.h"

int main() {
    Shape* rect = create_shape("Rectangle", 10, 20);
    Shape* circle = create_shape("Circle", 5, 5);

    if (!rect || !circle) {
        destroy_shape(rect);
        destroy_shape(circle);
        return 1;
    }

    shape_display(rect);
    shape_display(circle);

    destroy_shape(rect);
    destroy_shape(circle);

    return 0;
}
```