* In this part I did filtering observations, filtering variables, and creating transformations of variables.
clear
set more off

cd "C:\Users\Shala_Anesa\Desktop\Final Assignment"

* start from cleaned data in the main folder
use "epl_games_clean.dta", clear

* Filter Observations
keep if inrange(season, 2018, 2025)
drop if missing(team_home, team_away, goals_home, goals_away)
drop if goals_home < 0 | goals_away < 0 | goals_home > 15 | goals_away > 15
browse

* Filter Variables
keep season date team_home team_away goals_home goals_away points_home points_away
browse

* Transformations
gen goal_diff   = goals_home - goals_away
gen total_goals = goals_home + goals_away
gen result      = cond(goal_diff>0,"H", cond(goal_diff==0,"D","A"))   // H=home, D=draw, A=away
browse

* save processed data in the main folder
save "modified_data.dta", replace
