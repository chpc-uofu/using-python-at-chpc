# plot_files.py : plots temperature data given a USCRN HEADERS.txt file and one 
# or more data files.
#library(ggplot2)
#library(lubridate)
from matplotlib import pyplot, axes
import datetime
import sys
import pandas
import numpy as np

# Function to convert date from yyyymmdd format to ordinal date.
def convert_date(date_yyyymmdd):
    '''
    Returns ordinal date given date in "yyyymmdd" format.
    '''
    year=int(date_yyyymmdd[0:4])
    month=int(date_yyyymmdd[4:6])
    day=int(date_yyyymmdd[6:])
    delta=datetime.date(year,month,day) - datetime.date(year,1,1)
    return delta.days

# Function to read header file.
def ReadHeaders(headerfile):
    '''
    Returns column headers given a header file.
    '''
    with open(headerfile) as ifs:
        ifs.readline()  # Read and discard first row.
        headers = ifs.readline().strip().split(' ')
    return headers

def ReadData(headers,datafiles):
    '''
    Reads the T_DAILY_MAX value from each data file and returns a 
    data frame with those values, with columns labeled by the place 
    name.
    '''
    # Read the subsequent files into a data frame.
    final_dataset = None
    for datafile in datafiles:
        # Derive the place name from the data file name.
        fields = datafile.split('_')
        placename = '_'.join( fields[1:len(fields)-2] )
        # Read the data file into a data frame.
        dataset=pandas.read_table(datafile,names=[placename],header=None,sep='\s+',usecols=[5],dtype=np.float64)
        # Replace missing values with None.
        dataset[dataset==-9999.0]=None

        # Add this locations data to the growing final data set.
        if final_dataset is None:
            final_dataset = dataset
        else:
            final_dataset.insert(0,placename,dataset)
    return final_dataset

if __name__ == "__main__":
    # Read the column headers.
    headers = ReadHeaders(sys.argv[1])
    # Read the data files.
    dataset=ReadData(headers,sys.argv[2:])
    # Plot the data.
    print(dataset.columns)
    for location in dataset.columns:
        pyplot.plot(dataset[location],label=location)
    pyplot.legend()
    # Display the plot:
    #pyplot.show()
    # Save the plot to a PNG file.
    pyplot.savefig("figure1.png")
