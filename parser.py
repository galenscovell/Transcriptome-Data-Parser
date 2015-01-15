'''
TODO:
[X] 1. Find composition of columns as percentages
    [X] a. Pie-chart representation
    [ ] b. Using subarray terms
        [ ] i. Visual representation of results
[X] 2. Find individual row by search term
    [ ] a. Using subarray terms
    [ ] b. Filter by further search terms
[ ] 3. Search by column, filter results with further search terms
    [ ] a. Using subarray terms
[ ] 4. Output results (as CSV) and figures with date/time
[ ] 5. Cmdline interface -> GUI
[ ] 6. Create packaged executable for easy use across systems
'''

import sys, os.path, xlrd
import pandas as pd
import matplotlib.pyplot as plt




def filePrompt():
    # Ask for file path, check that file exists
    file_path = input("Enter the file path ('path/to/file.csv'): ")
    if os.path.exists(file_path):
        return file_path
    else:
        print("\tUnable to locate file.\n")
        sys.exit()


def createGraph(analyzed, total):
    # Pie-chart output init
    labels = []
    sizes = []
    colors = ['#2ecc71', '#f1c40f', '#1abc9c', '#e74c3c', '#9b59b6', '#e67e22']
    explode = []

    # Create 'explode' pie piece effect
    for n in analyzed:
        explode.append(0.05)

    # Fill pie-chart output with ratios of column of interest
    for element in analyzed:
        percentage = total.count(element) / len(total) * 100
        labels.append(element)
        sizes.append(percentage)

    # Display completed pie-chart
    plt.rcParams['font.size'] = 9.0
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.2f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.show()
    print("\n---------------------")


#def refine


def scanColumn(df):
    # Scan for all unique elements in column
    column_choice = " "
    header_info = list(df)
    while column_choice not in header_info:
        print("\nFollowing column headers found:")
        print(header_info)
        print("\n\tEnter column to return info on")
        column_choice = input("\t > ")
    column_total = []
    column_unique = []
    for row in df[column_choice]:
        if row not in column_total:
            column_unique.append(row)
        column_total.append(row)

    filter_decision = " "
    while filter_decision[0].lower() not in ('d', 'r'):
        print("\n\tAnalyze this data or further refine?")
        print("\t(Options: [D]one or [R]efine)")
        filter_decision = input("\t > ")
        if filter_decision[0].lower() == 'd':
            break
        else:
            print("\tRefinement here.")

    graph_choice = " "
    while graph_choice[0].lower() not in ('y', 'n'):
        print("\n\tCreate pie-chart with collected data (Y/N)?")
        graph_choice = input("\t > ")
        if graph_choice[0].lower() == 'y':
            createGraph(column_unique, column_total)
        else:
            break


def termPrompt():
    # Ask for search term of interest
    print("\n\tEnter search term")
    term = input("\t > ")
    print("")
    return term


def searchKeywords(df, search):
    # Return rows with term anywhere in columns
    # for column in df.columns:
    #     if len(df[df[column] == search]) > 0:
    #         print(df[df[column] == search])
    #     else:
    #         print("No results found for '" + search + "' in '" + column + "'")
    
    print(len(df))
    for row in df.Keywords:
        if type(row) is str and ';' in row:
                row_subarray = row.split(';')
                if search in row_subarray:
                    print(df[row].iloc)
    print("\n---------------------")
    
    


def main():
    f = filePrompt()

    print("\n____________[ PYTHON DATA PARSER ]____________\n")
    if f.endswith('.csv'):
        dataframe = pd.read_csv(f, header=0)
    elif f.endswith('.xls') or f.endswith('.xlsx'):
        dataframe = pd.read_excel(f, header=0)
    else:
        print("\tFile extension needs to be .csv, .xls, or .xlsx")
        sys.exit()

    running = True
    while running:
        choice = " "
        print("\nFILE IN USE: " + f + " (" + str(len(dataframe)) + " rows)")
        print("(Options: Scan [C]olumns, Search [K]eyword, [E]xit)")
        while choice[0].lower() not in ('c', 'k', 'e'):
            choice = input(" > ")
            if choice[0].lower() == 'c':
                scanColumn(dataframe)
            elif choice[0].lower() == 'k':
                t = termPrompt()
                searchKeywords(dataframe, t)
            elif choice[0].lower() == 'e':
                running = False
                break


    print("\n______________[ CLOSING PARSER ]______________\n")
    sys.exit()


if __name__ == '__main__':
    main()