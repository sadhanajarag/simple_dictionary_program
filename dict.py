# Dictionary containing course information
# Each course number maps to a list with room number, instructor, and meeting time
course_room = {
    'CSC101': [3004, "Haynes", "8:00 a.m."],
    'CSC102': [4501, "Alvarado", "9:00 a.m."],
    'CSC103': [6755, "Rich", "10:00 a.m."],
    'NET110': [1244, "Burke", "11:00 a.m."],
    'COM241': [1411, "Lee", "1:00 p.m."]
}

def get_course_details(course_number):
    """Function to retrieve course details based on course number.
     Args:  course_number (str): The course number to search for in the dictionary.
     Returns:str: A formatted string with course details or an error message.
    """
    try:
        # Check if the course number is in the dictionary
        if course_number in course_room:
            course_details = course_room.get(course_number)
            # Return formatted course details
            return (f"Course number: {course_number}, "
                    f"Room Number: {course_details[0]}, "
                    f"Instructor: {course_details[1]}, "
                    f"Meeting Time: {course_details[2]}")
        else:
            # Return error message if course number is not found
            return "Course number is not in the available dictionary"
    except ValueError:
        # Handle unexpected errors
        return "Course number is not available"

def main():
    """
    Main function to interact with the user and display course details.
    """
    while True:
        # Get course number from user input or exit the loop by providing the correct choice
        course_number = input("Enter a course number:(or type 'exit' to quit) ").strip()
        # check the choice of user and if that is 'exit' then exit the program
        if course_number.lower() == 'exit':
            print("exiting the loop")
            break
        # Get and display course details
        details = get_course_details(course_number)
        print(details)

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()