#include <stdio.h>

union FlexType {
    int intEl;
    float floatEl;
};

int main() {
    union FlexType el1;
    el1.intEl = 27; // We store an integer

    // UNSAFE: We read it back as a float.
    // The system reads the bit pattern of 27 as a float, resulting in garbage.
    float x = el1.floatEl;
    printf("The value 27 as float is: %f\n", el1.floatEl);
    printf("The value 27 as int is: %d\n", el1.intEl);
}