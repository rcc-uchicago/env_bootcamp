import geocoder, csv, time

inputfile = open("F:\\stuff\\projects\\pythonworkshop\\forworkshop\\villages_1815.csv", "rb")
reader = csv.reader(inputfile)
counter = 1
recordnumber = 1
for x in reader:
  print recordnumber
# print counter
  if counter == 10:
    time.sleep(2)
    counter = 1
  elif counter < 10:
    x = str(x)[1:-1]
# print x
    g = geocoder.google(x)
    gravy = g.latlng
# print gravy
    gravy = str(gravy)+ "\n"
    with open("F:\\stuff\\projects\\pythonworkshop\\forworkshop\\villages_1815_output.txt", "a") as myfile:
      myfile.write(gravy)
    counter = counter + 1
  recordnumber = recordnumber + 1
