# -*- coding: utf-8 -*-
import datetime
import Xlib.display
from pyvirtualdisplay import Display
import pyautogui
import os
from PQTs.MongoDB.MongoDB import MongoDB
from PQTs.Selenium.Base import BaseConexion
from PQTs.Paths import pathImg
import time
import random
from PQTs.Selenium.Acciones.AccionesReproducir import Acciones

def main():


    #--> Descomentar para ver en PC
    #display = Display(visible=True, size=(1200,768))

    display = Display(visible=True, size=(1900,1268), backend="xvfb", use_xauth=True)

    display.start()

    #--> Descomentar para ver en PC
    #pyautogui._pyautogui_x11._display = Xlib.display.Display(":0")

    pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])
    time.sleep (random.randint(1,4))
    hilos=1
    time.sleep (random.randint(1,5))
    start= time.time()

    db=MongoDB(hilos)
    db.iniciarDB()
    email=[]
    id=[]
    passw=[]

    result= db.findby2("accountmanager","acc_estado",5,"pais","US")

    for elem in result:
        email= (elem["email"])
        id=(elem["_id"])
        passw =(elem["pass"])
        db.updateOne("accountmanager",id,"acc_estado",7)
        db.updateOne("accountmanager",id,"datelogin",time.time())  
        #for elemid in id:
        #    db.updateOne("accountmanager",elemid,"creacionlistasentrenamiento",2)
        db.cerrarConexion()
    

    print (email, id,db,passw)

    def iniciarSpotify(email,password):
        
        driver = BaseConexion().conexionChrome()
        #driver = BaseConexion().conexionChromeHeadless()

        acciones = Acciones(driver)
        try:
            ingresando=acciones.ingresarSpotify()
        except:
            ingresando=acciones.ingresarSpotify()

        while ingresando==False:
            try:
                ingresando=acciones.ingresarSpotify()
            except:
                ingresando=acciones.ingresarSpotify()

        
        returnLoginSpotify= acciones.loginSpotify(email,password)
        while returnLoginSpotify== False:
            returnLoginSpotify= acciones.loginSpotify(email,password)
    
        pyautogui.screenshot(os.path.join(pathImg,f"01-{email}-loging.png"))
    
        if returnLoginSpotify == True:
            print(f"Hilo {email} - SinginSpotify {returnLoginSpotify}")

        acciones.sleep(10)    
        acciones.refreshweb()

        acciones.sleep(10)
        
        acciones.abrirlistareproduccion()
        pyautogui.screenshot(os.path.join(pathImg,f"01-{email}-nombbrelistacreada.png"))
        acciones.reproducir()
        pyautogui.screenshot(os.path.join(pathImg,f"01-{email}-finreproduccion.png"))
        return True

    result=iniciarSpotify (email,passw)
    



     
    display.stop()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        with open(os.path.join(pathImg,f"logerror.txt"), 'w') as f:
            f.write(str(e))



