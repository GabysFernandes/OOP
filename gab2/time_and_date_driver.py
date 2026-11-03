from datetime import date, datetime, timedelta, timezone

from event_countdown import EventCountdown

def days_until_next_christmas(today: date | None = None) -> int:
    if today is None:
        today = date.today()
    christmas = date(today.year, 12, 25)
    if today > christmas:
        christmas = date(today.year + 1, 12, 25)
    return (christmas - today).days

def next_birthday(month: int, day: int, today: date | None = None) -> date:

    if today is None:
        today = date.today()
    year = today.year
    while True:
        try:
            birthday = date(year, month, day)
        except ValueError:
            if (month, day) != (2,29):
                raise
            year += 1
            continue
        if birthday >= today:
            return birthday
        year += 1

def days_until_next_birthday(
        month: int, day: int, today: date | None = None
) -> int:
    if today is None:
        today = date.today()
    return (next_birthday(month, day, today) - today).days

def parse_date(text: str) -> datetime:
    return datetime.strptime(text.strip(), "%Y-%m-%d %H:%M")

class TimeAndDateDriver:
    def run(self) -> None:
        print("=" * 58)
        print("WEEK 7 | Time and date in python")
        print("=" * 58)
        self.show_app_details()
        self.utc_demo
        self.local_to_utc()
        self.date_formatting()
        self.christmas_countdown()
        self.duration_and_deadline()
        self.parse_date_string()
        self.event_countdown_driver()
        print ("\nFinished. Try the manu in challenge_solution.py!")

    def show_app_details(self) -> None:
        print("\n[1] Application details")

    def utc_demo(self) -> None:
        print("\n[2] Local time and UTC")
        # Two aware times representing the same instant:
        local_now = datetime.now().astimezone()
        utc_now = local_now.astimezone(timezone.utc)
        print(f"Local time: {local_now:%Y-%m-%d %H:%M:%S %z}")
        print(f"UTC time:   {utc_now:%Y-%m-%d %H:%M:%S %z}")

    def local_to_utc(self) -> None:
        print("\n[3] Converting local time to UTC")
        local_now = datetime.now().astimezone()
        converted = local_now.astimezone(timezone.utc)
        print("Local:", local_now.isoformat(timespec="seconds"))
        print("UTC:  ", converted.isoformat(timespec="seconds"))
        print("Same instant?", local_now == converted)

    def date_formatting(self) -> None:
        print("\n[4] Date and time formatting")
        now = datetime.now().astimezone()
        print("ISO 8601:     ", now.isoformat(timespec="minutes"))
        print("Short date:   ", now.strftime("%d/%m/%Y"))
        print("Readable date:", now.strftime("%A, %d %B %Y %H:%M"))

    def christmas_countdown(self) -> None:
        print("\n[5] Days until next Christmas")
        print("Days remaining:", days_until_next_christmas())

    def birthday_countdown(self) -> None:
        print("\n[6] Days until a birthday (14 June)")
        birthday = next_birthday(6, 14)
        print("Next birthday:", birthday.isoformat())
        print("Days remaining:", days_until_next_birthday(6, 14))

    def duration_and_deadline(self) -> None:
        print("\n[7] Adding a duration to a date")
        start = datetime(2026, 11, 2, 9, 0)
        duration = timedelta(days=2, hours=3, minutes=30)
        deadline = start + duration
        print("Start:", start.strftime("%d/%m/%Y %H:%M"))
        print("Duration:", duration)
        print("Deadline:", deadline.strftime("%d/%m/%Y %H:%M"))
        # This is a simple clock-time demo, not a time-zone scheduling engine.

    def parse_date_string(self) -> None:
        print("\n[8] Parsing a date string")
        text = "2026-12-31 23:59"
        parsed = parse_date(text)
        print("Original text:", text)
        print("Parsed value: ", parsed)
        try:
            parse_date("2026-15-40 09:00")
        except ValueError as error:
            print("Invalid date handled:", type(error).__name__)

    def event_countdown_driver(self) -> None:
        print("\n[9] Object-oriented event countdown")
        event = EventCountdown(date(date.today().year + 1, 6, 14), "Course celebration")
        print(event.describe())