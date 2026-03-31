##
## Programmer:    Craig Stuart Sapp <craig@ccrma.stanford.edu>
## Creation Date: Thu Jun  8 19:45:08 PDT 2023
## Last Modified: Thu Jun  8 19:45:11 PDT 2023
## Syntax:        GNU Makefile
## Filename:      _includes/metadata/Makefile
## vim:           ts=3:nowrap
##
## Description: Download metadata for the 1520s project from the Google Spreadsheet
##              for the project's metadata.  You need to update the SID variable below
##              when the deployment of the Google Apps Script has changed.
##
##              Type "make" in this directory to download the JSON files for the metadata.
##


#SID for 1520s Project Metadata
SID = AKfycbyqUJBsnMxgCUCugnXHko1V008gBKcALuhm2zfHlaYlPkIiRPzWrgKfv__ODQaq-K4c

all: download

download: works

works:
	curl -L "https://script.google.com/macros/s/$(SID)/exec" > works.json


	# Only update if the file has changed
	if ! cmp -s temp_Josquin.csv ../../Josquin/Josquin.csv; then \
		mv temp_Josquin.csv ../../Josquin/Josquin.csv; \
		mkdir -p ../../_data/Josquin; \
		date +"last_updated: %e %B %Y" | sed 's/^ *//g' > ../../_data/Josquin/csv_metadata.yml; \
	else \
		rm temp_Josquin.csv; \
	fi
