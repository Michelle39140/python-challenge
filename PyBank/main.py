

# Target: analyzing the financial records of your company. 
# Analyzes the records to calculate each of the following:
#   * The total number of months included in the dataset
#   * The total net amount of "Profit/Losses" over the entire period
#   * The average change in "Profit/Losses" between months over the entire period
#   * The greatest increase in profits (date and amount) over the entire period
#   * The greatest decrease in profits (date and amount) over the entire period

# Data:  a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date (one day per month)` and `Profit/Losses`
import csv
import os
# 1. read the csv file into an iterator
input_file_path =os.path.join('..','..','Instructions','PyBank','Resources','budget_data.csv')
with open(input_file_path,'r',newline="")as input_file:
    csviterator=csv.reader(input_file,delimiter=',')
    # 2. loop thru rows and calculate:
    
    header = next(csviterator)
    # print(header)

    month = 0
    revenue = 0

    for rows in csviterator:
    #   * The total number of months included in the dataset = total number of rows in he Date column
        month +=1
    #   * The total net amount of "Profit/Losses" over the entire period = sum of Profit/Losses column
        revenue += int(rows[1])
    #   in the first month, initialize vairables
        if month == 1:
            pro_lastmonth = int(rows[1])
            max_profit=int(rows[1])
            max_lose=int(rows[1])
            totalchanges=0
        else:
    #   * The average change in "Profit/Losses" between months over the entire period = sum(this month - last month)/# of month -1
            totalchanges += (int(rows[1])-pro_lastmonth)
            pro_lastmonth = int(rows[1]) # store the current profit for use in the next row
    #   * The greatest increase in profits (date and amount) over the entire period = max(profit/losses) & the corr month value
            if int(rows[1])>max_profit:
                max_profit = int(rows[1])
                mp_month = rows[0]
    #   * The greatest decrease in profits (date and amount) over the entire period = min(profit/losses) & the corr month value
            elif int(rows[1])<max_lose:
                max_lose= int(rows[1])
                ml_month = rows[0]


    # 3. print out results
    results =(f"Financial Analysis\n\
-----------------------------------------------\n\
Total Months: {month}\n\
Total: $ {revenue}\n\
Average Change: $ {totalchanges/(month-1):.2f}\n\
Greatest Increase in Profits: {mp_month} (${max_profit:.2f})\n\
Greatest Decrease in Profits: {ml_month} (${max_lose:.2f})")
    print(results)

    # 4. export result in txt file
    result_file_path="PyBank_results.txt" 
    with open(result_file_path,"w+") as result_file:
            result_file.write(results)


