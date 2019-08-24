# THE OS.PATH MODULE
import os

# Handling Absolute and Relative Paths
""" 
Calling `os.path.abspath(path)` will return a string of the absolute path of the argument. This is an easy way to convert a relative path into an absolute one.
Calling `os.path.isabs(path)` will return True if the argument is an abso- lute path and False if it is a relative path.
Calling `os.path.relpath(path, start)` will return a string of a relative path from the start path to path. If start is not provided, the current working directory is used as the start path.
"""

os.path.abspath('.')  # 'C:\\Python34'
os.path.abspath('.\\Scripts')  # 'C:\\Python34\\Scripts'
os.path.isabs('.')  # False
os.path.isabs(os.path.abspath('.'))  # True


os.path.relpath('C:\\Windows', 'C:\\')  # 'Windows'
os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')  # '..\\..\\Windows'
os.getcwd()  # 'C:\\Python34'

""" 
Calling os.path.dirname(path) will return a string of everything that comes before the last slash in the path argument. 
Calling os.path.basename(path) will return a string of everything that comes after the last slash in the path argument. 
"""
path = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(path)  # 'calc.exe'
os.path.dirname(path)  # 'C:\\Windows\\System32'

"""
Call os.path.split() to get a tuple value with these two strings
"""
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
os.path.split(calcFilePath)('C:\\Windows\\System32', 'calc.exe')

"""
Can also just put these methods in a tuple
"""
(os.path.dirname(calcFilePath), os.path.basename(calcFilePath))(
    'C:\\Windows\\System32', 'calc.exe')

"""  
Calling os.path.getsize(path) will return the size in bytes of the file in the path argument.
Calling os.listdir(path) will return a list of filename strings for each file in the path argument. (Note that this function is in the os module, not os.path.)
"""

os.path.getsize('C:\\Windows\\System32\\calc.exe')  # 776192
os.listdir('C:\\Windows\\System32')
# ['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll', 'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + \
        os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)  # 1117846456
