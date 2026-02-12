#include <iostream>
using namespace std;
enum Colors { RED, BLUE, GREEN };
enum Birds { CARDINAL, BLUEJAY };

int main() {
  Colors myColor = RED;
  // ALLOWED in C++: comparing two different enum types because they both coerce to int.
  // This is logically nonsense (Is Red equal to Cardinal?) but valid code.
  if (myColor == CARDINAL) {
    cout << "This is a red cardinal!" << endl;
  }

  // ALLOWED: Math on enums
  int x = myColor * 10;
}