from Event import Event
# Gregors Lasenbergs (s1075747)


class TaskList(Event):

    def __init__(self, name, description="!Tasks!:", start_time="00:00", end_time="23:59"):
        """
        Constructor for a new TaskList object

        Args:
            name (str): name of the task list
            description (str): Designated place for tasks
            start_time (str): default value task list "00:00"
            end_time (str): default value task list "23:59"
        """
        super().__init__(name, description, start_time, end_time)

    def add_tasks(self, task):
        """
        Adds one task to the task list

        Args:
            task(str): the name of the task

        Returns:
            None
        """
        self.description += "!T!"+str(task)

    def complete_task(self, task):
        """
        Completes one task by adding "[done]" to the string

        Args:
            task(str): Name of the task

        Returns:
            str: the new description string
        """
        if task+" [done]" in self.description:
            print("Task already done!")
        elif "!T!"+task:
            print("Task done!")
            self.description = self.description.replace("!T!"+task, "!T!"+task+" [done]")
            return self.description
        else:
            print("This task doesn't exist!")

    def print_event(self):
        """
        Returns event with all it's data

        Returns:
            str: event and it's data
        """
        tasks = self.description.split("!T!")
        event = ("\n" + self.name + "\n" +
                 "Tasks: " + "\n")
        for index in range(1, len(tasks)):
            event += "\t"+str(index)+") "+tasks[index]+"\n"
        return event
