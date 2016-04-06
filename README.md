# cast-pics

*Work in progress.*

Turn your Chromecast displays into a digital picture frames.

# Setup and configuration

Setup and install dependencies with `./setup.sh`.

Start the program with `./run.sh <images_directory>` where `images_directory`
is a directory containing the images you would like to display. The application
will connect to all the Chromecasts on your network loop randomly through the
100 most recent photos in the given directory. Each photo will be displayed for
a period of 1 minute before switching to the next one.
