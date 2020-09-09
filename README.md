# BoatIDLookup
 Lookup boat registration information by state's boat id

 Currently only available for texas lookups, but is written to easily integrate support for other states.
 
 ## API Auth Setup
 ### keys.json file
 This file is used to store all API keys 
 
 ```json
 {
	"tx": {
		"id": "<API KEY ID>",
		"secret": "<API KEY SECRET>"
	}
}
 ```
 ### Texas
 - Create an account on the [Socrata Developer Portal](https://dev.socrata.com/)
 - Create an API key and add the id & secret to the keys.json file
