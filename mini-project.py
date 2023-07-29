import tkinter as tk
from tkinter import ttk

# created a dictionary to store course name and their subjects
course_subjects = {
    "Mechanical Engineering": {
        1: ["ENGLISH", "BASIC SCIENCE", "BASIC MATHEMATICS"],
        2: ["APPLIED SCIENCE", "APPLIED MECHANICS", "APPLIED MATHEMATICS", "ENGINEERING DRAWING"],
        3: ["THERMAL ENGINEERING", "STRENGTH OF MATERIALS" , "BASIC ELECTRICAL AND ELECTRONICS ENGINEERING" , "ENGINEERING METROLOGY"],
        4: ["THEORY OF MACHINES", "MECHANICAL ENGINEERING MEASUREMENTS" , "FLUID MECHANICS AND MACHINERY" , "MANUFACTURING PROCESSES" , "ENVIRONMENTALSTUDIES"],
        5: ["MANAGEMENT","POWER ENGINEERING AND REFRIGERATION" ,"ADVANCED MANUFACTURING PROCESSES" ,"ELEMENTS OF MACHINE DESIGN" ],
        6: ["ENTERPRENURESHIP DEVELOPMENT","AUTOMOBILE ENGINEERING" ,"COMPUTER INTEGRATED MANUFACTURING" , "INDUSTRIAL HYDRAULICS AND PNEUMATICS" ,],
    },
    "Information Technology": {
        1: ["ENGLISH", "BASIC SCIENCE", "BASIC MATHEMATICS"],
        2: ["ELEMENTS OF ELECTRICAL ENGINEERING", "APPLIED MATHEMATICS", "BASIC ELECTRONICS","PROGRAMMING IN C"],
        3: ["OBJECT ORIENTED PROGRAMMING USING C++", "DATA STRUCTURE USING C++", "PRINCIPLES OF DATABASE","DATA COMMUNICATION","DIGITAL TECHNIQUES AND MICROPROCESSOR"],
        4: ["JAVA PROGRAMMING","SOFTWARE ENGINEERING","DATABASE MANAGEMENT","COMPUTER NETWORK"],
        5: ["ENVIRONMENTAL STUDIES", "OPERATING SYSTEMS", "ADVANCED JAVA PROGRAMMING", "SOFTWARE TESTING", "ADVANCED COMPUTER NETWORK"],
        6: ["MANAGEMENT", "PROGRAMMING WITH PYTHON", "MOBILE APPLICATION DEVELOPMENT", "EMERGING TRENDS IN COMPUTER AND INFORMATION TECHNOLOGY", "WEB BASED APPLICATION DEVELOPMENT USING PHP","WIRELESS AND MOBILE NETWORKS","CLOUD COMPUTING"],
    },
    "Computer Engineering": {
        1: ["ENGLISH", "BASIC SCIENCE", "BASIC MATHEMATICS"],
        2: ["ELEMENTS OF ELECTRICAL ENGINEERING", "APPLIED MATHEMATICS", "BASIC ELECTRONICS", "PROGRAMMING IN 'C'"],
        3: ["OBJECT ORIENTED PROGRAMMING USING C++", "DATA STRUCTURE USING C++", "COMPUTER GRAPHICS", "DATABASE MANAGEMENT SYSTEM", "DIGITAL TECHNIQUES"],
        4: ["SOFTWARE ENGINEERING", "DATA COMMUNICATION AND COMPUTER NETWORK", "JAVA PROGRAMMING", "MICROPROCESSORS"],
        5: ["ENVIRONMENTAL STUDIES", "OPERATING SYSTEMS", "ADVANCED JAVA PROGRAMMING", "SOFTWARE TESTING", "ADVANCED COMPUTER NETWORK"],
        6: ["MANAGEMENT", "PROGRAMMING WITH PYTHON", "MOBILE APPLICATION DEVELOPMENT", "EMERGING TRENDS IN COMPUTER AND INFORMATION TECHNOLOGY", "WEB BASED APPLICATION DEVELOPMENT USING PHP"],
    },
}

# Function to display subjects based on course name and semester number
def display_subjects():
    course = course_combo.get()
    semester = semester_combo.get()

    if course in course_subjects and int(semester) in course_subjects[course]:
        subjects = course_subjects[course][int(semester)]
        subject_text.delete(1.0, tk.END)  # Clear previous subjects
        subject_text.insert(tk.END, f"Subjects for {course}, Semester {semester}:\n")
        for subject in subjects:
            subject_text.insert(tk.END, f"- {subject}\n")
    else:
        subject_text.delete(1.0, tk.END)
        subject_text.insert(tk.END, "Course or semester not found.")

# Create the main window
window = tk.Tk()
window.title("MSBTE Course Subjects")

# create a label for course name selection
course_label = tk.Label(window, text="Select the course:")
course_label.pack()

# create a dropdown menu 
course_combo = ttk.Combobox(window, values=list(course_subjects.keys()))
course_combo.pack()

# Create a label for semester number selection
semester_label = tk.Label(window, text="Select the semester:")
semester_label.pack()

# Create a dropdown menu for semester number
semester_combo = ttk.Combobox(window, values=[1, 2, 3, 4, 5, 6])
semester_combo.pack()

# Create a button to display subjects
display_button = tk.Button(window, text="Display Subjects", command=display_subjects)
display_button.pack()

# Create a text widget to display the subjects
subject_text = tk.Text(window, height=6, width=30)
subject_text.pack()

# Run the GUI main loop
window.mainloop()