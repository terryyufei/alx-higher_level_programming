#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that get the message You got me!
curl -s -o /dev/null -w "You got me!" 0.0.0.0:5000/catch_me
