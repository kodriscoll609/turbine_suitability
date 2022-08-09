# turbine_suitability
Identifying suitable wind turbine locations in Groningen using map algebra
### Authors: Kevin O'Driscoll, Ruben Heinsbroek, Arend-Jan Tissing

## Description
The objective of this research is to investigate the available area for the construction of windmills and the maximum energy potential in the province of Groningen. By executing a land use analysis with a GIS based approach, the following research question will be answered: “Which locations are most suitable for the construction of windmills in the province of Groningen?” This project applies a Weighted Sum Method (WSM) to account for the social, economical, and wind energy potential factors that contribute to suitable locations for building farms.

#### Constraints
In order to exclude unsuitable sites from proximity analysis, a buffer algorithm was applied to the features of each vector layer representing the following constraints: Provincial Waterways, Natura 2000 Areas, Built-up Areas, and Roadways

#### Criteria
In order to optimize wind farm placement, a normalized raster was created for each criterion vector layer, resulting in each cell containing a suitability score ranging from 0 (least suitable) to 1 (most suitable). Distance from built-up areas and Natura 2000 areas were maximized to in order to reduce visual polution, whereas proximity to power transformers and locations with highest average wind speed at a height of 100 meters were minimized for wind energy potential. A proximity raster
algorithm was applied to raster layers for each of the 4 criteria to maximize and minimize distance. 
