# Gregors Lasenbergs (s1075747)


from Month import Month


class Year:
    year_nr = 0
    months_in_year = []

    def __init__(self, year_nr):
        """
        Constructor for Year object

        Args:
            year_nr (int): number of the year
        """
        self.year_nr = year_nr
        for month in range(1, 13):
            self.months_in_year.append(Month(year_nr, month))

    def print_year(self):
        """
        Print out number of the year, names of the months, days of the month and indicators for weekday

        Returns:
            None
        """
        print(str(self.year_nr).center(91) + "\n")
        first_month = 0
        last_month = 3
        for x in range(0, 4):

            for week_nr in range(0, 8):
                for month in range(first_month, last_month):
                    week = str(self.months_in_year[month]).split('\n')
                    if week_nr > len(week)-1:
                        print("\t"*8, end="")
                    else:
                        print(week[week_nr], "\t", end="")
                print("\n", end="")
            print("\n", end="")
            first_month += 3
            last_month += 3

    def change_today_symbol(self, symbol):
        """
        Changes symbol for today's date

        Args:
            symbol(str): new symbol for today's date

        Returns:
            None
        """
        for month in self.months_in_year:
            for day in month.days_in_month:
                day.change_today_symbol(symbol)

    def change_event_symbol(self, symbol):
        """
        Changes symbol for all dates with event

        Args:
            symbol (str): new symbol for days with event

        Returns:
            None
        """
        for month in self.months_in_year:
            for day in month.days_in_month:
                day.change_event_symbol(symbol)

    def sort_events(self, sort_by):
        """
        Sorts events in all days by name, description, duration or start time

        Args:
            sort_by (str): string that indicates sorting method

        Returns:
            None
        """
        for month in self.months_in_year:
            for day in month.days_in_month:
                day.sort(sort_by)
