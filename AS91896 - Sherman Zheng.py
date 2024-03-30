import easygui

#DECLARING VARIABLES
PRIORITY_UPPER_LIMIT = 3
PRIORITY_LOWER_LIMIT = 1

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
        "Description": "Implement payment processing for the website",
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
    "JLO": {
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
Outputting the task collection in a readable format, allows the user
to look through all task's informations. 
"""
def output_task_collection():
    output = ""
    for task_id, task_title in Task_Dictionary.items():
        output += f"\nTask ID: {task_id}\n"
        for task_title, task_info in task_title.items():
            output += f"{task_title}: {task_info}\n"

    easygui.msgbox(output)

def output_member_collection():
    output = ""
    for member_id, member_title in Team_Member_Dictionary.items():
        output += f"\nMember ID: {member_id}\n"
        for member_title, member_info in member_title.items():
            output += f"{member_title}: {member_info}\n"

    easygui.msgbox(output)

"""
Adding a new task to the project's task dictionary, in this
situation, the function will ask the user multiple questions.
Such as the title, description, priority, status of the new
created task.
"""

def add_new_task():
    while True:

        #Asking the user to add a title variable of the new task.
        title = easygui.enterbox("Enter the title of the task:")

        #Asking the user to add a description variable of the new task.
        description = easygui.enterbox("Enter the description of the task:")

        #Asking the user to add a priority variable of the new task.
        priority = easygui.integerbox("Enter the priorty rating (1 - 3):",\
        lowerbound= PRIORITY_LOWER_LIMIT, upperbound= PRIORITY_UPPER_LIMIT)
        
        #Asking the user to add a status variable of the new task.
        status = easygui.buttonbox("Select Priority", \
        choices=["Completed", "In Progress", "Blocked"])

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
        
        easygui.msgbox(f"New task added with ID: {new_task_id}.")

        #Asking the user whether or not to make another new task.
        another_new_task = easygui.buttonbox\
            ("Do you want to make another new task?",\
            choices=["Yes", "No"])
        if another_new_task == "No":
            break

"""
Updating a new information to a specific task from the task dictionary.
The function will allows user to update informations in specific task,
which is from the task dictionary.
"""
def update_task():
    while True:
        #Asking the user to update one task from the dictionary.
        update_task = easygui.enterbox\
        ("Enter the task to update: e.g.(T1, T2, T3 ...)")

        if update_task in Task_Dictionary:
                
            #Asking the user to update a status of the task.
            update_status = easygui.buttonbox("Select Priority", \
            choices=["Completed", "In Progress", "Blocked", "Not Started"])

            """
            Removing the task from the previous assignee's task list,
            if completed.
            """    
            if Task_Dictionary[update_task]["Status"] == "Completed":
                old_assignee = Task_Dictionary[update_task]["Assignee"]

                if update_task in Team_Member_Dictionary[old_assignee]\
                    ["Task Assigned"]:

                    Team_Member_Dictionary[old_assignee]\
                    ["Task Assigned"].remove(update_task)
                Task_Dictionary[update_task]["Status"] = update_status

            else:
                #Allows the Dictionary to update "Status" attribute.
                Task_Dictionary[update_task]["Status"] = update_status

            #Asking the user to update an assignee of the task.
            update_assignee = easygui.buttonbox\
            ("Enter the assignee to update:",\
            choices = ["JSM","JLO", "BDI"])

            Task_Dictionary[update_task]["Assignee"] = update_assignee

            #Asking the user whether or not to update another task.
            update_another_task = easygui.buttonbox\
                ("Do you want to update another new task?",\
                choices=["Yes", "No"])
            
            if update_another_task == "No":
                break
        else:
            easygui.msgbox\
            ("Task not found, please enter a valid task. \
            e.g.(T1, T2, T3 ...)")

"""
A main menu that allows the user to click the function that they like.
In this situation, the user will have the oppitunity to select the 
function they wan tot run.
"""

def main_menu():
    """
    Allows the user to repeat in the menu page, through the while loop,
    after the user finish one function.
    """
    while True:
        #Allows the user to make a choice.
        user_choices = easygui.buttonbox( "Select the opinion:", \
        choices=["Output Task Collection", "Add New Task", \
        "Update Task", "Member","Exit"])

        """
        Runs the output task collection function in the programme, 
        if the user click the Output Task Collection button.
        
        """
        """
        Runs the add new task function in the programme, 
        if the user click the Add New Task button.
        """
        """
        Runs the update task function in the programme, 
        if the user click the Update Task button.
        """
        if user_choices == "Output Task Collection":
            output_task_collection()
        elif user_choices == "Add New Task":
            add_new_task()
        elif user_choices == "Member":
            output_member_collection()
        elif user_choices == "Update Task":
            update_task()
        else:
            easygui.msgbox("Goodbye")
            break
main_menu()