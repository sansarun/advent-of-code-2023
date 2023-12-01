import Data.Char (isDigit)
import System.IO (readFile)

calculateSum :: String -> Int
calculateSum input = sum (map readCalibrationValue (lines input))
  where
    readCalibrationValue :: String -> Int
    readCalibrationValue line =
      let digits = filter isDigit line
       in if null digits
            then 0
            else read [head digits, last digits] :: Int

main :: IO ()
main = do
  input <- readFile "input/sample.txt"
  print $ calculateSum input
