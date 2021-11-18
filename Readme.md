Welcome to my quick CTA( Chicago Transit Authority ) API project. 
First install Pipenv , and then run `pipenv run basic_gui` this will show a neat GUI application. 

Alternatively you can run Pytest directly with `pipenv run basic_gui`


`pipenv run run_tests --json-report  --api_key CTA_API_KEY  --mapid CTA_MAP_ID , --expected_station_name Expected_Station_Name`

For example 
`pipenv run run_tests --json-report  --api_key CTA_API_KEY  --mapid 40360  --expected_station_name Southport`


