# BoatIDLookup
 Lookup boat registration information by state's boat id

 Currently only available for texas lookups, but is written to easily integrate support for other states.
 
 ## Usage
 ### Example 1
```python
from boatLookup import RegisteredBoats
boats = RegisteredBoats()

print(boats.lookup('TX12345'))

```
 ### Example 2
```python
from boatLookup import RegisteredBoats
import sys,json
boats = RegisteredBoats('/path/to/json/auth/file.json')



query = sys.argv[1] if len(sys.argv) > 1 else ''

while query != '/q':
    if query:
        ans = boats.lookup(query)
        print(json.dumps(ans,indent=2))

    query = input('Enter a boat id: ("/q" to quit)\n>')


```
 
 ## API Auth Setup
 ### keys.json file
 This file is used to store all API keys.
 By default, it is expected to be located in the base directory, but this can be changed by defining the filepath when instantiating the class: `RegisteredBoats("<Filepath>")`
 
#### The expected format looks like this
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
