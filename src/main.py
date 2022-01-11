import download_file
import regex_for_key

fileUrl = input("Enter the url of the file:")
fileName = input("\nEnter the name of the file (with extension) to be save as:")

print("Generating key of file using RegEx Code...")
fileKey = regex_for_key.regexForKey(fileUrl)

print("Downloading the specified file...")
download_file.downloadFile(fileKey, fileName)

print("The file has been downloaded!!")
