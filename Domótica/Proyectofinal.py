#!/usr/bin/python
# -*- coding: utf-8 -*-
# autor: Jefferson Rivera
# Abril de 2018
# email: riverajefer@gmail.com

import sys
from time import sleep
import signal
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import LED, Button, Servo, AngularServo, Buzzer
from threading import Thread
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


pigpio_factory = PiGPIOFactory()
LED5 = LED (26)
LED4 = LED(19)
LED3 = LED(27)
LED2 = LED (22)
LED = LED(18)
bz = Buzzer(3)
servo = Servo(17, pin_factory=pigpio_factory)

PAHT_CRED = '/home/pi/Demo/cred.json'
URL_DB = 'https://fir-7cc36-default-rtdb.firebaseio.com/'
REF_HOME = 'home'
REF_LUCES = 'luces'
REF_BOTONES = 'botones'
REF_LUZ_SALA = 'luz_sala'
REF_PULSADOR_A = 'pulsador_a'
REF_VENTILADOR = 'ventilador'
REF_PARQUEO = 'parqueo'
REF_BOCINA = 'bocina'
REF_FOCO = 'foco'



class IOT():

    def __init__(self):
        cred = credentials.Certificate(PAHT_CRED)
        firebase_admin.initialize_app(cred, {
            'databaseURL': URL_DB
        })

        self.refHome = db.reference(REF_HOME)
        
        self.estructuraInicialDB() 

        self.refLuces = self.refHome.child(REF_LUCES)
        self.refLuzSala = self.refLuces.child(REF_LUZ_SALA)
        self.refVentilador = self.refLuces.child(REF_VENTILADOR)
        self.refParqueo = self.refLuces.child(REF_PARQUEO)
        self.refFoco = self.refLuces.child(REF_FOCO)
        self.refBocina = self.refLuces.child(REF_BOCINA)

        self.refBotones = self.refHome.child(REF_BOTONES)
        self.refPulsadorA = self.refBotones.child(REF_PULSADOR_A)

    def estructuraInicialDB(self):
        self.refHome.set({
            'luces': {
                'bocina':True,
                'foco':True,
                'luz_sala':True,
                'parqueo':True,
                'ventilador':True
            },
            'botones':{
                'pulsador_a':True,
                
            }
        })
    
    def ledControlGPIO(self, estado):
        if estado:
            LED.on()
            print('Luz de sala encendida')
        else:
            LED.off()
            print('Luz de sala apagada')
    
    
    def ledControlGPIO2(self, estado2):
        if estado2:
            LED2.on()
            print('Ventilador Encendido')
        else:
            LED2.off()
            print('Ventilador Apagado')
            
            
    def ledControlGPIO3(self, estado3):
        if estado3:
            servo.max()
            sleep(1)
            print('Parqueo Abierto')
        else:
            servo.min()
            sleep(1)
            print('Parqueo Cerrado')
            
            
    def ledControlGPIO4(self, estado4):
        if estado4:
            LED4.on()
            print('Luz encendida')
        else:
            LED4.off()
            print('Luz apagada')
            
            
    def ledControlGPIO5(self, estado5):
        if estado5:
            LED5.on()
            print('Bocina encendida')
        else:
            LED5.off()
            print('Bocina apagada')
            
            
            
            
            

    def lucesStart(self):

        E, i = [], 0

        estado_anterior = self.refLuzSala.get()
        self.ledControlGPIO(estado_anterior)

        E.append(estado_anterior)

        while True:
          estado_actual = self.refLuzSala.get()
          E.append(estado_actual)

          if E[i] != E[-1]:
              self.ledControlGPIO(estado_actual)

          del E[0]
          i = i + i
          sleep(0.4)
          
          
          
          
          
    def lucesStart2(self):

        J, a = [], 0

        estado_anterior2 = self.refVentilador.get()
        self.ledControlGPIO2(estado_anterior2)

        J.append(estado_anterior2)

        while True:
          estado_actual2 = self.refVentilador.get()
          J.append(estado_actual2)

          if J[a] != J[-1]:
              self.ledControlGPIO2(estado_actual2)

          del J[0]
          a = a + a
          sleep(0.4)
          
          
          
    def lucesStart3(self):

        R, x = [], 0

        estado_anterior3 = self.refParqueo.get()
        self.ledControlGPIO3(estado_anterior3)

        R.append(estado_anterior3)

        while True:
          estado_actual3 = self.refParqueo.get()
          R.append(estado_actual3)

          if R[x] != R[-1]:
              self.ledControlGPIO3(estado_actual3)

          del R[0]
          x = x + x
          sleep(0.4)
          
          
    def lucesStart4(self):

        M, d = [], 0

        estado_anterior4 = self.refFoco.get()
        self.ledControlGPIO4(estado_anterior4)

        M.append(estado_anterior4)

        while True:
          estado_actual4 = self.refFoco.get()
          M.append(estado_actual4)

          if M[d] != M[-1]:
              self.ledControlGPIO4(estado_actual4)

          del M[0]
          d = d + d
          sleep(0.4)
          
          
    def lucesStart5(self):

        B, l = [], 0

        estado_anterior5 = self.refBocina.get()
        self.ledControlGPIO5(estado_anterior5)

        B.append(estado_anterior5)

        while True:
          estado_actual5 = self.refBocina.get()
          B.append(estado_actual5)

          if B[l] != B[-1]:
              self.ledControlGPIO5(estado_actual5)

          del B[0]
          l = l + l
          sleep(0.4)
          
          
          

    def pulsador_on(self):
        print('Pulsador On')
        self.refPulsadorA.set(True)




print ('CASA DE JONATHAN INICIADA')
iot = IOT()

subproceso_led = Thread(target=iot.lucesStart)
subproceso_led.daemon = True
subproceso_led.start()

subproceso_led2 = Thread(target=iot.lucesStart2)
subproceso_led2.daemon = True
subproceso_led2.start()

subproceso_led3 = Thread(target=iot.lucesStart3)
subproceso_led3.daemon = True
subproceso_led3.start()

subproceso_led4 = Thread(target=iot.lucesStart4)
subproceso_led4.daemon = True
subproceso_led4.start()

subproceso_led5 = Thread(target=iot.lucesStart5)
subproceso_led5.daemon = True
subproceso_led5.start()


signal.pause() 