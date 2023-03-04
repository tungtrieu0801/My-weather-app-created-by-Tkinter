from tkinter import *
from PIL import ImageTk,Image
import json
import requests
window=Tk()
window.title('My weather app created by Tkinter')
window.iconbitmap('C:/Users/nguye/Videos/test/img/myicon (1).ico')
window.geometry("500x100")
def ziplookup():
    try:
        api_requests=requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + zip.get()+ '&distance=25&API_KEY=7E67E495-5F61-44F0-BC41-4FCCFA993B8B')
        api=json.loads(api_requests.content)
        city=api[0]['ReportingArea']
        quality=api[0]['AQI']
        category=api[0]['Category']['Name']
        if category=='Good':
            weather_color= '#0c0'
        elif category=='Moderate':
            weather_color='#FFFF00'
        elif category=='Unhealthy for Sensitive Groups':
            weather_color='#ff9990'
        elif category=='Unhealthy':
            weather_color='FF0000'
        elif category=='Very Unhealthy':
            weather_color='#99066'
        elif category=='Hazardous':
            weather_color='#660000' 
        window.configure(background=weather_color)
        my_lbl=Label(window, text=city + ' Air quality ' + str(quality)+ ' is ' +category,font=("Helvetica, 20"),background=weather_color)
        my_lbl.grid(row=1,column=0,columnspan=2)
    except Exception as e:
        api = 'ERROR...'
        my_lbl=Label(window, text=api, background='#CCCCFF')
        my_lbl.grid(row=1,column=0,columnspan=2)
    window.configure(background='#99FF66')
zip=Entry(window)
zip.grid(row=0, column=0, sticky=W+E+N+S)

zipButton=Button(window, text='Type zipcode here', command=ziplookup)
zipButton.grid(row=0,column=1,sticky=W+E+N+S)
window.mainloop()
#bonus a web U.S. Zip Code
