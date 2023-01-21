import os


# recursively loop through all the files in all the directories
def create_dataset(dir_path,extension):
    output_path = 'output.txt'
    def loop_through_files(dir_path):
        for file in os.listdir(dir_path):
            if os.path.isdir(os.path.join(dir_path, file)):
                loop_through_files(os.path.join(dir_path, file))
            else:
                if file.endswith(extension):
                    # take contents of file and append to a new file
                    with open(os.path.join(dir_path, file), 'r') as f:
                        output_file.write(f.read())
    with open(output_path, 'a') as output_file:
        loop_through_files(dir_path)


if __name__ == '__main__':
    directory_path = '/Users/Shuza/Code/mastery-track'
    extension = '.py'
    create_dataset(directory_path,extension)