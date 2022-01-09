#!/bin/bash
# Making a request to get whatever catch_me got rewrite the domain using Origin
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
