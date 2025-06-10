import streamlit as st
import pandas as pd
import numpy as np
import random
import time
from src.helpers import get_participants, hash_password

def show_app():

    st.image("ppges.png", use_container_width=True)  
    st.title("Atividade Interativa: Desafios e Tendências no Big Data 🚀")
    pd.set_option('future.no_silent_downcasting', True)
    if st.session_state["sexo"] == "Feminino": 
        st.write(f"Bem-vinda, {st.session_state['name']}!")
    else:
        st.write(f"Bem-vindo, {st.session_state['name']}!")
    st.write("Nesta pequena atividade, você pode explorar alguns conceitos relacionados aos desafios e tendências futuras no campo do Big Data.")
    st.write("Primeiro, selecione um dos blocos abaixo, entre Desafios do Big Data e Tendências Futuras no Big Data, para começar a explorar os tópicos.")
    options = st.selectbox("Selecione um dos blocos:",["Nenhum","Desafios do Big Data", "Tendências Futuras no Big Data"],key="selected_lesson")
    st.write("Você pode navegar entre as abas para explorar diferentes tópicos.")
    mock_data = {
                "Nome": ["Paula", "Saulo", "João"],
                "Idade": [47, None, 80],
                "Sexo": ["Feminino", "Masculino", None],
                "Interesse": [None, "Machine Learning", "Data Science"]
    }
    try:
        participants = get_participants()[1]
        data = pd.DataFrame(participants, columns=["ID", "Nome", "Idade","Sexo","Interesse"]).drop(columns=["ID"])
        data.replace("", np.nan, inplace=True)
        data = pd.concat([data, pd.DataFrame(mock_data)], ignore_index=True)
        data2 = data.copy()
        for i in range(len(data2)):
            data2.at[i, "Nome"] = hash_password(str(data2.at[i, "Nome"]))
        data3 = data.copy()
    except Exception as e:
        st.error(f"Erro ao carregar os dados dos participantes: {str(e)}")
        data = pd.DataFrame(mock_data,columns=["Nome", "Idade", "Sexo", "Interesse"])    
        data.replace("", np.nan, inplace=True)
        data2 = data.copy()
        for i in range(len(data2)):
            data2.at[i, "Nome"] = hash_password(str(data2.at[i, "Nome"]))
        data3 = data.copy()
    if options == "Desafios do Big Data": 
        tab1, tab2, tab3 = st.tabs(["🔐 Privacidade e Proteção de Dados", "🧹 Qualidade de Dados", "🤖 Integração com IA, IoT e Blockchain"])

        # TAB 1 - Privacidade e Proteção de Dados
        with tab1:
            st.subheader("🔐 Anonimização de Dados: É suficiente?")
            st.markdown("Explore abaixo um conjunto de dados 'aparentemente anônimo' e veja como é possível reidentificar uma pessoa.")
            st.markdown("Nesta tabela, temos alguns dados de alunos que acessaram esta atividade. Para fins de demonstração, os nomes foram substituídos por hashes, mas os outros dados permanecem visíveis. Vamos analisar o risco de reidentificação.")
            
            st.dataframe(data2)    
            st.markdown("Digamos que você deseja identificar o interesse de um amigo seu específico na disciplina, mas não consegue identificá-lo pelo nome, já que está criptografado.")
            st.markdown("Aí você tem uma ideia. Não sei identificar o nome, mas posso filtrar por idade e sexo já que sei essas informações. Vamos ver se consigo encontrar um registro único que corresponda ao meu amigo.")
            st.markdown("Agora, arraste o filtro de idade abaixo e selecione uma opção de sexo e veja o risco de identificação:")
            st.markdown("Obs: Ambos os filtros são aplicados simultaneamente, ou seja, você deve selecionar uma faixa de idade e um sexo para filtrar os dados.")
            idade = st.slider("Filtrar por idade", 20, 90, (20, 90))
            sexo = st.selectbox("Filtrar por sexo", ["Todos"] + list(data2["Sexo"].unique()))
            filtered_data = data2.dropna(subset=["Idade"])  # Remove rows where "Idade" is NaN
            filtered_data = filtered_data[(filtered_data["Idade"].astype(int) >= idade[0]) & (filtered_data["Idade"].astype(int) <= idade[1])]
            if sexo != "Todos":
                filtered_data = filtered_data[filtered_data["Sexo"] == sexo]

            st.write("### 🔎 Resultado do Filtro:")
            st.dataframe(filtered_data)

            if len(filtered_data) == 1:
                st.warning("⚠️ Apenas um registro encontrado. Esse dado pode ser reidentificável!")

            st.markdown("➡️ **Conclusão:** Dados anonimizados ainda podem expor indivíduos, especialmente com cruzamentos ou informações externas.")

        # TAB 2 - Qualidade de Dados
        with tab2:
            st.subheader("🧹 Análise de Qualidade de Dados")

            st.markdown("Nesta atividade, vamos explorar a qualidade dos dados em um conjunto de dados obtidos dos alunos.")

            st.write("### 📄 Conjunto de dados:")
            st.dataframe(data3)

            st.info("Como pode notar, alguns valores estão ausentes. Vamos analisar a qualidade desses dados.")

            st.warning("### ❓ Valores ausentes por coluna:")
            st.dataframe(data3.isnull().sum())

            st.markdown("""
            - **Valores Ausentes**: Algumas colunas possuem valores ausentes, o que pode impactar análises futuras.
            - **Consistência**: Verifique se os dados seguem padrões esperados (ex: idade não pode ser negativa).
            - **Precisão**: Dados devem ser precisos e atualizados (ex: salário deve refletir o valor correto).
            """)

            st.write("### 🛠️ Sugestões de tratamento:")
            st.markdown("""
            - Preencher com média/mediana.
            - Remover linhas com muitos nulos.
            - Preencher com dados externos/contextuais.
            """)

            # Initialize session state for button tracking
            if "media_button_pressed" not in st.session_state:
                st.session_state["media_button_pressed"] = False

            # Add buttons for data cleaning
            if st.button("Preecher por média"):
                data3["Idade"] = data3["Idade"].fillna(np.ceil(data3["Idade"].mean()))
                st.success("Valores ausentes preenchidos com a média!")
                st.dataframe(data3)
                st.write("### ❓ Valores ausentes por coluna:")
                st.write(data3.isnull().sum())
                st.info("Ainda há alguns valores ausentes, mas agora a coluna 'Idade' foi preenchida com a média. Vamos remover os campos nulos restantes.")
                st.session_state["media_button_pressed"] = True  
            if st.session_state["media_button_pressed"]:
                if st.button("Remover dados incompletos"):
                    data3["Idade"] = data3["Idade"].fillna(np.ceil(data3["Idade"].mean()))
                    st.success("Valores ausentes preenchidos com a média!")
                    st.dataframe(data3)
                    st.write("### ❓ Valores ausentes por coluna:")
                    st.write(data3.isnull().sum())
                    st.info("Ainda há alguns valores ausentes, mas agora a coluna 'Idade' foi preenchida com a média. Vamos remover os campos nulos restantes.")
                    data3.dropna(inplace=True)
                    st.success("Linhas com valores ausentes removidas!")
                    st.dataframe(data3)
                    st.write("### ❓ Valores ausentes por coluna:")
                    st.write(data3.isnull().sum())
                    st.info("Agora, todas as linhas com valores ausentes foram removidas.")

        # TAB 3 - Integração com IA, IoT e Blockchain
        with tab3:
            st.subheader("🤖 Como Big Data se integra com IA, IoT e Blockchain")

            st.markdown(""" Imagine que você está monitorando centenas sensores de temperatura em uma fábrica de produtos de limpeza.
            Vamos simular a coleta de dados em tempo real de um dos sensores.""")
            st.markdown("### Exemplo de Pipeline prático:")
            st.markdown("""
            1. **IoT**: Sensores capturam dados de temperatura de um equipamento em tempo real.
            2. **IA**: Algoritmo detecta anomalias de superaquecimento.
            3. **Blockchain**: Registro do evento para auditoria e segurança.

            Você pode simular abaixo, controlando a faixa de temperatura de alerta e a temperatura lida pelo sensor:
            """)

            threshold = st.slider("Temperatura de alerta (°C)", 10, 100, (50,70))
            temp = st.slider("Temperatura lida pelo sensor (°C)", 10, 100, 45)

            if temp > threshold[1]:
                st.error("🚨 Alerta! Temperatura fora do padrão detectada pela IA.")
                st.markdown("🔗 Evento seria gravado na blockchain: `Hash123ABC456DEF`")
            elif temp > threshold[0]:
                st.warning("⚠️ Temperatura elevada. Monitoramento recomendado.")
                st.markdown("📄 Evento registrado como atenção.")
            else:
                st.success("✅ Temperatura dentro do padrão. Sem registro necessário.")

            st.markdown("➡️ **Reflexão:** A integração entre sensores, modelos preditivos e blockchain cria um ecossistema seguro e inteligente.")

    elif options == "Tendências Futuras no Big Data":
        tab4, tab5, tab6 = st.tabs(["📊 Dados em Tempo Real", "🌐 Edge Computing vs Computação em Nuvem", "☁️ Arquiteturas Serverless"])

        # TAB 4 - Simulação de dados em tempo real
        with tab4:
            st.subheader("📡 Simulação de Big Data em Tempo Real")

            st.markdown(""" Agora imagine que você está monitorando mais de 800 sensores de temperatura em uma fábrica de produtos de limpeza.
            Vamos simular a coleta de dados em tempo real de um dos sensores e visualizar esses dados em um gráfico dinâmico.""")
            st.markdown("Clique no botão abaixo para iniciar a simulação de temperatura dos sensores a cada meio segundo.")

            if st.button("Iniciar Simulação"):
                st.write("Simulando temperatura de sensores a cada meio segundo.")
                
                placeholder = st.empty()
                data = []

                for i in range(20):
                    new_row = {
                        "tempo (s)": i,
                        "temperatura (°C)": round(random.uniform(20, 30), 2)
                    }
                    data.append(new_row)
                    df = pd.DataFrame(data)
                    placeholder.line_chart(df.set_index("tempo (s)"))
                    time.sleep(0.3)

                st.success("✅ Simulação concluída!")

                st.markdown("➡️ **Reflexão:** A coleta de dados em tempo real permite monitoramento contínuo e respostas rápidas a eventos críticos. Mas, como garantir a qualidade e integridade desses dados em grande volume dado a geração de dados contínua de 800 sensores simultaneamente neste exemplo?")

        # TAB 5 - Edge Computing 
        with tab5:
            st.subheader("🌐 Edge Computing vs Computação em Nuvem")
            st.markdown("""
            **Edge Computing** é uma arquitetura onde o processamento dos dados ocorre **próximo da origem** (por exemplo, em sensores, câmeras, ou dispositivos locais),
            em vez de ser enviado diretamente para a nuvem.

            Isso reduz a latência, o uso de banda e aumenta a privacidade.

            ### Exemplos de uso:
            - Carros autônomos
            - Câmeras de segurança com reconhecimento facial
            - Monitoramento médico em tempo real

            🧠 Vamos refletir com um exemplo prático.
            """)

            st.subheader("⏱️ Comparando latência: Nuvem vs Edge")
            st.markdown("Seguindo o mesmo exemplo do item anterior, onde você está monitorando centenas de sensores de temperatura em uma fábrica de produtos de limpeza.")
            st.markdown("Dentre eles, há um sensor industrial que monitora a temperatura em tempo real de uma máquina num processo crítico, em que milissegundos podem fazer a diferença no resultado da etapa do processo.")
            st.markdown("Vamos simular a detecção de uma anomalia de superaquecimento nesse sensor, comparando o tempo de resposta entre processamento na nuvem e na borda (edge).")
            st.markdown("Clique para simular a detecção de uma anomalia em um sensor industrial:")

            col1, col2 = st.columns(2)

            with col1:
                if st.button("☁️ Processar na Nuvem"):
                    st.write("🔄 Enviando dados para a nuvem...")
                    latency = random.uniform(0.1, 3.0)
                    time.sleep(latency)
                    st.success(f"✅ Anomalia detectada pela nuvem em {latency:.2f} segundos")

            with col2:
                if st.button("🧊 Processar na Borda"):
                    st.write("📍 Processando localmente no dispositivo...")
                    latency = random.uniform(0.1, 0.4)
                    time.sleep(latency)
                    st.success(f"✅ Anomalia detectada localmente em {latency:.2f} segundos")

            st.markdown("➡️ A diferença de tempo demonstra a **vantagem do Edge Computing** para respostas críticas, permitindo a atuação mais eficaz.")        

        # TAB 6 - Explicação sobre Serverless
        with tab6:
            st.subheader("☁️ O que é uma Arquitetura Serverless?")
            st.markdown("""
            **Serverless** é um modelo de computação em nuvem onde você escreve apenas o código da função,
            e o provedor (como AWS, Google Cloud ou Azure) executa esse código sob demanda, sem necessidade de gerenciar servidores.

            ### Vantagens:
            - ✅ Escalabilidade automática.
            - 💸 Paga apenas pelo uso.
            - 🚀 Ideal para cargas event-driven (como Big Data streaming).

            ### Exemplos:
            - AWS Lambda processando dados recebidos do Kinesis.
            - Google Cloud Functions salvando arquivos processados em tempo real.

            Vamos simular isso com um cenário de ingestão de dados em Big Data.                        
            """)

            st.markdown("Imagine que você está recebendo um fluxo contínuo de dados de sensores em uma fábrica, e precisa processar esses dados em tempo real.")
            st.markdown("Vamos simular como uma arquitetura serverless pode escalar automaticamente para lidar com esse volume de dados.")
            st.markdown("### Simulação de Escalabilidade Automática")
            st.markdown("Nesta simulação, você pode ajustar o volume de dados que está sendo processado e ver como a arquitetura serverless responde automaticamente.")
            st.markdown("Cada função serverless pode processar até 1000 MB/s, e o sistema escala automaticamente para lidar com picos de carga.")

            # Interação do usuário
            data_rate = st.slider("📊 Volume de dados em tempo real (MB/s)", min_value=0, max_value=10000, value=1000, step=500)

            # Cálculo da capacidade e instâncias
            max_per_function = 1000
            num_functions = int(np.ceil(data_rate / max_per_function))
            total_capacity = num_functions * max_per_function

            # Gráfico com Streamlit nativo
            df = pd.DataFrame({
                "MB/s": [data_rate, total_capacity]
            }, index=["Dados recebidos", "Capacidade Serverless"])

            st.bar_chart(df, )

            # Métricas informativas
            col1, col2 = st.columns(2)
            col1.metric("🔧 Funções ativadas", f"{num_functions}")
            col2.metric("📦 Capacidade total", f"{total_capacity} MB/s")

            # Explicação adaptativa
            st.markdown(f"""
            ### 🔍 Interpretação:
            - Com **{data_rate} MB/s** de dados chegando, o sistema serverless ativou **{num_functions} função(ões)** simultâneas.
            - Cada função consegue lidar com até **{max_per_function} MB/s**.
            - Isso demonstra a **elasticidade** da arquitetura serverless, ideal para picos e escalabilidade horizontal.
            """)

            st.success("💡 Experimente mudar o volume de dados acima para ver a resposta dinâmica do sistema.")
    else:
        st.warning("Por favor, selecione um bloco para explorar os tópicos.")        

        