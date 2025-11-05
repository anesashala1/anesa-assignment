* In this part I created a summary statistics and a histogram. Then I saved the Graph as png.
clear
set more off

cd "C:\Users\Shala_Anesa\Desktop\Final Assignment"

use "modified_data.dta", clear

summarize, detail
hist total_goals

graph save "graphs\Graph_Histo.gph", replace
graph export "graphs\Graph_Histo.png", as(png) replace