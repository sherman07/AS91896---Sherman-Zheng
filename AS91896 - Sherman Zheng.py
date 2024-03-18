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

easygui.msgbox("Hi")