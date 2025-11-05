* In this part I run all steps in order.
clear all
set more off

cd "C:\Users\Shala_Anesa\Desktop\Final Assignment"

* create folders 
cap mkdir "do"
cap mkdir "graphs"

* run the other do files
do "do\01_load_clean.do"
do "do\02_filter_transform.do"
do "do\03_summary_graphs.do"