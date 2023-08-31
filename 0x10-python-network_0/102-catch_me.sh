#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that get the message You got me!
curl -sL 0:5000/catch_me -X PUT "You got me!" -H "Origin: X-School-User-Id" -d "user_id=98"
