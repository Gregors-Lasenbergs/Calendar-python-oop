# Gregors Lasenbergs (s1075747)


class Event:
    name = ""
    description = ""
    start_time = ""
    end_time = ""
    duration_in_minutes = 0

    def __init__(self, name, description, start_time, end_time):
        """
        Constructor for the Event object

        Args:
            name (str): name of the event
            description (str): description of the event
            start_time (str): start time of the event
            end_time (str): end time of the event
        """
        self.name = name
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        if start_time.split(":")[0] > end_time.split(":")[0] and start_time.split(":")[1] > end_time.split(":")[1]:
            self.start_time = "00:00"
            self.end_time = "23:59"
        self.duration_in_minutes = self.duration_minutes()

    def print_event(self):
        """
        Returns event with all it's data

        Returns:
            str: event and it's data
        """
        return ("\n" + self.name + "\n" +
                "Description: " + self.description + "\n" +
                "Start time: " + self.start_time + "\n" +
                "End time: " + self.end_time + "\n" +
                "Duration: " + self.duration())

    def duration(self):
        """
        Returns duration of the event as a string

        Returns:
            str: duration string with units
        """
        start = self.start_time.split(":")
        end = self.end_time.split(":")
        hours = int(end[0]) - int(start[0])

        if int(end[1]) - int(start[1]) < 0:
            hours -= 1
            minutes = (int(end[1]) + 60) - int(start[1])
        else:
            minutes = int(end[1]) - int(start[1])

        # Return duration in the correct string format
        if hours == 0:
            return str(minutes) + "min"
        elif minutes == 0:
            return str(hours) + "h"
        else:
            return str(hours) + "h " + str(minutes) + "min"

    def duration_minutes(self):
        """
        Returns duration in minutes

        Returns:
            int: duration in minutes
        """
        start = self.start_time.split(":")
        end = self.end_time.split(":")
        hours = int(end[0]) - int(start[0])

        if int(end[1]) - int(start[1]) < 0:
            hours -= 1
            minutes = (int(end[1]) + 60) - int(start[1])
        else:
            minutes = int(end[1]) - int(start[1])
        return (int(hours) * 60) + int(minutes)
