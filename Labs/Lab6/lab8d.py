'''
Name: John Niagwan
ID: 121092225
'''
import os

course_dir = '..'

print('Your current directory is: ' + os.path.abspath(course_dir))
for root, directories, filenames in os.walk(course_dir):
    for file in filenames:
        # Use os.path.join() to create paths
        file_path = os.path.join(root, file)
        print(file_path)
