from ics import Calendar, Event
from datetime import datetime, timedelta

def get_nth_weekday_of_month(year, month, weekday, occurrence):
    first_day_of_month = datetime(year, month, 1)
    first_weekday_of_month = first_day_of_month.weekday()
    days_to_first_weekday = (weekday - first_weekday_of_month + 7) % 7
    if occurrence == "last":
        # Find the last weekday of the month
        last_day_of_month = (first_day_of_month + timedelta(days=32)).replace(day=1) - timedelta(days=1)
        last_weekday_of_month = last_day_of_month.weekday()
        days_to_last_weekday = (last_weekday_of_month - weekday + 7) % 7
        event_date = last_day_of_month - timedelta(days=days_to_last_weekday)
    else:
        # Find the nth weekday of the month
        event_date = first_day_of_month + timedelta(days=days_to_first_weekday + (occurrence - 1) * 7)
    return event_date

def add_events(holiday, calendar, years):
    current_year = datetime.now().year
    
    if "recurring" in holiday and not holiday["recurring"]:
        event = Event()
        event.name = holiday["name"]
        event.begin = datetime(holiday["year"], holiday["month"], holiday["day"])
        event.make_all_day()
        calendar.events.add(event)
    else:
      for year in range(current_year, current_year + years):
          if "day" in holiday:
              # Fixed-date holiday
              event_date = datetime(year, holiday["month"], holiday["day"])
          else:
              # Weekday-based holiday
              event_date = get_nth_weekday_of_month(year, holiday["month"], holiday["weekday"], holiday["occurrence"])
          
          event = Event()
          event.name = holiday["name"]
          event.begin = event_date
          event.make_all_day()
          calendar.events.add(event)

holidays = [
    { "name": "New Year's Day", "month": 1, "day": 1 },
    { "name": "Groundhog Day", "month": 2, "day": 2 },
    { "name": "Martin Luther King Jr. Day", "month": 1, "weekday": 0, "occurrence": 3 },
    { "name": "Valentine's Day", "month": 2, "day": 14 },
    { "name": "Presidents' Day", "month": 2, "weekday": 0, "occurrence": 3 },
    { "name": "St. Patrick's Day", "month": 3, "day": 17 },
    { "name": "April Fool's Day", "month": 4, "day": 1 },
    { "name": "Earth Day", "month": 4, "day": 22 },
    { "name": "Mother's Day", "month": 5, "weekday": 6, "occurrence": 2 },
    { "name": "Memorial Day", "month": 5, "weekday": 0, "occurrence": "last" },
    { "name": "Flag Day", "month": 6, "day": 14 },
    { "name": "Father's Day", "month": 6, "weekday": 6, "occurrence": 3 },
    { "name": "Juneteenth", "month": 6, "day": 19 },
    { "name": "Independence Day", "month": 7, "day": 4 },
    { "name": "Labor Day", "month": 9, "weekday": 0, "occurrence": 1 },
    { "name": "Patriot Day", "month": 9, "day": 11 },
    { "name": "Columbus Day", "month": 10, "weekday": 0, "occurrence": 2 },
    { "name": "Halloween", "month": 10, "day": 31 },
    { "name": "Veterans Day", "month": 11, "day": 11 },
    { "name": "Thanksgiving Day", "month": 11, "weekday": 3, "occurrence": 4 },
    { "name": "Christmas Day", "month": 12, "day": 25 },
    { "name": "Easter", "year": 2024, "month": 3, "day": 31, "recurring": False },
    { "name": "Easter", "year": 2025, "month": 4, "day": 20, "recurring": False },
    { "name": "Easter", "year": 2026, "month": 4, "day": 5, "recurring": False },
    { "name": "Easter", "year": 2027, "month": 3, "day": 28, "recurring": False },
    { "name": "Easter", "year": 2028, "month": 4, "day": 16, "recurring": False },
    { "name": "Easter", "year": 2029, "month": 4, "day": 1, "recurring": False }
]

calendar = Calendar()

for holiday in holidays:
    add_events(holiday, calendar, 5)



with open("us_holidays.ics", "w") as file:
    file.writelines(calendar)
