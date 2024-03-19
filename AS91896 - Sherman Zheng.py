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
#Adding a new task to the project's task list:
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


    new_task_id = "T" + len(Task_Dictionary) + 1
    
    new_task = {
        "Title": title,
        "Description": description,
        "Assignee": "",
        "Priority": priority,
        "Status": status
    }
    
    Task_Dictionary[new_task_id] = new_task
    
    easygui.msgbox("New task added with ID: " + new_task_id)
