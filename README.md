# US Holidays ICS

A Python script to generate an iCal ICS file with federal and other popular
holidays in the United States.

It will generate events 5 years out from the date of script execution. Note that
Easter requires manual adjustment, so its dates are hardcoded up to **2029**.

The ICS file in this repository was generated on **October 30, 2024**.

## Usage

Import the `us_holidays.ics` into your calendar software of choice.

## Regenerate the File

You must have Python and git installed.

Clone this repository.

```sh
git clone https://github.com/travishorn/us_holidays_ics
```

Change into the directory.

```sh
cd us_holidays_ics
```

Install the dependencies.

```sh
pip install -r requirements.txt
```

Generate the ICS file.

```sh
python main.py
```

A file named `us_holidays.ics` will be written to the project root.

## License

The MIT License (MIT)

Copyright 2024 Travis Horn

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the “Software”), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
