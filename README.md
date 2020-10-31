# Home Downloader Telegram Bot
Telegram Bot based on youtube-dl devised to download media contents from the web.  
[The whole story behind this project](https://alerom90.medium.com/how-i-made-my-girlfriend-happy-with-a-simple-telegram-bot-2be8e4b150e7?source=friends_link&sk=742b5296b19b0eae0e7f8827dbc747f4).

## Requirements 
- `virtualenv` or `conda`
- `python3.8`
- `git`
- `samba`
- [Telegram Bot Token](https://core.telegram.org/bots)
## Installation  
Install `youtube-dl` (on Arch/Arch Arm):
```shell script
sudo pacman -S youtube-dl
```
Clone the project:
```shell script
git clone https://github.com/pigna90/home-downloader-bot.git
```
Set up the virtual environment:
```shell script
cd ./home-downloader-bot
python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```
### Run the Bot
Crete a configuration json file:
```shell script
cd ./home-downloader-bot
touch config.json
```
Populate it by following this structure:
```json
{
  "valid_users": [
    "username_1",
    "username_2"
  ],
  "bot_token": "secret_bot_token",
  "out_dir": "/path/to/sambda/shared/directory/",
  "owner_chat_id": "owner_chat_id",
  "valid_websites": ["https://www.youtube"]
}
```
Run the Bot:
```shell script
cd ./home-downloader-bot
chmod +x run_home_downloader.sh
./run_home_downloader.sh
```
## Usage  
- Start a new conversation with the Bot
- Send the link of the video to download
- The video will be downloaded into the shared folder
## Development
### Deploy to a remote machine
Here is how to deploy the code to a remote machine (e.g. Raspberry Pi) trough SSH:
```shell script
rpi_host=""
rpi_project_dir=""

cd ./home-downloader-bot

scp home_downloader.py ${rpi_host}:${rpi_project_dir}home_downloader.py
scp modules.py ${rpi_host}:${rpi_project_dir}modules.py
scp requirements.txt ${rpi_host}:${rpi_project_dir}requirements.txt
scp config.json ${rpi_host}:${rpi_project_dir}config.json
scp run_rpi.sh ${rpi_host}:${rpi_project_dir}run_home_downloader.sh

ssh ${rpi_host} chmod +x ${rpi_project_dir}run_home_downloader.sh
```

