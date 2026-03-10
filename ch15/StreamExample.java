import java.util.*;
import java.util.stream.*;

public class StreamExample {
    public static void main(String[] args) {
        // OOP: Using a List object to store data
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

        // Functional: Using a pipeline (filter and map) with lambda expressions
        List<Integer> evenCubes = numbers.stream()
            .filter(n -> n % 2 == 0)      // Functional: filter
            .map(n -> n * n * n)          // Functional: map (apply-to-all)
            .collect(Collectors.toList());

        System.out.println(evenCubes); // Output: [8, 64]
    }
}