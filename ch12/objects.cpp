#include <iostream>
#include <string>

class Animal {
public:
    virtual void speak() const { std::cout << "Generic animal sound\n"; }
    virtual ~Animal() = default; // Essential for dynamic memory
};

class Dog : public Animal {
public:
    void speak() const override { std::cout << "Woof! Woof!\n"; }
    void wagTail() const { std::cout << "Wagging tail...\n"; }
};

// This function causes SLICING because it takes Animal by value
void sliceMe(Animal a) {
    a.speak(); // Will always call Animal::speak(), even if a Dog is passed
}

int main() {
    // --- 1. LOCAL OBJECT (Stack) ---
    {
        Dog localDog;
        std::cout << "Local: ";
        localDog.speak();
    } // localDog is automatically destroyed here

    // --- 2. DYNAMIC OBJECT (Heap) ---
    Animal* dynamicDog = new Dog();
    std::cout << "Dynamic: ";
    dynamicDog->speak(); // Uses polymorphism to call Dog::speak()

    delete dynamicDog; // MUST manually delete to avoid memory leak

    // --- 3. OBJECT SLICING ---
    Dog myDog;
    std::cout << "Slicing demonstration: ";
    sliceMe(myDog); // The 'Dog' parts are sliced away!

    return 0;
}