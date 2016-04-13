# BayesDB

This document aims to show a new way of exploring the College Scorecard dataset recently published by the U.S. Department of Education: https://collegescorecard.ed.gov/data/.
The Economist triggered discussion about this dataset in an article describing a ranking system based only on earnings after graduation: http://www.economist.com/blogs/graphicdetail/2015/10/value-university
To explore trends in the data, we are going to use BayesDB.

BayesDB is a Bayesian database that lets users query the probable implications of their data as easily as a SQL database lets them query the data itself. Using the built-in Bayesian Query Language (BQL), users with no statistics training can solve basic data science problems, such as detecting predictive relationships between variables, inferring missing values, simulating probable observations, and identifying statistically similar database entries.
BayesDB is suitable for analyzing complex, heterogeneous data tables with up to tens of thousands of rows and hundreds of variables. No preprocessing or parameter adjustment is required, though experts can override BayesDB's default assumptions when appropriate.