# Energy Use and Affluence

I am reading the excellent book Energy and Civilization: A History by Vaclav Smil.

In Chapter 6, "Fossil-Fueled Civilization", Smil discusses how energy use directly correlates with a country's affluence. He provides an easy-to-understand correspondence:

Below ~120 kg oil equivalent/capita/year: Basic necessities cannot be guaranteed for all inhabitants.

Around 1 t oil equivalent/capita/year: Industrialization and rising incomes begin, with noticeable improvements in quality of life.

At least 2 t oil equivalent/capita/year: Achieving the beginnings of affluence—where most people enjoy a comfortable standard of living—typically requires at least 2 tons of oil equivalent per person per year, even in countries that use energy fairly efficiently.

Curious to see how this plays out in real-world data, I went to World Bank Data https://data.worldbank.org and downloaded two time series for each country:

GDP per capita, PPP (constant 2021 international $)

Energy use (kg of oil equivalent per capita)

After downloading these datasets, I wrote a Python script to plot both time series on the same graph (with dual axes) and to interpolate missing years. You can find the time series and script here: https://github.com/sergiorf/smilbook.

Plotting different countries or groups of countries together is fascinating and raises many questions. Let's look at some examples:

United States vs Western Europe

While both regions are well above Smil's 2t threshold for affluent societies, the first striking observation is the massive gap in energy use—almost 4t more oil equivalent per capita per year in the US. This may reflect greater energy efficiency in Europe among other factors.

Interestingly, energy use has been declining in both regions since the early 2000s, with a steep drop around the 2008 financial crisis that never fully recovered. In contrast, GDP per capita continues to rise, largely decoupled from energy use, except for dips during the 2008 crisis and the 2019 pandemic.

How to explain this decoupling? Likely factors include the shift toward service-based economies and improvements in energy efficiency. However, this makes me wonder whether these World Bank statistics account for indirect energy use—the energy incorporated in imported manufactured goods. If not, part of the energy footprint may simply be “offshored,” making the comparison more complex.

Spain vs Poland

This is a fascinating graph. The first property that catches my attention is how well correlated energy use and GDP per capita are for both Poland and Spain. Unlike the examples of the US and Western Europe, in these two countries both curves are closely coupled—perhaps indicating that the service sector is relatively less important compared to the previous regions.

Another striking feature is the sharp drop in energy consumption during the 2008 financial crisis in Spain, which burst an enormous real estate bubble and caused significant damage to the economy. Interestingly, even though GDP has now recovered to pre-2008 levels (after both the 2008 crisis and the 2019 pandemic), energy consumption has not fully rebounded and appears to be "decoupling" from GDP growth. I don't have a clear explanation for this.

The case of Poland is more straightforward: there has been steady growth since the early 1990s, likely due to the end of the Communist regime. Poland has now almost caught up with Spain in terms of GDP per capita, although energy use in Poland remains significantly higher—about 300 kg of oil equivalent per capita more. This may be due to lower energy efficiency, a higher share of manufacturing in the economy, a colder climate, or perhaps a combination of these factors.

Brazil vs China