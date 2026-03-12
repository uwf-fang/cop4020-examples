-- This will work because the digit '7' appears eventually!
allKeysWithSeven :: [String]
allKeysWithSeven = [ "Key" ++ show n | n <- [1..], '7' `elem` show n ]

main :: IO ()
main = do
    putStrLn "Finding keys that contain the digit '7'..."
    -- This will now return [ "Key7", "Key17", "Key27", "Key37", "Key47" ]
    print $ take 5 allKeysWithSeven
