# effective_terrorism_exploration

DAI COHORT 8 - Chris Thompson

### **Agenda**

- Data Information

- Objectives

- Exploratory Data Analysis

- Options for Future Analysis

- Conclusion/Recommendations

### **Introduction**

- **PURPOSE:** The primary purpose of this project is to explore the data given in the Global Terrorism Database to see correlations and develop future actionable insights and recommendations.

- **PROCESS**:

  - Data Cleaning

  - Exploratory Data Analysis

  - Interpretation of Results

  - Presentation and Visualization

## **Original Dataset**

- 1970 - 2020 Global Terrorism Database
- The original dataset had 209706 Rows and 135 columns.
- This was cleaned to 209706 Rows and 57 columns.

- Removed NaN values and columns not necessary for analysis.
- 9 categories of attacks
- Top 20 countries
- 12 Regions
- Where the dataset can be found.https://www.start.umd.edu/gtd/contact/download

## **About this dataset?**

- Global Terrorism Database
- 1962 - 2020 World Wide Terrorist attacks and events
- 190 Countries
- 12 regions

Description of fields.

- Categorical Fields:
- Event ID (eventid): A unique identifier for each terrorist event.
- Year (iyear): The year in which the incident occurred.
- Month (imonth): The month of the incident.
- Day (iday): The day of the month of the incident.
- Extended (extended): Indicates whether the duration of the incident was extended.
- Resolution (resolution): Details about the resolution of the incident.
- Country Code (country): A numerical code representing the country in which the incident occurred.
- Country Name (country\_txt): The name of the country in which the incident occurred.
- Region Code (region): A numerical code representing the geographical region of the incident.
- Database Source (dbsource): The source from which the data was obtained.
- International Logistical (INT\_LOG), International Ideological (INT\_IDEO), International Miscellaneous (INT\_MISC), International Any (INT\_ANY): These seem to be binary flags indicating international involvement or connections.
- Related Incidents (related): Related incidents or events.

Quantitative Fields:

Approximate Date (approxdate): An approximate date of the incident if the exact date is unknown.

Missing Data or Erroneous Values:

- The "approxdate" field", "resolution" field", "addnotes", "scite1", "scite2", and "scite3" fields all contain "NaN" indicating missing data.
- Also Negative values i.e. -9 are present in fields like "INT\_LOG", "INT\_IDEO", "INT\_MISC", and "INT\_ANY".

Data Summarization:

- The data appears to be raw and unprocessed, containing detailed information on terrorist incidents.
- Each row represents a separate incident

Potential inquiries

- Trend Analysis:
- What are the trends in terrorism incidents over time?
- Are there any seasonal patterns or spikes in terrorist activity?

Geographical Analysis:

- Which regions/countries are most affected by terrorism?
- Are there specific areas within countries that experience higher incidents?

Attack Characteristics:

- What are the most common types of terrorist attacks (e.g., bombings, shootings)?
- Are there specific weapons or tactics frequently used?

Casualties and Impact:

- How have casualties varied over time and across different regions?
- Are there certain types of targets that result in more casualties?

Perpetrator Analysis:

- What are the profiles of terrorist groups responsible for attacks?
- Are there any trends in the affiliation or ideology of these groups?

Counterterrorism Efforts:

- How effective have counterterrorism measures been in reducing incidents or mitigating impact?
- Are there any correlations between specific policies and changes in terrorist activity?
- Potential Recommendations

- Implementing targeted security measures in regions with high terrorist activity.
- Enhancing intelligence-sharing and cooperation among countries to combat transnational terrorism.
- Investing in community-based initiatives to address underlying grievances and prevent radicalization.
- Evaluating the effectiveness of existing counterterrorism policies and adjusting strategies as needed.

## Cleaning The Data

Step one transform the data to .csv

Dataset was originally excel spreadsheet, so I changed it to a .csv for easier manipulation

Step two first exploration of data.

Ensured the data was loaded correctly and was able to see how many rows, columns, and what information I was working with.

Conduct basic checks to see .head; .sample; .info; .describe

upon doing basic data exploration these are the following column descriptions

- Event ID (eventid): A unique identifier for each terrorist event.
- Year (iyear): The year of the incident.
- Month (imonth): The month of the incident.
- Day (iday): The day of the incident.
- Approximate Date (approxdate): An approximate date of the incident.
- Extended (extended): Indicates whether the incident extended beyond 24 hours.
- Resolution (resolution): The resolution of the incident.
- Country Code (country): A numeric code representing the country where the incident occurred.
- Country Name (country\_txt): The name of the country where the incident occurred.
- Region Code (region): A numeric code representing the region where the incident occurred.
- Region Name (region\_txt): The name of the region where the incident occurred.
- Province/State (provstate): The name of the province or state where the incident occurred.
- City (city): The name of the city where the incident occurred.
- Latitude (latitude): The latitude coordinate of the incident location.
- Longitude (longitude): The longitude coordinate of the incident location.
- Specificity (specificity): Indicates the specificity of the location information.
- Vicinity (vicinity): Indicates whether the incident occurred in the vicinity of the location.
- Location (location): Description of the location.
- Summary (summary): A summary of the incident.
- Criteria 1, 2, 3 (crit1, crit2, crit3): Criteria indicating the certainty that the incident is terrorism-related.
- Doubtful Terrorism (doubtterr): Indicates whether there is doubt about the incident being a terrorist act.
- Alternative (alternative): Alternative information about the incident.
- Multiple (multiple): Indicates whether there were multiple incidents involved.
- Success (success): Indicates the success of the attack.
- Suicide (suicide): Indicates whether the attack was a suicide attack.
- Attack Type 1, 2, 3 (attacktype1, attacktype2, attacktype3): Numeric code representing the primary attack type.
- Target Type 1, 2, 3 (targtype1, targtype2, targtype3): Numeric code representing the primary target type.
- Target Subtype 1, 2, 3 (targsubtype1, targsubtype2, targsubtype3): Numeric code representing the primary target subtype.
- Corp/Business 1, 2, 3 (corp1, corp2, corp3): Name of the corporation or business entity targeted in the incident.
- Target 1, 2, 3 (target1, target2, target3): Description of the target.
- Nationality 1, 2, 3 (natlty1, natlty2, natlty3): Numeric code representing the nationality of the target.
- Group Name (gname): Name of the terrorist group responsible for the incident.
- Group Subname (gsubname): Subname of the terrorist group responsible for the incident.
- Motive (motive): Motive behind the incident.
- Gun Uncertainty 1, 2, 3 (guncertain1, guncertain2, guncertain3): Indicates uncertainty regarding the use of firearms.
- Individual (individual): Indicates whether the incident was carried out by an individual.
- Number of Perpetrators (nperps): Number of perpetrators involved in the incident.
- Number of Perpetrators Captured (nperpcap): Number of perpetrators captured.
- Claimed (claimed): Indicates whether the incident was claimed by a group or individual.
- Claim Mode 1, 2, 3 (claimmode, claimmode2, claimmode3): Numeric code representing the claim mode.
- Claim Mode Text 1, 2, 3 (claimmode\_txt, claimmode2\_txt, claimmode3\_txt): Textual description of the claim mode.
- Compensation Claim (compclaim): Indicates whether there was a claim for compensation.
- Weapon Type 1, 2, 3, 4 (weaptype1, weaptype2, weaptype3, weaptype4): Numeric code representing the primary weapon type used.
- Weapon Subtype 1, 2, 3, 4 (weapsubtype1, weapsubtype2, weapsubtype3, weapsubtype4): Numeric code representing the primary weapon subtype used.
- Weapon Detail (weapdetail): Details about the weapons used.
- Number of Killed (nkill): Number of people killed in the incident.
- Number of U.S. Citizens Killed (nkillus): Number of U.S. citizens killed in the incident.
- Number of Perpetrators Killed (nkillter): Number of perpetrators killed in the incident.
- Number of Wounded (nwound): Number of people wounded in the incident.
- Number of U.S. Citizens Wounded (nwoundus): Number of U.S. citizens wounded in the incident.
- Number of Perpetrators Wounded (nwoundte): Number of perpetrators wounded in the incident.
- Property Damage (property): Indicates whether property was damaged in the incident.
- Property Extent (propextent): Extent of property damage.
- Property Extent Text (propextent\_txt): Textual description of the property extent.
- Property Value (propvalue): Value of the property damaged.
- Property Comment (propcomment): Comment on the property damage.
- Is Hostage Taken (ishostkid): Indicates whether hostages were taken in the incident.
- Number of Hostages (nhostkid): Number of hostages taken in the incident.
- Number of U.S. Citizens Taken Hostage (nhostkidus): Number of U.S. citizens taken hostage in the incident.
- Duration in Hours (nhours): Duration of the incident in hours.
- Duration in Days (ndays): Duration of the incident in days.
- Divert (divert): Indicates whether the incident involved an attempted diversion or distraction.
- Kidnapping/Hijacking Country (kidhijcountry): Country where the kidnapping or hijacking took place.
- Ransom (ransom): Indicates whether ransom was demanded.
- Ransom Amount (ransomamt): Amount of ransom demanded.
- Ransom Paid in USD (ransompaidus): The amount of ransom paid in U.S. dollars.
- Ransom Note (ransomnote): Details or contents of any ransom note left by the perpetrators.
- Hostage Outcome (hostkidoutcome): Outcome of the hostage situation, represented numerically.
- Hostage Outcome Description (hostkidoutcome\_txt): Textual description of the outcome of the hostage situation.
- Number Released (nreleased): Number of hostages released.
- Additional Notes (addnotes): Any additional notes or details about the incident.
- scite1, scite2, scite3: Source citations or references providing information about the incident.
- dbsource: Source from which the data was obtained.
- INT\_LOG: Binary flag indicating whether the incident had an international logistical component.
- INT\_IDEO: Binary flag indicating whether the incident had an international ideological component.
- INT\_MISC: Binary flag indicating whether the incident had other international components.
- INT\_ANY: Binary flag indicating whether the incident had any international component.
- related: Related incidents or events.

Created a new data frame and removed the following columns. The data frames are too large to update to Github.

# Remove columns to make database smaller.
columns_to_remove = ["imonth", "iday", "approxdate", "extended", "specificity", "property", "resolution", "claimmode", "claimmode_txt", "claim2", "claimmode2", "claimmode2_txt", "claim3", "claimmode3", "claimmode3_txt", "compclaim", "propextent", "propextent_txt", "propvalue", "propcomment", "nhours", "ndays", "addnotes", "scite1", "scite2", "scite3", "dbsource", "INT_LOG", "INT_IDEO", "INT_MISC", "INT_ANY", "location", "alternative", "alternative_txt", "provstate", "city"]

# Drop the columns
cleaned_terrorism_df.drop(columns=columns_to_remove, inplace=True)

# Create a new CSV file
cleaned_terrorism_df.to_csv("cleaned_terrorism.csv", index=False)

# Select object columns only
object_columns = cleaned_terrorism_df.select_dtypes(include=['object'])
object_columns.sample(20)

### **Objectives**

- Assess temporal trends.

- Analyze the frequency of terrorist incidents over time.

- Investigate the different types of terrorists attacks

- Correlation Analysis: Explore potential correlations between different variables, such as attack type and success, region and attack frequency, or where the most likely danger zones are located.

## **Applied Metrics for exploration.**

- **Year: The year of the incident.**

- **Country Name: The name of the country where the incident occurred.**

- **Region Name: The name of the region where the incident occurred.**

- **Target Type: Type of target that attack was meant for.**

- **Attack Type: Bombing, Armed assault, kidnapping, etc.**

- **Attack Success: Was the attack successful or not? (yes or no)**

- ![42068034-5daa-483e-960d-2d61c2035d3d](https://github.com/OKI300MER/effective_terrorism_exploration/assets/155767990/3b49f37f-3581-4523-9c72-53292009a9e3)Steady rise until mid- 1990's when it peaked before dropping considerably

  - Counterterrorism Measures

  - Diplomatic Efforts

○Economy

- Early 2000's began to rise until peak 2015 before returning back to early 1990's numbers

  - World Conflicts

  - Rise of ISIL

  - Proliferation of Extremist Ideologies

  - Globalization of Terrorism

- ![7474a8b0-fbca-4fee-a77f-e55c2e14b887](https://github.com/OKI300MER/effective_terrorism_exploration/assets/155767990/9e95ec49-e7e0-4fd6-adf8-baa60f3647e2)
Lethality is directly connected to the number of attacks

- As weapons and methods increased so did fatalities

- The most fatalities came from the Iraq Afghanistan conflicts

![aeaaf7c0-9bba-45f8-b3dc-66284995d48d](https://github.com/OKI300MER/effective_terrorism_exploration/assets/155767990/ef86c28d-0c37-497c-96aa-6005b5c5886c)

- Middle East & North Africa Highest

- South Asia

 - ![de1903be-9407-42eb-8686-a7173eadd1e1](https://github.com/OKI300MER/effective_terrorism_exploration/assets/155767990/844c3d5b-286e-4163-a3aa-ec663a7deeb4)Most likely to be involved in bombing or armed assault, these cause the most damage in the least amount of time

- Iraq and Afghanistan are top countries for attacks

- ![40784357-f116-47c4-97d4-d213de2dfa67](https://github.com/OKI300MER/effective_terrorism_exploration/assets/155767990/818bfec8-34b5-4fcb-a9dc-f05471e11255)Bombing and Armed assaults are most used and successful

- ![e4a08216-28c7-41e3-9bcd-1352ac296f0e](https://github.com/OKI300MER/effective_terrorism_exploration/assets/155767990/888d5c53-791e-434d-9dbe-8ea3f1c44530)Middle East is the top region for Terrorist Attacks

- Due to instability and multiple factions in the region

![878de2f1-4aa5-4dad-ad99-8a516f87faef](https://github.com/OKI300MER/effective_terrorism_exploration/assets/155767990/db96e920-d1e0-4b7f-a345-748a487d5842)

![d79fb536-2ad5-438a-88ac-51ba8b690def](https://github.com/OKI300MER/effective_terrorism_exploration/assets/155767990/f494cf21-db9a-498c-bf9f-28eb2d717adb)

## **Future Analysis**

- Create a predictive model based on the increase in attacks over years, countries with the most attacks, and the most used and successful types of attacks.

  - When and where will attacks happen?

  - In what regions will attacks be more successful?

  - What types of attacks will be the most successful?

## **Conclusions/Recommendations**

- Further investigation into the data to discover more trends for analysis.

- Conduct predictive analysis to help predict where and when attacks will happen.

- Conduct predictive analysis to help prevent terrorist attacks by improving Counterterrorism practices.
- The Middle East & North Africa and South Asia are the deadliest and most attacked regions.
  - Iraq and Afghanistan had the highest attack count from 2015 - 2020

- Bombing and Armed Assaults seem to be the most used and successful types of Terrorist Attack
- Prior to 1970 US had a lot of attacks due to civil rights
- 1980's Salvadoran Civil War
- Late 1980's early 1990's conflicts and civil war if Africa
- Iraq and Afghanistan had the highest amount of attacks in the last 2000's this is probably due to the ongoing conflicts
- Private citizens are easy target of opportunity
- Actual targeted are military, police, or government entities
