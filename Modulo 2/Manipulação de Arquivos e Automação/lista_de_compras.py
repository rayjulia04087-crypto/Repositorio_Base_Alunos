import csv                           # Imports the csv module for handling CSV files

csvfile = open("lista_de_compras.csv","w")    # Opens (or creates) the CSV file for writing
examplecsv = csv.writer(csvfile, delimiter=";") # Creates a CSV writer object with ';' as separator outra forma with open("lista_de_compras.csv", "w") as arquivo

examplecsv.writerow(["macas","bananas","morangos"])   # Writes the first row with fruit items
examplecsv.writerow([ "leite", "queijo","iogurte"])   # Writes the second row with dairy items
examplecsv.writerow(["sabao","detergente","esponja"]) # Writes the third row with cleaning items

csvfile.close()                        # Closes the file
