# Gregors Lasenbergs (s1075747)


from Day import Day
from datetime import date

TODAY = date.today()


class Month:
    year_nr = 0
    month_nr = 0
    month_string = ""
    months = {"JANUARY": 31, "FEBRUARY": 28, "MARCH": 31, "APRIL": 30, "MAY": 31, "JUNE": 30, "JULY": 31, "AUGUST": 31,
              "SEPTEMBER": 30, "OCTOBER": 31, "NOVEMBER": 30, "DECEMBER": 31}

    def __init__(self, year_nr, month):
        """
        Constructor for the Month object

        Args:
            year_nr (int): year for the month
            month (int): number of the month

        Return:
            None
        """
        self.days_in_month = []
        self.year_nr = year_nr

        if self.check_leap():
            self.months.update({"FEBRUARY": 29})

        # Making month when month number is given
        self.month_string = self.get_month_from_number(month)
        self.month_nr = month
        self.add_days_to_month(self.get_month_from_number(month))

    def __str__(self):
        """
        String representation of the month

        Returns:
            None
        """
        # Adds month name and weekdays
        full_month = "\t\t"+self.get_month_string().center(10) + "\t\t\t\n"
        full_month += "Mon\tTue\tWed\tThu\tFri\tSat\tSun\t" \
                      "\n"
        # Formats the day strings with correct spacing according to weekdays
        for day in self.days_in_month:
            if day.number == 1:
                full_month += "\t" * (self.day_in_week(day) - 1)
            full_month += (str(day) + "\t")
            if (self.day_in_week(day) % 7) == 0 and day.number != len(self.days_in_month):
                full_month += "\n"
            if day.number == len(self.days_in_month) and (self.day_in_week(day) % 7) != 0:
                full_month += "\t" * (7 - self.day_in_week(day))
        return full_month

    def add_days_to_month(self, month):
        """
        Adds days for the list in the month

        Args:
            month (str): Name of the month

        Returns:
            None
        """
        until = self.months.get(month)
        today_date = str(TODAY).split("-")
        for day in range(0, until):
            new_day = Day(day)
            if today_date[1] == self.get_month_nr_two_digits() and today_date[2] == str(int(day)+1):
                new_day.this_date = True
            self.days_in_month.append(new_day)

    def get_month_from_number(self, nr):
        """
        Return month string from the month number

        Args:
            nr (int): month number

        Returns:
            str: Name of the month
        """
        keys = list(self.months.keys())
        return keys[nr - 1]

    def get_number_from_string(self, month):
        """
        Returns number of the month from the month name

        Args:
            month (str): name of the month

        Returns:
            int: number of the month
        """
        keys = list(self.months.keys())
        return keys.index(month) + 1

    def get_month_string(self):
        """
        Return name of the month

        Returns
            str: name of the month
        """
        return self.month_string

    def get_month_nr_two_digits(self):
        """
        Return month number in two digits

        Returns
            int:
        """
        return "{:0>2d}".format(self.month_nr)

    def day_in_week(self, day):
        """
        Return number that indicated a day in the week using Zeller’s Congruence

        Args:
            day (int): day in the month

        Returns:
            int: number that indicates day in the week
        """
        year = self.year_nr
        month = self.month_nr
        if month == 1:
            month = 13
            year -= 1
        if month == 2:
            month = 14
            year -= 1

        K = year % 100
        J = year / 100
        number_of_day = int((day.number + ((13 * (month + 1)) / 5) + K + (K / 4) + (J / 4) - (2 * J)) % 7)
        number_of_day += 6
        number_of_day %= 7
        if number_of_day == 0:
            number_of_day = 7
        return number_of_day

    def check_leap(self):
        """
        Checks leap year

        Returns:
            bool: returns true if a year is leap year
        """
        # Checking if the given year is leap year
        if ((self.year_nr % 400 == 0) or
                (self.year_nr % 100 != 0) and
                (self.year_nr % 4 == 0)):
            return True
        else:
            return False
