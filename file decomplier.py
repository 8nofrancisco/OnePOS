#Francisco Cordova
#OnePOS 1/11/24
#Decompress multiple folders to one folder.
import os
import zipfile

def extractor():
    #Input and check folders
    print("Enter in the folder source Example: C:/OnePOS/15914 \n")
    sourceFolder = input("Enter the path of the source folder: ")
    print("\nEnter in the folder destination Example: C:/OnePOS/JOURNALS \n")
    destinationFolder = input("Enter the path of the destination folder: ")

    if not os.path.exists(sourceFolder):
        print(f"\nThe source folder {sourceFolder} does not exist.\n")
        return
    
    if not os.path.exists(destinationFolder):
        print(f"\nThe folder {destinationFolder} does not exist.\n")
        creationFolder = input(f"Would you like to make {destinationFolder} a new folder? Y/N:")
        if (creationFolder == 'Y'):
            os.makedirs(destinationFolder)
            print(f"Folder {destinationFolder} created.")
        else:
            return
    
    extractionDone = False

    # Get list of all files and folders in the specified directory
    for root, dirs, files in os.walk(sourceFolder):
        for file in files:
            if file.endswith('.zip'):
                zipFilePath = os.path.join(root, file)
                print(f"Extracting {zipFilePath}")
                
                # Extract the ZIP file to the destination directory
                with zipfile.ZipFile(zipFilePath, 'r') as zipRef:
                    zipRef.extractall(destinationFolder)
                
                print(f"{zipFilePath} extracted successfully to {destinationFolder}.")
                extraction_done = True

    if not extraction_done:
        print(f"No ZIP files were found in {sourceFolder} to the destination folder {destinationFolder}.")

extractor()


# Replace 'your_source_folder_path_here' with the path of the folder you want to scan
# Replace 'your_destination_folder_path_here' with the path of the folder you want to extract files to
extractor()
