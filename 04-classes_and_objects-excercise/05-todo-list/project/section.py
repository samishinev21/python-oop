class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)

            return f"Task {new_task} is added to the section"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"
        
    def clean_section(self):
        completed = 0
        for task in self.tasks:
            if task.completed:
                completed += 1
        
        self.tasks = [task for task in self.tasks if not task.completed]

        return f"Cleared {completed} tasks."
    
    def view_section(self):
        result = "\n".join([task.details() for task in self.tasks])
        return f"Section {self.name}:\n{result}"