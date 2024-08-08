# Python Code Examples for Accessing and Analyzing SEC's XBRL Data Sets

This repository contains Python code examples to demonstrate how to read data from SEC's Financial Statement and Notes Data Sets using the Pandas package https://pypi.org/project/pandas. These examples help Python programmers understand different ways to access, analyze and visualize data from SEC's Data Sets.

The code examples use the following two SEC's Data Sets. 

1. [Financial Statement Data Sets](https://www.sec.gov/dera/data/financial-statement-data-sets)
2. [Financial Statement and Notes Data Sets](https://www.sec.gov/dera/data/financial-statement-and-notes-data-set)

### Table of Contents
 - Getting Started
 - Requirements
 - Examples
 - Installation
 - Usage

### Getting Started

To get started with these examples, you need to have Python installed on your system. The examples use Python 3.x, so make sure you have the appropriate version installed. In addition to Python, you will need Jupyter https://jupyter.org to run the examples. 

The free edition of the Anaconda distribution of Python available from https://www.anaconda.com/download comes bundled with Jupyter notebooks along with open-source python packages for data exploration and visualization.  

### Requirements

- Python 3.x
- Jupyter notebook
- pandas
- numpy
- pyplot
- seaborn

### Examples

| Example | Description |
| :-- | :-- |
| **1_Read_And_Analyze_Submissions.ipynb** | This example reads submissions for one calendar quarter from Financial Statement Data Sets into a Pandas data frame. You will find code for generating descriptive statistics, filtering data by numeric and/or text matching criteria, grouping data and computing group sizes. The visualizations use the pyplot library.  |
| **2_Read_Multiple_Data_Sets.ipynb** | This example reads submissions for four calendar quarters from Financial Statement Data Sets. You will find code for concatenating four quarters of data into a single data frame, constructing a new column in data frame and visualizing the data using the new column. |
| **3_Find_Numeric_Facts.ipynb** | This example joins submissions with numeric data sets to search for numeric facts for some companies and create a visual comparison across companies. |
| **4_Find_Dimensional_Facts.ipynb** | This example joins submissions, numeric and dimensions data sets to search for dimensional facts. |
| **5_Find_Narrative_Text_Facts.ipynb** | This example joins submissions and text data sets to search for narrative facts and create an Excel download file for search results.|
| **6_Find_Custom_Facts.ipynb** |  This example joins submissions, numeric and tags data sets to search for custom facts. |

### Installation

To run these examples, you need to install the required Python libraries. You can install them using pip:

---
`pip install pandas numpy matplotlib seaborn IPython`

OR 

`pip install -r requirements.txt`

### Usage

1. Clone this repository:

`  git clone https://github.com/sec-gov/python-for-dera-financial-datasets`

2. cd to the python-for-dera-financial-datasets/examples folder. 
>Juptyer notebooks are in the examples folder. These notebooks have been saved with output so that you know what to expect after running the code. Data for these examples is copied for you in the data subfolder.

3. To run the examples, open Jupyter notebook from command prompt or shell:

`  jupyter notebook`

4. From the examples webpage in Jupyter, you can select a specific example of interest to run.


**Suggestions directed to StructuredData@sec.gov regarding code examples are welcome.**
