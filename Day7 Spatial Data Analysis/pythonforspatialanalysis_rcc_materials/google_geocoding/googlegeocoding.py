# Google Geocoder example
#   script written by T.Schuble 2016
#   modified by J.Tharsen 09-2018
# 
# Outputs a CSV file with four fields:
# City, State, Lat, Long

import geocoder, csv, time

inputfile = open("villages_1815.csv", "r")  # read-only input

outputfile = open("villages_1815_output.csv", "a") # append mode for output
outputfile.write("City, State, Lat, Long \n") # write CSV header row

reader = csv.reader(inputfile)

counter = 1
recordnumber = 1

for x in reader:
# print (recordnumber)
# print (counter)
  if counter == 10:
    time.sleep(2)
    counter = 1
  elif counter < 10:
    x = str(x)[1:-1]
# print (x)
    g = geocoder.google(x)
    gravy = g.latlng
    print (str(recordnumber) + " " + str(x) + " : " + str(gravy))
    # gravy = str(gravy)+ "\n"
    gravystr = str(gravy)
    gravystr = gravystr.replace("[","")
    gravystr = gravystr.replace("]","")
    gravystr = str(x).replace("'","") + ", " + gravystr + "\n"
    outputfile.write(gravystr)
    counter = counter + 1
  recordnumber = recordnumber + 1
