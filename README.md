# power_school_assignment
16MIS0280 - MURARI MAHITH

for powerschool assignment done by Murari Mahith
Note: The code is available in github. https://github.com/MurariMahith/power_school_assignment

Auto - Complete text:

Installations:

1. Python
2. python-pip
3. flask (pip dependencies)
Note: To install flask `pip install flask`
4. http.server(available in python3)

Dependencies:

1. jquery
2. jquery-ui

Directions to use:

Assuming that all the softwares and dependendencies are installed and working,
For running Backend API server
1. Go to backend directory.
2. Run `python api.py` 
3. This will start api server running at 127.0.0.1:5000

For running front end
1. Go to front_end directory.
2. Run `python front_end.py`
3. Open any browser and enter 127.0.0.1:8080
4. You can see a small stylised form with one text box 
5. Enter any english word and after entering 2 words your suggestions should appear

Note : As we are working with two servers the time taken to show suggestions may take some time based on number of words with entered text(request) in dataset.
Note: As the words oncreases in our array it may take time to show suggestions please 'WAIT' if not shown suggestions, it will come up
Note: The output of api can be viewed in console(in web browser) for debugging purpose.

Working: 
We have a english words data set named 'words_dictionary.jsoon'
We load it in our api.py, here we accept a request and response with a json array.
The responded json array consists of words that contain the request word. (ex: request has 'co' the suggestions include 'acCOunts, COmpletions ...)
Now, in our index.html, on keypress event on our text box, we FETCH the the data from 127.0.0.1:5000 and THEN convert in into json format and THEN use in as array
Now, we use jquery and jquery-ui auto complete widget to show our auto complete suggestions in our ui
In index.html, we include all the relevant jquery and jquery-ui files, as a source for auto-complete widget we give the fetched json array from our api server

our project is up and running

CSS:
try,
hovering on button and text box, 

we can also use startswith() function in api.py to give words that starts with requested word only (ex: request-'co' suggested ='COmputer, COmplete ...' but not acCOunt, acCOmplish..')

Method 2:

if running python server to render index.html is very slow, please open the index.html in normal method and try suggestions (not recemmended)
this way we dont render our page on request with server but we simply open index.html file in front_end directory'

Test Outputs
