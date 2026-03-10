-- File: CurryPartialDemo.hs

-- 1. Currying (Implicit in Haskell)
-- Though this looks like it takes two arguments, Haskell treats it
-- as a function that takes one 'Int' and returns a function (Int -> Int).
add :: Int -> Int -> Int
add x y = x + y

-- 2. Partial Evaluation
-- We create a new function 'add10' by applying 'add' to only its first argument.
-- This is only possible because 'add' is curried.
add10 :: Int -> Int
add10 = add 10

-- 3. Higher-Order usage with Partial Application
-- We can partially apply the multiplication operator (*) to create
-- a 'triple' function on the fly.
tripleAll :: [Int] -> [Int]
tripleAll list = map (* 3) list

main :: IO ()
main = do
    putStrLn "--- Currying & Partial Evaluation Demo ---"

    -- Using the fully applied function
    let sumResult = add 5 7
    putStrLn $ "Full Application (add 5 7): " ++ show sumResult

    -- Using the partially evaluated function
    let partialResult = add10 20
    putStrLn $ "Partial Application (add10 20): " ++ show partialResult

    -- Using an inline partial application with map
    let listResult = tripleAll [1, 2, 3]
    putStrLn $ "Map with Partial (* 3): " ++ show listResult