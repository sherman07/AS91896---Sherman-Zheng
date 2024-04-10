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
        "Name": "John Smith",
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
        

def check_if_input_is_ok(user_input, user_message, user_title):

    """
    The function checks if the user input is valid(Not just empty).

    Args:
      user_input: The user's input to be validated.
      user_message: The message to display to the user in the input box.
      user_title: The title of the input box.

    """

    #Loop until the user enter valid input.
    while True:

    #Display the message for user to enter a valid input.
        tell_user_to_input = "Invalid, please enter something."

    #If user click cancel or exit button, back to main menu.
        if user_input is None:
            main_menu()

    #If user input is empty string, tell the user through msgbox.
        elif user_input.strip() == "":
            easygui.msgbox(tell_user_to_input, user_title)
            user_input = easygui.enterbox(user_message, user_title)

            """
            If the user input is valid (not None or not empty string), 
            return back to user_input.
            """
        else:
            return user_input
        
def add_new_task():

    """
    Adding a new task to the project's task dictionary, in this
    situation, the function will ask the user multiple questions.
    Such as the title, description, priority, status of the new
    created task.
    """
            
    #Diplay the function that the user is on right now. 
    add_title = "Add New Task"

    #Display the message for user to add a new task.
    add_title_msg = "Enter the title of the task:"

    #Display the message for user to add description for new task.
    add_description_msg = "Enter the description of the task:"

    #Display the message for user to add priority for new task.
    add_priority_msg = "Enter the priorty rating (1 - 3):"

    #Display the message for user to add status for new task
    add_status_msg = "Select Priority:"

    #Choices for user to choose for add a status.
    add_status_choices = \
["Completed", "In Progress", "Blocked", "Not Started"]
    
    #Display the message for user that task have been add with new ID.
    add_task_msg = "New task added with ID: "
        
        
    #Asking the user to add a description variable of the new task.
    title = easygui.enterbox(add_title_msg, add_title)
    
    """
    Run the check_if_input_is_ok function, 
    if the user click cancel or other things.
    """
    title = check_if_input_is_ok(title, add_title_msg, add_title) 

    #Asking the user to add a description variable of the new task.
    description = easygui.enterbox(add_description_msg, add_title)

    """
    Run the check_if_input_is_ok function, 
    if the user click cancel or other things.
    """
    description = \
check_if_input_is_ok(description, add_description_msg, add_title)  
                
    #Asking the user to add a priority variable of the new task.
    priority = easygui.integerbox(add_priority_msg,add_title, \
owerbound = PRIORITY_LOWER_LIMIT, upperbound = PRIORITY_UPPER_LIMIT)
    
    """
    If we do the same error prevention method like title.
    Due to the priority have the box of interger,
    the programme will jump the error of:
    AttributeError: 'int' object has no attribute 'strip'.
    So, I will need to make a single prevention for priorpity.
    """
    if priority == None:
        main_menu()
                
    #Asking the user to add a status variable of the new task.
    status = easygui.buttonbox(add_status_msg, add_title, add_status_choices)
    
    """
    Run the check_if_input_is_ok function, 
    if the user click cancel or other things.
    """
    status = check_if_input_is_ok(status, add_status_msg, add_title)

    """
    The ID = ... . This Will creates a new task ID, having the T 
    as task. 
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
                    
    easygui.msgbox(f"{add_task_msg}{new_task_id}.", add_title)

    #Finish the function and back to main menu.
    main_menu()

def update_task():

    """
    Updating a new information to a specific task from the task 
    dictionary. The function will allows user to update informations 
    in specific task, which is from the task dictionary.
    """

    #Diplay the function that the user is on right now. 
    update_title = "Update Task"

    #Display the message for user to update a task.
    update_task_msg = "Enter the task to update e.g.(T1, T2, T3 ...):"

    #Display the message for user to update an assignee.
    update_assignee_msg = \
"Enter the name of the assignee to update for the task:"
        
    #Choices for user to choose for update an assignee.
    update_assignee_choices = ["JSM", "JLO", "BDI"]

    #Display the message for user to update a status.
    update_status_msg = "Select the new task status:"

    #Choices for user to choose for update a status.
    update_status_choices = \
        ["Completed", "In Progress", "Blocked", "Not Started"]
        
    #Display the message to user that task have been updated.
    update_msg = "Task has been updated."

    #Create an empty list to hold task catogories.
    update_task_catogories = [] 

    #Adding the Task List from Task Dictionary to a list.
    for update_task_list in Task_Dictionary: 
        update_task_catogories.append(update_task_list)

    #Asking the user to update one task from the dictionary.
    update_user_task = easygui.buttonbox\
    (update_task_msg, update_title, update_task_catogories)

    """
    Run the check_if_input_is_ok function, 
    if the user click cancel or other things.
    """
    update_user_task = \
check_if_input_is_ok(update_user_task, update_task_msg, update_title)
    
    #Asking the user to update the task assignee.
    update_assignee = easygui.buttonbox\
    (update_assignee_msg, update_title, update_assignee_choices)

    """
    Run the check_if_input_is_ok function, 
    if the user click cancel or other things.
    """
    update_assignee = \
check_if_input_is_ok(update_assignee, update_assignee_msg, update_title)

    #Asking the user to update the task status.
    update_status = easygui.buttonbox\
(update_status_msg,update_title, update_status_choices)

    """
    Run the check_if_input_is_ok function, 
    if the user click cancel or other things.
    """
    update_status = check_if_input_is_ok\
(update_status, update_assignee_msg, update_title)


    """
    Add the task to member's task list, 
    if the task is not in member's task list.
    """
    if update_user_task not in Team_Member_Dictionary\
[update_assignee]["Task Assigned"]:

    #Add the Task into the Assignee's task list.
        Team_Member_Dictionary[update_assignee]\
        ["Task Assigned"].append(update_user_task)
                    
        #Update the Assignee in the Task Dictionary.
        Task_Dictionary[update_user_task]["Assignee"] = update_assignee

        #Update the task status to the Task Dictionary.
        Task_Dictionary[update_user_task]["Status"] = update_status

        """
        Update the assignee to the Task Dictionary, 
        if the task is not Completed and is in the 
         member's task list.
        """
    if update_status not in Team_Member_Dictionary and update_user_task \
in Team_Member_Dictionary[Task_Dictionary[update_user_task]\
["Assignee"]]["Task Assigned"]:
                
    #Update the Assignee in the Task Dictionary.
        Task_Dictionary[update_user_task]["Assignee"] = update_assignee

        #Update the task status to the Task Dictionary.
        Task_Dictionary[update_user_task]["Status"] = update_status

    """
    Remove the task from member's task list, 
    if the task is in the member's task list and is Completed.
    """
    if update_status == "Completed" and update_user_task in \
Team_Member_Dictionary[Task_Dictionary[update_user_task]\
["Assignee"]]["Task Assigned"]:
                        
    #Remove the Completed task from the Assignee's task list.
        Team_Member_Dictionary[Task_Dictionary[update_user_task]\
["Assignee"]]["Task Assigned"].remove(update_user_task)

    #Update the Assignee of the Completed task to None.
        Task_Dictionary[update_user_task]["Assignee"] = None

    #Update the task status to the Task Dictionary.
        Task_Dictionary[update_user_task]["Status"] = update_status

    """ 
    Display a message box to inform the user, 
    that the task has been updated.
    """
    easygui.msgbox(f"{update_user_task} {update_msg}", update_title)
            
    #Finish the function and back to main menu.
    main_menu()

            
def search_task_member():
    

    """
    Search function will allows user to search a specific task or 
    member. In this situation, the programme provide two choices for 
    user to click, task and member. Then the user will able to choose 
    the specific task or member to search on.
    """

    #Diplay the function that the user is on right now. 
    search_task_member_title = "Search Task or Member"

    #Display the message for user to search a task or member.
    search_task_member_msg = "Do you want search for a Task or Member:"

    #Choices for user to choose for search a task ot member.
    search_task_member_choices = ["Task", "Member"]


    #Asking the user to search for one choice, from Task or Member.
    search_task_or_member = easygui.buttonbox\
(search_task_member_msg, search_task_member_title, search_task_member_choices)
    
    """
    Run the check_if_input_is_ok function, 
    if the user click cancel or other things.
    """
    search_task_or_member = \
check_if_input_is_ok\
(search_task_or_member, search_task_member_msg, search_task_member_title)

    #If the choice is Task...
    if search_task_or_member == "Task":

    #An empty variable that store all final serach information.
            task_output = "" 

    #Create an empty list to hold task catogories.
            task_catogories = [] 

    #Diplay the function that the user is on right now. 
            task_title = "Task Search" 
        
    #Display the message for user to search a task.
            task_msg = "Click on the Task you would like displayed" 


    #Adding the Task List from Task Dictionary to a list.
            for task_list in Task_Dictionary: 
                task_catogories.append(task_list)

    #Display a button box for the user to select a specific task.
            search_task_member = easygui.buttonbox\
(task_msg, task_title, task_catogories) 

            """
            Run the check_if_input_is_ok function, 
            if the user click cancel or other things.
            """
            search_task_member = \
check_if_input_is_ok(search_task_member, task_msg, task_list)

    #Retrieve and display the informations of the selected task.
            for tasks in Task_Dictionary[search_task_member]: 
                task_output += \
f"\n{tasks}: {Task_Dictionary[search_task_member][tasks]}" 

    #Display member's informations through message box.
    easygui.msgbox(task_output, task_title)

    main_menu()

    #If the choice is Member...   
    if search_task_or_member == "Member":
            
    #An empty variable that store all final serach information.
            member_output = ""

    #Create an empty list to hold member catogories.
            member_categories = []

    #Diplay the function that the user is on right now. 
            member_title = "Member Search"

    #Display the message for user to search a member.
            member_msg = "Click on the Member you would like displayed"
            
    #Adding the Member List from Team Member Dictionary to a list.
            for member_list in Team_Member_Dictionary: 
                member_categories.append(member_list) 

    #Display a button box for the user to select a specific member.
            search_task_member = easygui.buttonbox\
(member_msg, member_title, member_categories) 
            
            """
            Run the check_if_input_is_ok function, 
            if the user click cancel or other things.
            """
            search_task_member = \
check_if_input_is_ok(search_task_member, member_msg, member_title) 
            
    #Retrieve and display the informations of the selected member.
            for members in Team_Member_Dictionary[search_task_member]: 
                member_output +=\
f"\n{members}: {Team_Member_Dictionary[search_task_member][members]}" 

    #Display member's informations through message box.
    easygui.msgbox(member_output, member_title)
            
    #Finish the function and back to main menu.
    main_menu()

        
def generate_report():

    """
    Generate out the current task status, this allows the user to
    have a view of the current tasks progress.
    """

    #Diplay the function that the user is on right now. 
    generate_report_title = "Generate Report"

    #The default counters for different task statuses.
    num_completed = 0
    num_in_progress = 0
    num_in_blocked = 0
    num_not_started = 0

    #Repeat over tasks to count different statuses
    for task in Task_Dictionary.values():
        task_status = task["Status"]

    #If there is a "Completed" status task, the counter + 1.
        if task_status == "Completed":
            num_completed += 1

    #If there is a "In Progress" status task, the counter + 1.
        elif task_status == "In Progress":
            num_in_progress += 1
        
    #If there is a "Blocked" status task, the counter + 1.
        elif task_status == "Blocked":
            num_in_blocked += 1

    #If there is a "Not Strated" status task, the counter + 1.
        elif task_status == "Not Started":
            num_not_started += 1

    #Generate the report.
    generate_task_status_report = f"Project Progress Report:\
    \n\nCompleted Tasks: {num_completed}\
    \nIn Progress Tasks: {num_in_progress}\
    \nBlocked Tasks: {num_in_blocked}\
    \nNot Started Tasks: {num_not_started}"

    #Display the report, through message box.
    easygui.msgbox(generate_task_status_report, generate_report_title)

    #Finish the function and back to main menu.
    main_menu()
        
def output_task_collection():

    """
    Outputting the task collection in a readable format, allows the user
    to look through all task's informations. 
    """
    

    #An empty string to store new informations.
    task_output = ""

    #Diplay the function that the user is on right now. 
    output_task_title = "Output Task Collection"

    #Loop through task ID and title in the Task_Dictionary.
    for task_id, task_title in Task_Dictionary.items():
    #Add informations in to the empty task_output.
        task_output += f"\nTask ID: {task_id}\n"

    #Loop through task title and info in the task_title dictionary.
        for task_title, task_info in task_title.items():
        #Add informations in to the empty task_output.
            task_output += f"{task_title}: {task_info}\n"
                
    #Display the task collection through easygui message box.
    easygui.msgbox(task_output, output_task_title)

    #Finish the function and back to main menu.
    main_menu()


def main_menu():


    """
    A main menu that allows the user to click the function that they 
    like. In this situation, the user will have the oppitunity to 
    select the function they want to run.
    """

    """
        Allows the user to repeat in the menu page, through the while loop,
        after the user finish one function.
    """

    #Diplay the function that the user is on right now. 
    menu_title = "Welcome to Task Management System"

    #Display message for user to make an option.
    menu_info = "Select One Option:"

    #Choices for user to choose start a function.
    menu_choices = ["Add New Task", "Update Task", \
"Search Task or Member", "Generate Task Report", \
"Output Task Collection", "Exit"]
        

    #Allows the user to make a choice.
    user_choices = easygui.buttonbox(menu_info, menu_title, menu_choices)

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

    """
    Runs the output task collection function in the programme, 
    if the user click the Output Task Collection button.
    """

     #Stop the programme, if the user click Exit button.

    if user_choices == "Add New Task":
        add_new_task()
    elif user_choices == "Update Task":
        update_task()
    elif user_choices == "Search Task or Member":
        search_task_member()
    elif user_choices == "Generate Task Report":
        generate_report()
    elif user_choices == "Output Task Collection":
        output_task_collection()
    else:
        exit()

    """
    Run the Main Menu function at first, 
    so the user will able to make a choice of which function they
    would like to run.
    """
main_menu()