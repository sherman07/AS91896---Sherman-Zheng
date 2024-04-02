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
    "JSM": {
        "Name": "Jone Smith",
        "Email": "John@techvision.com",
        "Task Assigned": ["T1", "T2"]
    },
    "JLO": {
        "Name": "Jane Love",
        "Email": "Jane@techvision.com",
        "Task Assigned": ["T4"]
    },
    "BDI": {
        "Name": "Bob Dillon",
        "Email": "Bob@techvision.com",
        "Task Assigned": ["T5"]
    }
}

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
        choices=["Completed", "In Progress", "Blocked", "Not Started"])

        """
        The ID = ... will creates a new task ID, having the T as task.
        Having the current number of Task in the dictionary + 1.
        """
        new_task_id = "T" + str(len(Task_Dictionary) + 1)
        
        #The new_task cantains all information that the user had input.
        new_task = {
            "Title": title,
            "Description": description,
            "Assignee": None,
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

        #If the task can be identified in the Task Dictionary.
        if update_task in Task_Dictionary:

        #Asking the user to update the task status.
            update_status = easygui.buttonbox("Select the new task status:",\
            choices=["Completed", "In Progress", "Blocked", "Not Started"])

        #Update the task status to the Task Dictionary.
            Task_Dictionary[update_task]["Status"] = update_status

        #Asking the user to update the task assignee.
            update_assignee = easygui.buttonbox\
            (f"Enter the name of the assignee to update for {update_task}", 
            choices= ["JSM", "JLO", "BDI"])

            """
            Add the task to the team member's task list, 
            if the task is not in the member task list.
            """
            if update_task not in Team_Member_Dictionary\
                        [update_assignee]["Task Assigned"]:

                        Team_Member_Dictionary[update_assignee]\
                        ["Task Assigned"].append(update_task)
                    
            Task_Dictionary[update_task]["Assignee"] = update_assignee

            """
            Remove the task to the team member's task list, 
            if the task is in the member task list and is completed.
            """
            if update_status == "Completed" and update_task in \
                    Team_Member_Dictionary[Task_Dictionary[update_task]\
                    ["Assignee"]]["Task Assigned"]:
                        
        #Remove the Completed task from the Team Member Dictionary.
                        Team_Member_Dictionary[Task_Dictionary[update_task]\
                        ["Assignee"]]["Task Assigned"].remove(update_task)
                    
            Task_Dictionary[update_task]["Assignee"] = update_assignee

            easygui.msgbox(f"Task {update_task} has been updated")

        #Asking the user whether or not to update another task.
            update_another_task = easygui.buttonbox\
                        ("Do you want to update another new task?",\
                        choices=["Yes", "No"])
                    
            if update_another_task == "No":
                        break
        else:
            easygui.msgbox\
            ("Task not found, please enter a valid task.")
            
"""
Search function will allows user to search a specific task or member.
In this situation, the programme provide two choices for user to click,
Task and Member. Then the user will able to choose the specific task or
member to search on.
"""
def search_task_member():
    while True:

        #Asking the user to search for one choice, from Task or Member.
        search_task_or_member = easygui.buttonbox\
        ("Do you want search for a Task or Member", \
        choices= ["Task", "Member"])

        #If the choice is Task...
        if search_task_or_member == "Task":

            task_output = "" 
            task_catogories = [] 
            task_title = "Task Search" 
            task_msg = "Click on the Task you would like displayed" 

        #Adding the Task List from the Task Dictionary to a list.
            for task_list in Task_Dictionary: 
                task_catogories.append(task_list)

        #easygui.msgbox(task_catogories) 
            search_task_member = easygui.buttonbox\
            (task_msg, task_title, task_catogories) 

            for tasks in Task_Dictionary[search_task_member]: 
                task_output += \
                f"\n{tasks}: {Task_Dictionary[search_task_member][tasks]}" 

            easygui.msgbox(task_output) 

        #If the choice is Member...   
        if search_task_or_member == "Member":
            
            member_output = ""
            member_categories = []
            member_title = "Category Search"
            member_msg = "Click on the Member you would like displayed" 

        #Adding the Member List from the Team Member Dictionary to a list.
            for member_list in Team_Member_Dictionary: 
                member_categories.append(member_list) 

        #easygui.msgbox(member_catogories) 
            search_task_member = easygui.buttonbox\
            (member_msg, member_title, member_categories) 

            for members in Team_Member_Dictionary[search_task_member]: 
                member_output +=\
                f"\n{members}: {Team_Member_Dictionary[search_task_member]\
                [members]}" 

            easygui.msgbox(member_output) 

        #Asking the user whether or not to search another Task/Member.
        search_another_task = easygui.buttonbox\
        ("Do you want to search another new task/member?",\
        choices=["Yes", "No"])
                    
        if search_another_task == "No":
            break
        
def generate_report():
    while True:
        num_completed = 0
        num_in_progress = 0
        num_in_blocked = 0
        num_not_started = 0

        for task in Task_Dictionary.values():
            task_status = task["Status"]
            if task_status == "Completed":
                num_completed += 1

            elif task_status == "In Progress":
                num_in_progress += 1

            elif task_status == "In Blocked":
                num_in_blocked += 1

            elif task_status == "Not Started":
                num_not_started += 1

        generate_task_status_report = f"Project Progress Report:\
        \n\nCompleted Tasks: {num_completed}\
        \nIn Progress Tasks: {num_in_progress}\
        \nBlocked Tasks: {num_in_blocked}\
        \nNot Started Tasks: {num_not_started}"

        easygui.msgbox(generate_task_status_report)

        search_another_report = easygui.buttonbox\
        ("Do you want to generate another task status report?",\
        choices=["Yes", "No"])
                    
        if search_another_report == "No":
            break
        



"""
Outputting the task collection in a readable format, allows the user
to look through all task's informations. 
"""
def output_task_collection():

    #An empty string to store new informations.
    task_output = ""

    #Loop through task ID and title in the Task_Dictionary.
    for task_id, task_title in Task_Dictionary.items():
    #Add informations in to the empty task_output.
        task_output += f"\nTask ID: {task_id}\n"

    #Loop through task title and info in the task_title dictionary.
        for task_title, task_info in task_title.items():
    #Add informations in to the empty task_output.
            task_output += f"{task_title}: {task_info}\n"
            
    #Display the task collection through easygui message box.
    easygui.msgbox(task_output)
     
        
"""
A main menu that allows the user to click the function that they like.
In this situation, the user will have the oppitunity to select the 
function they want to run.
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
        "Update Task", "Member","Search Task or Member",\
        "Generate Task Report","Exit"])

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
        """
        Runs the search task or member function in the programme, 
        if the user click the Search Task or Member button.
        """
        """
        Runs the generate task report function in the programme, 
        if the user click the Generate Task Report button.
        """
        #Stop the programme, if the user click Exit button.
        if user_choices == "Output Task Collection":
            output_task_collection()
        elif user_choices == "Add New Task":
            add_new_task()
        elif user_choices == "Member":
            output_member_collection()
        elif user_choices == "Update Task":
            update_task()
        elif user_choices == "Search Task or Member":
            search_task_member()
        elif user_choices == "Generate Task Report":
            generate_report()
        else:
            easygui.msgbox("Goodbye")
            break
main_menu()