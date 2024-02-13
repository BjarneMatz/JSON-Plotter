"""Main module for the plotter application."""
import os
import json
from matplotlib import pyplot

PLOT_FOLDER = os.path.join(os.getcwd(), "/data")



def read(filename: str) -> dict:
    """Reads the plot instructions from a file and returns them as a dictionary."""
    with open(filename, 'r', encoding="UTF-8") as file_data:
        return json.load(file_data)

def get_files() -> list:
    """Returns a list of all files in the data folder."""
    plot_files = []
    for file in os.listdir():
        if file.endswith(".json") and file != "plot_example.json":
            plot_files.append(file)
    return plot_files

def menu():
    """Selection menu for the user to choose a file to plot."""
    print("Datei zum Plotten auswählen:")
    files = get_files()
    for i, file in enumerate(files):
        print(f"{i+1}: {file}")
    print("0: Beenden")
    try:
        selection = int(input("Auswahl: "))
        if selection < 0 or selection > len(files):
            raise ValueError("Ungültige Auswahl!")
        elif selection == 0:
            exit()
        else:
            return files[selection-1]
    except ValueError:
        print("Ungültige Auswahl!")
        return menu()

def plot(data: dict):
    """Plots the data from the given dictionary."""
    pyplot.plot(data["x"], data["y"])
    pyplot.title(data["title"])
    pyplot.xlabel(data["xlabel"])
    pyplot.ylabel(data["ylabel"])
    pyplot.grid()
    pyplot.show()

def main():
    """Main function for the plotter application."""
    filename = menu()
    data = read(filename)
    plot(data)

if __name__ == "__main__":
    main()
    print("Tschüss!")
