import Data.Char (isSpace)
import Data.List (isInfixOf)
import Data.List.Split (splitOn)
import System.IO (readFile)

solve input = do
  let inputLines = lines input
  let result = map gemCount inputLines
  sum (map calValue (zipWithIndex result))

calValue tuple = do
  if (snd tuple) == True
    then (fst tuple) + 1
    else 0

strip :: String -> String
strip = f . f
  where
    f = reverse . dropWhile isSpace

allTrue = all id

zipWithIndex xs = zip [0 ..] xs

gemCount line = do
  let gameData = splitOn ":" line !! 1
  let rounds = splitOn ";" gameData
  allTrue (map validRound rounds)

validRound round = do
  let gems = splitOn "," round
  allTrue (map validGem gems)

validGem gemData = do
  let num = read (head (splitOn " " (strip gemData))) :: Int
  not ((isInfixOf "red" gemData && num > 12) || (isInfixOf "green" gemData && num > 13) || (isInfixOf "blue" gemData && num > 14))

main :: IO ()
main = do
  input <- readFile "input/input.txt"
  print $ solve input
