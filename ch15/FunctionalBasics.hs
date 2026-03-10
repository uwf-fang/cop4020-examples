-- File: FunctionalBasics.hs

-- 1. Recursion: Standard vs Tail Recursive
-- Standard: Multiplies after the recursive call returns (unwinding stack).
factorialStandard :: Integer -> Integer
factorialStandard 0 = 1
factorialStandard n = n * factorialStandard (n - 1)

-- Tail Recursive: Recursive call is the last operation.
-- Uses an accumulating parameter (acc) for efficiency.
factorialTail :: Integer -> Integer
factorialTail n = helper n 1
  where
    helper 0 acc = acc
    helper n acc = helper (n - 1) (n * acc)

-- 2. Higher-Order Functions: Apply-to-All (Map)
-- Cubes every number in a list using a lambda expression.
cubeAll :: [Integer] -> [Integer]
cubeAll list = map (\x -> x * x * x) list

-- 3. List Comprehensions: Derived from set notation.
-- Returns cubes of even numbers from a range.
evenCubes :: Integer -> [Integer]
evenCubes maxVal = [x * x * x | x <- [1..maxVal], x `mod` 2 == 0]

main :: IO ()
main = do
    putStrLn $ "Standard 5!: " ++ show (factorialStandard 5)
    putStrLn $ "Tail-Recursive 5!: " ++ show (factorialTail 5)
    putStrLn $ "Cubes: " ++ show (cubeAll [1..3])
    putStrLn $ "Even Cubes (1-10): " ++ show (evenCubes 10)
