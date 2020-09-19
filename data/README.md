# Dataset Readme


## Data Reference

This dataset is an SQLite database that contains the following information:.

The source file can be found on [Kaggle | 1.88 Million US Wildfires](https://www.kaggle.com/rtatman/188-million-us-wildfires).


## Data Dictionary

| Column Name | Data Type | Description |
|:---|:---|:---|
| **FOD_ID**                     | Integer | Global unique identifier. |
| **FPA_ID**                     | String | Unique identifier that contains information necessary to track back to the original record in the source dataset. |
| **SOURCESYSTEMTYPE**           | String | Type of source database or system that the record was drawn from (federal, nonfederal, or interagency). |
| **SOURCESYSTEM**               | String | Name of or other identifier for source database or system that the record was drawn from. See Table 1 in Short (2014), or \Supplements\FPAFODsourcelist.pdf, for a list of sources and their identifier. |
| **NWCGREPORTINGAGENCY**        | String | Active National Wildlife Coordinating Group (NWCG) Unit Identifier for the agency preparing the fire report (BIA = Bureau of Indian Affairs, BLM = Bureau of Land Management, BOR = Bureau of Reclamation, DOD = Department of Defense, DOE = Department of Energy, FS = Forest Service, FWS = Fish and Wildlife Service, IA = Interagency Organization, NPS = National Park Service, ST/C&L = State, County, or Local Organization, and TRIBE = Tribal Organization). |
| **NWCGREPORTINGUNIT_ID**       | String | Active NWCG Unit Identifier for the unit preparing the fire report. |
| **NWCGREPORTINGUNIT_NAME**     | String | Active NWCG Unit Name for the unit preparing the fire report. |
| **SOURCEREPORTINGUNIT**        | String | Code for the agency unit preparing the fire report, based on code/name in the source dataset. |
| **SOURCEREPORTINGUNIT_NAME**   | String | Name of reporting agency unit preparing the fire report, based on code/name in the source dataset. |
| **LOCALFIREREPORT_ID**         | String | Number or code that uniquely identifies an incident report for a particular reporting unit and a particular calendar year. |
| **LOCALINCIDENTID**            | String | Number or code that uniquely identifies an incident for a particular local fire management organization within a particular calendar year. |
| **FIRE_CODE**                  | String | Code used within the interagency wildland fire community to track and compile cost information for emergency fire suppression (https://www.firecode.gov/).|
| **FIRE_NAME**                  | String | Name of the incident, from the fire report (primary) or ICS-209 report (secondary). |
| **ICS209INCIDENT_NUMBER**      | String | Incident (event) identifier, from the ICS-209 report. |
| **ICS209NAME**                 | String | Name of the incident, from the ICS-209 report. |
| **MTBS_ID**                    | String | Incident identifier, from the MTBS perimeter dataset. |
| **MTBSFIRENAME**               | String | Name of the incident, from the MTBS perimeter dataset. |
| **COMPLEX_NAME**               | String | Name of the complex under which the fire was ultimately managed, when discernible. |
| **FIRE_YEAR**                  | Integer | Calendar year in which the fire was discovered or confirmed to exist. |
| **DISCOVERY_DATE**             | Float | Date on which the fire was discovered or confirmed to exist. |
| **DISCOVERY_DOY**              | Integer | Day of year on which the fire was discovered or confirmed to exist. |
| **DISCOVERY_TIME**             | String | Time of day that the fire was discovered or confirmed to exist. |
| **STATCAUSECODE**              | Float | Code for the (statistical) cause of the fire. |
| **STATCAUSEDESCR**             | String | Description of the (statistical) cause of the fire. |
| **CONT_DATE**                  | Float | Date on which the fire was declared contained or otherwise controlled (mm/dd/yyyy where mm=month, dd=day, and yyyy=year). |
| **CONT_DOY**                   | Float | Day of year on which the fire was declared contained or otherwise controlled. |
| **CONT_TIME**                  | String | Time of day that the fire was declared contained or otherwise controlled (hhmm where hh=hour, mm=minutes). |
| **FIRE_SIZE**                  | Float | Estimate of acres within the final perimeter of the fire. |
| **FIRESIZECLASS**              | String | Code for fire size based on the number of acres within the final fire perimeter expenditures (A=greater than 0 but less than or equal to 0.25 acres, B=0.26-9.9 acres, C=10.0-99.9 acres, D=100-299 acres, E=300 to 999 acres, F=1000 to 4999 acres, and G=5000+ acres). |
| **LATITUDE**                   | Float | Latitude (NAD83) for point location of the fire (decimal degrees). |
| **LONGITUDE**                  | Float | Longitude (NAD83) for point location of the fire (decimal degrees). |
| **OWNER_CODE**                 | Float | Code for primary owner or entity responsible for managing the land at the point of origin of the fire at the time of the incident. |
| **OWNER_DESCR**                | String | Name of primary owner or entity responsible for managing the land at the point of origin of the fire at the time of the incident. |
| **STATE**                      | String | Two-letter alphabetic code for the state in which the fire burned (or originated), based on the nominal designation in the fire report. |
| **COUNTY**                     | String | County, or equivalent, in which the fire burned (or originated), based on nominal designation in the fire report. |
| **FIPS_CODE**                  | String | Three-digit code from the Federal Information Process Standards (FIPS) publication 6-4 for representation of counties and equivalent entities. |
| **FIPS_NAME**                  | String | County name from the FIPS publication 6-4 for representation of counties and equivalent entities. |


