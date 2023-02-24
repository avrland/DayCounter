# DayCounter-pyqt

DayCounter-pyqt is a simple desktop application built using PyQt5 framework. It's simple tool to calculate day from selected day (from future or past). There are ready to use releases for Windows, however you can simply run in on rest of OS.

## Usage

1. Clone repo

```
git clone https://github.com/avrland/DayCounter-pyqt.git
```

2. Run it

```
python start.py
```

## Features

- allows you to select date manually from calender
- reading date from json list
- can calculate dates from future and past

## Json events date list

I provide example list in event_list.json. Name of file is irrelevant, I'm simply taking first found json file from root path.
```json
{
    "September 11 attacks": "11.09.2001",
    "United States invasion of Iraq": "20.03.2003",
    "Fall of Baghdad": "04.04.2003",
    "Indian Ocean earthquake and tsunami": "26.12.2004",
    "Hurricane Katrina": "29.08.2005",
    "Beijing Olympics opening ceremony": "08.08.2008",
    "Barack Obama elected President of the United States": "04.11.2008",
    "Tohoku earthquake and tsunami in Japan": "11.03.2011",
    "Death of Osama bin Laden": "02.05.2011",
    "United Kingdom European Union membership referendum": "23.06.2016",
    "United States presidential election": "08.11.2016",
    "Donald Trump elected President of the United States": "08.11.2016",
    "Donald Trump's inauguration as President of the United States": "20.01.2017",
    "2017 Las Vegas shooting": "03.10.2017",
    "GDPR comes into effect in the European Union": "25.05.2018",
    "Collapse of Morandi Bridge in Italy": "10.08.2018",
    "Notre-Dame de Paris fire": "15.04.2019",
    "Hong Kong protests": "15.06.2019",
    "Outbreak of COVID-19 in Wuhan, China": "31.12.2019",
    "WHO declares COVID-19 a pandemic": "11.03.2020"
  }
```
## Contributing

Contributions are always welcome!

## License

This project is licensed under the [GNU GPL](LICENSE).
