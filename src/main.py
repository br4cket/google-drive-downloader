import download_file
import regex_for_key

print('''
    \nWelcome to the Google Drive Downloader.\n
    This script is developed on python. it takes url and asks file name for input
    and downlods the file associated with the url link.
    -> If you are executing this on windows then enter the filename with file format
    -> If you are on linux, just the file name is fine.
    \n\n**NOTE: The url link must have permission that anyone with this link can view the file 
    _______________________________________________________________________________________________
''')

fileUrl = input("Enter the url of the file:")
fileName = input("\nEnter the name of the file (with extension) to be save as:")

print("Generating key of file using RegEx Code...")
fileKey = regex_for_key.regexForKey(fileUrl)

print("Downloading the specified file...")
download_file.downloadFile(fileKey, fileName)

print("The file has been downloaded!!")
