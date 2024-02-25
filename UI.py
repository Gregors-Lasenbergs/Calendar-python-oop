# Gregors Lasenbergs (s1075747)


from Year import Year
from Event import Event
from TaskList import TaskList


class UI:
    year = Year

    def __init__(self, this_year):
        """
        Creates new user interface for a this year

        Args:
            this_year (int): number of the year
        """
        self.year = Year(this_year)

    def open_calendar(self):
        """
        Displays the calendar and displays new commands

        Returns:
            None
        """
        self.year.print_year()
        while True:
            print("""\nCommands:
        1) See events in a day
        2) Add event
        3) Add task list
        4) Complete task
        5) Delete event
        6) Back
                    """)
            calendar_answer = input("Please choose a command: ").lower()
            if calendar_answer == "back" or calendar_answer == "6":
                break
            elif calendar_answer == "see events in a day" or calendar_answer == "1":
                self.year.print_year()
                self.see_event_in_day()

            elif calendar_answer == "add event" or calendar_answer == "2":
                self.add_event()
                self.year.print_year()

            elif calendar_answer == "add task list" or calendar_answer == "3":
                self.add_task_list()
                self.year.print_year()

            elif calendar_answer == "complete task" or calendar_answer == "4":
                self.complete_task()
                self.year.print_year()

            elif calendar_answer == "delete event" or calendar_answer == "5":
                self.delete_event()
                self.year.print_year()

            else:
                print("This command doesnt exist!")

    def see_event_in_day(self):
        """
        Asks for day details and displays all the events in a day

        Returns:
            None
        """
        # Asks for user input
        values = self.get_month_and_day_input()
        month = values[0]
        day = values[1]
        UI.year.months_in_year[int(month) - 1].days_in_month[int(day) - 1].print_events()

    def add_task_list(self):
        """
        Asks for day details and adds task list to a day

        Returns:
            None
        """
        # Asks for user input
        values = self.get_month_and_day_input()
        month = values[0]
        day = values[1]

        for event in UI.year.months_in_year[month - 1].days_in_month[int(day) - 1].events:
            if isinstance(event, TaskList):
                print("Day can only have maximum of one task list!")
                break
            else:
                task_list_name = input("Enter name of the task list: ")

                # Safely receives task amount
                task_amount = 0
                try:
                    task_amount = int(input("How many tasks you want to add?: "))
                    if int(task_amount) <= 0:
                        raise ValueError
                except ValueError:
                    while not isinstance(day, int) or int(task_amount) <= 0:
                        try:
                            task_amount = int(input("How many tasks you want to add?: "))
                        except ValueError:
                            pass
                task_amount = int(task_amount)

                # Adds all tasks
                description = "!Tasks!:"
                for task in range(1, task_amount+1):
                    description += "!T!" + input("Please enter the name of the task "+str(task)+": ").lower()

                # Adds task to the day
                task_list = TaskList(task_list_name, description)
                UI.year.months_in_year[month - 1].days_in_month[int(day) - 1].add_event(task_list)

                # Prepares a string that will be added to the text file
                in_file = open("events.txt", "r")
                new_text = ""
                lines = in_file.readlines()
                for line in lines:
                    new_text += line
                new_text += "\n" + str(
                    month) + "_-_" + str(
                    day) + "_-_" + task_list_name + "_-_" + description + "_-_" + "00:00" + "_-_" + "23:59" + "_-_\n"
                in_file.close()

                # Empty lines removed, to avoid errors
                self.remove_empty_lines_and_write(new_text)

    def complete_task(self):
        """
        Completes one task in a task list by adding "[done]" string

        Returns:
            None
        """
        # Asks for user input
        values = self.get_month_and_day_input()
        month = values[0]
        day = values[1]

        for event in UI.year.months_in_year[month - 1].days_in_month[int(day) - 1].events:
            if isinstance(event, TaskList):
                task = input("Please enter the name of the task: ").lower()
                description = event.complete_task(task)

                # Prepares a string that will be added to the text file
                in_file = open("events.txt", "r")
                new_text = ""
                lines = in_file.readlines()
                for line in lines:
                    if str(month) + "_-_" + str(day) + "_-_" + event.name + "_-_" in line:
                        new_text += "\n" + str(month) + "_-_" + str(day) + "_-_" + event.name + "_-_" + description \
                                    + "_-_" + "00:00" + "_-_" + "23:59" + "_-_\n"
                    else:
                        new_text += line
                in_file.close()

                # Empty lines removed, to avoid errors
                self.remove_empty_lines_and_write(new_text)

    def add_event(self):
        """
        Asks for day details and adds event to a day

        Returns:
            None
        """
        # Asks for user input
        values = self.get_month_and_day_input()
        month = values[0]
        day = values[1]
        event_name = input("Enter name of the event: ")
        description = input("Enter description about the event: ")
        while True:
            try:
                start_time = input("Input start time for the event (24h): ")

                if len(start_time.split(":")[0]) == 2 and 24 > int(start_time.split(":")[0]) >= 0 and \
                        len(start_time.split(":")[1]) == 2 and 60 > int(start_time.split(":")[1]) >= 0:
                    break
            except IndexError:
                pass

        while True:
            try:
                end_time = input("Input end time for the event (24h): ")

                # Gets the input in "00:00" format. And end time can't be bigger than start time.
                # One small if statement for the program, one giant leap for mankind.
                if len(end_time.split(":")[0]) == 2 and 24 > int(end_time.split(":")[0]) >= 0 and \
                        len(end_time.split(":")[1]) == 2 and 60 > int(end_time.split(":")[1]) >= 0 and \
                        ((int(end_time.split(":")[0]) > int(start_time.split(":")[0])) or
                         (int(end_time.split(":")[0]) == int(start_time.split(":")[0]) and
                          (int(end_time.split(":")[1]) >= int(start_time.split(":")[1])))):
                    break
            except IndexError:
                pass

        event = Event(event_name, description, start_time, end_time)
        UI.year.months_in_year[month - 1].days_in_month[int(day) - 1].add_event(event)

        # Prepares a string that will be added to the text file
        in_file = open("events.txt", "r")
        new_text = ""
        lines = in_file.readlines()
        for line in lines:
            new_text += line
        new_text += "\n" + str(
            month) + "_-_" + str(
            day) + "_-_" + event_name + "_-_" + description + "_-_" + start_time + "_-_" + end_time + "_-_\n"
        in_file.close()

        # Empty lines removed, to avoid errors
        self.remove_empty_lines_and_write(new_text)

    def delete_event(self):
        """
        Asks for the event details and deletes event from the day

        Returns:
            None
        """
        # Gets the date that contains the event
        values = self.get_month_and_day_input()
        month = values[0]
        day = values[1]

        # Prepares a string that will be added to the text file
        event_name = input("Enter name of the event you want to delete: ")
        UI.year.months_in_year[month - 1].days_in_month[int(day) - 1].delete_event(event_name)
        in_file = open("events.txt", "r")
        new_text = ""
        lines = in_file.readlines()
        for line in lines:
            if (str(month) + "_-_" + str(day) + "_-_" + event_name) not in line:
                new_text += line
            else:
                pass
        in_file.close()

        # Empty lines removed, to avoid errors
        self.remove_empty_lines_and_write(new_text)

    def setting(self):
        """
        Displays settings and commands for the settings

        Returns:
            None
        """
        while True:
            print("""Commands:
        1) Change today's date indicator
        2) Change event day indicator
        3) Sorting
        4) Back
                    """)
            setting_answer = input("Please choose a command: ").lower()
            if setting_answer == "back" or setting_answer == "4":
                break

            elif setting_answer == "change today's date indicator" or setting_answer == "1":
                setting_answer = input("Please enter a symbol with length 1: ")
                while len(setting_answer) > 1:
                    setting_answer = input("Please a enter symbol with length 1: ")
                self.year.change_today_symbol(setting_answer)

            elif setting_answer == "change event day indicator" or setting_answer == "2":
                setting_answer = input("Please enter a symbol with length 1: ")
                while len(setting_answer) > 1:
                    setting_answer = input("Please a enter symbol with length 1: ")
                self.year.change_event_symbol(setting_answer)

            elif setting_answer == "sorting" or setting_answer == "3":
                self.sorting()

            else:
                print("This command doesnt exist!")

    def sorting(self):
        """
        Displays sorting options and asks commands

        Returns:
            None
        """
        while True:
            print("""Sort by:
        1) Name
        2) Description
        3) Duration
        4) Start time
        5) Back
                    """)
            sorting_answer = input("Please choose a command: ").lower()
            if sorting_answer == "back" or sorting_answer == "5":
                break

            elif sorting_answer == "name" or sorting_answer == "1":
                self.year.sort_events("name")

            elif sorting_answer == "description" or sorting_answer == "2":
                self.year.sort_events("description")

            elif sorting_answer == "duration" or sorting_answer == "3":
                self.year.sort_events("duration")

            elif sorting_answer == "start time" or sorting_answer == "4":
                self.year.sort_events("start time")

            else:
                print("This command doesnt exist!")

    def read_events(self, filename="events.txt"):
        """
        Reads all the saved events from a text file

        Args:
            filename (str): name of the file that will be read

        Returns:
            None
        """
        in_file = open(filename, "r")
        line = " "
        while line:
            line = in_file.readline()
            if line != "":
                try:
                    data_list = line.split("_-_")
                    if "!Tasks!:" in data_list[3]:
                        task_list = TaskList(data_list[2], data_list[3], data_list[4], data_list[5])
                        UI.year.months_in_year[int(data_list[0]) - 1].days_in_month[int(data_list[1]) - 1].add_event(
                            task_list)
                    else:
                        event = Event(data_list[2], data_list[3], data_list[4], data_list[5])
                        UI.year.months_in_year[int(data_list[0]) - 1].days_in_month[int(data_list[1]) - 1].add_event(event)
                finally:
                    pass
        in_file.close()

    def get_month_and_day_input(self):
        """
        Safely receives input for a month and a day

        Returns:
            list: with first value as a month and second value as a day in a month
        """
        month = ""
        day = ""
        # Get's month without any user errors
        try:
            month = int(input("Which month is this event or task list happening? (1-12): "))
            if 13 <= int(month) or int(month) <= 0:
                raise ValueError
        except ValueError:
            while not isinstance(month, int) or 13 <= int(month) or int(month) <= 0:
                try:
                    month = int(input("Please enter a month number from 1 to 12: "))
                except ValueError:
                    pass
            month = int(month)

        max_days = UI.year.months_in_year[int(month) - 1].months.get(
            UI.year.months_in_year[int(month) - 1].get_month_string())

        # Get's day without user errors
        try:
            day = int(input("Which day is this event or task list happening? (1-" + str(max_days) + "): "))
            if int(max_days) < int(day) or int(day) <= 0:
                raise ValueError
        except ValueError:
            while not isinstance(day, int) or int(max_days) < int(day) or int(day) <= 0:
                try:
                    day = int(input("Please enter a day from 1 to " + str(max_days) + ": "))
                except ValueError:
                    pass
            day = int(day)
        return [month, day]

    def remove_empty_lines_and_write(self, text):
        """
        Removes empty lines from a string and writes the string in the text document

        Args:
            text (str): string that will have empty lines removed

        Returns:
            None
        """
        # Prepares a string that will be added to the text file
        lines = text.split("\n")
        non_empty_lines = [line for line in lines if line.strip() != ""]
        string_without_empty_lines = ""
        for line in non_empty_lines:
            string_without_empty_lines += line + "\n"

        # writes the new string to the text document
        in_file = open("events.txt", "w")
        in_file.write(string_without_empty_lines)
        in_file.close()

    def start_ui(self):
        """
        Starts user interface and displays menu commands

        Returns:
            None
        """
        UI.read_events(self)

        while True:
            print("""Commands:
            1) Open calendar
            2) Settings
            3) Quit
            """)
            answer = input("Please choose a command: ").lower()
            if answer == "open calendar" or answer == "1":
                UI.open_calendar(self)
            elif answer == "settings" or answer == "2":
                UI.setting(self)
            elif answer == "quit" or answer == "3":
                break
            else:
                print("This command doesnt exist!")
