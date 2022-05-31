from calendar import Calendar
from datetime import date
from logging import root
from pathlib import Path
from tabnanny import check
from tkinter import *
from tkinter.ttk import *
from typing_extensions import Self
from click import command
from cupshelpers import missingExecutables
from pytz import HOUR
from tkcalendar import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
from fpdf import FPDF



import time 


root = Tk()
root.title('Relatório diário')
root.geometry('1500x950')



num = IntVar()

#criando calendario 
#myCal = Calendar(root, setmode = 'day', date_pattern = 'dd/mm/yyyy')
#myCal.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)


#Criando combobox
combo_entry = Combobox(root)

combo2_entry = Combobox(root)

#definindo valores combobox
combo_entry['values' ] = ('Barra Mansa 1', 'Barra Mansa 2', 'Três Rios 1', 'Três Rios 2')

combo2_entry['values' ] = ('Não', 'Sim')

#posicionando a combobox
combo_entry.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)
label0 = Label(root, text='Selecione o Gerador')
label0.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)

combo2_entry.grid(row=22, column=1, padx=5, pady=5, sticky=NSEW)
label0 = Label(root, text='Amostra de óleo coletada?')
label0.grid(row=22, column=0, padx=5, pady=5, sticky=NSEW)





#criando uma checkbox

c = Checkbutton(root, text='Gerador em Operação?' )
c.grid(row=4, column=3, padx=8, pady=8, sticky=NSEW)






#fazendo o relógio

def clock ():
    hour = time.strftime('%H')
    minute = time.strftime('%M')
    date = time.strftime('%d-%m-%Y')

    label_clock.config(text= date + '   ' + hour + ':' + minute )
    label_clock.after(1000, clock)

def update():
    label_clock.config(text='New Text')
labelclock = Label(root, text='Data e Hora')
labelclock.grid(row=3, column=0)
label_clock = Label(root, text='', font=('Helvetica', 20))
label_clock.grid(row=3, column=1)

clock()

#labels

calendario_entry = time.strftime('%d-%m-%Y')

h1 = time.strftime('%H:%M')

def limpa_tela():

        hora_entry.delete(0, END)
        arranque_entry.delete(0, END)
        itron_entry.delete(0, END)
        diane_entry.delete(0, END)

        hora_entry.delete(0, END)
        combo_entry.delete(0, END)
        combo2_entry.delete(0, END)
        arranque_entry.delete(0, END)
        itron_entry.delete(0, END)
        diane_entry.delete(0, END)
        potat_entry.delete(0, END)
        potap_entry.delete(0, END)

        tbat_entry.delete(0, END)

        tmist_entry.delete(0, END)
        pcarga_entry.delete(0, END)
        gasmixer_entry.delete(0, END)
        mariposa_entry.delete(0, END)
        bypass_entry.delete(0, END)
        toil_entry.delete(0, END)
        poil_entry.delete(0, END)
        twat_entry.delete(0, END)
        pwat_entry.delete(0, END)

        #cilindros

        cil_1_entry.delete(0, END)
        cil_2_entry.delete(0, END)
        cil_3_entry.delete(0, END)
        cil_4_entry.delete(0, END)
        cil_5_entry.delete(0, END)
        cil_6_entry.delete(0, END)
        cil_7_entry.delete(0, END)
        cil_8_entry.delete(0, END)
        cil_9_entry.delete(0, END)
        cil_10_entry.delete(0, END)
        cil_11_entry.delete(0, END)
        cil_12_entry.delete(0, END)
        cil_13_entry.delete(0, END)
        cil_14_entry.delete(0, END)
        cil_15_entry.delete(0, END)
        cil_16_entry.delete(0, END)
        cil_17_entry.delete(0, END)
        cil_18_entry.delete(0, END)
        cil_19_entry.delete(0, END)
        cil_20_entry.delete(0, END)

        #dados do gas

        vaz_entry.delete(0, END)
        met_entry.delete(0, END)
        h2s_entry.delete(0, END)
        oxi_entry.delete(0, END)

        #dados do chiller

        chiller1_entry.delete(0, END)
        chiller2_entry.delete(0, END)
        chiller3_entry.delete(0, END)
        chiller4_entry.delete(0, END)

        #temperatura bobina do trafo

        bobina1_entry.delete(0, END)
        bobina2_entry.delete(0, END)
        bobina3_entry.delete(0, END)

        #Dados cabina de média tensão

        kv_entry.delete(0, END)
        amp_entry.delete(0, END)
        exp_entry.delete(0, END)
        noil_entry.delete(0,END)






 

label0 = Label(root, text='Dados do Gerador')
label0.grid(row=4, column=0, padx=8, pady=8, sticky=NSEW)


label1 = Label(root, text='Horas de operação:')
label1.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
hora_entry = Entry(root, width = 10)
hora_entry.grid(row=5, column=1)

label2 = Label(root, text='Número de arranques:')
label2.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
arranque_entry = Entry(root, width = 10)
arranque_entry.grid(row=6, column=1)

label3 = Label(root, text='Energia produzida Itron:')
label3.grid(row=7, column=0, padx=5, pady=5, sticky=NSEW)
itron_entry = Entry(root, width = 10)
itron_entry.grid(row=7, column=1)

label4 = Label(root, text='Energia produzida Diane:')
label4.grid(row=8, column=0, padx=5, pady=5, sticky=NSEW)
diane_entry = Entry(root, width = 10)
diane_entry.grid(row=8, column=1)

label5 = Label(root, text='Potência ativa:')
label5.grid(row=9, column=0, padx=5, pady=5, sticky=NSEW)
potat_entry = Entry(root, width = 10)
potat_entry.grid(row=9, column=1)

label6 = Label(root, text='Potência aparente:')
label6.grid(row=10, column=0, padx=5, pady=5, sticky=NSEW)
potap_entry = Entry(root, width = 10)
potap_entry.grid(row=10, column=1)


label7 = Label(root, text='Tensão das baterias:')
label7.grid(row=11, column=0, padx=5, pady=5, sticky=NSEW)
tbat_entry = Entry(root, width = 10)
tbat_entry.grid(row=11, column=1)

label8 = Label(root, text='Dados Leanox')
label8.grid(row=12, column=0, padx=5, pady=5, sticky=NSEW)

label9 = Label(root, text='Temperatura da mistura:')
label9.grid(row=13, column=0, padx=5, pady=5, sticky=NSEW)
tmist_entry = Entry(root, width = 10)
tmist_entry.grid(row=13, column=1)

label10 = Label(root, text='Pressão de carga:')
label10.grid(row=14, column=0, padx=5, pady=5, sticky=NSEW)
pcarga_entry = Entry(root, width = 10)
pcarga_entry.grid(row=14, column=1)

label11 = Label(root, text='Posição do regulador de gás:')
label11.grid(row=15, column=0, padx=5, pady=5, sticky=NSEW)
gasmixer_entry = Entry(root, width = 10)
gasmixer_entry.grid(row=15, column=1)

label12 = Label(root, text='Posição da válvula borboleta:')
label12.grid(row=16, column=0, padx=5, pady=5, sticky=NSEW)
mariposa_entry = Entry(root, width = 10)
mariposa_entry.grid(row=16, column=1)

label13 = Label(root, text='Posição do bypass:')
label13.grid(row=17, column=0, padx=5, pady=5, sticky=NSEW)
bypass_entry = Entry(root, width = 10)
bypass_entry.grid(row=17, column=1)

label14 = Label(root, text='Temperatura do óleo:')
label14.grid(row=18, column=0, padx=5, pady=5, sticky=NSEW)
toil_entry = Entry(root, width = 10)
toil_entry.grid(row=18, column=1)

label15 = Label(root, text='Pressão de óleo:')
label15.grid(row=19, column=0, padx=5, pady=5, sticky=NSEW)
poil_entry = Entry(root, width = 10)
poil_entry.grid(row=19, column=1)

label16 = Label(root, text='Temperatura de água:')
label16.grid(row=20, column=0, padx=5, pady=5, sticky=NSEW)
twat_entry = Entry(root, width = 10)
twat_entry.grid(row=20, column=1)

label17 = Label(root, text='Pressão de água:')
label17.grid(row=21, column=0, padx=5, pady=5, sticky=NSEW)
pwat_entry = Entry(root, width = 10)
pwat_entry.grid(row=21, column=1)

label18 = Label(root, text='Temperatura de cilindros')
label18.grid(row=23, column=0, padx=5, pady=5, sticky=NSEW)

label19 = Label(root, text='Cilindro 1')
label19.grid(row=24, column=0, padx=5, pady=5, sticky=NSEW)
cil_1_entry = Entry(root, width = 10)
cil_1_entry.grid(row=24, column=1)

label20 = Label(root, text='Cilindro 2')
label20.grid(row=25, column=0, padx=5, pady=5, sticky=NSEW)
cil_2_entry = Entry(root, width = 10)
cil_2_entry.grid(row=25, column=1)

label21 = Label(root, text='Cilindro 3')
label21.grid(row=26, column=0, padx=5, pady=5, sticky=NSEW)
cil_3_entry = Entry(root, width = 10)
cil_3_entry.grid(row=26, column=1)

label22 = Label(root, text='Cilindro 4')
label22.grid(row=27, column=0, padx=5, pady=5, sticky=NSEW)
cil_4_entry = Entry(root, width = 10)
cil_4_entry.grid(row=27, column=1)

label23 = Label(root, text='Cilindro 5')
label23.grid(row=28, column=0, padx=5, pady=5, sticky=NSEW)
cil_5_entry = Entry(root, width = 10)
cil_5_entry.grid(row=28, column=1)


label24 = Label(root, text='Cilindro 6')
label24.grid(row=24, column=2, padx=5, pady=5, sticky=NSEW)
cil_6_entry = Entry(root, width = 10)
cil_6_entry.grid(row=24, column=3)

label25 = Label(root, text='Cilindro 7')
label25.grid(row=25, column=2, padx=5, pady=5, sticky=NSEW)
cil_7_entry = Entry(root, width = 10)
cil_7_entry.grid(row=25, column=3)

label26 = Label(root, text='Cilindro 8')
label26.grid(row=26, column=2, padx=5, pady=5, sticky=NSEW)
cil_8_entry = Entry(root, width = 10)
cil_8_entry.grid(row=26, column=3)

label27 = Label(root, text='Cilindro 9')
label27.grid(row=27, column=2, padx=5, pady=5, sticky=NSEW)
cil_9_entry = Entry(root, width = 10)
cil_9_entry.grid(row=27, column=3)

label28 = Label(root, text='Cilindro 10')
label28.grid(row=28, column=2, padx=5, pady=5, sticky=NSEW)
cil_10_entry = Entry(root, width = 10)
cil_10_entry.grid(row=28, column=3)


label29 = Label(root, text='Cilindro 11')
label29.grid(row=24, column=4, padx=5, pady=5, sticky=NSEW)
cil_11_entry = Entry(root, width = 10)
cil_11_entry.grid(row=24, column=6)

label30 = Label(root, text='Cilindro 12')
label30.grid(row=25, column=4, padx=5, pady=5, sticky=NSEW)
cil_12_entry = Entry(root, width = 10)
cil_12_entry.grid(row=25, column=6)

label31 = Label(root, text='Cilindro 13')
label31.grid(row=26, column=4, padx=5, pady=5, sticky=NSEW)
cil_13_entry = Entry(root, width = 10)
cil_13_entry.grid(row=26, column=6)

label32 = Label(root, text='Cilindro 14')
label32.grid(row=27, column=4, padx=5, pady=5, sticky=NSEW)
cil_14_entry = Entry(root, width = 10)
cil_14_entry.grid(row=27, column=6)

label33 = Label(root, text='Cilindro 15')
label33.grid(row=28, column=4, padx=5, pady=5, sticky=NSEW)
cil_15_entry = Entry(root, width = 10)
cil_15_entry.grid(row=28, column=6)


label34 = Label(root, text='Cilindro 16')
label34.grid(row=24, column=7, padx=5, pady=5, sticky=NSEW)
cil_16_entry = Entry(root, width = 10)
cil_16_entry.grid(row=24, column=8)

label35 = Label(root, text='Cilindro 17')
label35.grid(row=25, column=7, padx=5, pady=5, sticky=NSEW)
cil_17_entry = Entry(root, width = 10)
cil_17_entry.grid(row=25, column=8)

label36 = Label(root, text='Cilindro 18')
label36.grid(row=26, column=7, padx=5, pady=5, sticky=NSEW)
cil_18_entry = Entry(root, width = 10)
cil_18_entry.grid(row=26, column=8)

label37 = Label(root, text='Cilindro 19')
label37.grid(row=27, column=7, padx=5, pady=5, sticky=NSEW)
cil_19_entry = Entry(root, width = 10)
cil_19_entry.grid(row=27, column=8)

label38 = Label(root, text='Cilindro 20')
label38.grid(row=28, column=7, padx=5, pady=5, sticky=NSEW)
cil_20_entry = Entry(root, width = 10)
cil_20_entry.grid(row=28, column=8)

label39 = Label(root, text='Dados do Gás')
label39.grid(row=29, column=0, padx=5, pady=5, sticky=NSEW)

label40 = Label(root, text='Vazão de gás')
label40.grid(row=30, column=0, padx=5, pady=5, sticky=NSEW)
vaz_entry = Entry(root, width = 10)
vaz_entry.grid(row=30, column=1)

label41 = Label(root, text='Teor de metano')
label41.grid(row=30, column=2, padx=5, pady=5, sticky=NSEW)
met_entry = Entry(root, width = 10)
met_entry.grid(row=30, column=3)

label42 = Label(root, text='Nível de H2s')
label42.grid(row=30, column=5, padx=5, pady=5, sticky=NSEW)
h2s_entry = Entry(root, width = 10)
h2s_entry.grid(row=30, column=6)

label43 = Label(root, text='Teor de Oxigênio')
label43.grid(row=30, column=7, padx=5, pady=5, sticky=NSEW)
oxi_entry = Entry(root, width = 10)
oxi_entry.grid(row=30, column=8)

#dados do chiller

label44 = Label(root, text='Dados do chiller')
label44.grid(row=33, column=0, padx=5, pady=5, sticky=NSEW)

label45 = Label(root, text='Primeiro estágio')
label45.grid(row=34, column=0, padx=5, pady=5, sticky=NSEW)
chiller1_entry = Entry(root, width = 10)
chiller1_entry.grid(row=34, column=1)

label46 = Label(root, text='Segundo estágio')
label46.grid(row=34, column=2, padx=5, pady=5, sticky=NSEW)
chiller2_entry = Entry(root, width = 10)
chiller2_entry.grid(row=34, column=3)

label47 = Label(root, text='Terceiro estágio')
label47.grid(row=34, column=5, padx=5, pady=5, sticky=NSEW)
chiller3_entry = Entry(root, width = 10)
chiller3_entry.grid(row=34, column=6)

label48 = Label(root, text='Quarto estágio')
label48.grid(row=34, column=7, padx=5, pady=5, sticky=NSEW)
chiller4_entry = Entry(root, width = 10)
chiller4_entry.grid(row=34, column=8)

#nível de óleo

noillabel= Label(root, text='Nível de óleo' )
noillabel.grid(row=8, column=3, padx=5, pady=5, sticky=NSEW)
noil_entry = Entry(root, width = 10)
noil_entry.grid(row=8, column=4)



#bobina do trafo

label49 = Label(root, text='Temperatura do Trafo')
label49.grid(row=11, column=3, padx=5, pady=5, sticky=NSEW)


label50 = Label(root, text='Bobina 1')
label50.grid(row=12, column=3, padx=5, pady=5, sticky=NSEW)
bobina1_entry = Entry(root, width = 10)
bobina1_entry.grid(row=12, column=4)

label51 = Label(root, text='Bobina 2')
label51.grid(row=12, column=6, padx=5, pady=5, sticky=NSEW)
bobina2_entry = Entry(root, width = 10)
bobina2_entry.grid(row=12, column=7)

label52 = Label(root, text='Bobina 3')
label52.grid(row=12, column=9, padx=5, pady=5, sticky=NSEW)
bobina3_entry = Entry(root, width = 10)
bobina3_entry.grid(row=12, column=10)

label53 = Label(root, text='Dados cabine de média tensão')
label53.grid(row=15, column=3, padx=5, pady=5, sticky=NSEW)



label54 = Label(root, text='Tensão')
label54.grid(row=16, column=3, padx=5, pady=5, sticky=NSEW)
kv_entry = Entry(root, width = 10)
kv_entry.grid(row=16, column=4)

label55 = Label(root, text='Corrente')
label55.grid(row=16, column=6, padx=5, pady=5, sticky=NSEW)
amp_entry = Entry(root, width = 10)
amp_entry.grid(row=16, column=7)

label56 = Label(root, text='Energia exportada')
label56.grid(row=16, column=9, padx=5, pady=5, sticky=NSEW)
exp_entry = Entry(root, width = 10)
exp_entry.grid(row=16, column=10)












#botão imprimir pdf

class Relatorios():
    def printPdf(self):
        webbrowser.open('relatorio_diário')


def geraRelatorio():

        combo = combo_entry.get()
        combo2 = combo2_entry.get()
        calendario = calendario_entry
        
        c = canvas.Canvas('Relatório diário' ' ' + combo + ' ' + calendario + '.pdf')

        hora = hora_entry.get()
        gerador = combo_entry.get()
        arranque = arranque_entry.get()
        itron = itron_entry.get()
        diane = diane_entry.get()
        potat = potat_entry.get()
        potap = potap_entry.get()

        tbat = tbat_entry.get()

        tmist = tmist_entry.get()
        pcarga = pcarga_entry.get()
        gasmixer = gasmixer_entry.get()
        mariposa = mariposa_entry.get()
        bypass = bypass_entry.get()
        toil = toil_entry.get()
        poil = poil_entry.get()
        twat = twat_entry.get()
        pwat = pwat_entry.get()
        noil = noil_entry.get()

        #cilindros

        cil1 = cil_1_entry.get()
        cil2 = cil_2_entry.get()
        cil3 = cil_3_entry.get()
        cil4 = cil_4_entry.get()
        cil5 = cil_5_entry.get()
        cil6 = cil_6_entry.get()
        cil7 = cil_7_entry.get()
        cil8 = cil_8_entry.get()
        cil9 = cil_9_entry.get()
        cil10 = cil_10_entry.get()
        cil11 = cil_11_entry.get()
        cil12 = cil_12_entry.get()
        cil13 = cil_13_entry.get()
        cil14 = cil_14_entry.get()
        cil15 = cil_15_entry.get()
        cil16 = cil_16_entry.get()
        cil17 = cil_17_entry.get()
        cil18 = cil_18_entry.get()
        cil19 = cil_19_entry.get()
        cil20 = cil_20_entry.get()

        #dados do gas

        vaz = vaz_entry.get()
        met = met_entry.get()
        h2s = h2s_entry.get()
        oxi = oxi_entry.get()

        #dados do chiller

        chiller1 = chiller1_entry.get()
        chiller2 = chiller2_entry.get()
        chiller3 = chiller3_entry.get()
        chiller4 = chiller4_entry.get()


        # controle nível de óleo

        noil = noil_entry.get()

        #temperatura bobina do trafo

        bobina1 = bobina1_entry.get()
        bobina2 = bobina2_entry.get()
        bobina3 = bobina3_entry.get()

        #Dados cabina de média tensão

        kv = kv_entry.get()
        amp = amp_entry.get()
        exp = exp_entry.get()







    


        #cabeçalho

        c.setFont('Helvetica', 18)
        c.drawString(30, 780, 'Relatório diário posição em ' + calendario )
        

       
        c.setFont('Helvetica', 10)
        c.drawString(30, 730, 'Gerador:')
        c.drawString(330, 730, gerador)
        c.drawString(30, 715,  'Data')
        c.drawString(220, 715, 'dd-mm-yyyy')
        c.drawString(330, 715, calendario)
        c.drawString(30, 700,  'Hora')
        c.drawString(220, 700, 'hh:mm')
        c.drawString(330, 700, '{}'.format(h1))







        c.drawString(30, 685, 'Horas de operação:')
        c.drawString(220, 685, 'horas')
        c.drawString(330, 685, hora)
        c.drawString(30, 670, 'Número de arranques:')
        c.drawString(220, 670, 'Qtd')
        c.drawString(330, 670, arranque)
        c.drawString(30, 655, 'Energia produzida Itron:')
        c.drawString(220, 655, 'KWh')
        c.drawString(330, 655, itron)
        c.drawString(30, 640, 'Energia produzida Diane:')
        c.drawString(220, 640, 'MWh')
        c.drawString(330, 640, diane)

        c.drawString(30, 625, 'Potência ativa:')
        c.drawString(220, 625, 'KW')
        c.drawString(330, 625, potat)
        c.drawString(30, 610, 'Potência aparente:')
        c.drawString(220, 610, 'Kva')
        c.drawString(330, 610, potap)






        c.drawString(30, 595, 'Tensão das baterias:')
        c.drawString(220, 595, 'Vcc')
        c.drawString(330, 595, tbat)



        c.setFont('Helvetica', 12)
        c.drawString(30, 570, 'Dados de Leanox')

        c.setFont('Helvetica', 10)

        c.drawString(30, 545, 'Temperatura da mistura:')
        c.drawString(220, 545, 'ºC')
        c.drawString(330, 545, tmist)

        c.drawString(30, 530, 'Pressão de carga:')
        c.drawString(220, 530, 'Bar')
        c.drawString(330, 530, pcarga)

        c.drawString(30, 515, 'Posição do gás mixer:')
        c.drawString(220, 515, '%')
        c.drawString(330, 515, gasmixer)

        c.drawString(30, 500, 'Posição da válvula borboleta:')
        c.drawString(220, 500, '%')
        c.drawString(330, 500, mariposa)

        c.drawString(30, 485, 'Posição do bypass:')
        c.drawString(220, 485, '%')
        c.drawString(330, 485, bypass)

        c.drawString(30, 470, 'Temperatura de óleo:')
        c.drawString(220, 470, 'ºC')
        c.drawString(330, 470, toil)

        c.drawString(30, 455, 'Pressão de óleo:')
        c.drawString(220, 455, 'Bar')
        c.drawString(330, 455, poil)

        c.drawString(30, 440, 'Temperatura de água:')
        c.drawString(220, 440, 'ºC')
        c.drawString(330, 440, twat)

        c.drawString(30, 425, 'Pressão de água:')
        c.drawString(220, 425, 'Bar')
        c.drawString(330, 425, pwat)

        c.drawString(30, 410, 'Amostra de óleo coletada:')
        c.drawString(220, 410, 'S/N')
        c.drawString(330, 410, combo2)

        c.setFont('Helvetica', 12)
        c.drawString(30, 385, 'Temperatura de cilindros')
        c.setFont('Helvetica', 10)

        c.drawString(30, 360, 'Cilindro 1')
        c.drawString(90, 360, 'ºC')
        c.drawString(122, 360, cil1)

        c.drawString(30, 345, 'Cilindro 2')
        c.drawString(90, 345, 'ºC')
        c.drawString(122, 345, cil2)

        c.drawString(30, 330, 'Cilindro 3')
        c.drawString(90, 330, 'ºC')
        c.drawString(122, 330, cil3)

        c.drawString(30, 315, 'Cilindro 4')
        c.drawString(90, 315, 'ºC')
        c.drawString(122, 315, cil4)

        c.drawString(30, 300, 'Cilindro 5')
        c.drawString(90, 300, 'ºC')
        c.drawString(122, 300, cil5)

        c.drawString(180, 360, 'Cilindro 6')
        c.drawString(240, 360, 'ºC')
        c.drawString(272, 360, cil6)

        c.drawString(180, 345, 'Cilindro 7')
        c.drawString(240, 345, 'ºC')
        c.drawString(272, 345, cil7)

        c.drawString(180, 330, 'Cilindro 8')
        c.drawString(240, 330, 'ºC')
        c.drawString(272, 330, cil8)

        c.drawString(180, 315, 'Cilindro 9')
        c.drawString(240, 315, 'ºC')
        c.drawString(272, 315, cil9)

        c.drawString(180, 300, 'Cilindro 10')
        c.drawString(240, 300, 'ºC')
        c.drawString(272, 300, cil10)

        c.drawString(330, 360, 'Cilindro 11')
        c.drawString(390, 360, 'ºC')
        c.drawString(422, 360, cil11)

        c.drawString(330, 345, 'Cilindro 12')
        c.drawString(390, 345, 'ºC')
        c.drawString(422, 345, cil12)

        c.drawString(330, 330, 'Cilindro 13')
        c.drawString(390, 330, 'ºC')
        c.drawString(422, 330, cil13)

        c.drawString(330, 315, 'Cilindro 14')
        c.drawString(390, 315, 'ºC')
        c.drawString(422, 315, cil14)

        c.drawString(330, 300, 'Cilindro 15')
        c.drawString(390, 300, 'ºC')
        c.drawString(422, 300, cil15)

        c.drawString(480, 360, 'Cilindro 16')
        c.drawString(540, 360, 'ºC')
        c.drawString(572, 360, cil16)

        c.drawString(480, 345, 'Cilindro 17')
        c.drawString(540, 345, 'ºC')
        c.drawString(572, 345, cil17)

        c.drawString(480, 330, 'Cilindro 18')
        c.drawString(540, 330, 'ºC')
        c.drawString(572, 330, cil18)

        c.drawString(480, 315, 'Cilindro 19')
        c.drawString(540, 315, 'ºC')
        c.drawString(572, 315, cil19)

        c.drawString(480, 300, 'Cilindro 20')
        c.drawString(540, 300, 'ºC')
        c.drawString(572, 300, cil20)

        c.setFont('Helvetica', 12)
        c.drawString(30, 275, 'Dados do gás')
        c.setFont('Helvetica', 10)

        c.drawString(30, 250, 'Vazão de gás')
        c.drawString(220, 250, 'Nm³')
        c.drawString(330, 250, vaz)

        c.drawString(30, 235, 'Teor de metano')
        c.drawString(220, 235, '%')
        c.drawString(330, 235, met)

        c.drawString(30, 220, 'Nível de H2s')
        c.drawString(220, 220, 'ppm')
        c.drawString(330, 220, h2s)

        c.drawString(30, 205, 'Nível de oxigênio')
        c.drawString(220, 205, '%')
        c.drawString(330, 205, oxi)

        c.setFont('Helvetica', 12)
        c.drawString(30, 180, 'Dados do chiller')
        c.setFont('Helvetica', 10)

        c.drawString(30, 155, 'Temperatura primeiro estágio')
        c.drawString(200, 155, 'ºC')
        c.drawString(240, 155, chiller1)

        c.drawString(30, 140, 'Temperatura segundo estágio')
        c.drawString(200, 140, 'ºC')
        c.drawString(240, 140, chiller2)

        c.drawString(310, 155, 'Temperatura terceiro estágio')
        c.drawString(440, 155, 'ºC')
        c.drawString(480, 155, chiller3)

        c.drawString(310, 140, 'Temperatura quarto estágio')
        c.drawString(440, 140, 'ºC')
        c.drawString(480, 140, chiller4)

        c.setFont('Helvetica', 11)
        c.drawString(30, 115, 'Temperatura bobina do trafo')
        c.setFont('Helvetica', 10)

        c.drawString(30, 90, 'Bobina 1')
        c.drawString(100, 90, 'ºC' )
        c.drawString(140, 90, bobina1)

        c.drawString(30, 75, 'Bobina 2')
        c.drawString(100, 75, 'ºC' )
        c.drawString(140, 75, bobina2)

        c.drawString(30, 60, 'Bobina 3')
        c.drawString(100, 60, 'ºC' )
        c.drawString(140, 60, bobina3)

        c.setFont('Helvetica', 11)
        c.drawString(310, 115, 'Dados cabine média tensão')
        c.setFont('Helvetica', 10)

        c.drawString(310, 90, 'Tensão')
        c.drawString(400, 90, 'KV' )
        c.drawString(440, 90, kv)

        c.drawString(310, 75, 'Corrente')
        c.drawString(400, 75, 'A' )
        c.drawString(440, 75, amp)

        c.drawString(310, 60, 'Energia exportada')
        c.drawString(400, 60, 'MWh' )
        c.drawString(440, 60, exp)

        c.drawString(460, 410, 'Nível de óleo')
        c.drawString(540, 410, 'cm' )
        c.drawString(572, 410, noil)
















        c.showPage()
        c.save()
       

mybutton = Button(root, text='Gerar Pdf!', command=geraRelatorio)
mybutton.grid(row=4, column=5)


mybutton2 = Button(root, text='Limpar tela!', command=limpa_tela)
mybutton2.grid(row=6, column=5)

        






root.mainloop()
