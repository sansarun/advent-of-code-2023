import Data.Char (isDigit)
import System.IO (readFile)

solve :: String -> Int
solve input = sum (map calibrationValue (lines input))
  where
    calibrationValue :: String -> Int
    calibrationValue line =
      let digits = filter isDigit line
       in if null digits
            then 0
            else read [head digits, last digits] :: Int

main :: IO ()
main = do
  input <- readFile "input/input.txt"
  print $ solve input
