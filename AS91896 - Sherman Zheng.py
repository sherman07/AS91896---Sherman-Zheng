import easygui

#The Task Dictionary that stores the information of all tasks.
Task_Dictionary = {
    #Task 1
    "T1": {
        "Title": "Design Homepage",
        "Description": "Create a mockup of the homepage",
        "Assignee": "JSM",
        "Priority": "3",
        "Status": "In Progress"
    },
    #Task 2
    "T2": {
        "Title": "Implement Login page",
        "Description": "Create the Login page for the website",
        "Assignee": "JSM",
        "Priority": "3",
        "Status": "Blocked"
    },
    #Task 3
    "T3": {
        "Title": "Fix navigation menu",
        "Description": "Fix the navigation menu to be more user-friendly",
        "Assignee": "None",
        "Priority": "1",
        "Status": "Not Started"
    },
    #Task 4
    "T4": {
        "Title": "Add payment processing",
        "Description": "Implement payment processing for website",
        "Assignee": "JLO",
        "Priority": "2",
        "Status": "In Progress"
    },
    #Task 5
    "T5": {
        "Title": "Create an About Us Page",
        "Description": "Create a page with information about the company",
        "Assignee": "BDI",
        "Priority": "1",
        "Status": "Blocked"
    }
    
}
#The Team Member Dictionary that stores the information of all member.
Team_Member_Dictionary = {
    #Team member Jone Smith
    "JSM": {
        "Name": "Jone Smith",
        "Email": "John@techvision.com",
        "Task Assigned": "[“T1”,“T2”]"
    },
    #Team member Jane Love
    "JSM": {
        "Name": "Jane Love",
        "Email": "Jane@techvision.com",
        "Task Assigned": "[“T4”]"
    },
    #Team member Bob Dillon
    "BDI": {
        "Name": "Bob Dillon",
        "Email": "Bob@techvision.com",
        "Task Assigned": "[“T5”]"
    }

}

"""
Adding a new task to the project's task dictionary,in this
situation, the function will ask the user multiple questions.
Such as the title, description, priority, status of the new
created task.
"""
def add_new_task():

    #Asking the user to add a title variable of the new task.
    title = easygui.enterbox("Enter the title of the task:")

    #Asking the user to add a description variable of the new task.
    description = easygui.enterbox("Enter the description of the task:")

    #Asking the user to add a priority variable of the new task.
    priority = easygui.buttonbox("Select Priority", \
                                        choices=["1", "2", "3"])
    
    #Asking the user to add a status variable of the new task.
    status = easygui.buttonbox("Select Priority", \
                                        choices=["Completed", \
                                                 "In Progress", "Blocked"])
    """
    The ID = ... will creates a new task ID, having the T as task.
    Having the current number of Task in the dictionary + 1.
    """
    new_task_id = "T" + str(len(Task_Dictionary) + 1)
    
    #The new_task cantains all information that the user had input.
    new_task = {
        "Title": title,
        "Description": description,
        "Assignee": "",
        "Priority": priority,
        "Status": status
    }

    #Adding a new task to the Task_Dictionary, with an ID.
    Task_Dictionary[new_task_id] = new_task
    
    easygui.msgbox("New task added with ID: " + new_task_id)
add_new_task()
"""
Updating a new information to a specific task from the task dictionary.
The function will allows user to update informations in specific task,
which is from the task dictionary.
"""
def update_task():
    #Asking the user to 
    update_task = easygui.enterbox("Enter the task to update:")
    #Asking the user to update a title variable of the specific task.
    update_title = easygui.enterbox("Enter the title to update:")
    update_description = easygui.enterbox("Enter the description to update:")
    update_assignee = easygui.enterbox("Enter the assignee to update:")
    update_priority = easygui.buttonbox("Select Priority", \
                                        choices=["1", "2", "3"])
    update_status = easygui.buttonbox("Select Priority", \
                                        choices=["Completed", \
                                                 "In Progress", "Blocked"])
update_task()
    

