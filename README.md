# BoatIDLookup
 Lookup boat registration information by state's boat id

 Currently only available for texas lookups, but is written to easily integrate support for other states.
 
 ## API Auth Setup
 ### keys.json file
 This file is used to store all API keys.
 By default, it is expected to be located in the base directory, but this can be changed by defining the filepath when instantiating the class: `BoatLookup("<Filepath>")`
 
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
