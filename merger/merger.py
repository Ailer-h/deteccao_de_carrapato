import os
import time as t

file_counter: int = 0

# Gets the label tag for the file based on the folder
def get_label_tag(text: str, divider: str = "_", position: int = 1) -> str | None:
    if not text:
        return None
    
    return text.split(divider)[position]

# Appends a line of text to a file
def append_to_file(new_file_location: str, line_to_append: str) -> None:
    with open(new_file_location, "a") as new_file:
        new_file.write(line_to_append)

# Reads a file and relocates it, fixing its tag
def relocate_file(file_infos: dict[str, str], new_file_folder: str, current_tag: int | str) -> None:
    if not file_infos["file_name"]:
        raise ValueError("file_name is not valid")
    
    if not file_infos["folder"]:
        raise ValueError("folder of file is not valid")
    
    if not file_infos["labeled_filename"]:
        raise ValueError("labeled_filename is not valid")
    
    if not new_file_folder:
        raise ValueError("new file folder is not valid")

    if type(current_tag) != str and type(current_tag) != int:
        raise ValueError("current tag is not valid")

    current_file_path: str = os.path.join(file_infos["folder"], file_infos["file_name"])
    new_file_path: str = os.path.join(new_file_folder, file_infos["labeled_filename"])

    with open(current_file_path, "r") as current_file:
        file_lines = current_file.readlines()

        for i, line in enumerate(file_lines, start=1):
            correctly_labled_line: str = f"{str(current_tag)} " + " ".join(line.split()[1::])

            if i != len(file_lines):
                correctly_labled_line += "\n"

            append_to_file(new_file_path, correctly_labled_line)

# Merges all the files on the src folder into a single folder
def merge_files(src_folder: str, destination_folder: str) -> None:
    global file_counter
    if not os.path.exists(src_folder):
        raise ValueError(f"source folder does not exist\nTrying to acces {src_folder}")
    
    if not os.path.exists(destination_folder):
        raise ValueError(f"destination folder does not exist\nTrying to acces {destination_folder}")

    label_ix: int = 0

    for folder in os.listdir(src_folder):
        folder_path = os.path.join(src_folder, folder)

        for file_name in os.listdir(folder_path):

            label_tag = get_label_tag(folder)
            new_filename = f"{label_tag}_{file_name}"

            relocate_file({"file_name": file_name, "folder": folder_path, "labeled_filename": new_filename}, destination_folder, label_ix)
            file_counter += 1 #Increases the file counter

        label_ix += 1
    

src: str = r"C:\Users\henri\OneDrive\Área de Trabalho\YOLO\deteccao_de_carrapato\merger\folders_to_merge"
dst: str = r"C:\Users\henri\OneDrive\Área de Trabalho\YOLO\deteccao_de_carrapato\merger\valid\labels"

if __name__ == "__main__":
    start_time: float = t.time()
    
    merge_files(src, dst)
    
    end_time: float = t.time()

    #Calculates the time it took to send the messages
    minutes: int = int((end_time - start_time) // 60)
    seconds: int = int((end_time - start_time) % 60)

    print(f"It took {minutes}m{seconds}s to merge {file_counter} files")