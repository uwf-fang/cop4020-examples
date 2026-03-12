import java.util.stream.Stream;

public class LazySquares {
    public static void main(String[] args) {
        int target = 7;

        boolean isPerfect = Stream.iterate(0, n -> n + 1) // Infinite stream: 0, 1, 2...
            .map(n -> n * n)                             // Map to squares: 0, 1, 4...
            .filter(s -> s >= target)                    // Wait until we hit or pass target
            .findFirst()                                 // Grab the very first one that matches
            .map(s -> s == target)                       // Check if it's the target
            .orElse(false);

        System.out.println("Is " + target + " a perfect square? " + isPerfect);
    }
}