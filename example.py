from boatLookup import RegisteredBoats
import sys,json

boats = RegisteredBoats()
#can also be:
#boats = RegisteredBoats('/path/to/json/auth/file.json')
#if none defined, './keys.json' is default


query = sys.argv[1] if len(sys.argv) > 1 else ''

while query != '/q':
    if query:
        ans = boats.lookup(query)
        print(json.dumps(ans,indent=2))

    query = input('Enter a boat id: ("/q" to quit)\n>')
