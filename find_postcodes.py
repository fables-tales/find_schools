import csv

if __name__ == "__main__":
    x = csv.reader(open("subscribed_people.csv"))
    print "postcode"
    for line in x:
        if len(line) > 0:
            values = line[4].rsplit()
            if len(values) > 2:
                str = values[-2] + " " + values[-1]
                str = str.replace("Surrey ", "")
                str = str.replace("S0", "SO")
                if str[0] == "9":
                    print "BS9 3AW"
                else:
                    print str
