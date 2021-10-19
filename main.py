from kivy.app import App
""""
#Desenvolvido por: Witaley da Silva Souza
#31 07 2019

"""
#pip install kivy-u4-qpython
# pip install xlwt
# pip install config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
#import smtplib
from datetime import date
from datetime import datetime
import socket
import time
unm='wss.automaticsoftwareaguanabicavvalvsslipshsplash'
pwd='dvdcot'

kmchegada=str()
kmsaida=str()
litroi=str()
litrof=str()

m=str()
p=str()
kg=str()
media=str()
full=str()
reiniciar=  000
usuario= 123

#esp da base movel
PORT= 121
svr="192.168.43.224"

#esp resoldado
svr2="192.168.43.11"
PORT2= 122

#novo esp 
svr3="192.168.43.120"
PORT3= 123



wf2=0
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s2= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s3= socket.socket(socket.AF_INET, socket.SOCK_STREAM)



try:
    #s.connect((svr, PORT))
    digite='w'
    #s.send(bytes(digite, "utf-8")) 
    wf=1
    #time.sleep(2)
    #s.close()
except:
    wf=0
    print('erro')

usuario=000
#cria arquivo so para coexistir diretorio
if usuario==123:

    dados= open('DadosPlanilhaapp.txt','a')                                                  
    dados.write('')
    dados.close()

#Abrir o arquivo para ver texto
    dados= open('DadosPlanilhaapp.txt')
    #criar uma variavel que vai receber os dados

    info= dados.readlines()
    infostr= str(info)
    fix=infostr
    print(infostr)
    


hoje1=date.today()
hoje=str(hoje1)

def enviaemail(tip, oque):
    try:
        #server=smtplib.SMTP('smtp.gmail.com:587')
        #server.ehlo()
        #server.starttls()
        #server.login(unm, pwd)
        #message= 'Subject: {}\n\n{}'.format(tip,oque)
        #server.sendmail(unm, unm, message)
       # server.quit()
        print('sucess')
       # os.remove('DadosPlanilhaapp.txt')
    except:
        print('Salvo em banco de dados')
        #dados= open('DadosPlanilhaapp.txt','a')
        #dados.write(full)
        #dados.close()
             
#inicio
ou="oiie"
#time.sleep(3)

Builder.load_string("""
<ScreenOne>:
    BoxLayout:
        orientation: 'vertical' 
        Label:
            markup: True
            id: my_label
            text: '[i][b]...PAINEL DE CONTROLE...[/b][/i]'
            font_size: 60
            color: 0, 0, 1, 1
        Button:
            text: ">>>LIGAR LAMPADA<<<"
            font_size: 50
            color: 0, 1, 0, 1
            background_color: 0, 1, 1, 1
            on_press:
                root.btn1()
                
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_one"

        Button:
            text: "<<<DESLIGAR LAMPADA>>>"
            font_size: 40
            color: 0, 1, 1, 1
            background_color: 0, 1, 1, 1
            on_press:
                root.btn2()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_one"
        Button:
            text: "LIGAR TOMADA (:)"
            font_size: 50
            color: 1, 0, 0, 1
            background_color: 0, 1, 1, 1
            on_press:
                root.btn3()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_one"

        Button:
            text: "DESLIGAR TOMADA (:)"
            font_size: 40
            color: 0, 1, 1, 1
            background_color: 0, 1, 1, 1
            on_press:
                root.btn4()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_one"

        Button:
            text: "PREFERENCIAL = >>> LUZ <<<"
            font_size: 50
            color: 0, 1, 0, 1
            background_color: 0, 1, 1, 1
            on_press:
                root.btn5()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_one"

        Button:
            text: "PREFERENCIAL = TOMADA (:)"
            font_size: 40
            color: 1, 0, 0, 1
            background_color: 0, 1, 1, 1
            on_press:
                root.btn6()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_one"

        Button:
            text: "ASSUSTA INVASOR"
            font_size: 50
            color: 1, 1, 1, 1
            background_color: 0, 1, 1, 1
            on_press:
                root.btn7()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_one"

        Button:
            text: "CASA SEGURA"
            font_size: 50
            color: 1, 0, 1, 1
            background_color: 0, 1, 1, 1
            on_press:
                root.btn8()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_one"

        Button:
            markup: True
            text: "[i][b]<<<[/b][/i]"
            font_size: 80
            color: 1, 0, 0, 1
            background_color: 0, 1, 1, 1
            on_press:
                root.btn9()
            on_release:
                
                root.manager.transition.direction= "right"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_two"

<ScreenTwo>:
    BoxLayout:        
        orientation: 'vertical' 
        Label:
            markup: True
            id: my_label
            text: '[i][b]__SELECIONE O COMODO DA CASA__[/b][/i]'
            font_size: 40
            color: 0, 1, 0, 1
            
        
        Button:
            text: "COZINHA"
            font_size: 60
            color: 1, 0, 0, 1
            background_color: 0, 1, 1, 1

            on_press:
                root.btn1()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_one"

        Button:
            text: "QUARTO"
            font_size: 50
            color: 1, 1, 1, 1
            background_color: 0, 1, 1, 1
            on_press:
                root.btn2()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_one"

        Button:
            text: "SALA"
            font_size: 60
            color: 1, 0, 0, 1
            background_color: 0, 1, 1, 1
            on_press:
                root.btn3()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_one"

        Button:
            text: "TODOS"
            font_size: 50
            color: 1, 1, 1, 1
            background_color: 0, 1, 1, 1

            on_press:
                root.btn4()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_one"

               
        Button:
            markup: True
            text: "[i][b]Config...[/b][/i]"
            font_size: 80
            color: 0, 0, 0, 1
            background_color: 0, 1, 1, 1
            on_release:
                
                root.manager.transition.direction= "down"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_config"

<ScreenConfig>:
    BoxLayout:        
        orientation: 'vertical' 
        Label:
            background_color: 0, 1, 1, 1
            markup: True
            id: my_label
            text: '[i][b]Alterar Cores de Layout[/b][/i]'
            font_size: 65
            color: 1, 0, 0, 1
            
        
        Button:
            text: "Layout Colorido"
            font_size: 50
            color: 1, 0, 0, 1
            background_color: 0, 1, 1, 1

            on_press:
                root.btn1()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_two"

        Button:
            markup: True
            text: "[i]Layout Monocromatico[/i]"
            font_size: 50
            color: 1, 1, 1, 1
            
            on_press:
                root.btn2()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twoneutra"

        Button:
            markup: True
            text: "[i]Layout Rosa[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 1, 0, 1, 1
            
            on_press:
                root.btn5()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_tworosa"
 
        
        Button:
            markup: True
            text: "[i]Layout Soft[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 1, 1
            
            on_press:
                root.btn3()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twosoft"
        
        
        Button:
            markup: True
            text: "[i]Layout Verde[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 0, 1
            
            on_press:
                root.btn4()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twoverdetropical"

      
        Button:
            markup: True
            text: "[i][b]<<<[/b][/i]"
            font_size: 80
            color: 1, 0, 0, 1
            background_color: 0, 1, 1, 1
            on_release:
                
                root.manager.transition.direction= "up"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_two"


<ScreenOneNeutra>:
    BoxLayout:
        orientation: 'vertical' 
        Label:
            markup: True
            id: my_label
            text: '[i][b]...PAINEL DE CONTROLE...[/b][/i]'
            font_size: 60
            
        Button:
            markup: True
            text: "[i]LIGAR LAMPADA[/i]"
            font_size: 50
            
            on_press:
                root.btn1()
                
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneneutra"

        Button:
            markup: True
            text: "[i]DESLIGAR LAMPADA[/i]"
            font_size: 50
            
            on_press:
                root.btn2()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneneutra"
        Button:
            markup: True
            text: "[i]LIGAR TOMADA[/i]"
            font_size: 50
            
            on_press:
                root.btn3()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneneutra"

        Button:
            markup: True
            text: "[i]DESLIGAR TOMADA[/i]"
            font_size: 50
            
            on_press:
                root.btn4()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneneutra"

        Button:
            markup: True
            text: "[i]PREFERENCIAL [b]LAMPADA[/b][/i]"
            font_size: 50
                       
            on_press:
                root.btn5()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneneutra"

        Button:
            markup: True
            text: "[i]PREFERENCIAL [b]TOMADA[/b][/i]"
            font_size: 50
                
            on_press:
                root.btn6()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneneutra"

        Button:
            markup: True
            text: "[i]ASSUSTA INVASOR[/i]"
            font_size: 50
            
            on_press:
                root.btn7()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneneutra"

        Button:
            markup: True
            text: "[i]CASA SEGURA[/i]"
            font_size: 50
                       
            on_press:
                root.btn8()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneneutra"

        Button:
            markup: True
            text: "[i][b]<<<[/b][/i]"
            font_size: 80
            color: 0, 0, 0,1           
            on_press:
                root.btn9()
            on_release:
                
                root.manager.transition.direction= "right"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twoneutra"





<ScreenTwoNeutra>:
    BoxLayout:        
        orientation: 'vertical' 
        Label:
            markup: True
            id: my_label
            text: '[i][b]__SELECIONE O COMODO DA CASA__[/b][/i]'
            font_size: 40
            
            
        
        Button:
            markup: True
            text: "[i]COZINHA[/i]"
            font_size: 60
           
            on_press:
                root.btn1()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneneutra"

        Button:
            markup: True
            text: "[i]QUARTO[/i]"
            font_size: 60
                      
            on_press:
                root.btn2()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneneutra"

        Button:
            markup: True
            text: "[i]SALA[/i]"
            font_size: 60
                        
            on_press:
                root.btn3()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneneutra"

        Button:
            markup: True
            text: "[i]TODOS[/i]"
            font_size: 60
     
            on_press:
                root.btn4()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneneutra"

               
        Button:
            markup: True
            text: "[i][b]Config...[/b][/i]"
            font_size: 80
            color: 0, 0, 0, 1
          
            on_release:
                
                root.manager.transition.direction= "down"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_configneutra"



<ScreenConfigNeutra>:
    BoxLayout:        
        orientation: 'vertical' 
        Label:
            markup: True
            id: my_label
            text: '[i][b]Alterar Cores de Layout[/b][/i]'
            font_size: 65
            color: 1, 1, 1, 1
            
        
        Button:
            text: "Layout Colorido"
            font_size: 50
            color: 1, 0, 0, 1
            background_color: 0, 1, 1, 1

            on_press:
                root.btn1()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_two"

        Button:
            markup: True
            text: "[i]Layout Monocromatico[/i]"
            font_size: 50
            color: 1, 1, 1, 1
            
            on_press:
                root.btn2()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twoneutra"

        Button:
            markup: True
            text: "[i]Layout Rosa[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 1, 0, 1, 1
            
            on_press:
                root.btn5()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_tworosa"
 
        
        Button:
            markup: True
            text: "[i]Layout Soft[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 1, 1
            
            on_press:
                root.btn3()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twosoft"
        
        
        Button:
            markup: True
            text: "[i]Layout Verde[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 0, 1
            
            on_press:
                root.btn4()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twoverdetropical"
        
       
         
        Button:
            markup: True
            text: "[i][b]<<<[/b][/i]"
            font_size: 80
            color: 1, 1, 1, 1
            
            on_release:
                
                root.manager.transition.direction= "up"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twoneutra"

<ScreenOneRosa>:
    BoxLayout:
        orientation: 'vertical' 
        Label:
            markup: True
            id: my_label
            text: '[i][b]...PAINEL DE CONTROLE...[/b][/i]'
            font_size: 60
            color: 1, 0, 1, 1
            
        Button:
            markup: True
            text: "[i]Ligar Lampada[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 1, 0, 1, 1
            on_press:
                root.btn1()
                
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onerosa"

        Button:
            markup: True
            text: "[i]Desligar Lampada[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 1, 0, 1, 1
            on_press:
                root.btn2()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onerosa"
        Button:
            markup: True
            text: "[i]Ligar Tomada[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 1, 0, 1, 1
            on_press:
                root.btn3()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onerosa"

        Button:
            markup: True
            text: "[i]Desligar Tomada[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 1, 0, 1, 1
            on_press:
                root.btn4()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onerosa"

        Button:
            markup: True
            text: "[i]Preferencial [b]LAMPADA[/b][/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 1, 0, 1, 1
            on_press:
                root.btn5()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onerosa"

        Button:
            markup: True
            text: "[i]Preferencial [b]TOMADA[/b][/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 1, 0, 1, 1
            on_press:
                root.btn6()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onerosa"

        Button:
            markup: True
            text: "[i]Assusta Invasor[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 1, 0, 1, 1
            on_press:
                root.btn7()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onerosa"

        Button:
            markup: True
            text: "[i]Casa Segura[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 1, 0, 1, 1
            on_press:
                root.btn8()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onerosa"

        Button:
            markup: True
            text: "[i][b]<<<[/b][/i]"
            background_color: 0, 0, 0, 1
            font_size: 80
            color: 1, 0, 1, 1           
            on_press:
                root.btn9()
            on_release:
                
                root.manager.transition.direction= "right"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_tworosa"





<ScreenTwoRosa>:
    BoxLayout:        
        orientation: 'vertical' 
        Label:
            markup: True
            id: my_label
            text: '[i][b]__SELECIONE O COMODO DA CASA__[/b][/i]'
            background_color: 0, 0, 0, 1
            font_size: 40
            color: 1, 0, 1, 1
            
        
        Button:
            markup: True
            text: "[i]Cozinha[/i]"
            background_color: 0, 0, 0, 1
            font_size: 60
            color: 1, 0, 1, 1
            on_press:
                root.btn1()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onerosa"

        Button:
            markup: True
            text: "[i]Quarto[/i]"
            background_color: 0, 0, 0, 1
            font_size: 60
            color: 1, 0, 1, 1
            on_press:
                root.btn2()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onerosa"

        Button:
            markup: True
            text: "[i]Sala[/i]"
            background_color: 0, 0, 0, 1
            font_size: 60
            color: 1, 0, 1, 1
            on_press:
                root.btn3()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onerosa"

        Button:
            markup: True
            text: "[i]Todos[/i]"
            background_color: 0, 0, 0, 1
            font_size: 60
            color: 1, 0, 1, 1
            on_press:
                root.btn4()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onerosa"

               
        Button:
            markup: True
            text: "[i][b]Config...[/b][/i]"
            background_color: 0, 0, 0, 1
            font_size: 80
            color: 1, 0, 1, 1
          
            on_release:
                
                root.manager.transition.direction= "down"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_configrosa"



<ScreenConfigRosa>:
    BoxLayout:        
        orientation: 'vertical' 
        Label:
            markup: True
            id: my_label
            text: '[i][b]Alterar Cores de Layout[/b][/i]'
            font_size: 65
            color: 1, 0, 1, 1
            
        
        Button:           
            text: "Layout Colorido"
            font_size: 50
            color: 1, 0, 0, 1
            background_color: 0, 1, 1, 1

            on_press:
                root.btn1()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_two"

        Button:
            markup: True
            text: "[i]Layout Monocromatico[/i]"
            font_size: 50
            color: 1, 1, 1, 1
            
            on_press:
                root.btn2()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twoneutra"
        
        Button:
            markup: True
            text: "[i]Layout Rosa[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 1, 0, 1, 1
            
            on_press:
                root.btn5()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_tworosa"
 
        
        Button:
            markup: True
            text: "[i]Layout Soft[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 1, 1
            
            on_press:
                root.btn3()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twosoft"
       
         
        Button:
            markup: True
            text: "[i]Layout Verde[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 0, 1
            
            on_press:
                root.btn4()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twoverdetropical"

        
               
        Button:
            markup: True
            text: "[i][b]<<<[/b][/i]"
            background_color: 0, 0, 0, 1
            font_size: 80
            color: 1, 0, 1, 1
            
            on_release:
                
                root.manager.transition.direction= "up"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_tworosa"



<ScreenOneSoft>:
    BoxLayout:
        orientation: 'vertical' 
        Label:
            markup: True
            id: my_label
            text: '[i][b]...PAINEL DE CONTROLE...[/b][/i]'
            font_size: 60
            color: 0, 1, 1, 1
            
        Button:
            markup: True
            text: "[i]Ligar Lampada[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 1, 1
            on_press:
                root.btn1()
                
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onesoft"

        Button:
            markup: True
            text: "[i]Desligar Lampada[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 1, 1
            on_press:
                root.btn2()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onesoft"
        Button:
            markup: True
            text: "[i]Ligar Tomada[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 1, 1
            on_press:
                root.btn3()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onesoft"

        Button:
            markup: True
            text: "[i]Desligar Tomada[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 1, 1
            on_press:
                root.btn4()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onesoft"

        Button:
            markup: True
            text: "[i]Preferencial [b]LAMPADA[/b][/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 1, 1
            on_press:
                root.btn5()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onesoft"

        Button:
            markup: True
            text: "[i]Preferencial [b]TOMADA[/b][/i]"
            background_color: 0, 0, 0, 1 
            font_size: 50
            color: 0, 1, 1, 1
            on_press:
                root.btn6()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onesoft"

        Button:
            markup: True
            text: "[i]Assusta Invasor[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 1, 1
            on_press:
                root.btn7()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onesoft"

        Button:
            markup: True
            text: "[i]Casa Segura[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 1, 1
            on_press:
                root.btn8()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onesoft"

        Button:
            markup: True
            text: "[i][b]<<<[/b][/i]"
            background_color: 0, 0, 0, 1
            font_size: 80
            color: 0, 1, 1, 1           
            on_press:
                root.btn9()
            on_release:
                
                root.manager.transition.direction= "right"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twosoft"





<ScreenTwoSoft>:
    BoxLayout:        
        orientation: 'vertical' 
        Label:
            markup: True
            id: my_label
            text: '[i][b]__SELECIONE O COMODO DA CASA__[/b][/i]'
            background_color: 0, 0, 0, 1
            font_size: 40
            color: 0, 1, 1, 1
            
        
        Button:
            markup: True
            text: "[i]Cozinha[/i]"
            background_color: 0, 0, 0, 1
            font_size: 60
            color: 0, 1, 1, 1
            on_press:
                root.btn1()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onesoft"

        Button:
            markup: True
            text: "[i]Quarto[/i]"
            background_color: 0, 0, 0, 1
            font_size: 60
            color: 0, 1, 1, 1
            on_press:
                root.btn2()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onesoft"

        Button:
            markup: True
            text: "[i]Sala[/i]"
            background_color: 0, 0, 0, 1
            font_size: 60
            color: 0, 1, 1, 1
            on_press:
                root.btn3()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onesoft"

        Button:
            markup: True
            text: "[i]Todos[/i]"
            background_color: 0, 0, 0, 1
            font_size: 60
            color: 0, 1, 1, 1
            on_press:
                root.btn4()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_onesoft"

               
        Button:
            markup: True
            text: "[i][b]Config...[/b][/i]"
            background_color: 0, 0, 0, 1
            font_size: 80
            color: 0, 1, 1, 1
          
            on_release:
                
                root.manager.transition.direction= "down"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_configsoft"



<ScreenConfigSoft>:
    BoxLayout:        
        orientation: 'vertical' 
        Label:
            markup: True
            id: my_label
            text: '[i][b]Alterar Cores de Layout[/b][/i]'
            font_size: 65
            color: 0, 1, 1, 1
            
        
        Button:           
            text: "Layout Colorido"
            font_size: 50
            color: 1, 0, 0, 1
            background_color: 0, 1, 1, 1

            on_press:
                root.btn1()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_two"

        Button:
            markup: True
            text: "[i]Layout Monocromatico[/i]"
            font_size: 50
            color: 1, 1, 1, 1
            
            on_press:
                root.btn2()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twoneutra"
        
        Button:
            markup: True
            text: "[i]Layout Rosa[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 1, 0, 1, 1
            
            on_press:
                root.btn5()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_tworosa"
 
        
        Button:
            markup: True
            text: "[i]Layout Soft[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 1, 1
            
            on_press:
                root.btn3()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twosoft"
       
         
        Button:
            markup: True
            text: "[i]Layout Verde[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 0, 1
            
            on_press:
                root.btn4()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twoverdetropical"

        
               
        Button:
            markup: True
            text: "[i][b]<<<[/b][/i]"
            background_color: 0, 0, 0, 1
            font_size: 80
            color: 0, 1, 1, 1
            
            on_release:
                
                root.manager.transition.direction= "up"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twosoft"


<ScreenOneVerde>:
    BoxLayout:
        orientation: 'vertical' 
        Label:
            markup: True
            id: my_label
            text: '[i][b]...PAINEL DE CONTROLE...[/b][/i]'
            font_size: 60
            color: 0, 1, 0, 1
            
        
        Button:
            markup: True
            text: "[i]Ligar Lampada[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 0, 1
            on_press:
                root.btn1()
                
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneverdetropical"

        Button:
            markup: True
            text: "[i]Desligar Lampada[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 0, 1
            on_press:
                root.btn2()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneverdetropical"
        Button:
            markup: True
            text: "[i]Ligar Tomada[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 0, 1
            on_press:
                root.btn3()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneverdetropical"

        Button:
            markup: True
            text: "[i]Desligar Tomada[/i]"
            background_color: 0, 0, 0, 1 
            font_size: 50
            color: 0, 1, 0, 1
            on_press:
                root.btn4()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneverdetropical"

        Button:
            markup: True
            text: "[i]Preferencial [b]LAMPADA[/b][/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 0, 1
            on_press:
                root.btn5()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneverdetropical"

        Button:
            markup: True
            text: "[i]Preferencial [b]TOMADA[/b][/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 0, 1
            on_press:
                root.btn6()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneverdetropical"

        Button:
            markup: True
            text: "[i]Assusta Invasor[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 0, 1
            on_press:
                root.btn7()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneverdetropical"

        Button:
            markup: True
            text: "[i]Casa Segura[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 0, 1
            on_press:
                root.btn8()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneverdetropical"

        Button:
            markup: True
            text: "[i][b]<<<[/b][/i]"
            background_color: 0, 0, 0, 1
            font_size: 80
            color: 0, 1, 0, 1           
            on_press:
                root.btn9()
            on_release:
                
                root.manager.transition.direction= "right"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twoverdetropical"





<ScreenTwoVerde>:
    BoxLayout:        
        orientation: 'vertical' 
        Label:
            markup: True
            id: my_label
            text: '[i][b]__SELECIONE O COMODO DA CASA__[/b][/i]'
            font_size: 40
            color: 0, 1, 0, 1
            
        
        Button:
            markup: True
            text: "[i]Cozinha[/i]"
            background_color: 0, 0, 0, 1 
            font_size: 60
            color: 0, 1, 0, 1
            on_press:
                root.btn1()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneverdetropical"

        Button:
            markup: True
            text: "[i]Quarto[/i]"
            background_color: 0, 0, 0, 1
            font_size: 60
            color: 0, 1, 0, 1
            on_press:
                root.btn2()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneverdetropical"

        Button:
            markup: True
            text: "[i]Sala[/i]"
            background_color: 0, 0, 0, 1
            font_size: 60
            color: 0, 1, 0, 1
            on_press:
                root.btn3()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneverdetropical"

        Button:
            markup: True
            text: "[i]Todos[/i]"
            background_color: 0, 0, 0, 1
            font_size: 60
            color: 0, 1, 0, 1
            on_press:
                root.btn4()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_oneverdetropical"

               
        Button:
            markup: True
            text: "[i][b]Config...[/b][/i]"
            background_color: 0, 0, 0, 1
            font_size: 80
            color: 0, 1, 0, 1
          
            on_release:
                
                root.manager.transition.direction= "down"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_configverdetropical"



<ScreenConfigVerde>:
    BoxLayout:        
        orientation: 'vertical' 
        Label:
            markup: True
            id: my_label
            text: '[i][b]Alterar Cores de Layout[/b][/i]'
            font_size: 65
            color: 0, 1, 0, 1
            
        
        Button:           
            text: "Layout Colorido"
            font_size: 50
            color: 1, 0, 0, 1
            background_color: 0, 1, 1, 1

            on_press:
                root.btn1()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_two"

        Button:
            markup: True
            text: "[i]Layout Monocromatico[/i]"
            font_size: 50
            color: 1, 1, 1, 1
            
            on_press:
                root.btn2()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twoneutra"
        
        Button:
            markup: True
            text: "[i]Layout Rosa[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 1, 0, 1, 1
            
            on_press:
                root.btn5()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_tworosa"
 
        
        Button:
            markup: True
            text: "[i]Layout Soft[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 1, 1
            
            on_press:
                root.btn3()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twosoft"
        
        
        Button:
            markup: True
            text: "[i]Layout Verde[/i]"
            background_color: 0, 0, 0, 1
            font_size: 50
            color: 0, 1, 0, 1
            
            on_press:
                root.btn4()
            on_release:
                
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twoverdetropical"

              
               
        Button:
            markup: True
            text: "[i][b]<<<[/b][/i]"
            background_color: 0, 0, 0, 1
            font_size: 80
            color: 0, 1, 0, 1
            
            on_release:
                
                root.manager.transition.direction= "up"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_twoverdetropical"



<ScreenThree>:
    texto: texto
    BoxLayout:
        orientation: 'vertical'         
        Label:           
            text:"ESCOLHA SEU PERFIL FAVORITO"
            font_size: 40
        TextInput:
            id:texto            
            multiline:False
            
            size:210,300
        Button:
            text: "ENTER"
            on_press:
                root.btn()
            on_release:                   
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_four"                              
        Button:
            text: "LIMPAR"
            on_press:
                root.limpar()             

        Button:
            text: "Voltar"
            on_release:
                
                root.manager.transition.direction= "right"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_two"


<ScreenFour>:
    texto: texto
    BoxLayout:
        orientation: 'vertical'         
        Label:           
            text:"..QUAL O PESO DA CARGA EM KG?.."
        TextInput:
            id:texto
            multiline:False
            
            size:210,300
        Button:
            text: "ENTER"
            on_press:
                root.btn()
            on_release:                   
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_five"                              
        Button:
            text: "LIMPAR"
            on_press:
                root.limpar()             
            
        Button:
            text: "Voltar"
            on_release:
                
                root.manager.transition.direction= "right"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_three"

<ScreenFive>:
    texto: texto
    BoxLayout:
        orientation: 'vertical'         
        Label:           
            text:"..INFORME A QUANTIDADE DE COMBUSTIVEL INICIAL.."
        TextInput:
            id:texto
            multiline:False
            
            size:210,300
         
        Button:
            text: "ENTER"
            on_press:
                root.btn()
            on_release:                   
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_six"                              
        Button:
            text: "LIMPAR"
            on_press:
                root.limpar()             
            
        Button:
            text: "Voltar"
            on_release:
                
                root.manager.transition.direction= "right"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_four"
<ScreenSix>:
    texto: texto
    BoxLayout:
        orientation: 'vertical'         
        Label:           
            text:"..INFORME O KM DE CHEGADA.."
        TextInput:
            id:texto
            multiline:False
            
            size:210,300
        Button:
            text: "ENTER"
            on_press:
                root.btn()
            on_release:                   
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_seven"                              
        Button:
            text: "LIMPAR"
            on_press:
                root.limpar()             
            
        Button:
            text: "Voltar"
            on_release:
                
                root.manager.transition.direction= "right"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_five"

<ScreenSeven>:
    texto: texto
    BoxLayout:
        orientation: 'vertical'         
        Label:           
            text:"..INFORME A QUANTIDADE DE COMBUSTIVEL FINAL.."
        TextInput:
            id:texto
            multiline:False
            
            size:210,300
         
        Button:
            text: "ENTER"
            on_press:
                root.btn()
            on_release:                   
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_eight"                              
        Button:
            text: "LIMPAR"
            on_press:
                root.limpar()             
            
        Button:
            text: "Voltar"
            on_release:
                
                root.manager.transition.direction= "right"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_six"


<ScreenEight>:
    
    BoxLayout:
        orientation: 'vertical'         
        Label:           
            text:"..CLIQUE PARA FINALIZAR.."

           
        Button:
            text: "FINALIZAR"
            on_press:
                root.btn()
            on_release:                   
                root.manager.transition.direction= "left"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_one"                              
            
        Button:
            text: "Voltar"
            on_release:
                
                root.manager.transition.direction= "right"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_seven"




<ScreenGrid>:
        
    GridLayout:
        
        cols:3
        Label:           
            text:""
        
        Label:
            id: lbl           
            text:""           
        Label:           
            text:""
        Button:
            text: "1"       
            on_release:                   
        Button:
            text: "2"               
            on_release:                   
        Button:
            text: "3"               
            on_release:                   
        Button:
            text: "4"       
            on_release:                   
        Button:
            text: "5"               
            on_release:                   
        Button:
            text: "6"               
            on_release:                   
        Button:
            text: "7"       
            on_release:                   
        Button:
            text: "8"               
            on_release:                   
        Button:
            text: "9"               
            on_release:
                root.n9() 
                              
        Button:
            text: "VOLTAR"               
            on_release:                   
                root.manager.transition.direction= "right"
                root.manager.transition.duration= 0.5
                root.manager.current= "screen_two"                              

        Button:
            text: "0"               
            
                              
        Button:
            text: "ENTER"               
            on_release:                   
                self.text="BOSTA"
             


            
""")
#Window.clearcolor=(0.10,.30,.50,1)   
      
# declara uma class screen com o que o button faz  

      
class ScreenOne(Screen):    
    
    def btn1(self):
        m="ADRIANO"
        op="1"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)
    def btn2(self):  
        m="CAIO"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)   
        dados1.close()  
        op="0"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5) 
                
    def btn3(self):
        m="DIOGO"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="2"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)          
    def btn4(self):
        m="GABRIEL"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m) 
        dados1.close()
        op="3"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)           
    def btn5(self):
        m="IGOR"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="5"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)            
    def btn6(self):
        m="MATEUS"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        op="4"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)            
    def btn7(self):
        m="OTAVIO"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="6"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            try:
                s.send("0".encode( "utf-8"))
                s.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='cozinha':
            try: 
                s2.send("0".encode( "utf-8"))
                s2.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='sala':
            try:
                s3.send("0".encode( "utf-8"))
                s3.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='todos':
            try:
                s.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s2.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s3.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s.send(op.encode( "utf-8"))
            except:
                print('')
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')

        time.sleep(1)           
       # op="3"
        #s.send(op.encode( "utf-8"))  
       # time.sleep(1)                   
    def btn8(self):
        m="PATRICK"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="7"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            try:
                s.send("0".encode( "utf-8"))
                s.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='cozinha':
            try:    
                s2.send("0".encode( "utf-8"))
                s2.send(op.encode( "utf-8"))  
            except:
                print('')
        if pl=='sala':   
            try: 
                s3.send("0".encode( "utf-8"))
                s3.send(op.encode( "utf-8"))  
            except:
                print('')
        if pl=='todos':
            try: 
                s.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s2.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s3.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s.send(op.encode( "utf-8")) 
            except:
                print('')
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')
        time.sleep(1)  
       # op="7"
      #  s.send(op.encode( "utf-8")) 
       # time.sleep(1)           
                   
    def btn9(self):
        m="WITALEY"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)            
        dados1.close()   
        #op="8"
        #s.send(op.encode( "utf-8")) 
        time.sleep(0.5)
class ScreenTwo(Screen):
    
    def btn1(self):
        p="cozinha"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s2.connect((svr2, PORT2))
            time.sleep(1)
        except:
            print('erro')
             
    def btn2(self):
        p="quarto"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s.connect((svr, PORT))
            time.sleep(1)
        except:
            print('erro')
           
    def btn3(self):
        p="sala"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s3.connect((svr3, PORT3))
            time.sleep(1)
        except:
            print('erro')
           
    def btn4(self):
        p="todos"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s.connect((svr, PORT))
            time.sleep(1)
            s2.connect((svr2, PORT2))
            time.sleep(1)
            s3.connect((svr3, PORT3))
            time.sleep(1)
        except:
            print('erro')

class ScreenConfig(Screen):
    
    def btn1(self):
        p="colorido"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
             
    def btn2(self):
        p="monocromatico"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        
    def btn3(self):
        p="soft"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        
    def btn4(self):
        p="verdetropical"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()

    def btn5(self):
        p="rosa"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()



############## telas neutras#########

class ScreenOneNeutra(Screen):    
    
    def btn1(self):
        m="ADRIANO"
        op="1"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
                
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)
    def btn2(self):  
        m="CAIO"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)   
        dados1.close()  
        op="0"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
                
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5) 
                
    def btn3(self):
        m="DIOGO"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="2"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)          
    def btn4(self):
        m="GABRIEL"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m) 
        dados1.close()
        op="3"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)           
    def btn5(self):
        m="IGOR"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="5"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)            
    def btn6(self):
        m="MATEUS"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        op="4"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)            
    def btn7(self):
        m="OTAVIO"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="6"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            try:
                s.send("0".encode( "utf-8"))
                s.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='cozinha':
            try: 
                s2.send("0".encode( "utf-8"))
                s2.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='sala':
            try:
                s3.send("0".encode( "utf-8"))
                s3.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='todos':
            try:
                s.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s2.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s3.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s.send(op.encode( "utf-8"))
            except:
                print('')
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')

        time.sleep(1)           
       # op="3"
        #s.send(op.encode( "utf-8"))  
       # time.sleep(1)                   
    def btn8(self):
        m="PATRICK"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="7"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            try:
                s.send("0".encode( "utf-8"))
                s.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='cozinha':
            try:    
                s2.send("0".encode( "utf-8"))
                s2.send(op.encode( "utf-8"))  
            except:
                print('')
        if pl=='sala':   
            try: 
                s3.send("0".encode( "utf-8"))
                s3.send(op.encode( "utf-8"))  
            except:
                print('')
        if pl=='todos':
            try: 
                s.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s2.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s3.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s.send(op.encode( "utf-8")) 
            except:
                print('')
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')
        time.sleep(1)  
       # op="7"
      #  s.send(op.encode( "utf-8")) 
       # time.sleep(1)           
                   
    def btn9(self):
        m="WITALEY"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)            
        dados1.close()   
        #op="8"
        #s.send(op.encode( "utf-8")) 
        time.sleep(0.5)
class ScreenTwoNeutra(Screen):
    
    def btn1(self):
        p="cozinha"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s2.connect((svr2, PORT2))
            time.sleep(1)
        except:
            print('erro')
             
    def btn2(self):
        p="quarto"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s.connect((svr, PORT))
            time.sleep(1)
        except:
            print('erro')
           
    def btn3(self):
        p="sala"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s3.connect((svr3, PORT3))
            time.sleep(1)
        except:
            print('erro')
           
    def btn4(self):
        p="todos"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s.connect((svr, PORT))
            time.sleep(1)
            s2.connect((svr2, PORT2))
            time.sleep(1)
            s3.connect((svr3, PORT3))
            time.sleep(1)
        except:
            print('erro')

class ScreenConfigNeutra(Screen):
    
    def btn1(self):
        p="colorido"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
             
    def btn2(self):
        p="monocromatico"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        
    def btn3(self):
        p="soft"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
    
    def btn4(self):
        p="verdetropical"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
       
    def btn5(self):
        p="rosa"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
       

##############fim telas neutras######

############## telas Rosas #########

class ScreenOneRosa(Screen):    
    
    def btn1(self):
        m="ADRIANO"
        op="1"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)
    def btn2(self):  
        m="CAIO"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)   
        dados1.close()  
        op="0"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5) 
                
    def btn3(self):
        m="DIOGO"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="2"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)          
    def btn4(self):
        m="GABRIEL"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m) 
        dados1.close()
        op="3"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)           
    def btn5(self):
        m="IGOR"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="5"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)            
    def btn6(self):
        m="MATEUS"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        op="4"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)            
    def btn7(self):
        m="OTAVIO"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="6"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            try:
                s.send("0".encode( "utf-8"))
                s.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='cozinha':
            try: 
                s2.send("0".encode( "utf-8"))
                s2.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='sala':
            try:
                s3.send("0".encode( "utf-8"))
                s3.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='todos':
            try:
                s.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s2.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s3.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s.send(op.encode( "utf-8"))
            except:
                print('')
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')

        time.sleep(1)           
       # op="3"
        #s.send(op.encode( "utf-8"))  
       # time.sleep(1)                   
    def btn8(self):
        m="PATRICK"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="7"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            try:
                s.send("0".encode( "utf-8"))
                s.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='cozinha':
            try:    
                s2.send("0".encode( "utf-8"))
                s2.send(op.encode( "utf-8"))  
            except:
                print('')
        if pl=='sala':   
            try: 
                s3.send("0".encode( "utf-8"))
                s3.send(op.encode( "utf-8"))  
            except:
                print('')
        if pl=='todos':
            try: 
                s.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s2.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s3.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s.send(op.encode( "utf-8")) 
            except:
                print('')
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')
        time.sleep(1)  
       # op="7"
      #  s.send(op.encode( "utf-8")) 
       # time.sleep(1)          
                   
    def btn9(self):
        m="WITALEY"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)            
        dados1.close()   
        #op="8"
        #s.send(op.encode( "utf-8")) 
        time.sleep(0.5)
class ScreenTwoRosa(Screen):
    
    def btn1(self):
        p="cozinha"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s2.connect((svr2, PORT2))
            time.sleep(1)
        except:
            print('erro')
             
    def btn2(self):
        p="quarto"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s.connect((svr, PORT))
            time.sleep(1)
        except:
            print('erro')
           
    def btn3(self):
        p="sala"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s3.connect((svr3, PORT3))
            time.sleep(1)
        except:
            print('erro')
           
    def btn4(self):
        p="todos"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s.connect((svr, PORT))
            time.sleep(1)
            s2.connect((svr2, PORT2))
            time.sleep(1)
            s3.connect((svr3, PORT3))
            time.sleep(1)
        except:
            print('erro')

class ScreenConfigRosa(Screen):
    
    def btn1(self):
        p="colorido"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
             
    def btn2(self):
        p="monocromatico"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        
    def btn3(self):
        p="soft"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        
    def btn4(self):
        p="verdetropical"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()

    def btn5(self):
        p="rosa"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()


##############fim telas Rosas######


############## telas softs #########

class ScreenOneSoft(Screen):    
    
    def btn1(self):
        m="ADRIANO"
        op="1"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)
    def btn2(self):  
        m="CAIO"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)   
        dados1.close()  
        op="0"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5) 
                
    def btn3(self):
        m="DIOGO"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="2"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)          
    def btn4(self):
        m="GABRIEL"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m) 
        dados1.close()
        op="3"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)           
    def btn5(self):
        m="IGOR"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="5"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)            
    def btn6(self):
        m="MATEUS"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        op="4"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)            
    def btn7(self):
        m="OTAVIO"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="6"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            try:
                s.send("0".encode( "utf-8"))
                s.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='cozinha':
            try: 
                s2.send("0".encode( "utf-8"))
                s2.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='sala':
            try:
                s3.send("0".encode( "utf-8"))
                s3.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='todos':
            try:
                s.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s2.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s3.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s.send(op.encode( "utf-8"))
            except:
                print('')
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')

        time.sleep(1)           
       # op="3"
        #s.send(op.encode( "utf-8"))  
       # time.sleep(1)                   
    def btn8(self):
        m="PATRICK"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="7"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            try:
                s.send("0".encode( "utf-8"))
                s.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='cozinha':
            try:    
                s2.send("0".encode( "utf-8"))
                s2.send(op.encode( "utf-8"))  
            except:
                print('')
        if pl=='sala':   
            try: 
                s3.send("0".encode( "utf-8"))
                s3.send(op.encode( "utf-8"))  
            except:
                print('')
        if pl=='todos':
            try: 
                s.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s2.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s3.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s.send(op.encode( "utf-8")) 
            except:
                print('')
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')
        time.sleep(1)  
       # op="7"
      #  s.send(op.encode( "utf-8")) 
       # time.sleep(1)          
                   
    def btn9(self):
        m="WITALEY"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)            
        dados1.close()   
        #op="8"
        #s.send(op.encode( "utf-8")) 
        time.sleep(0.5)
class ScreenTwoSoft(Screen):
    
    def btn1(self):
        p="cozinha"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s2.connect((svr2, PORT2))
            time.sleep(1)
        except:
            print('erro')
             
    def btn2(self):
        p="quarto"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s.connect((svr, PORT))
            time.sleep(1)
        except:
            print('erro')
           
    def btn3(self):
        p="sala"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s3.connect((svr3, PORT3))
            time.sleep(1)
        except:
            print('erro')
           
    def btn4(self):
        p="todos"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s.connect((svr, PORT))
            time.sleep(1)
            s2.connect((svr2, PORT2))
            time.sleep(1)
            s3.connect((svr3, PORT3))
            time.sleep(1)
        except:
            print('erro')

class ScreenConfigSoft(Screen):
    
    def btn1(self):
        p="colorido"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
             
    def btn2(self):
        p="monocromatico"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        
    def btn3(self):
        p="soft"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        
    def btn4(self):
        p="verdetropical"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()

    def btn5(self):
        p="rosa"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()


##############fim telas Softs######

##############inicio telas verde tropical######
class ScreenOneVerde(Screen):    
    
    def btn1(self):
        m="ADRIANO"
        op="1"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)
    def btn2(self):  
        m="CAIO"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)   
        dados1.close()  
        op="0"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5) 
                
    def btn3(self):
        m="DIOGO"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="2"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)          
    def btn4(self):
        m="GABRIEL"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m) 
        dados1.close()
        op="3"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)           
    def btn5(self):
        m="IGOR"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="5"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)            
    def btn6(self):
        m="MATEUS"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        op="4"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            
            try:    
                s.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='cozinha':
            try:       
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
        if pl=='sala':
            try:       
                s3.send(op.encode( "utf-8"))
            except:
                print('')   
        if pl=='todos':
            try:       
                s.send(op.encode( "utf-8"))
            except:
                print('') 
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')  
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')  

        time.sleep(0.5)            
    def btn7(self):
        m="OTAVIO"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="6"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            try:
                s.send("0".encode( "utf-8"))
                s.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='cozinha':
            try: 
                s2.send("0".encode( "utf-8"))
                s2.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='sala':
            try:
                s3.send("0".encode( "utf-8"))
                s3.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='todos':
            try:
                s.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s2.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s3.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s.send(op.encode( "utf-8"))
            except:
                print('')
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')

        time.sleep(1)           
       # op="3"
        #s.send(op.encode( "utf-8"))  
       # time.sleep(1)                   
    def btn8(self):
        m="PATRICK"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)
        dados1.close()
        op="7"
        leitura2=open('bton2.txt')
        texto2= leitura2.readlines()
        pl2=str(texto2)
        pl=pl2[2:-2]
        if pl=='quarto':
            try:
                s.send("0".encode( "utf-8"))
                s.send(op.encode( "utf-8"))
            except:
                print('')
        if pl=='cozinha':
            try:    
                s2.send("0".encode( "utf-8"))
                s2.send(op.encode( "utf-8"))  
            except:
                print('')
        if pl=='sala':   
            try: 
                s3.send("0".encode( "utf-8"))
                s3.send(op.encode( "utf-8"))  
            except:
                print('')
        if pl=='todos':
            try: 
                s.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s2.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s3.send("0".encode( "utf-8"))
            except:
                print('')
            try:
                s.send(op.encode( "utf-8")) 
            except:
                print('')
            try:
                s2.send(op.encode( "utf-8"))
            except:
                print('')
            try:
                s3.send(op.encode( "utf-8"))
            except:
                print('')
        time.sleep(1)  
       # op="7"
      #  s.send(op.encode( "utf-8")) 
       # time.sleep(1)            
                   
    def btn9(self):
        m="WITALEY"
        dados1= open('bton1.txt','w')                                                  
        dados1.write(m)            
        dados1.close()   
        #op="8"
        #s.send(op.encode( "utf-8")) 
        time.sleep(0.5)
class ScreenTwoVerde(Screen):
    
    def btn1(self):
        p="cozinha"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s2.connect((svr2, PORT2))
            time.sleep(1)
        except:
            print('erro')
             
    def btn2(self):
        p="quarto"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s.connect((svr, PORT))
            time.sleep(1)
        except:
            print('erro')
           
    def btn3(self):
        p="sala"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s3.connect((svr3, PORT3))
            time.sleep(1)
        except:
            print('erro')
           
    def btn4(self):
        p="todos"
        dados2= open('bton2.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        try:
            s.connect((svr, PORT))
            time.sleep(1)
            s2.connect((svr2, PORT2))
            time.sleep(1)
            s3.connect((svr3, PORT3))
            time.sleep(1)
        except:
            print('erro')

class ScreenConfigVerde(Screen):
    
    def btn1(self):
        p="colorido"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
             
    def btn2(self):
        p="monocromatico"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        
    def btn3(self):
        p="soft"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        
    def btn4(self):
        p="verdetropical"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        
    def btn5(self):
        p="rosa"
        dados2= open('config.txt','w')                                                  
        dados2.write(p) 
        dados2.close()
        

##############fim telas verde tropical######


            
#tela km inicial    
class ScreenThree(Screen):
    texto= ObjectProperty(None)
    def btn(self):
        ytr3=open('bton3.txt')
        ytr3linha= ytr3.readlines()
        info1=str(ytr3linha)
        info=info1[2:-2]
        if (info!=''):
            self.texto.text=info        
        kmsaida=self.texto.text        
        dados3= open('bton3.txt','w')                                                  
        dados3.write(kmsaida)        
        dados3.close()
    def limpar(self):
        self.texto.text=""    
        dados3= open('bton3.txt','w')                                                  
        dados3.write("")        
        dados3.close()           
class ScreenFour(Screen): 

    texto= ObjectProperty(None)       
    def btn(self):
       ytr4=open('bton4.txt')
       ytr4linha= ytr4.readlines()
       info4=str(ytr4linha)
       info=info4[2:-2]
       if(info!=''):
           self.texto.text=info        
        
       kg= self.texto.text
       dados4= open('bton4.txt','w')                                                  
       dados4.write(kg)        
       dados4.close()
       
    def limpar(self):
       self.texto.text="" 
       dados4= open('bton4.txt','w')                                                  
       dados4.write("")        
       dados4.close()    
#tela litros inicial    
class ScreenFive(Screen): 
    texto= ObjectProperty(None)       
    def btn(self):
       ytr5=open('bton5.txt')
       ytr5linha= ytr5.readlines()
       info5=str(ytr5linha)
       info=info5[2:-2]
       if(info!=''):
           self.texto.text=info        
        
       litroi= self.texto.text
       dados5= open('bton5.txt','w')                                                  
       dados5.write(litroi)        
       dados5.close()
       
    def limpar(self):
       self.texto.text="" 
       dados5= open('bton5.txt','w')                                                  
       dados5.write("")        
       dados5.close()         
#tela km final
class ScreenSix(Screen): 
    texto= ObjectProperty(None)     
    def btn(self):
       ytr6=open('bton6.txt')
       ytr6linha= ytr6.readlines()
       info6=str(ytr6linha)
       info=info6[2:-2]
       if(info!=''):
           self.texto.text=info        
        
       kmchegada= self.texto.text
       dados6= open('bton6.txt','w')                                                  
       dados6.write(kmchegada)        
       dados6.close()
       
    def limpar(self):
       self.texto.text="" 
       dados6= open('bton6.txt','w')                                                  
       dados6.write("")        
       dados6.close()         
#tela litros final    
class ScreenSeven(Screen): 
    texto= ObjectProperty(None)       
    def btn(self):
       ytr7=open('bton7.txt')
       ytr7linha= ytr7.readlines()
       info7=str(ytr7linha)
       info=info7[2:-2]
       if(info!=''):
           self.texto.text=info        
        
       litrof= self.texto.text
       dados7= open('bton7.txt','w')                                                  
       dados7.write(litrof)        
       dados7.close()
       dados7= open('bton7.txt','w')                                                  
       dados7.write("")        
       dados7.close()        
    def limpar(self):
       self.texto.text="" 
       
       dados7= open('bton7.txt','w')                                                  
       dados7.write("")        
       dados7.close() 
        

    
class ScreenGrid(Screen):
    def n1(self):
       self.lbl.text= "1"        
       abc=1
    def n2(self):
       self.lbl.text= "2"        
       abc=2  
    def n3(self):
       self.lbl.text= "3"        
       abc=3
    def n4(self):
       self.lbl.text= "4"        
       abc=4   
    def n5(self):
       self.lbl.text= "5"        
       abc=5
    def n6(self):
       self.lbl.text= "6"        
       abc=6   
    def n7(self):
       self.lbl.text= "7"        
       abc=7
    def n8(self):
       self.lbl.text= "8"        
       abc=8   
    def n9(self,obj):
           
       abc=9
    def n0(self):
       self.lbl.text= "0"        
       abc=0   
    def nV(self):
       self.lbl.text= ""        
   
    def nE(self):
       self.lbl.text= "(OK)"  
       
class ScreenEight(Screen):
    def btn(self):   
        xtr1=open('bton1.txt')
        xtr1linha= xtr1.readlines()
        m1=str(xtr1linha)
        m=m1[2:-2]
        
        xtr2=open('bton2.txt')
        xtr2linha= xtr2.readlines()
        p1=str(xtr2linha)
        p=p1[2:-2]
        
        xtr3=open('bton3.txt')
        xtr3linha= xtr3.readlines()
        kmsaida1=str(xtr3linha)
        kmsaida=kmsaida1[2:-2]
        
        xtr4=open('bton4.txt')
        xtr4linha= xtr4.readlines()
        kg1=str(xtr4linha)
        kg=kg1[2:-2]
        
        xtr5=open('bton5.txt')
        xtr5linha= xtr5.readlines()
        litroi1=str(xtr5linha)
        litroi=litroi1[2:-2]
        
        xtr6=open('bton6.txt')
        xtr6linha= xtr6.readlines()
        kmchegada1=str(xtr6linha)
        kmchegada=kmchegada1[2:-2]
        
        xtr7=open('bton7.txt')
        xtr7linha= xtr7.readlines()
        litrof1=str(xtr7linha)
        litrof=litrof1[2:-2]
        
        
        
        km= kmchegada+'-'+kmsaida
        litros='('+litroi+'-'+litrof+')'
        media='=ARRED(('+km+')/'+litros+';2)'       
        full=m+': '+p+': '+kg+': '+media+': '+hoje+'$_'
        enviaemail(full,"")
     
        #zerar botao3
        dados3= open('bton3.txt','w')                                                  
        dados3.write("")        
        dados3.close() 

        #zerar botao4
        dados4= open('bton4.txt','w')                                                  
        dados4.write("")        
        dados4.close() 

        #zerar botao5
        dados5= open('bton5.txt','w')                                                  
        dados5.write("")        
        dados5.close() 

        #zerar botao6
        dados6= open('bton6.txt','w')                                                  
        dados6.write("")        
        dados6.close() 

        #zerar botao7
        dados7= open('bton7.txt','w')                                                  
        dados7.write("")        
        dados7.close() 

        
screen_manager=ScreenManager()

leitura3=open('config.txt')
texto2= leitura3.readlines()
cor2=str(texto2)
cor=cor2[2:-2]

if cor=='colorido':      
    #screen_manager.add_widget(ScreenOne(name="screen_one"))   
    screen_manager.add_widget(ScreenTwo(name="screen_two"))
    screen_manager.add_widget(ScreenConfig(name="screen_config"))
    screen_manager.add_widget(ScreenOne(name="screen_one"))  

if cor=='monocromatico':
    screen_manager.add_widget(ScreenTwoNeutra(name="screen_twoneutra"))
    screen_manager.add_widget(ScreenConfigNeutra(name="screen_configneutra"))
    screen_manager.add_widget(ScreenOneNeutra(name="screen_oneneutra"))  

if cor=='soft':         
    screen_manager.add_widget(ScreenTwoSoft(name="screen_twosoft"))
    screen_manager.add_widget(ScreenConfigSoft(name="screen_configsoft"))
    screen_manager.add_widget(ScreenOneSoft(name="screen_onesoft"))  


if cor=='rosa':         
    screen_manager.add_widget(ScreenTwoRosa(name="screen_tworosa"))
    screen_manager.add_widget(ScreenConfigRosa(name="screen_configrosa"))
    screen_manager.add_widget(ScreenOneRosa(name="screen_onerosa"))  

if cor=='verdetropical':         
    screen_manager.add_widget(ScreenTwoVerde(name="screen_twoverdetropical"))
    screen_manager.add_widget(ScreenConfigVerde(name="screen_configverdetropical"))
    screen_manager.add_widget(ScreenOneVerde(name="screen_oneverdetropical"))  
 
 
       
#screen_manager.add_widget(ScreenOne(name="screen_one"))   
screen_manager.add_widget(ScreenTwo(name="screen_two"))
screen_manager.add_widget(ScreenConfig(name="screen_config"))
screen_manager.add_widget(ScreenOne(name="screen_one"))  


screen_manager.add_widget(ScreenTwoNeutra(name="screen_twoneutra"))
screen_manager.add_widget(ScreenConfigNeutra(name="screen_configneutra"))
screen_manager.add_widget(ScreenOneNeutra(name="screen_oneneutra"))  

screen_manager.add_widget(ScreenTwoRosa(name="screen_tworosa"))
screen_manager.add_widget(ScreenConfigRosa(name="screen_configrosa"))
screen_manager.add_widget(ScreenOneRosa(name="screen_onerosa"))  


screen_manager.add_widget(ScreenTwoSoft(name="screen_twosoft"))
screen_manager.add_widget(ScreenConfigSoft(name="screen_configsoft"))
screen_manager.add_widget(ScreenOneSoft(name="screen_onesoft"))  

screen_manager.add_widget(ScreenTwoVerde(name="screen_twoverdetropical"))
screen_manager.add_widget(ScreenConfigVerde(name="screen_configverdetropical"))
screen_manager.add_widget(ScreenOneVerde(name="screen_oneverdetropical"))  
 

screen_manager.add_widget(ScreenThree(name="screen_three"))   
screen_manager.add_widget(ScreenFour(name="screen_four"))   
screen_manager.add_widget(ScreenFive(name="screen_five"))   
screen_manager.add_widget(ScreenSix(name="screen_six"))   
screen_manager.add_widget(ScreenSeven(name="screen_seven"))   
screen_manager.add_widget(ScreenEight(name="screen_eight"))   

class typ(BoxLayout):
      
    pass
               
class MyApp(App):

        def build(self):          
                        
            return screen_manager
 
                                  
if __name__=="__main__":
    
          
    MyApp().run()
        

