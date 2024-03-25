# effective_terrorism_tactics_exploration

Where the dataset can be found.
https://www.start.umd.edu/gtd/contact/download

Name of exploration.
effective_terrorism_tactics_exploration
	what type of weapons and attacks successfully used most often 

Size of Dataset.
How many Rows and Columns?
    209706 rows and 128 columns

Description of fields.
    Categorical Fields:
    Event ID (eventid): A unique identifier for each terrorist event.
    Year (iyear): The year in which the incident occurred.
    Month (imonth): The month of the incident.
    Day (iday): The day of the month of the incident.
    Extended (extended): Indicates whether the duration of the incident was extended.
    Resolution (resolution): Details about the resolution of the incident.
    Country Code (country): A numerical code representing the country in which the incident occurred.
    Country Name (country_txt): The name of the country in which the incident occurred.
    Region Code (region): A numerical code representing the geographical region of the incident.
    Database Source (dbsource): The source from which the data was obtained.
    International Logistical (INT_LOG), International Ideological (INT_IDEO), International Miscellaneous (INT_MISC), International Any (INT_ANY): These seem to be binary flags indicating international involvement or connections.
    Related Incidents (related): Related incidents or events.

    Quantitative Fields:
    Approximate Date (approxdate): An approximate date of the incident if the exact date is unknown.

    Mixed Fields:
    Add Notes (addnotes): Additional notes or details about the incident.
    Source Citation 1 (scite1), Source Citation 2 (scite2), Source Citation 3 (scite3): Citations or sources providing information about the incident.

    Missing Data or Erroneous Values:
    The "approxdate" field",  "resolution" field",  "addnotes", "scite1", "scite2", and "scite3" fields all contain "NaN" indicating missing data.
    Also Negative values i.e. -9 are present in fields like "INT_LOG", "INT_IDEO", "INT_MISC", and "INT_ANY".

    Data Summarization:
    The data appears to be raw and unprocessed, containing detailed information on terrorist incidents.
    Each row represents a separate incident

Potential inquies
    Trend Analysis:

    What are the trends in terrorism incidents over time?
    Are there any seasonal patterns or spikes in terrorist activity?
    Geographical Analysis:

    Which regions/countries are most affected by terrorism?
    Are there specific areas within countries that experience higher incidents?
    Attack Characteristics:

    What are the most common types of terrorist attacks (e.g., bombings, shootings)?
    Are there specific weapons or tactics frequently used?
    Casualties and Impact:

    How have casualties varied over time and across different regions?
    Are there certain types of targets that result in more casualties?
    Perpetrator Analysis:

    What are the profiles of terrorist groups responsible for attacks?
    Are there any trends in the affiliation or ideology of these groups?
    Counterterrorism Efforts:

    How effective have counterterrorism measures been in reducing incidents or mitigating impact?
    Are there any correlations between specific policies and changes in terrorist activity?

Poltential Recommendations
    Possible recommendations

    Implementing targeted security measures in regions with high terrorist activity.

    Enhancing intelligence-sharing and cooperation among countries to combat transnational terrorism.

    Investing in community-based initiatives to address underlying grievances and prevent radicalization.

    Evaluating the effectiveness of existing counterterrorism policies and adjusting strategies as needed.


OUTLINE FOR THIS EXPLORATION
    1. Load data
    2. Explor data
    3. Clean data
    4. Plot data


Step one transform the data to .csv
    Dataset was origonally excel spreadsheet, so I changed it to a .csv for easier manipulation

Step two first exploration of data
    Ensured the data was loaded correctly and was able to see how many rows, columns, and what information I was working with.

    conduct basic checks to see .head; .sample; .info; .describe
        upon doing basic data eploration these are the follwoing column descriptions
            Event ID (eventid): A unique identifier for each terrorist event.
            Year (iyear): The year of the incident.
            Month (imonth): The month of the incident.
            Day (iday): The day of the incident.
            Approximate Date (approxdate): An approximate date of the incident.
            Extended (extended): Indicates whether the incident extended beyond 24 hours.
            Resolution (resolution): The resolution of the incident.
            Country Code (country): A numeric code representing the country where the incident occurred.
            Country Name (country_txt): The name of the country where the incident occurred.
            Region Code (region): A numeric code representing the region where the incident occurred.
            Region Name (region_txt): The name of the region where the incident occurred.
            Province/State (provstate): The name of the province or state where the incident occurred.
            City (city): The name of the city where the incident occurred.
            Latitude (latitude): The latitude coordinate of the incident location.
            Longitude (longitude): The longitude coordinate of the incident location.
            Specificity (specificity): Indicates the specificity of the location information.
            Vicinity (vicinity): Indicates whether the incident occurred in the vicinity of the location.
            Location (location): Description of the location.
            Summary (summary): A summary of the incident.
            Criteria 1, 2, 3 (crit1, crit2, crit3): Criteria indicating the certainty that the incident is terrorism-related.
            Doubtful Terrorism (doubtterr): Indicates whether there is doubt about the incident being a terrorist act.
            Alternative (alternative): Alternative information about the incident.
            Multiple (multiple): Indicates whether there were multiple incidents involved.
            Success (success): Indicates the success of the attack.
            Suicide (suicide): Indicates whether the attack was a suicide attack.
            Attack Type 1, 2, 3 (attacktype1, attacktype2, attacktype3): Numeric code representing the primary attack type.
            Target Type 1, 2, 3 (targtype1, targtype2, targtype3): Numeric code representing the primary target type.
            Target Subtype 1, 2, 3 (targsubtype1, targsubtype2, targsubtype3): Numeric code representing the primary target subtype.
            Corp/Business 1, 2, 3 (corp1, corp2, corp3): Name of the corporation or business entity targeted in the incident.
            Target 1, 2, 3 (target1, target2, target3): Description of the target.
            Nationality 1, 2, 3 (natlty1, natlty2, natlty3): Numeric code representing the nationality of the target.
            Group Name (gname): Name of the terrorist group responsible for the incident.
            Group Subname (gsubname): Subname of the terrorist group responsible for the incident.
            Motive (motive): Motive behind the incident.
            Gun Uncertainty 1, 2, 3 (guncertain1, guncertain2, guncertain3): Indicates uncertainty regarding the use of firearms.
            Individual (individual): Indicates whether the incident was carried out by an individual.
            Number of Perpetrators (nperps): Number of perpetrators involved in the incident.
            Number of Perpetrators Captured (nperpcap): Number of perpetrators captured.
            Claimed (claimed): Indicates whether the incident was claimed by a group or individual.
            Claim Mode 1, 2, 3 (claimmode, claimmode2, claimmode3): Numeric code representing the claim mode.
            Claim Mode Text 1, 2, 3 (claimmode_txt, claimmode2_txt, claimmode3_txt): Textual description of the claim mode.
            Compensation Claim (compclaim): Indicates whether there was a claim for compensation.
            Weapon Type 1, 2, 3, 4 (weaptype1, weaptype2, weaptype3, weaptype4): Numeric code representing the primary weapon type used.
            Weapon Subtype 1, 2, 3, 4 (weapsubtype1, weapsubtype2, weapsubtype3, weapsubtype4): Numeric code representing the primary weapon subtype used.
            Weapon Detail (weapdetail): Details about the weapons used.
            Number of Killed (nkill): Number of people killed in the incident.
            Number of U.S. Citizens Killed (nkillus): Number of U.S. citizens killed in the incident.
            Number of Perpetrators Killed (nkillter): Number of perpetrators killed in the incident.
            Number of Wounded (nwound): Number of people wounded in the incident.
            Number of U.S. Citizens Wounded (nwoundus): Number of U.S. citizens wounded in the incident.
            Number of Perpetrators Wounded (nwoundte): Number of perpetrators wounded in the incident.
            Property Damage (property): Indicates whether property was damaged in the incident.
            Property Extent (propextent): Extent of property damage.
            Property Extent Text (propextent_txt): Textual description of the property extent.
            Property Value (propvalue): Value of the property damaged.
            Property Comment (propcomment): Comment on the property damage.
            Is Hostage Taken (ishostkid): Indicates whether hostages were taken in the incident.
            Number of Hostages (nhostkid): Number of hostages taken in the incident.
            Number of U.S. Citizens Taken Hostage (nhostkidus): Number of U.S. citizens taken hostage in the incident.
            Duration in Hours (nhours): Duration of the incident in hours.
            Duration in Days (ndays): Duration of the incident in days.
            Divert (divert): Indicates whether the incident involved an attempted diversion or distraction.
            Kidnapping/Hijacking Country (kidhijcountry): Country where the kidnapping or hijacking took place.
            Ransom (ransom): Indicates whether ransom was demanded.
            Ransom Amount (ransomamt): Amount of ransom demanded.
            Ransom Paid in USD (ransompaidus): The amount of ransom paid in U.S. dollars.
            Ransom Note (ransomnote): Details or contents of any ransom note left by the perpetrators.
            Hostage Outcome (hostkidoutcome): Outcome of the hostage situation, represented numerically.
            Hostage Outcome Description (hostkidoutcome_txt): Textual description of the outcome of the hostage situation.
            Number Released (nreleased): Number of hostages released.
            Additional Notes (addnotes): Any additional notes or details about the incident.
            scite1, scite2, scite3: Source citations or references providing information about the incident.
            dbsource: Source from which the data was obtained.
            INT_LOG: Binary flag indicating whether the incident had an international logistical component.
            INT_IDEO: Binary flag indicating whether the incident had an international ideological component.
            INT_MISC: Binary flag indicating whether the incident had other international components.
            INT_ANY: Binary flag indicating whether the incident had any international component.
            related: Related incidents or events.

Created a new datafram and removed the following columns. The data frams are too large to update to github.
    # Remove columns to make database smaller.
    columns_to_remove = ["imonth", "iday", "approxdate", "extended", "latitude", "longitude", "specificity", "property", "resolution", "claimmode",	"claimmode_txt",	"claim2",	"claimmode2",	"claimmode2_txt",	"claim3",	"claimmode3",	"claimmode3_txt",	"compclaim", "propextent",	"propextent_txt",	"propvalue",	"propcomment", "nhours", "ndays", "addnotes", "scite1", "scite2", "scite3", "dbsource", "INT_LOG", "INT_IDEO", "INT_MISC", "INT_ANY", "location", "alternative",	"alternative_txt"]

    # Drop the columns
    cleaned_terrorism_df.drop(columns = columns_to_remove, inplace = True)

    # Create a new CSV file
    #cleaned_terrorism_df.to_csv("cleaned_terrorism.csv", index = False)


