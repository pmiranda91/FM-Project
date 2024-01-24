import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd

pasta_datasets = Path(__file__).parent.parent/'assets'
caminho_CPT = pasta_datasets/'CPT - MATRIZ.csv'
df_CPT = pd.read_csv(caminho_CPT,decimal=',',sep=';',index_col=0)

lista_atividades = ['Atividade 1','Atividade 2','Atividade 3','Atividade 4','Atividade 5','Atividade 6','Atividade 7','Atividade 8','Atividade 9']
lista_valores = ['Espírito de Equipe','Respeito','Comprometimento','Coragem','Confiança']
cat_ativ = ['Futebol de Rua', 'Atividade Técnica', 'Pequeno Jogo', 'Grande Jogo', 'Jogo Formal', 'Atividade Complementar']
atv_comp = ['Vazio','Psicologia', 'Fisiologia', 'Academia', 'Vídeo', 'Palestra','Aquecimento Dinâmico', 'Preventivo']
carac_at = ['Vazio','Recuperação', 'Quantidade', 'Regularidade','Rapidez','Revisão', 'Avaliação','Competição']
categorias =['SUB 20','SUB 20-B','SUB 17','SUB 16','SUB 15','SUB 14','SUB 13','SUB 12','SUB 11','SUB 10','SUB 09']
meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
dias_semana = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo']

st.set_page_config(
    layout="wide"
)

selected = option_menu(
    menu_title="CPT - Controle Pedagógico do Treinamento",
    options=["Planejamento","Preparação","Microciclo","Controle","Individual"],
    default_index=0,
    orientation='horizontal',
)

cat = st.sidebar.selectbox("**Escolha sua categoria:**",categorias)

if selected == "Planejamento":
    tab1, tab2 = st.tabs(['Adicionar','Editar'])
    with tab1:
        jogajunto = False
        movimenta = False
        ritmo = False
        agressividade = False
        qualidade = False
        marcajunto = False
        pressiona = False
        correpratras = False
        protegeogol = False
        comunicacao = False
        escanteio = False
        faltadir = False
        faltaind = False
        penalti = False
        lateral = False
        col1,col2 = st.columns(2)
        data_selec = col1.date_input('**Inserir data:**',datetime.today(),format='DD/MM/YYYY')
        data_selec2 = data_selec.strftime('%d/%m/%Y')
        ativ_selec = col2.selectbox('**Escolha a atividade:**',lista_atividades)
        col3,col5 = st.columns(2)
        inserir = col3.button(':heavy_plus_sign:',use_container_width=True)
        excluir = col5.button(':wastebasket:',use_container_width=True)
        st.write('**Escolha os valores:**')
        col6,col7,col8,col9,col10 = st.columns(5)
        esp_selec = col6.checkbox('Espírito de Equipe')
        resp_selec = col7.checkbox('Respeito')
        comp_selec = col8.checkbox('Comprometimento')
        cora_selec = col9.checkbox('Coragem')
        conf_selec = col10.checkbox('Confiança')
        col11,col12,col13,col14 = st.columns(4)
        princ_selec = col11.write('**Escolha os Prícipios de Jogo:**')
        col12.write('**Escolha os sub-princípios:**')
        col13.write('_')
        col14.write('_')
        posse = col11.checkbox('Posse')
        vai_dentro = col11.checkbox('Vai Dentro')
        reage = col11.checkbox('Reage')
        organiza = col11.checkbox('Organiza')
        bpof = col11.checkbox('Bola Parada Ofensiva')
        bpdef = col11.checkbox('Bola Parada Defensiva')
        
        if posse or vai_dentro:
                jogajunto = col12.checkbox("Joga Junto")
                movimenta = col12.checkbox("Movimenta")
                ritmo = col12.checkbox("Ritmo")
                agressividade = col12.checkbox("Agressividade")
                qualidade = col12.checkbox("Qualidade")
        if reage or organiza:
                marcajunto = col13.checkbox("Marca Junto")
                pressiona = col13.checkbox("Pressiona")
                correpratras = col13.checkbox("Corre pra trás")
                protegeogol = col13.checkbox("Protege o Gol")
                comunicacao = col13.checkbox("Comunicação")
        if bpof or bpdef:
                escanteio = col14.checkbox("Escanteio")
                faltaind = col14.checkbox("Falta Indireta")
                faltadir = col14.checkbox("Falta Direta")
                penalti = col14.checkbox("Penalti")
                lateral = col14.checkbox("Lateral")
        
        col15,col16,col17 = st.columns(3)
        cat_atv = col15.selectbox("**Escolha a categoria da atividade:**",cat_ativ)

        if cat_atv == 'Atividade Complementar':
                ativ_comp = col17.selectbox("**Escolha a atividade complementar:**",atv_comp)
        else:    
                carac_ativ = col16.selectbox("**Escolha a característica da Sessão**",carac_at)
        
        st.divider()

        nome_at = st.text_input("**Nome da Atividade:**")
        desc_at = st.text_area('**Descrição da Atividade:**')

        col18,col19 = st.columns(2)
        largura = col18.text_input('**Largura:**')
        comprimento = col19.text_input('**Comprimento:**')

        st.divider()
        col20,col21,col22,col23 = st.columns(4)
        est = col20.number_input("**Estímulo:**",step=0.5,min_value=0.0)
        rec = col21.number_input("**Recuperação:**",step=0.5,min_value=0.0)
        rep = col22.number_input("**Repetições:**",step=1,min_value=0)
        voltot = est*rep+rec*(rep-1)
        col23.write("**Volume Total:**")
        col23.write(str(voltot))
        nota = st.number_input("**Nota:**",step=0.5,max_value=5.0,min_value=0.0)


        if inserir:
                valores=[esp_selec,resp_selec,comp_selec,cora_selec,conf_selec]
                valor=['','','','','']
                valores_final =[]
                if valores[0] == True:
                        valor[0] = 'Espírito de Equipe'
                if valores[1] == True:
                        valor[1] = 'Respeito'
                if valores[2] == True:
                        valor[2] = 'Comprometimento'
                if valores[3] == True:
                        valor[3] = 'Coragem'
                if valores[4] == True:
                        valor[4] = 'Confiança'
                for i in range(len(valor)):
                        if valor[i]!='':
                                valores_final.append(valor[i])
                valores_final = ', '.join(valores_final)
                                
                principios=[posse,vai_dentro,reage,organiza,bpof,bpdef]
                principio=['','','','','','']
                principios_final=[]
                if principios[0] == True:
                        principio[0] = 'Posse'
                if principios[1] == True:
                        principio[1] = 'Vai Dentro'
                if principios[2] == True:
                        principio[2] = 'Reage'
                if principios[3] == True:
                        principio[3] = 'Organiza'
                if principios[4] == True:
                        principio[4] = 'Bola Parada Ofensiva'
                if principios[5] == True:
                        principio[5] = 'Bola Parada Defensiva'
                for i in range(len(principio)):
                        if principio[i]!='':
                                principios_final.append(principio[i])
                principios_final = ', '.join(principios_final)

                comportamentos=[jogajunto,movimenta,ritmo,agressividade,qualidade,marcajunto,pressiona,correpratras,protegeogol,comunicacao,escanteio,faltaind,faltadir,penalti,lateral]
                comportamento=['','','','','','','','','','','','','','','']
                comportamentos_final=[]
                if comportamentos[0] == True:
                        comportamento[0] = 'Joga Junto'
                if comportamentos[1] == True:
                        comportamento[1] = 'Movimenta'
                if comportamentos[2] == True:
                        comportamento[2] = 'Ritmo'
                if comportamentos[3] == True:
                        comportamento[3] = 'Agressividade'
                if comportamentos[4] == True:
                        comportamento[4] = 'Qualidade'
                if comportamentos[5] == True:
                        comportamento[5] = 'Marca Junto'
                if comportamentos[6] == True:
                        comportamento[6] = 'Pressiona'
                if comportamentos[7] == True:
                        comportamento[7] = 'Corre Pra Trás'
                if comportamentos[8] == True:
                        comportamento[8] = 'Protege o Gol'
                if comportamentos[9] == True:
                        comportamento[9] = 'Comunicação'
                if comportamentos[10] == True:
                        comportamento[10] = 'Escanteio'
                if comportamentos[11] == True:
                        comportamento[11] = 'Falta Indireta'
                if comportamentos[12] == True:
                        comportamento[12] = 'Falta Direta'
                if comportamentos[13] == True:
                        comportamento[13] = 'Penalti'
                if comportamentos[14] == True:
                        comportamento[14] = 'Lateral'
                for i in range(len(comportamento)):
                        if comportamento[i]!='':
                                comportamentos_final.append(comportamento[i])
                comportamentos_final = ', '.join(comportamentos_final)

                if cat_atv == 'Atividade Complementar':
                        carac_ativ_final = 'Vazio'
                        ativ_comp_final = ativ_comp
                else:
                        ativ_comp_final = 'Vazio'
                        carac_ativ_final = carac_ativ

                m = meses[data_selec.month-1]
                y = data_selec.year

                lista_adicionar = [cat,data_selec2,m,y,ativ_selec,valores_final, principios_final,comportamentos_final,cat_atv,carac_ativ_final,ativ_comp_final,nome_at,desc_at,largura,comprimento,est,rec,rep,voltot,nota,(nota*voltot)/5]
                df_CPT.loc[(cat+'-'+str(data_selec2)+'-'+ativ_selec)] = lista_adicionar
                df_CPT.to_csv(caminho_CPT,decimal=',',sep=';')
                col3.success("Atividade inserida com sucesso!")

        
        id_remocao = cat+'-'+str(data_selec2)+'-'+ativ_selec
        if excluir:
                if id_remocao not in df_CPT.index:
                        col5.error("Essa atividade ainda não foi inserida!")
                else:
                        df_CPT = df_CPT.drop(labels=id_remocao,axis=0)
                        df_CPT.to_csv(caminho_CPT,decimal=',',sep=';')

        with tab2:
                jogajunto_load = False
                movimenta_load = False
                ritmo_load = False
                agressividade_load = False
                qualidade_load = False
                marcajunto_load = False
                pressiona_load = False
                correpratras_load = False
                protegeogol_load = False
                comunicacao_load = False
                escanteio_load = False
                faltadir_load = False
                faltaind_load = False
                penalti_load = False
                lateral_load = False
                if 'clicked' not in st.session_state:
                        st.session_state.clicked = {1:False,2:False}

                def clicked(button):
                        st.session_state.clicked[button] = True

                
                col24,col25 = st.columns(2)
                data_selec_edit = col24.date_input('**Escolha a data:**',datetime.today(),format='DD/MM/YYYY')
                data_selec2_edit = data_selec_edit.strftime('%d/%m/%Y')
                ativ_selec_edit = col25.selectbox('**Escolha a atividade que deseja carregar:**',lista_atividades)
                id_load = cat+'-'+str(data_selec2_edit)+'-'+ativ_selec_edit
                col26,col27 =  st.columns(2)
                m_edit = meses[data_selec_edit.month-1]
                y_edit = data_selec_edit.year
                carregar = col27.button(":open_file_folder:",use_container_width=True,on_click=clicked,args=[1])
                if st.session_state.clicked[1]:
                        if id_load not in df_CPT.index:
                                valores_final_load = None
                                principios_final_load = None
                                comportamentos_final_load = None
                                cat_ativ_load = None
                                carac_ativ_load = None
                                ativ_comp_load = None
                                nome_at_load = None
                                desc_at_load = None
                                largura_load = None
                                comprimento_load = None
                                est_load = 0.0
                                rec_load = 0.0
                                rep_load = 0
                                voltot_load = 0.0
                                nota_load = 0.0
                                st.error("Essa atividade ainda não foi inserida!")
                        else:
                                st.write('**Valores carregados:**')
                                col27,col28,col29,col30,col31 = st.columns(5)
                                
                                if 'Espírito de Equipe' in str(df_CPT['VALORES'][id_load]):
                                        esp_load = col27.checkbox('Espírito de Equipe ',value=True)
                                else:
                                        esp_load = col27.checkbox('Espírito de Equipe ')
                                if 'Respeito' in str(df_CPT['VALORES'][id_load]):
                                        resp_load = col28.checkbox('Respeito ',value=True)
                                else:
                                        resp_load = col28.checkbox('Respeito ')
                                if 'Comprometimento' in str(df_CPT['VALORES'][id_load]):
                                        comp_load = col29.checkbox('Comprometimento ',value=True)
                                else:
                                        comp_load = col29.checkbox('Comprometimento ')
                                if 'Coragem' in str(df_CPT['VALORES'][id_load]):
                                        cora_load = col30.checkbox('Coragem ',value=True)
                                else:
                                        cora_load = col30.checkbox('Coragem ')
                                if 'Confiança' in str(df_CPT['VALORES'][id_load]):
                                        conf_load = col31.checkbox('Confiança ',value=True)
                                else:
                                        conf_load = col31.checkbox('Confiança ')
                        
                                col32,col33,col34,col35 = st.columns(4)
                                col32.write('**Princípios de Jogo carregados:**')
                                if 'Posse' in str(df_CPT['PRINCIPIOS_DE_JOGO'][id_load]):
                                        posse_load = col32.checkbox('Posse ',value=True)
                                else:
                                        posse_load = col32.checkbox('Posse ')
                                if 'Vai Dentro' in str(df_CPT['PRINCIPIOS_DE_JOGO'][id_load]):
                                        vai_dentro_load = col32.checkbox('Vai Dentro ',value=True)
                                else:
                                        vai_dentro_load = col32.checkbox('Vai Dentro ')
                                if 'Reage' in str(df_CPT['PRINCIPIOS_DE_JOGO'][id_load]):
                                        reage_load = col32.checkbox('Reage ',value=True)
                                else:
                                        reage_load = col32.checkbox('Reage ')
                                if 'Organiza' in str(df_CPT['PRINCIPIOS_DE_JOGO'][id_load]):
                                        organiza_load = col32.checkbox('Organiza ',value=True)
                                else:
                                        organiza_load = col32.checkbox('Organiza ')
                                if 'Bola Parada Ofensiva' in str(df_CPT['PRINCIPIOS_DE_JOGO'][id_load]):
                                        bpof_load = col32.checkbox('Bola Parada Ofensiva ',value=True)
                                else:
                                        bpof_load = col32.checkbox('Bola Parada Ofensiva ')
                                if 'Bola Parada Defensiva' in str(df_CPT['PRINCIPIOS_DE_JOGO'][id_load]):
                                        bpdef_load = col32.checkbox('Bola Parada Defensiva ',value=True)
                                else:
                                        bpdef_load = col32.checkbox('Bola Parada Defensiva ')
                                col33.write("**Sub princípios carregados:**")
                                col34.write("**-**")
                                col35.write("**-**")
                                if posse_load or vai_dentro_load:
                                        if 'Joga Junto' in str(df_CPT['COMPORTAMENTOS'][id_load]):
                                                jogajunto_load = col33.checkbox("Joga Junto", value=True)
                                        else:
                                                jogajunto_load = col33.checkbox("Joga Junto")
                                        if 'Movimenta' in str(df_CPT['COMPORTAMENTOS'][id_load]):
                                                movimenta_load = col33.checkbox("Movimenta",value=True)
                                        else:
                                                movimenta_load = col33.checkbox("Movimenta")
                                        if 'Ritmo' in str(df_CPT['COMPORTAMENTOS'][id_load]):
                                                ritmo_load = col33.checkbox("Ritmo",value=True)
                                        else:
                                                ritmo_load = col33.checkbox("Ritmo")
                                        if 'Agressividade' in str(df_CPT['COMPORTAMENTOS'][id_load]):
                                                agressividade_load = col33.checkbox("Agressividade",value=True)
                                        else:
                                                agressividade_load = col33.checkbox("Agressividade")
                                        if 'Qualidade' in str(df_CPT['COMPORTAMENTOS'][id_load]):
                                                qualidade_load = col33.checkbox("Qualidade",value=True)
                                        else:
                                                qualidade_load = col33.checkbox("Qualidade")
                                if reage_load or organiza_load:
                                        if 'Marca Junto' in str(df_CPT['COMPORTAMENTOS'][id_load]):
                                                marcajunto_load = col34.checkbox("Marca Junto",value=True)
                                        else:
                                                marcajunto_load = col34.checkbox("Marca Junto")
                                        if 'Pressiona' in str(df_CPT['COMPORTAMENTOS'][id_load]):
                                                pressiona_load = col34.checkbox("Pressiona",value=True)
                                        else:
                                                pressiona_load = col34.checkbox("Pressiona")
                                        if 'Corre Pra Trás' in str(df_CPT['COMPORTAMENTOS'][id_load]):
                                                correpratras_load = col34.checkbox("Corre pra trás",value=True)
                                        else:        
                                                correpratras_load = col34.checkbox("Corre pra trás")
                                        if 'Protege o Gol' in str(df_CPT['COMPORTAMENTOS'][id_load]):
                                                protegeogol_load = col34.checkbox("Protege o Gol",value=True)
                                        else:        
                                                protegeogol_load = col34.checkbox("Protege o Gol")
                                        if 'Comunicação' in str(df_CPT['COMPORTAMENTOS'][id_load]):
                                                comunicacao_load = col34.checkbox("Comunicação",value=True)
                                        else:
                                                comunicacao_load = col34.checkbox("Comunicação")
                                if bpof_load or bpdef_load:
                                        if 'Escanteio' in str(df_CPT['COMPORTAMENTOS'][id_load]):
                                                escanteio_load = col35.checkbox("Escanteio",value=True)  
                                        else:      
                                                escanteio_load = col35.checkbox("Escanteio")
                                        if 'Falta Indireta' in str(df_CPT['COMPORTAMENTOS'][id_load]):
                                                faltaind_load = col35.checkbox("Falta Indireta",value=True)
                                        else:
                                                faltaind_load = col35.checkbox("Falta Indireta")
                                        if 'Falta Direta' in str(df_CPT['COMPORTAMENTOS'][id_load]):
                                                faltadir_load = col35.checkbox("Falta Direta",value=True)
                                        else:
                                                faltadir_load = col35.checkbox("Falta Direta")
                                        if 'Penalti' in str(df_CPT['COMPORTAMENTOS'][id_load]):
                                                penalti_load = col35.checkbox("Penalti",value=True)
                                        else:
                                                penalti_load = col35.checkbox("Penalti")
                                        if 'Penalti' in str(df_CPT['COMPORTAMENTOS'][id_load]):
                                                lateral_load = col35.checkbox("Lateral",value=True)
                                        else:
                                                lateral_load = col35.checkbox("Lateral")
                                col36,col37,col38 =st.columns(3)
                                cat_ativ_load_item = str(df_CPT['CATEGORIA_DE_ATIVIDADE'][id_load])
                                cat_ativ_load = col36.selectbox("Categoria de Atividade carregada:",options=cat_ativ,index=cat_ativ.index(cat_ativ_load_item))
                                if cat_ativ_load == 'Atividade Complementar':
                                        ativ_comp_load_item = str(df_CPT['ATIVIDADE_COMPLEMENTAR'][id_load])
                                        ativ_comp_load = col38.selectbox("Atividade Complementar carregada:",options=atv_comp,index=atv_comp.index(ativ_comp_load_item))
                                        carac_ativ_load = "Vazio"
                                else:
                                        carac_ativ_load_item = str(df_CPT['CARACTERISTICA_DA_ATIVIDADE'][id_load])
                                        carac_ativ_load = col37.selectbox("Característica da Atividade carregada:",options=carac_at,index=carac_at.index(carac_ativ_load_item))
                                        ativ_comp_load="Vazio"
                                st.divider()

                                nome_at_load = st.text_input("**Nome da atividade carregada:**",value=str(df_CPT['NOME_DA_ATIVIDADE'][id_load]))
                                desc_at_load = st.text_area("**Descrição da atividade carregada:**",value=str(df_CPT['DESCRICAO_DA_ATIVIDADE'][id_load]))
                                
                                col39,col40 = st.columns(2)
                                largura_load = col39.text_input('**Largura:**',value=str(df_CPT['LARGURA'][id_load]))
                                comprimento_load = col40.text_input('**Comprimento:**',value=str(df_CPT['COMPRIMENTO'][id_load]))

                                st.divider()

                                col41,col42,col43,col44 = st.columns(4)
                                est_load = col41.number_input("**Estímulo:**",step=0.5,value=float(df_CPT['ESTIMULO'][id_load]),min_value=0.0)
                                rec_load = col42.number_input("**Recuperação:**",step=0.5,value=float(df_CPT['RECUPERACAO'][id_load]),min_value=0.0)
                                rep_load = col43.number_input("**Repetições:**",step=1,value=int(df_CPT['REPETICAO'][id_load]),min_value=0)
                                voltot_load = est_load*rep_load+rec_load*(rep_load-1)
                                col44.write("**Volume Total:**")
                                col44.write(str(voltot_load))
                                nota_load = st.number_input("**Nota:**",step=0.5,value=float(df_CPT['NOTA'][id_load]),max_value=5.0,min_value=0.0)


                                valores_load=[esp_load,resp_load,comp_load,cora_load,conf_load]
                                valor_load=['','','','','']
                                valores_final_load =[]
                                if valores_load[0] == True:
                                        valor_load[0] = 'Espírito de Equipe'
                                if valores_load[1] == True:
                                        valor_load[1] = 'Respeito'
                                if valores_load[2] == True:
                                        valor_load[2] = 'Comprometimento'
                                if valores_load[3] == True:
                                        valor_load[3] = 'Coragem'
                                if valores_load[4] == True:
                                        valor_load[4] = 'Confiança'
                                for i in range(len(valor_load)):
                                        if valor_load[i]!='':
                                                valores_final_load.append(valor_load[i])
                                valores_final_load = ', '.join(valores_final_load)   

                                principios_load=[posse_load,vai_dentro_load,reage_load,organiza_load,bpof_load,bpdef_load]
                                principio_load=['','','','','','']
                                principios_final_load=[]
                                if principios_load[0] == True:
                                        principio_load[0] = 'Posse'
                                if principios_load[1] == True:
                                        principio_load[1] = 'Vai Dentro'
                                if principios_load[2] == True:
                                        principio_load[2] = 'Reage'
                                if principios_load[3] == True:
                                        principio_load[3] = 'Organiza'
                                if principios_load[4] == True:
                                        principio_load[4] = 'Bola Parada Ofensiva'
                                if principios_load[5] == True:
                                        principio_load[5] = 'Bola Parada Defensiva'
                                for i in range(len(principio_load)):
                                        if principio_load[i]!='':
                                                principios_final_load.append(principio_load[i])
                                principios_final_load = ', '.join(principios_final_load)     

                                comportamentos_load=[jogajunto_load,movimenta_load,ritmo_load,agressividade_load,qualidade_load,marcajunto_load,pressiona_load,correpratras_load,protegeogol_load,comunicacao_load,escanteio_load,faltaind_load,faltadir_load,penalti_load,lateral_load]
                                comportamento_load=['','','','','','','','','','','','','','','']
                                comportamentos_final_load=[]
                                if comportamentos_load[0] == True:
                                        comportamento_load[0] = 'Joga Junto'
                                if comportamentos_load[1] == True:
                                        comportamento_load[1] = 'Movimenta'
                                if comportamentos_load[2] == True:
                                        comportamento_load[2] = 'Ritmo'
                                if comportamentos_load[3] == True:
                                        comportamento_load[3] = 'Agressividade'
                                if comportamentos_load[4] == True:
                                        comportamento_load[4] = 'Qualidade'
                                if comportamentos_load[5] == True:
                                        comportamento_load[5] = 'Marca Junto'
                                if comportamentos_load[6] == True:
                                        comportamento_load[6] = 'Pressiona'
                                if comportamentos_load[7] == True:
                                        comportamento_load[7] = 'Corre Pra Trás'
                                if comportamentos_load[8] == True:
                                        comportamento_load[8] = 'Protege o Gol'
                                if comportamentos_load[9] == True:
                                        comportamento_load[9] = 'Comunicação'
                                if comportamentos_load[10] == True:
                                        comportamento_load[10] = 'Escanteio'
                                if comportamentos_load[11] == True:
                                        comportamento_load[11] = 'Falta Indireta'
                                if comportamentos_load[12] == True:
                                        comportamento_load[12] = 'Falta Direta'
                                if comportamentos_load[13] == True:
                                        comportamento_load[13] = 'Penalti'
                                if comportamentos_load[14] == True:
                                        comportamento_load[14] = 'Lateral'
                                for i in range(len(comportamento_load)):
                                        if comportamento_load[i]!='':
                                                comportamentos_final_load.append(comportamento_load[i])
                                comportamentos_final_load = ', '.join(comportamentos_final_load)



                        inserir2 = col26.button(":heavy_plus_sign: ",use_container_width=True,on_click=clicked,args=[2])
                        if inserir2:
                                lista_adicionar2 = [cat,data_selec2_edit,m_edit,y_edit,ativ_selec_edit,valores_final_load, principios_final_load,comportamentos_final_load,cat_ativ_load,carac_ativ_load,ativ_comp_load,nome_at_load,desc_at_load,largura_load,comprimento_load,est_load,rec_load,rep_load,voltot_load,nota_load,(nota_load*voltot_load)/5]
                                df_CPT.loc[(id_load)] = lista_adicionar2
                                df_CPT.to_csv(caminho_CPT,decimal=',',sep=';')
                                col26.success("Atividade inserida com sucesso!")
                
                



if selected == "Preparação":
    st.title(f"{selected}")
if selected == "Microciclo":
    data_micro = st.date_input("**Escolha a data desejada:**", value=datetime.today(),format='DD/MM/YYYY')
    col1,col2,col3,col4,col5,col6,col7 = st.columns(7)
    col1.write("**SEGUNDA**")
    if dias_semana[data_micro.weekday()] == 'Segunda':
            seg = data_micro.strftime("%d/%m/%Y")
            col1.write(seg)
    else:
            seg = data_micro-timedelta(days=data_micro.weekday())
            seg = seg.strftime("%d/%m/%Y")
            col1.write(seg)
    

    col2.write("**TERÇA**")
    if dias_semana[data_micro.weekday()] == 'Terça':
            ter = data_micro.strftime("%d/%m/%Y")
            col2.write(ter)
    elif data_micro.weekday() == 0 :
            ter = data_micro+timedelta(days=1)
            ter = ter.strftime("%d/%m/%Y")
            col2.write(ter)
    else:
            ter = data_micro-timedelta(days=(data_micro.weekday()-1))
            ter = ter.strftime("%d/%m/%Y")
            col2.write(ter)

    col3.write("**QUARTA**")
    if dias_semana[data_micro.weekday()] == 'Quarta':
            qua = data_micro.strftime("%d/%m/%Y")
            col3.write(qua)
    elif data_micro.weekday() < 2 :
            qua = data_micro+timedelta(days=(2-data_micro.weekday()))
            qua = qua.strftime("%d/%m/%Y")
            col3.write(qua)
    else:
            qua = data_micro-timedelta(days=(data_micro.weekday()-2))
            qua = qua.strftime("%d/%m/%Y")
            col3.write(qua)

    col4.write("**QUINTA**")
    if dias_semana[data_micro.weekday()] == 'Quinta':
            qui = data_micro.strftime("%d/%m/%Y")
            col4.write(qui)
    elif data_micro.weekday() < 3 :
            qui = data_micro+timedelta(days=(3-data_micro.weekday()))
            qui = qui.strftime("%d/%m/%Y")
            col4.write(qui)
    else:
            qui = data_micro-timedelta(days=(data_micro.weekday()-3))
            qui = qui.strftime("%d/%m/%Y")
            col4.write(qui)
    
    col5.write("**SEXTA**")
    if dias_semana[data_micro.weekday()] == 'Sexta':
            sex = data_micro.strftime("%d/%m/%Y")
            col5.write(sex)
    elif data_micro.weekday() < 4 :
            sex = data_micro+timedelta(days=(4-data_micro.weekday()))
            sex = sex.strftime("%d/%m/%Y")
            col5.write(sex)
    else:
            sex = data_micro-timedelta(days=(data_micro.weekday()-4))
            sex = sex.strftime("%d/%m/%Y")
            col5.write(sex)
    
    col6.write("**SÁBADO**")
    if dias_semana[data_micro.weekday()] == 'Sábado':
            sab = data_micro.strftime("%d/%m/%Y")
            col6.write(sab)
    elif data_micro.weekday() < 5 :
            sab = data_micro+timedelta(days=(5-data_micro.weekday()))
            sab = sab.strftime("%d/%m/%Y")
            col6.write(sab)
    else:
            sab = data_micro-timedelta(days=(data_micro.weekday()-5))
            sab = sab.strftime("%d/%m/%Y")
            col6.write(sab)

    col7.write("**DOMINGO**")
    if dias_semana[data_micro.weekday()] == 'Domingo':
            dom = data_micro.strftime("%d/%m/%Y")
            col7.write(dom)
    else:
            dom = data_micro+timedelta(days=6-data_micro.weekday())
            dom = dom.strftime("%d/%m/%Y")
            col7.write(dom)

    id_seg_1 = cat+'-'+seg+'-'+'Atividade 1'
    if id_seg_1 in df_CPT.index:
        col1.write("ATIVIDADE 1")
        expander_seg1 = col1.expander(df_CPT['NOME_DA_ATIVIDADE'][id_seg_1])
        expander_seg1.write(df_CPT['CATEGORIA_DE_ATIVIDADE'][id_seg_1])
        expander_seg1.write(df_CPT['PRINCIPIOS_DE_JOGO'][id_seg_1])
        expander_seg1.caption(df_CPT['DESCRICAO_DA_ATIVIDADE'][id_seg_1])
        expander_seg1.write(str(df_CPT['VOLUME'][id_seg_1])+"("+str(df_CPT['REPETICAO'][id_seg_1])+"x"+str(df_CPT['ESTIMULO'][id_seg_1])+'/'+str(df_CPT['RECUPERACAO'][id_seg_1])+")")
        expander_seg1.write(df_CPT['NOTA'][id_seg_1])

    id_seg_2 = cat+'-'+seg+'-'+'Atividade 2'
    if id_seg_2 in df_CPT.index:
        col1.write("ATIVIDADE 2")
        expander_seg1 = col1.expander(df_CPT['NOME_DA_ATIVIDADE'][id_seg_2])
        expander_seg1.write(df_CPT['CATEGORIA_DE_ATIVIDADE'][id_seg_2])
        expander_seg1.write(df_CPT['PRINCIPIOS_DE_JOGO'][id_seg_2])
        expander_seg1.caption(df_CPT['DESCRICAO_DA_ATIVIDADE'][id_seg_2])
        expander_seg1.write(str(df_CPT['VOLUME'][id_seg_2])+"("+str(df_CPT['REPETICAO'][id_seg_2])+"x"+str(df_CPT['ESTIMULO'][id_seg_2])+'/'+str(df_CPT['RECUPERACAO'][id_seg_2])+")")
        expander_seg1.write(df_CPT['NOTA'][id_seg_2])



                


if selected == "Controle":
    st.title(f"{selected}")
if selected == "Individual":
    st.title(f"{selected}")



