def file_modifier():
    try:
        # Get input filename from user
        input_file = input("Enter the input file name: ")
        
        # Read the input file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Modify the content (convert to uppercase)
        modified_content = content.upper()
        
        # Get output filename from user
        output_file = input("Enter the output file name: ")
        
        # Write modified content to new file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"Success! Modified content written to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except PermissionError:
        print("Error: You don't have permission to access this file.")
    except IOError as e:
        print(f"Error: An I/O error occurred - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    file_modifier()