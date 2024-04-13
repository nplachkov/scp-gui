
# Secure Copy Protocol (SCP) GUI



## Features

- Simple, easy to use and yet efficient user interface
- Transfer either a file or a whole directory
- Dynamic buttons/fields
    - Example: When you start typing in the "Remote Directory" field, it means that you'll be sending stuff. Then, the other input field dissapears along with the "Receive Files" button to avoid confusion.


## Deployment

Clone the project

```bash
  git clone https://github.com/nplachkov/scp-gui
```

Go to the project directory

```bash
  cd scp-gui
```

Start the script

```bash
  python3 scp-gui.py
```


## Usage/Examples

NOTE: Please make sure to edit the "port" variable on line 7 to your open SSH port. I've purposely left it at a random port (not the default 22) in order to bring attention to default port usage. It is widely considered that running SSH on any other port that the default could lower the likelyhood of people trying to SSH into your device.

```javascript
#Specify your SSH/SCP port
port = "707"
```

### GUI Usage
Upon startup, you will be presented with a simple screen asking you to input your credentials (User and IP) from/to which we'll be sending/receiving files. 

After entering your credentials and continuing, you will see two input fields, a checkbox and three buttons (Receive Files, Send Files, Back).

`Remote File Path:` The full path to the file you wish to receive from that user. E.g. /home/pi/test-folder/log.csv

`Remote Directory` The full path to the directory to which you wish to send files. E.g. /home/pi

`Whole Directory checkbox` In case you wish to either send or receive a whole directory rather than a singular file, you need to check this box and then proceed as usual.

`Receive and Send files buttons` Both buttons work the same way. The simply allow you to select a file from your local machine to send or a directory in which to save the files. Be advised that there is no extra confirmation after selecting the file/directory. Those will be immediately sent/received upon selecting them.