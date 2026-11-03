from datetime import date

class EventCountdown:
    def __init__(self, event_date: date, event_name: str = "My event"):
        self.event_date = event_date
        self.event_name = event_name

    def get_days_remaining(self, today: date | None = None) -> int:
        if today is None:
            today = date.today()
        return (self.event_date - today).days

    def describe(self, today: date | None = None) -> str:
        days = self.get_days_remaining(today)

        if days == 0:
            return f"{self.event_name} is today!"
        if days > 0:
            return f"{self.event_name}: {days} day(s) remaining."
        return f"{self.event_name} was {-days} day(s) ago"