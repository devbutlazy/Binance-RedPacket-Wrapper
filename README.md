# Binance CryptoBox Wrapper
![binance_wrapper](https://github.com/user-attachments/assets/e0615cb7-43e1-457f-8b68-9262a9147920)

### A tool to wrap cryptoboxes from Telegram channels automatically.

## ⚕️ Manual installation:
`1` Download python from [python.org](https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe)  
`2` Install git from [git-scm.com](https://github.com/git-for-windows/git/releases/download/v2.44.0.windows.1/Git-2.44.0-64-bit.exe)  
`3` Clone this repository 
```
git clone https://github.com/devbutlazy/Binance-RedPacket-Wrapper
```
`4` Navigate to project folder: `cd PATH)_TO_PROJECT`  
`5` Install required packages: `pip install -r requirements.txt`
`6` Enter the telegram API_HASH and API_ID to `core/config.py` from [here](https://my.telegram.org/auth)    
`7` Login to your [Binance Account](https://www.binance.com/uk-UA), go to [Binance Crypto Box](https://www.binance.com/uk-UA/my/wallet/account/payment/cryptobox) press F12 and go to `Network`. After that, enter a valid Crypto Box code. When entered, look for "grabV2" POST method in `Network` section. When found, go to POST method `Request Headers` and copy-paste all the neccessery information (cookie, device_info, id, etc...) from there to `core/config.py`.  
`8` Run the program:
```
python main.py
```

# How it works? What are the features?

### [v2.0.0]
    - Rewritten to a new user-bot lib: migration pyrogram => telethon (for better efficiency)
    
    - The token is passed to Binance API within 1-5 seconds (to prevent input automation). 

    - Better configuration in core/config.py

    - The console gives information about found crypto-tokens, amount and valid-state.

    - If there is a timeout, the programm will CORRECTLY pause all the proccesses.

# How to create an EXE file from python code?
`0.` Type in all correct information into `core/config.py`  
`1.` If you want to compile with console, run the `BUILD/with_console.bat`  
`2.` If you want to compile WITHOUGHT console, run `BUILD/without_console.bat`

**NOTE: Cookies, and other configurations should be entered in `core/config.py`, before running pyinstaller!** 


### (c) License: MIT-LICENSE
