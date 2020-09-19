# Google Search With Python
A python script you can use this to develop a backend service for a desktop application or implement a website search or app search with the python code running on your server

## What does it do?
It performs brings back the top x results you would see if you search "SEARCH TEXT" on Google's website. You can search anything in this way even change the tld for different regions results.

## How to use?
search(query, tld = 'co.in', lang = 'en', num = 10, start = 0, stop = None, pause = 2)
### query: This is the text that you search
### tld: This refers to the top level domain value like com.pk or comm
### lang: Language you choose
### num: Specifies the number of results we want
### start: Specify from wehre to start the results. We keep it to 0 to begin from the very start
### stop: Last result to retrieve (If None, keeps searching forever)
### pause: Used to specify the number of seconds to pause between consecutive HTTP requests because if we hit too many requests, Google can block our IP
