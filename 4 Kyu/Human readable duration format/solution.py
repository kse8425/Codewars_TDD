MAX_SECOND = 60
MAX_MINUTE = 60
MAX_HOUR = 24
MAX_DAY = 365


def format_duration(seconds):
    if seconds == 0:
        return 'now'
    return Timer(seconds).result()


class Timer:
    def __init__(self, seconds):
        self.seconds = seconds
        self._format_time()

    def _format_time(self):
        minutes, seconds = divmod(self.seconds, MAX_SECOND)
        hours, minutes = divmod(minutes, MAX_MINUTE)
        days, hours = divmod(hours, MAX_HOUR)
        years, days = divmod(days, MAX_DAY)
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
        self.days = days
        self.years = years

    def get_str_seconds(self):
        unit = 'seconds' if self.seconds > 1 else 'second'
        return f'{self.seconds} {unit}'

    def get_str_minutes(self):
        unit = 'minutes' if self.minutes > 1 else 'minute'
        return f'{self.minutes} {unit}'

    def get_str_hours(self):
        unit = 'hours' if self.hours > 1 else 'hour'
        return f'{self.hours} {unit}'

    def get_str_days(self):
        unit = 'days' if self.days > 1 else 'day'
        return f'{self.days} {unit}'

    def get_str_years(self):
        unit = 'years' if self.years > 1 else 'year'
        return f'{self.years} {unit}'

    def result(self):
        arr = self.make_arr()
        if len(arr) == 1:
            return arr[0]
        if len(arr) >= 2:
            last_element = arr.pop(-1)
            return ', '.join(arr) + f' and {last_element}'

    def make_arr(self):
        seconds = self.get_str_seconds()
        minutes = self.get_str_minutes()
        hours = self.get_str_hours()
        days = self.get_str_days()
        years = self.get_str_years()
        result = []
        if self.years > 0:
            result.append(years)
        if self.days > 0:
            result.append(days)
        if self.hours > 0:
            result.append(hours)
        if self.minutes > 0:
            result.append(minutes)
        if self.seconds > 0:
            result.append(seconds)
        return result
