# 
# Script: Ops 301d5 Ops Challenge Solution 08
# Author: Jon Salhus                  
# Date of latest revision: 9/8/2022   
# Purpose: Creates a new user in AD with associated information

New-ADUser -Name "Franz Ferdinand" -City "Springfield" -Company "GlobeX USA" -State "OR" -Department "TPS" -Country "USA" -Office "Springfield, OR" -OtherAttributes @{'title'="TPS Reporting Lead";'mail'="ferdi@globexpower.com"}
