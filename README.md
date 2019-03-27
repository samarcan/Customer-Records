# Intercom - Customer records

This program has been developed in python 3 and does not use any external library.

## How to run the program
Execute the following command in a terminal inside the folder of the project:

```
python3 customrrecords
```

This program has been configured to stored a log of each action in a file inside the `log` folder. If the `log` folder does not exist will be created automatically. You can see and example in `log_example.txt`.

## Output

```
Id: 4   Name: Ian Kehoe
Id: 5   Name: Nora Dempsey
Id: 6   Name: Theresa Enright
Id: 8   Name: Eoin Ahearn
Id: 11  Name: Richard Finnegan
Id: 12  Name: Christina McArdle
Id: 13  Name: Olive Ahearn
Id: 15  Name: Michael Ahearn
Id: 17  Name: Patricia Cahill
Id: 23  Name: Eoin Gallagher
Id: 24  Name: Rose Enright
Id: 26  Name: Stephen McArdle
Id: 29  Name: Oliver Ahearn
Id: 30  Name: Nick Enright
Id: 31  Name: Alan Behan
Id: 39  Name: Lisa Ahearn
```

## How to run the unittests

Execute the following command in a terminal inside the folder of the project:
```
python3 -m unittest discover -s tests/
```