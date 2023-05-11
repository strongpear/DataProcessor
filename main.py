import zipfile
import re
import glob
import shutil

calendarItemsFileDir = "C:\Users\jlee4\Documents\classes\personal\Updated-Data_Checker2-20230511T012859Z-002\calendar_items_wave1.json"
surveyItemsFileDir = "C:\Users\jlee4\Documents\classes\personal\Updated-Data_Checker2-20230511T012859Z-002\survey_items_wave1.json"
dbFilesDir = "C:\Users\jlee4\Documents\classes\personal\Updated-Data_Checker2-20230511T012859Z-002\db_reader\db files"
zipFilesDir = ""
rawDataDir = "C:\Users\jlee4\Documents\classes\personal\Updated-Data_Checker2-20230511T012859Z-002\Raw Data"
processedDataDir = "C:\Users\jlee4\Documents\classes\personal\Updated-Data_Checker2-20230511T012859Z-002\processed_data"


def main():

    # Deal with the zip files
    unzip(zipFilesDir, rawDataDir)

    # put DB files in db files folder
    placeDBFiles(zipFilesDir, dbFilesDir)

    # Number of trips calendar_items_wave1.json
    findNumOfTrips()

    # Total Duration calendar_items_wave1.json
    findTotalDuration()

    # Data Checking GPS, EDA(GSR in filename), BVP, IMU (in processed data)
    checkDataExistence()

    # E4 Duration look in trip data in processed data
    findE4Duration()

    # number of stresses -> survey_items_wave1.json
    findNumberStresses()

    # Survey -> N if -1 -1 -1 -1 0
    checkSurvey()

    # spit out some type of excel file 
    createExcel()
    return


def unzip(fileDir, destination):
    # filename starts with sub and then their number then and @
    print("Dealing with the zip files...")
    regex = '^(sub\d+)@'    
    for file in glob.glob(fileDir, "*.zip"):
        reg = re.match(regex, file)
        if len(reg) == 0:
            print("This filename is weird and doesn't hit the regex:", file)
            print("Did not extract.")
            continue

        # Placing the extracted folder into the correct raw data file
        destinationPath = destination + "/" + reg.group()
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(destinationPath)
    return

def placeDBFiles(fileDir, destination):
    print("Dealing with the DB files...")
    regex = '^(sub\d+)@'
    for file in glob.glob(fileDir, "*.db"):
        reg = re.match(regex, file)

        if len(reg) == 0:
            print("This filename is weird and doesn't hit the regex:", file)
            print("Did not move.")
            continue
        shutil.move(file, destination + file)
        print("Moved:" + file)
    return

def findNumOfTrips():
    return

def findTotalDuration():
    return

def checkDataExistence():
    return

def findE4Duration():
    return

def findNumberStresses():
    return

def checkSurvey():
    return

def createExcel():
    return

main()