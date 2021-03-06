### Pitches
Repo link: https://github.com/macc254/Pitches.git

## Author
Mercy Bore
## Project description

In life, you only have 60 seconds to impress someone. 1 minute can make or break you. This is an app that allows you to make a pitch, other users can downvote or upvote it and leave comments 
## BDD
A user should be able to:
- See the pitches other people have posted.
- Be signed to leave a comment
- Receive a welcoming email on sign up.
- View the pitches  created in  profile page.
- Comment on the different pitches and leave feedback.
- Submit a pitch in any category.
- View the different categories.


### Set-up instructions

- Install Python3 installed in your machine together with venv and pip.
- Set up the virtual environment and activate it

$ python3.8 -m venv virtual
$ source virtual/bin/activate

$ git clone https://github.com/macc254/Pitches.git
- Navigate into the cloned project.

- Install all the necessary modules using requiments.txt 
pip install -r requirements.txt

$ cd news-api

Create a start.sh file
- $ touch start.sh

On your start.sh file , add the command for executing manage.py (python3.8 manage.py server), which will start the server.


Give the file execution permissions.
- $ chmod a+x start.sh

command to run your application
- $ ./start.sh

## Technologies Used

- Python (Flask)
- Jinja2
- HTML
- CSS
- Bootstrap

## LICENSE
Copyright 2022 Mercy Bore.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
