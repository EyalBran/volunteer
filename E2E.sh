#!/bin/bash

#Register a new user
response=$(curl -s -X POST -d "firstname=John&lastname=Doe&birthdate=1990-01-01&city=New York&username=johndoe&password=pass123" http://localhost:80/register)
if [ "$response" != "Thank you for registering!" ]; then
  echo "Error: Registration failed"
  exit 1
fi

# Log in as the newly registered user
response=$(curl -s -X POST -d "username=johndoe&password=pass123" http://localhost:80/)
if ! echo "$response" | grep -q "Redirecting."; then
  echo "Error: Login failed"
  exit 1
fi

# Register a new event

response=$(curl -s -X POST -d "name=Event1" http://localhost:80/vRegister)
if [ "$response" != "Event1" ]; then
  echo "Error: Event registration failed"
  exit 1
fi

# Check the user's events
response=$(curl -s http://localhost:80/myevents)
if ! echo "$response" | grep -q "שם האירוע"; then
  echo "Error: User's events not found"
  exit 1
fi

echo "All tests passed successfully"