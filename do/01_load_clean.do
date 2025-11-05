* In this part I load the raw data and do basic cleaning.
clear all
set more off

cd "C:\Users\Shala_Anesa\Desktop\Final Assignment"

* load data directly from the main folder
use "C:\Users\Shala_Anesa\Desktop\Final Assignment\epl_games.dta", clear
browse

* In this part I deleted the missing values and unrelated variables.
codebook
describe
tabulate goals_away, missing
drop if missing(goals_away)
drop div hometeam_uid awayteam_uid
count

* save an intermediate cleaned file in the main folder
save "epl_games_clean.dta", replace