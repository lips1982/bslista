# -*- coding: utf-8 -*-
import Xlib.display
from pyvirtualdisplay import Display
import pyautogui
import os
from PQTs.MongoDB.MongoDB import MongoDB
from PQTs.Selenium.Base import BaseConexion
from PQTs.Paths import pathImg
import time
import random
from PQTs.Selenium.Acciones.Accioneslagregarlistanueva import Acciones
from PQTs.Selenium.Acciones.enviaremail import enviaremailerror

def main():


    display = Display(visible=True, size=(1900,1268), backend="xvfb", use_xauth=True)

    display.start()


    pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])
    
    
    hilos=1
    db=MongoDB(hilos)
    db.iniciarDB()
    email=[]
    id=[]
    passw=[]

    result= db.findby1("accountmanager","acc_estado",1)
    print (result)
    for elem in result:
        email= (elem["email"])
        id=(elem["_id"])
        passw =(elem["pass"])
        db.updateOne("accountmanager",id,"acc_estado",2)
        db.updateOne("accountmanager",id,"datelogin",time.time())  
        #for elemid in id:
        #    db.updateOne("accountmanager",elemid,"creacionlistasentrenamiento",2)
        db.cerrarConexion()

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
        i=0
        while i <=3:
            if returnLoginSpotify== False:
                returnLoginSpotify= acciones.loginSpotify(email,password)
                i+=1
            else:
                i=4
        time.sleep(10)    
        ckecloging= acciones.checklogingok()
        if ckecloging == True:
            db.iniciarDB()
            db.updateOne("accountmanager",id,"ckeclog","logfail")
            db.updateOne("accountmanager",id,"acc_estado",0)
            db.cerrarConexion()
            exit()

        if ckecloging == False:
            #print(f"Hilo {email} - SinginSpotify {returnLoginSpotify}")
            #pyautogui.screenshot(os.path.join(pathImg,f"01-{email}-loging.png"))
            #loging= f"01-{email}-loging.png"
            #enviaremailerror(email,loging, password)  
            db.iniciarDB()
            db.updateOne("accountmanager",id,"ckeclog","logingok")
            db.cerrarConexion()
        acciones.sleep(4)
        acciones.refreshweb()
        acciones.sleep(10)
        acciones.borrarlista()
        acciones.sleep(10)
        acciones.nuevalistanombre()
        acciones.sleep(5)
        #pyautogui.screenshot(os.path.join(pathImg,f"01-{email}-nombbrelistacreada.png"))
        acciones.buscaryagregarartista()
        acciones.sleep(3)

        chequear=acciones.abrirlistareproduccion()
        
        while chequear==False:
            acciones.borrarlista()
            chequear=acciones.abrirlistareproduccion()

        acciones.sleep(20)
        pyautogui.screenshot(os.path.join(pathImg,f"{email}.png"))
        
        acciones.sleep(20)
        acciones.enviardatos(email)
        db.iniciarDB()
        db.updateOne("accountmanager",id,"acc_estado",5)
        urllistaReproduccion=acciones.getUrlLista()
        db.updateOne("accountmanager",id,"urllista",urllistaReproduccion)
        db.cerrarConexion()
        return True        
    try:
        iniciarSpotify (email,passw)

    except Exception as e:
        with open(os.path.join(pathImg,f"error.txt"), 'w') as f:
            f.write(str(e))  
        pyautogui.screenshot(os.path.join(pathImg,f"error.png"))      
        db.iniciarDB()
        db.updateOne("accountmanager",id,"acc_estado",3)
        db.cerrarConexion()
        adjunto= "error.png"
        enviaremailerror(email,adjunto,passw,e)
    
    display.stop()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print (e)
        with open(os.path.join(pathImg,f"error.txt"), 'w') as f:
            f.write(str(e))  
