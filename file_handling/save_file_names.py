import os


def save_file_names(folder_path, output_file):
    try:
        with open(output_file, "w") as file:
            for root, dirs, files in os.walk(folder_path):
                for name in files:
                    file.write(f"{name}\n")
        print(f"File names saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
folder_path = "T:\Marvel.Cinematic.Universe.Phase.1-3"
output_file = "marvel_movie_list.txt"
save_file_names(folder_path, output_file)

with open(output_file, "r") as file:
    content = file.read()
    print("Content of the output file:")
    print(content)
