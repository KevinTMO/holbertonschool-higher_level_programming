#!/bin/bash
# Making a request to get whatever catch_me got rewrite the domain using Origin
curl -sL -X PUT -d "You got me!" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
