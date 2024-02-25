# Gregors Lasenbergs (s1075747)


class Day:
    number = 0
    this_date = False
    has_event = False
    this_date_symbol = "#"
    event_symbol = "!"

    def __init__(self, number):
        """
        Constructor for Day object

        Args:
            number (int): Day in month

        Returns:
            None
        """
        self.events = []
        self.number = number + 1

    def print_events(self):
        """
        Prints all events for a day

        Returns:
            str: all events
        """
        for event in self.events:
            print(event.print_event())

    def add_event(self, event):
        """
        Adds event to the list

        Args:
            event (Event): Event object that will be added to the list

        Returns:
            None
        """
        self.events.append(event)
        self.has_event = True

    def delete_event(self, name):
        """
        Deletes specified event from the day

        Args:
            name (str): Name of the event

        Returns:
            None
        """
        for event in self.events:
            if event.name == name:
                print("removed")
                self.events.remove(event)
        if len(self.events) == 0:
            self.has_event = False

    def sort(self, sort_by):
        """
        Sorts the list by specified value

        Args:
            sort_by (str): String to indicate sorting method

        Returns:
            None
        """
        if sort_by == "name":
            self.events.sort(key=lambda x: x.name)
        elif sort_by == "description":
            self.events.sort(key=lambda x: x.description)
        elif sort_by == "duration":
            self.events.sort(key=lambda x: x.duration_in_minutes)
        elif sort_by == "start time":
            self.events.sort(key=lambda x: x.start_time)

    def change_today_symbol(self, symbol):
        """
        Changes symbol that indicates today's date in the calendar

        Args:
            symbol (str): New symbol for today's date

        Returns:
            None
        """
        self.this_date_symbol = symbol

    def change_event_symbol(self, symbol):
        """
        Changes symbol that indicates date with event in the calendar

        Args:
            symbol (str): New symbol for date with event

        Returns:
            None
        """
        self.event_symbol = symbol

    def __str__(self):
        """
        String format for Day object

        Returns:
            str: day as a string
        """
        if self.this_date:
            return str(self.number) + self.this_date_symbol
        elif self.has_event:
            return str(self.number) + self.event_symbol
        else:
            return str(self.number)
