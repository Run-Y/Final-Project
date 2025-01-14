# 警告内容列表
ANALYSIS_ICE = [
    "Glacier melting reduces surface reflectivity, causing the Arctic to absorb more solar energy, accelerating global warming and affecting climate stability.",
    "Glacier melting changes ocean salinity, impacting marine ecosystems and species that depend on salinity balance.",
    "Initially, excessive glacier meltwater causes flooding; later, the disappearance of glaciers leads to long-term freshwater shortages.",
    "Glacier melting may cause glacial lake outburst floods, landslides, and floods, threatening residents in mountainous regions.",
    "Glacier retreat reduces freshwater supply, affecting crop yields in regions relying on glacier-fed irrigation.",
    "Melting glaciers decrease river flow, impacting hydropower generation in glacier-fed regions."
]

# 建议内容列表
ADVICES_ICE = [
    "Use energy-efficient appliances, opt for public transport, cycling, or walking to minimize fossil fuel use.",
    "Promote renewable energy such as solar and wind power to reduce reliance on coal and oil.",
    "Curb unnecessary consumption, especially high-energy products and services, to minimize resource waste.",
    "Participate in tree-planting activities to increase greenery and absorb carbon dioxide.",
    "Actively participate in or donate to glacier conservation funds to promote scientific research and ecological restoration.",
]

# 模板库文件：用于生成冰层质量分析的随机句式
ANALYSIS_ICE_Analysis_Templates = [
    "From {start_year} to {end_year}, the {ice_mass_type} ice mass showed {trend}. Starting at {start_mass:.2f} Gigatonnes and ending at {end_mass:.2f} Gigatonnes, the total change was {total_change_abs:.2f} Gigatonnes. On average, it changed by {average_change_rate:.2f} Gigatonnes per year.",
    "Between {start_year} and {end_year}, the {ice_mass_type} ice mass experienced {trend}. The ice mass decreased from {start_mass:.2f} to {end_mass:.2f} Gigatonnes, a total loss of {total_change_abs:.2f} Gigatonnes, averaging a yearly change of {average_change_rate:.2f} Gigatonnes.",
    "Over the period from {start_year} to {end_year}, the {ice_mass_type} ice mass exhibited {trend}, with a total change of {total_change_abs:.2f} Gigatonnes from {start_mass:.2f} to {end_mass:.2f} Gigatonnes, averaging {average_change_rate:.2f} Gigatonnes per year."
]



# 警告内容列表
ANALYSIS_SEA = [
    "The global sea level has risen by about 20 cm over the past century, with the rate accelerating in the last 30 years, damaging coastal ecosystems and reducing biodiversity.",
    "Coastal areas face frequent floods and storm surges, causing property damage and casualties. For example, if sea levels continue rising at the current rate, cities like New York and Shanghai may face severe flooding in the coming decades.",
    "Residents in low-lying areas are forced to migrate, creating environmental refugees and increasing social pressure.",
]

# 建议内容列表
ADVICES_SEA = [
    "Use energy-efficient appliances, opt for public transport, cycling, or walking to minimize fossil fuel use.",
    "Promote renewable energy such as solar and wind power to reduce reliance on coal and oil."
]

# 模板库文件
ANALYSIS_SEA_Sentence_Templates = [
    "Between {start_year} and {end_year}, the Global Mean Sea Level (GMSL) showed significant changes. "
    "It started at {start_gmsl:.2f} mm and increased to {end_gmsl:.2f} mm, resulting in a total rise of {gmsl_change:.2f} mm. "
    "On average, the sea level was {mean_gmsl:.2f} mm during this period.",

    "From {start_year} to {end_year}, the GMSL rose from {start_gmsl:.2f} mm to {end_gmsl:.2f} mm, "
    "with a total increase of {gmsl_change:.2f} mm. The average sea level during these years was {mean_gmsl:.2f} mm, "
    "ranging between a minimum of {min_gmsl:.2f} mm and a maximum of {max_gmsl:.2f} mm.",

    "During the years {start_year} to {end_year}, the sea level data reveals a clear upward trend. "
    "The GMSL began at {start_gmsl:.2f} mm and ended at {end_gmsl:.2f} mm, marking a rise of {gmsl_change:.2f} mm. "
    "Average levels hovered around {mean_gmsl:.2f} mm, with extremes recorded at {min_gmsl:.2f} mm and {max_gmsl:.2f} mm.",

    "The GMSL experienced noticeable changes between {start_year} and {end_year}. "
    "Starting at {start_gmsl:.2f} mm, it rose to {end_gmsl:.2f} mm, "
    "resulting in a net increase of {gmsl_change:.2f} mm. "
    "Average sea levels over this period were {mean_gmsl:.2f} mm, with values ranging from {min_gmsl:.2f} mm to {max_gmsl:.2f} mm.",

    "From {start_year} to {end_year}, the global sea level saw a rise from {start_gmsl:.2f} mm to {end_gmsl:.2f} mm. "
    "This represents a total increase of {gmsl_change:.2f} mm. The average GMSL during this time was around {mean_gmsl:.2f} mm, "
    "with the highest and lowest levels recorded at {max_gmsl:.2f} mm and {min_gmsl:.2f} mm, respectively."
]

climate_disasters = {
    1993: "Severe floods hit Germany, Austria, and the Czech Republic, resulting in hundreds of deaths and significant property damage.",
    1994: "A severe drought hit northeast Brazil, impacting millions of people and leading to agricultural losses and water shortages.",
    1997: "One of the strongest El Niño events of the 20th century, causing global climate anomalies, including droughts and floods in several regions, especially affecting South Asia, Southeast Asia, and South America.",
    1999: "A major hurricane in the U.S. caused extensive flooding along the east coast, particularly in North Carolina, with significant property damage and several deaths.",
    2000: "Australia experienced extreme temperatures during the summer, leading to a severe heatwave that contributed to wildfires and crop failures.",
    2003: "Several European countries experienced extreme heat, with temperatures exceeding 40°C, leading to over 70,000 deaths and severe agricultural damage.",
    2004: "Although caused by an earthquake, the tsunami had far-reaching impacts, affecting several countries along the Indian Ocean and causing over 230,000 deaths.",
    2005: "One of the most destructive hurricanes in U.S. history, leading to about 1,800 deaths, severe flooding in New Orleans, and significant economic loss.",
    2006: "India experienced a heatwave that led to hundreds of deaths, with temperatures soaring above 45°C in several regions.",
    2007: "A series of devastating bushfires in southeastern Australia, resulting in over 170 deaths and the destruction of thousands of homes.",
    2008: "A devastating tropical cyclone struck Myanmar, causing more than 130,000 deaths and widespread destruction.",
    2009: "A powerful cyclone hit Bangladesh and India, causing floods, landslides, and leading to hundreds of deaths and the displacement of thousands of people.",
    2010: "Russia experienced extreme heat, with temperatures surpassing 40°C, leading to devastating wildfires and agricultural losses, causing numerous deaths.",
    2011: "A massive earthquake and tsunami struck Japan, causing over 15,000 deaths and triggering the Fukushima nuclear disaster.",
    2012: "One of the most devastating storms in U.S. history, affecting the East Coast and causing widespread flooding and power outages, resulting in dozens of deaths.",
    2013: "The Philippines was struck by Typhoon Haiyan, one of the strongest tropical cyclones in history, resulting in over 6,000 deaths and massive property damage.",
    2014: "A series of intense bushfires across Australia, leading to the destruction of large areas of land and affecting thousands of people.",
    2015: "The 2015 El Niño event intensified, leading to severe droughts, floods, and extreme weather phenomena across the globe.",
    2016: "A massive wildfire in Alberta, Canada, caused the evacuation of over 88,000 residents and destroyed thousands of homes.",
    2017: "One of the most devastating hurricanes in U.S. history, particularly impacting Texas, causing widespread flooding and over 100 deaths.",
    2018: "Several large wildfires in California, including the Camp Fire, caused the deaths of 85 people and the destruction of entire communities.",
    2019: "A massive bushfire destroyed millions of hectares of land, caused at least 33 deaths, and led to the loss of billions of animals, with climate change exacerbating the fire intensity and spread.",
    2020: "In 2020, the U.S. experienced multiple extreme weather events, including hurricanes, storms, and floods, resulting in severe infrastructure damage and casualties.",
    2021: "Heavy rainfall caused severe flooding in Germany, Belgium, and the Netherlands, leading to hundreds of deaths, displacing tens of thousands, and presenting challenging recovery efforts.",
    2022: "Pakistan experienced one of the most severe floods in its history in 2022. Continuous rainfall caused rivers to overflow, resulting in over 1,700 deaths, the destruction of millions of homes, and significant damage to agriculture and infrastructure.",
    2023: "The Middle East experienced extreme heat, with heatwaves and wildfires in the Hormuz region causing massive property damage and loss of life, with climate change exacerbating the occurrence of extreme weather.",
    2024: "In early 2024, several Southeast Asian countries, such as Vietnam, Thailand, and the Philippines, experienced heavy rainfall and flooding, leading to significant casualties and infrastructure damage. Climate change intensified extreme rainfall events, worsening flood disasters in the region.",
}

environmental_recommendations = {
    1993: "Implement sustainable urban planning to improve flood defenses, including natural barriers such as wetlands and mangrove forests, to mitigate the impacts of rising sea levels.",

    1994: "Promote water conservation practices and adopt water-efficient technologies, such as drip irrigation, while also reducing carbon emissions that contribute to global warming and extreme weather events.",

    1997: "Strengthen international cooperation for climate resilience, invest in early warning systems, and reduce greenhouse gas emissions to slow the pace of global warming and ocean acidification.",

    1999: "Enhance coastal protection infrastructure, including sea walls, dunes, and natural buffers, and advocate for policies to limit coastal development that exacerbates the impacts of sea level rise.",

    2000: "Invest in renewable energy sources to reduce dependence on fossil fuels, which contribute to climate change and extreme weather events. Protect forests and green spaces to absorb CO2 and reduce urban heat islands.",

    2003: "Implement strategies for cooling cities, such as increasing tree canopy coverage and green roofs, and support policies that limit carbon emissions to slow the pace of ice cap melting and ocean warming.",

    2004: "While tsunamis are not directly caused by climate change, rising sea levels can increase the risk of coastal flooding. It's important to invest in disaster preparedness, coastal defenses, and ecosystem restoration to protect vulnerable communities.",

    2005: "Support coastal restoration efforts, including mangrove and coral reef protection, to buffer coastal communities from storm surges, and reduce emissions to prevent the exacerbation of hurricane intensity due to climate change.",

    2006: "Strengthen climate adaptation strategies, including water management improvements and cooling technologies, and advocate for the global reduction of fossil fuel emissions to slow global warming and mitigate extreme heat events.",

    2007: "Promote controlled burns and forest management strategies to prevent wildfires, and reduce the carbon footprint of agriculture and transportation to slow the melting of polar ice, which can contribute to more severe fire seasons.",

    2008: "Build resilient infrastructure to withstand extreme weather, and invest in renewable energy to reduce global emissions, which contribute to the increasing frequency and intensity of cyclones.",

    2009: "Strengthen flood defenses and improve disaster response mechanisms, while also focusing on the mitigation of climate change through the reduction of greenhouse gas emissions to limit the impacts of future cyclones and rising sea levels.",

    2010: "Expand the use of renewable energy to reduce reliance on fossil fuels, which contribute to higher global temperatures, and enhance forest fire management strategies to protect ecosystems and communities.",

    2011: "Focus on renewable energy solutions and energy efficiency to decrease reliance on nuclear power and fossil fuels, reducing the risk of environmental disasters exacerbated by climate change, including rising sea levels and extreme weather events.",

    2012: "Implement coastal defense strategies such as restoring wetlands and dunes, and adopt green energy policies to reduce the carbon emissions that contribute to more frequent and intense storms.",

    2013: "Support climate resilience initiatives, such as the development of disaster-resistant infrastructure and early warning systems, while addressing the root causes of climate change through global emission reductions.",

    2014: "Promote land restoration and reforestation to mitigate the effects of wildfires, and transition to a low-carbon economy to slow the impacts of climate change and reduce the occurrence of extreme heat events.",

    2015: "Foster international collaboration on climate adaptation and invest in sustainable agriculture to help regions vulnerable to El Niño events, while reducing emissions to prevent future extreme climate events linked to global warming.",

    2016: "Strengthen wildfire prevention and mitigation strategies, while promoting policies aimed at reducing emissions from industries and transportation that contribute to rising global temperatures and increasing wildfire risks.",

    2017: "Implement stricter regulations for coastal development and invest in flood mitigation strategies, while committing to a global reduction in carbon emissions to mitigate the frequency and intensity of hurricanes.",

    2018: "Expand the use of renewable energy to reduce fossil fuel emissions, and support fire prevention strategies that focus on land management and climate-resilient communities.",

    2019: "Address climate change by implementing carbon reduction policies and investing in ecosystem restoration projects to prevent the devastation caused by bushfires.",

    2020: "Strengthen climate resilience efforts, including building infrastructure designed to withstand extreme weather events and promoting policies that reduce carbon emissions and mitigate climate change.",

    2021: "Improve flood management systems and invest in nature-based solutions, such as restoring wetlands, to absorb excess water and protect vulnerable areas from the impacts of rising sea levels.",

    2022: "Invest in flood control infrastructure, and implement sustainable water management practices, while addressing the root causes of climate change by reducing global emissions.",

    2023: "Focus on sustainable land use and renewable energy solutions to reduce heat intensity and prevent further environmental degradation from rising temperatures.",

    2024: "Strengthen flood defenses and improve disaster preparedness plans, while addressing climate change through mitigation efforts such as reducing deforestation and promoting low-carbon energy solutions.",
}



