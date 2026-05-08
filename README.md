# Data Science - Coffee Analysis

## Data
Data sources:
    https://www.kaggle.com/datasets/michals22/coffee-dataset/data?select=Coffee_domestic_consumption.csv

    https://www.kaggle.com/datasets/PromptCloudHQ/world-happiness-report-2019

The first leads to a web page with several different versions of csv files with coffee related statistics between 1990 and 2019. I have included these in my github submission under data/raw. 
The second link leads to a similar web page with a version of the 2019 World Happiness Report in a csv file. This has also been included under data/raw.


## Src
Under src is a number of scripts that I have used to clean and tidy the data, 'organise_coffee.py' and 'sort_happiness.py' respectively. As they do distinctly different tasks it felt apt to name one organise and one sort.
The script 'merge_coffee_happiness.py' does exactly that. It combines the consumption statistic with the happiness for the respective countries and allows for further tools to be used. The next script I mention 'regression_happiness_on_consumption.py' is one of these tools and provides both a regression and correlation value. See the blog for further information.

## Blog
This is a pretty straightforward file just containing the blog. A more informal explanation and analysis of the code I've developed.