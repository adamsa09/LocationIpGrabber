# IP Information Grabber
## Adam Sarhan

# Note: I AM NOT RESPONSIBLE FOR YOUR ACTIONS WITH THIS PROGRAM!!!
## Not as loud note: this program requires an internet connection.
#
>## Usage
`git clone https://github.com/adamsa09/LocationIpGrabber.git`  
`cd LocationIpGrabber`  
`python main.py`  

### Edit `config.json` Set `sender_email` to your gmail,   
### set `sender_password` to your gmail password (if you dont feel comfortable look at the source code),  
### set `recv_email` to the email to send the info to (you can use the same email as `sender_email` if you like.),  
### set `subject` to the email subject you would like,  
### set `args` to the arguments corresponding to the info you want:
```
-i   Get IP address  
-h   Get hostname  
-c   Get city  
-r   Get region  
-co  Get country  
-l   Get location (long, lat)  
-o   Organizion  
-p   Postal  
-t   Timezone  
-a   All Info
```

### Then, run `generate.py`.  
#
# Last step
### Now, you would probably want to convert the `generated.py` to a `.exe` so that people wont see your personal email and password, and code the rest of `generated.py` to be an app that anybody would click. (Rock paper scissors game, todolist....) possibilities are obviously endless.
