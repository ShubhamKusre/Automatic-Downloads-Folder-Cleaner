import os
import shutil


downloads_folder = r'C:\Users\shubh\Downloads'
folders = {
    'Images': r'C:\Users\shubh\OneDrive\Pictures',
    'Documents': r'C:\Users\shubh\OneDrive\Documents',
    'Videos': r'C:\Users\shubh\Videos',
    'Music': r'C:\Users\shubh\Music',
}


file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.xls', '.csv', '.pptx', '.sql', '.ipynb', '.exe', '.zip', '.rar', '.msi'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav'],
}


def move_files():
    for file_name in os.listdir(downloads_folder):                               #Loop Through Files in the Downloads Folder
        file_path = os.path.join(downloads_folder, file_name)                    #Construct File Path to move
        if os.path.isfile(file_path):                                            #Check if path is a file
            file_ext = os.path.splitext(file_name)[1].lower()                    #Split file name and extension
            for folder, extensions in file_types.items():
                if file_ext in extensions:                                       #Check if file extension matches folder extension at the top
                    dest_folder = folders[folder]
                    dest_path = os.path.join(dest_folder, file_name)             #Set the destination for where the file should go
                    if os.path.exists(dest_path):
                        base_name, ext = os.path.splitext(file_name)             #Checks for duplicates and changes file name by adding 1 to the end
                        new_name = f"{base_name}_1{ext}"
                        dest_path = os.path.join(dest_folder, new_name)
                    shutil.move(file_path, dest_path)                            #Move the File
                    print(f'Moved: {file_name} to {dest_folder}')
                    break

if __name__ == "__main__":
    move_files()
