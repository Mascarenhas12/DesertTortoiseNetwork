# Network Science - Project 2020/2021

The project runs a yearly analysis, on chosen years,  of a given data dataset. In the analysis 4 properties are taken in consideration:
* Average Path Length (only for the largest strongly connected component) 
* Average Degree
* Degree Distribution
* Clustering Coefficient

The corresponding graph and a Histogram of the Degree Distribution will be displayed for each year. In the end it will also be display a graph of the yearly evolution of the Average Degree, Clustering Coefficient and Average Path Length. 


In order to run this analysis on a dataset:
* Ensure that the data file has each edge represented in a line with this format `node1 node2 year`
* The dataset file must be in the project's main folder
* Enter the `src` folder
* Run the file `main.py [Data_Set_File_Name] [Starting_Year] [End_Year]`

The files of the graphs will be saved to the folder `results`. The filenames of the saved files will have the following format:
* `DD_[Year]`, Degree Distribution Graph of a specific [Year] 
* `GD_[Year]`, Graph of the Network in of the specific [Year]
* `TA`, Graph of the yearly evolution of the Average Degree, Clustering Coefficient and Average Path Length

---

#### Developed By

| Name | University | Identifier | Email |
| ---- | ---- | ---- | ---- |
| Sara Machado | Instituto Superior Técnico | 86923 | sara.f.machado@tecnico.ulisboa.pt |
| João Galamba | Instituto Superior Técnico | 90735 | joao.catarino.g@tecnico.ulisboa.pt |
| Manuel Mascarenhas | Instituto Superior Técnico | 90751 | manuel.d.mascarenhas@tecnico.ulisboa.pt |

