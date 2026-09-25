import pytz
import zoneinfo
import dateutil.tz  # timezone libraries
import datetime
import icalendar
e = icalendar.Event()
tz = dateutil.tz.tzstr("Europe/London")
e["X-DT-DATEUTIL"] = icalendar.vDatetime(
    datetime.datetime(2024, 6, 19, 10, 1, tzinfo=tz))
tz = pytz.timezone("Europe/London")
e["X-DT-USE-PYTZ"] = icalendar.vDatetime(
    datetime.datetime(2024, 6, 19, 10, 1, tzinfo=tz))
tz = zoneinfo.ZoneInfo("Europe/London")
e["X-DT-ZONEINFO"] = icalendar.vDatetime(
    datetime.datetime(2024, 6, 19, 10, 1, tzinfo=tz))
print(e.to_ical())  # the libraries yield the same result
