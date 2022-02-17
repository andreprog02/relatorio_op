import streamlit as st
from datetime import date
from streamlit import caching



from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

cnv = canvas.Canvas("Meu_pdf.pdf")
cnv.save()




st.header('Relatório diário')


ger = st.selectbox('Escolha um gerador', ['BM1', 'BM2'])
chb = st.checkbox('Gerador em operação?')
dat = st.date_input('Data:')
dat_obj = dat.strftime('%d_%m_%Y')
dat_for = dat.strftime('%d-%m-%Y')
#st.write(dat.strftime("%d/%m/%Y"))
h = st.time_input('Hora')
h1 = h.strftime('%H:%M')
st.subheader('Dados do gerador')
horas_op = st.text_input('Horas de operação:', value=0)
arr = st.text_input('Numeros de arranques:', value=0)
if chb:
    potat = st.number_input('Potência ativa:', max_value= 1060, min_value= 528, value=900)
    potav = st.number_input('Potência aparente', value=0)
else:
    potat = 0
    potav = 0
epi = st.text_input('Energia produzida Itron:')
epd = st.text_input('Energia produzida Diane:')
bat = st.text_input('Tensão das baterias:', value=0)



if chb:
    st.subheader('Dados Leanox')
    tmist = st.number_input('Temperatura da mistura:')
    pcar = st.number_input('Pressão de carga:')
    preg = st.number_input('Posição do regulador de gás:')
    pval = st.number_input('Posição da válvula borboleta:')
    pby = st. number_input('Posição do bypass:')
else:
    tmist = 0
    pcar = 0
    preg = 0
    pval = 0
    pby = 0


if chb:
    st.subheader('Água e óleo')
    toil = st.number_input('Temperatura do óleo:', max_value= 85, min_value= 60, value=70)
    poil = st.number_input('Pressao do óleo:', max_value= 4.5, min_value= 3.9, value=4.0)
    twat = st.number_input('Temperatura da água:', max_value= 85, min_value= 60, value=70)
    pwat = st.number_input('Pressao da agua:', max_value= 1.60, min_value= 1.0, value=1.2)


else:
    toil = '-'
    poil = '-'
    twat = '-'
    pwat = '-'

coil = st.selectbox('Amostra de óleo coletada?', ['NÃO', 'SIM'])

if chb:
    st.subheader('Temperatura de cilindros')

    col1, col2, = st.columns(2)

    with col1:

     cil1 = st.number_input('Temperatura cilindro 1', max_value= 650, min_value= 500, value=600)
     cil2 = st.number_input('Temperatura cilindro 2', max_value= 650, min_value= 500, value=600)
     cil3 = st.number_input('Temperatura cilindro 3', max_value= 650, min_value= 500, value=600)
     cil4 = st.number_input('Temperatura cilindro 4', max_value= 650, min_value= 500, value=600)
     cil5 = st.number_input('Temperatura cilindro 5', max_value= 650, min_value= 500, value=600)
     cil6 = st.number_input('Temperatura cilindro 6', max_value= 650, min_value= 500, value=600)
     cil7 = st.number_input('Temperatura cilindro 7', max_value= 650, min_value= 500, value=600)
     cil8 = st.number_input('Temperatura cilindro 8', max_value= 650, min_value= 500, value=600)
     cil9 = st.number_input('Temperatura cilindro 9', max_value= 650, min_value= 500, value=600)
     cil10 = st.number_input('Temperatura cilindro 10', max_value= 650, min_value= 500, value=600)

    with col2:
      cil11 = st.number_input('Temperatura cilindro 11', max_value= 650, min_value= 500, value=600)
      cil12 = st.number_input('Temperatura cilindro 12', max_value= 650, min_value= 500, value=600)
      cil13 = st.number_input('Temperatura cilindro 13', max_value= 650, min_value= 500, value=600)
      cil14 = st.number_input('Temperatura cilindro 14', max_value= 650, min_value= 500, value=600)
      cil15 = st.number_input('Temperatura cilindro 15', max_value= 650, min_value= 500, value=600)
      cil16 = st.number_input('Temperatura cilindro 16', max_value= 650, min_value= 500, value=600)
      cil17 = st.number_input('Temperatura cilindro 17', max_value= 650, min_value= 500, value=600)
      cil18 = st.number_input('Temperatura cilindro 18', max_value= 650, min_value= 500, value=600)
      cil19 = st.number_input('Temperatura cilindro 19', max_value= 650, min_value= 500, value=600)
      cil20 = st.number_input('Temperatura cilindro 20', max_value= 650, min_value= 500, value=600)

else:
    st.write('Valores cilindros igual a 0')

    cil1 = '-'
    cil2 = '-'
    cil3 = '-'
    cil4 = '-'
    cil5 = '-'
    cil6 = '-'
    cil7 = '-'
    cil8 = '-'
    cil9 = '-'
    cil10 = '-'
    cil11 = '-'
    cil12 = '-'
    cil13 = '-'
    cil14 = '-'
    cil15 = '-'
    cil16 = '-'
    cil17 = '-'
    cil18 = '-'
    cil19 = '-'
    cil20 = '-'







st.subheader('Dados do gás')

if chb:
    vaz = st.text_input('Vazão de gás:', value=0)
else:
    vaz = 0
ch4 = st.text_input('Teor de metano:')
h2s = st.text_input('Teor de H2S:')
o2 = st.slider('Teor de oxigênio', max_value= 3.5, min_value= 0.0, value=1.5, step=0.1)

st.subheader('Dados do chiller')
if chb:
    ch1 = st.number_input('Temperatura primeiro estágio:', max_value = 65, min_value = 20, value = 40, step=1)
    ch2 = st.number_input('Temperatura segundo estágio:', max_value = 30, min_value = 10, value = 20, step=1)
    ch3 = st.number_input('Temperatura terceiro estágio:', max_value = 65, min_value = 40, value = 50, step=1)
    chi4 = st.number_input('Temperatura quarto estágio:', max_value = 40, min_value = 25, value = 30, step=1)
else:
    ch1 = 'NA'
    ch2 = 'NA'
    ch3 = 'NA'
    chi4 = 'NA'


st.subheader('Temperatura bobinas do transformador')

bob1 = st.slider('Temperatura bobina 1', max_value= 50, min_value= 0, value=25)
bob2 = st.slider('Temperatura bobina 2', max_value= 50, min_value= 0, value=25)
bob3 = st.slider('Temperatura bobina 3', max_value= 50, min_value= 0, value=25)

st.subheader('Dados cabine média tensão')

tm = st.slider('Tensao de media:', max_value= 14.2, min_value= 13.0, value=13.8, step=0.1)

if chb:
    com = st.slider('Corrente de média:', max_value= 50, min_value= 5, value=25, step=1)
else:
    com = 0
exp = st.text_input('Energia exportada:')

imp = st.button('Gerar PDF')



if imp:




    cnv = canvas.Canvas("Relatório diário {}_{}.pdf".format(ger,dat_for))
    cnv = canvas.Canvas("/home/i/Downloads/Relatorios/relatorio_diario/Relatório diário {}_{}.pdf".format(ger, dat_obj))


    cnv.drawString(50,800, 'Relatório diário {}'.format(dat_for))
    cnv.drawString(200, 800, '{}'.format(ger))
    cnv.drawString(50, 750, 'Gerador')
    cnv.drawString(310, 750, '{}'.format(ger))
    cnv.drawString(50, 735, 'Data')
    cnv.drawString(310, 735, '{}'.format(dat_for))
    cnv.drawString(220,735, 'dd-mm-yyyy')
    cnv.drawString(50, 720, 'Hora')
    cnv.drawString(220, 720, 'hh:mm')
    cnv.drawString(310, 720, '{}'.format(h1))
    cnv.drawString(50, 705, 'Horas de operação')
    cnv.drawString(220, 705, 'horas')
    cnv.drawString(310, 705, '{}'.format(horas_op))
    cnv.drawString(50, 690, 'Número de arranques')
    cnv.drawString(220,690, "Qtd")
    cnv.drawString(310, 690,'{}'.format(arr))
    cnv.drawString(50, 675, 'Potência ativa')
    cnv.drawString(220, 675, 'Kw')
    cnv.drawString(310, 675, '{}'.format(potat))
    cnv.drawString(50, 660, 'Potência aparente')
    cnv.drawString(220, 660, 'Kva')
    cnv.drawString(310, 660, '{}'.format(potav))
    cnv.drawString(50, 645, 'Energia prodruzida itron')
    cnv.drawString(220, 645, 'KWh')
    cnv.drawString(310, 645, '{}'.format(epi))
    cnv.drawString(50, 630, 'Energia produzida diane')
    cnv.drawString(220,630, 'MWh')
    cnv.drawString(310, 630, '{}'.format(epd))
    cnv.drawString(50, 615, 'Tensão das baterias')
    cnv.drawString(220,615,"Vcc")
    cnv.drawString(310,615,'{}'.format(bat))
    cnv.drawString(50, 600, 'Temperatura da mistura')
    cnv.drawString(220, 600, 'ºC')
    cnv.drawString(310, 600,'{}'.format(tmist))
    cnv.drawString(50, 585, 'Pressão de carga')
    cnv.drawString(220,585,'Bar')
    cnv.drawString(310,585,'{}'.format(pcar))
    cnv.drawString(50, 570, 'Posição regulador de gás')
    cnv.drawString(220,570,'%')
    cnv.drawString(310, 570, '{}'.format(preg))
    cnv.drawString(50, 555, 'Posição válvula borboleta')
    cnv.drawString(220, 555, '%')
    cnv.drawString(310, 555, '{}'.format(preg))
    cnv.drawString(50, 540, 'Posição bypass')
    cnv.drawString(220, 540, '%')
    cnv.drawString(310, 540, '{}'.format(pby))
    cnv.drawString(50,525,'Temperatura do óleo')
    cnv.drawString(220, 525, 'ºC')
    cnv.drawString(310, 525, '{}'.format(toil))
    cnv.drawString(50, 510, 'Pressão do óleo')
    cnv.drawString(220, 510, 'Bar')
    cnv.drawString(310, 510, '{}'.format(poil))
    cnv.drawString(50, 495, 'Temperatura da água')
    cnv.drawString(220, 495, 'ºC')
    cnv.drawString(310, 495, '{}'.format(twat))
    cnv.drawString(50, 480, 'Pressão da água')
    cnv.drawString(220, 480, 'Bar')
    cnv.drawString(310, 480, '{}'.format(pwat))
    cnv.drawString(50, 465, 'Amostra de óleo coletada?')
    cnv.drawString(220, 465,'S/N')
    cnv.drawString(310,465,'{}'.format(coil))
    cnv.drawString(200,430,'Temperatura gases de cilindro')
    cnv.drawString(50, 400, 'Cilindro 01')
    cnv.drawString(115, 400, 'ºC')
    cnv.drawString(135,400,'{}'.format(cil1))
    cnv.drawString(50, 385, 'Cilindro 02')
    cnv.drawString(115, 385, 'ºC')
    cnv.drawString(135, 385, '{}'.format(cil2))
    cnv.drawString(50, 370, 'Cilindro 03')
    cnv.drawString(115, 370, 'ºC')
    cnv.drawString(135, 370, '{}'.format(cil3))
    cnv.drawString(50, 355, 'Cilindro 04')
    cnv.drawString(115, 355, 'ºC')
    cnv.drawString(135, 355, '{}'.format(cil4))
    cnv.drawString(50, 340, 'Cilindro 05')
    cnv.drawString(115, 340, 'ºC')
    cnv.drawString(135, 340, '{}'.format(cil5))
    cnv.drawString(190, 400, 'Cilindro 06')
    cnv.drawString(255, 400, 'ºC')
    cnv.drawString(275, 400, '{}'.format(cil6))
    cnv.drawString(190, 385, 'Cilindro 07')
    cnv.drawString(255, 385, 'ºC')
    cnv.drawString(275, 385, '{}'.format(cil7))
    cnv.drawString(190, 370, 'Cilindro 08')
    cnv.drawString(255, 370, 'ºC')
    cnv.drawString(275, 370, '{}'.format(cil8))
    cnv.drawString(190, 355, 'Cilindro 09')
    cnv.drawString(255, 355, 'ºC')
    cnv.drawString(275, 355, '{}'.format(cil9))
    cnv.drawString(190, 340, 'Cilindro 10')
    cnv.drawString(255, 340, 'ºC')
    cnv.drawString(275, 340, '{}'.format(cil10))
    cnv.drawString(335, 400, 'Cilindro 11')
    cnv.drawString(400, 400, 'ºC')
    cnv.drawString(420, 400, '{}'.format(cil11))
    cnv.drawString(335, 385, 'Cilindro 12')
    cnv.drawString(400, 385, 'ºC')
    cnv.drawString(420, 385, '{}'.format(cil12))
    cnv.drawString(335, 370, 'Cilindro 13')
    cnv.drawString(400, 370, 'ºC')
    cnv.drawString(420, 370, '{}'.format(cil13))
    cnv.drawString(335, 355, 'Cilindro 14')
    cnv.drawString(400, 355, 'ºC')
    cnv.drawString(420, 355, '{}'.format(cil14))
    cnv.drawString(335, 340, 'Cilindro 15')
    cnv.drawString(400, 340, 'ºC')
    cnv.drawString(420, 340, '{}'.format(cil15))
    cnv.drawString(470, 400, 'Cilindro 16')
    cnv.drawString(535, 400, 'ºC')
    cnv.drawString(555, 400, '{}'.format(cil16))
    cnv.drawString(470, 385, 'Cilindro 17')
    cnv.drawString(535, 385, 'ºC')
    cnv.drawString(555, 385, '{}'.format(cil17))
    cnv.drawString(470, 370, 'Cilindro 18')
    cnv.drawString(535, 370, 'ºC')
    cnv.drawString(555, 370, '{}'.format(cil18))
    cnv.drawString(470, 355, 'Cilindro 19')
    cnv.drawString(535, 355, 'ºC')
    cnv.drawString(555, 355, '{}'.format(cil19))
    cnv.drawString(470, 340, 'Cilindro 20')
    cnv.drawString(535, 340, 'ºC')
    cnv.drawString(555, 340, '{}'.format(cil20))
    cnv.drawString(50,310,'Dados do gás')
    cnv.drawString(50, 290, 'Vazão de gás')
    cnv.drawString(220, 290, 'Nm³')
    cnv.drawString(310,290,'{}'.format(vaz))
    cnv.drawString(50, 275, 'Teor de metano')
    cnv.drawString(220,275,'%')
    cnv.drawString(310,275,'{}'.format(ch4))
    cnv.drawString(50, 260, 'Nível de H2s')
    cnv.drawString(220, 260, 'ppm')
    cnv.drawString(310, 260, '{}'.format(h2s))
    cnv.drawString(50, 245, 'Teor de oxigênio')
    cnv.drawString(220, 245, '%')
    cnv.drawString(310, 245, '{}'.format(o2))
  #  cnv.drawString(50, 170, 'Teor de H2s: {} ppm'.format(h2s))
  #  cnv.drawString(50, 155, 'Teor de oxigênio: {} %'.format(o2))
    cnv.drawString(50, 220, 'Dados do chiller')
    cnv.drawString(50, 200, 'Temperatura primeiro estágio')
    cnv.drawString(220, 200, 'ºC')
    cnv.drawString(310, 200, '{}'.format(ch1))
    cnv.drawString(50, 185, 'Temperatura segundo estágio')
    cnv.drawString(220, 185, 'ºC')
    cnv.drawString(310, 185, '{}'.format(ch2))
    cnv.drawString(50, 170, 'Temperatura terceiro estágio')
    cnv.drawString(220, 170, 'ºC')
    cnv.drawString(310, 170, '{}'.format(ch3))
    cnv.drawString(50, 155, 'Temperatura quarto estágio')
    cnv.drawString(220, 155, 'ºC')
    cnv.drawString(310, 155, '{}'.format(chi4))
    cnv.drawString(50, 120, 'Temperaturas bobina do trafo')
    cnv.drawString(50, 100, 'Temperatura bobina 1')
    cnv.drawString(180, 100, 'ºC')
    cnv.drawString(205, 100, '{}'.format(bob1))
    cnv.drawString(50, 85, 'Temperatura bobina 2')
    cnv.drawString(180, 85, 'ºC')
    cnv.drawString(205, 85, '{}'.format(bob2))
    cnv.drawString(50, 70, 'Temperatura bobina 3')
    cnv.drawString(180, 70, 'ºC')
    cnv.drawString(205, 70, '{}'.format(bob3))
    cnv.drawString(320, 120,'Dados cabine média tensão')
    cnv.drawString(320, 100, 'Tensão em média')
    cnv.drawString(430, 100, 'KV')
    cnv.drawString(465, 100, '{}'.format(tm))
    cnv.drawString(320, 85, 'Corrente em média')
    cnv.drawString(430, 85, 'A')
    cnv.drawString(465, 85, '{}'.format(com))
    cnv.drawString(320, 70, 'Energia exportada')
    cnv.drawString(430, 70, 'MWh')
    cnv.drawString(465, 70, '{}'.format(exp))
  #  cnv.drawString(50, 20, 'Corrente de média: {} A'.format(com))
  #  cnv.drawString(50, 5, 'Energia exportada: {} MWh'.format(exp))
    cnv.save()

