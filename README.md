# Genome-Data-Parser

This repository is dedicated to the design and construction of a genomic data parser for the Tublitz Neuroscience lab at the University of Oregon. All of the actual genomic data is hidden and private, and depending on how things play out the final version of this parser may also be made private.

The program utilizes 
* <b>Pandas</b> for handling CSV data 
* <b>XLRD</b> module for backup Excel support
* <b>PyQT4</b> for GUI creation
* <b>Matplotlib</b> for statistical representations
* <b>Py2exe</b> for executable construction

Features:
* Works with all csv/xls/xlsx data files
* Search across all column rows by keyword, including rows containing sub-arrays
* Refine data through additional searches across columns
* Pie-chart output for representations of data composition
* Output final data as CSV in auto-dated files with optional user savenames

The end goal is a multifaceted interface for combing through very large sets of data with visuals describing terms of interest.
