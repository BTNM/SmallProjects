# Import the necessary libraries
from ipywidgets import widgets
from IPython.display import display


# Function to add a task
def add_task(button):
    task = text.value
    if task:
        tasks.append(task)
        list_box.value = "\n".join(tasks)
        text.value = ""


# GUI setup
text = widgets.Text(placeholder="Enter task")
add_button = widgets.Button(description="Add Task")
add_button.on_click(add_task)
list_box = widgets.Textarea(value="", disabled=True)

# Display the widgets
display(text)
display(add_button)
display(list_box)

# List to store tasks
tasks = []
