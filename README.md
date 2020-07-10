# Search phrase mentions stats on vk.com
This script will give you last 7 days statistics on a search phrase mentions on www.vk.com website.  
In the `main` you will find where to insert the phrase `search_phrase = "search phrase"`    
if you want to extend days range for example you can do so by changing the value in the `main` function
`days_range = 7` 

## How to install
`Python3` should be already installed. Then use pip (or pip3, if there is a conflict with `Python2`) to install dependencies:   

```
pip install -r requirements.txt
```  
## setting up .env variables   
  You will  have to set your environment variables up, with `.env` file where you going to store
  your `VK_SERVICE_TOKEN` and your `PLOTLY_USERNAME` &
`PLOTLY_API_KEY`  
[About VK Service Token](https://vk.com/dev/access_token?f=3.%20Сервисный%20ключ%20доступа)  
[Create Plotly account](https://chart-studio.plotly.com/settings/api#/)  
[Chart studio documentation](https://plotly.com/python/getting-started-with-chart-studio/)
  


  You can use [Notepad++](https://notepad-plus-plus.org/downloads/) to create `.env` file for Windows,
or [CotEditor](https://coteditor.com/) for MacOS.
  
##### This is an example of how it looks like inside of your .env file. 
(You can choose your own variable names if you want)  
```
VK_SERVICE_TOKEN=Your_ServiceToken
PLOTLY_USERNAME=yourUserName
PLOTLY_API_KEY=Your_ApiKey
```

Variables has to be with CAPITAL letters and without any spaces at all!  

### Project Goals  
To make life easier
