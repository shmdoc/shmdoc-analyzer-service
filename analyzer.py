#
# Contains the main functionality for calling all the modules for the analyzing process
#
import csv_analyzer

def analyze_file(file_location):
    csv_analyzer.analyze(file_location)
    # with open(file_location) as file:
    #     csv_analyzer.analyze(file)