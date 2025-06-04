import streamlit as st
import pandas as pd
import random
import time

def show_app():

    st.title("Mini-Dashboard: Desafios e Tendências no Big Data 🚀")
    st.write(f"Bem-vindo, {st.session_state['name']}! Você pode acessar as aulas abaixo:")

    options = st.selectbox("Selecione uma aula:",["Desafios do Big Data", "Tendências Futuras no Big Data"],key="selected_lesson")

    if options == "Desafios do Big Data": 
        tab1, tab2, tab3 = st.tabs(["🔐 Privacidade e Proteção de Dados", "🧹 Qualidade de Dados", "🤖 Integração com IA, IoT e Blockchain"])

        # TAB 1 - Privacidade e Proteção de Dados
        with tab1:
            st.subheader("🔐 Anonimização de Dados: É suficiente?")
            st.markdown("Explore abaixo um conjunto de dados 'aparentemente anônimo' e veja como é possível reidentificar uma pessoa.")

            data = pd.DataFrame({
                "idade": [34, 45, 28, 60],
                "cidade": ["Campinas", "Curitiba", "Recife", "Curitiba"],
                "doença": ["hipertensão", "diabetes", "asma", "câncer"]
            })
            
            st.dataframe(data)

            st.markdown("Agora, selecione um filtro e veja o risco de identificação:")
            idade = st.slider("Filtrar por idade", 20, 70, (20, 70))
            cidade = st.selectbox("Filtrar por cidade", ["Todas"] + list(data["cidade"].unique()))

            filtered_data = data[(data["idade"] >= idade[0]) & (data["idade"] <= idade[1])]
            if cidade != "Todas":
                filtered_data = filtered_data[filtered_data["cidade"] == cidade]

            st.write("### 🔎 Resultado do Filtro:")
            st.dataframe(filtered_data)

            if len(filtered_data) == 1:
                st.warning("⚠️ Apenas um registro encontrado. Esse dado pode ser reidentificável!")

            st.markdown("➡️ **Conclusão:** Dados anonimizados ainda podem expor indivíduos, especialmente com cruzamentos externos.")

        # TAB 2 - Qualidade de Dados
        with tab2:
            st.subheader("🧹 Análise de Qualidade de Dados")
            
            df_quality = pd.DataFrame({
                "nome": ["Ana", "Pedro", None, "João"],
                "idade": [25, None, 40, 32],
                "salário": [3500, 4000, 3900, None]
            })

            st.write("### 📄 Conjunto de dados:")
            st.dataframe(df_quality)

            st.write("### ❓ Valores ausentes por coluna:")
            st.write(df_quality.isnull().sum())

            st.write("### 🛠️ Sugestões de tratamento:")
            st.markdown("""
            - Preencher com média/mediana.
            - Remover linhas com muitos nulos.
            - Preencher com dados externos/contextuais.
            """)

        # TAB 3 - Integração com IA, IoT e Blockchain
        with tab3:
            st.subheader("🤖 Como Big Data se integra com IA, IoT e Blockchain")

            st.markdown("### Exemplo de Pipeline:")
            st.markdown("""
            1. **IoT**: Sensores capturam dados de temperatura de um equipamento.
            2. **IA**: Algoritmo detecta anomalias de superaquecimento.
            3. **Blockchain**: Registro do evento para auditoria e segurança.

            Você pode simular abaixo:
            """)

            temp = st.slider("Temperatura lida pelo sensor (°C)", 10, 100, 45)

            if temp > 70:
                st.error("🚨 Alerta! Temperatura fora do padrão detectada pela IA.")
                st.markdown("🔗 Evento seria gravado na blockchain: `Hash123ABC456DEF`")
            elif temp > 50:
                st.warning("⚠️ Temperatura elevada. Monitoramento recomendado.")
                st.markdown("📄 Evento registrado como atenção.")
            else:
                st.success("✅ Temperatura dentro do padrão. Sem registro necessário.")

            st.markdown("➡️ **Reflexão:** A integração entre sensores, modelos preditivos e blockchain cria um ecossistema seguro e inteligente.")

            st.markdown("### Analogia para os Desafios do Big Data:")
            st.markdown("""
            Para entender os desafios do Big Data, imagine duas situações:

            1. **Dispositivo de armazenamento limitado**: 
               É como tentar guardar toda a água de um balde em uma garrafa pequena. Você precisa decidir o que é mais importante ou encontrar formas de compactar os dados.

            2. **Blockchain**: 
               É como registrar cada gota de água em um livro de registros. Quanto mais gotas você tenta registrar, mais lento e difícil fica para verificar cada entrada no livro.

            ➡️ **Conclusão:** Assim como na analogia, o Big Data exige estratégias inteligentes para lidar com grandes volumes de dados, seja otimizando o armazenamento ou garantindo que os registros sejam eficientes e escaláveis.
            """)

    else:
        tab4, tab5, tab6 = st.tabs(["📊 Dados em Tempo Real", "🌐 Edge Computing vs Computação em Nuvem", "☁️ Arquiteturas Serverless"])

        # TAB 4 - Simulação de dados em tempo real
        with tab4:
            st.subheader("📡 Simulação de Big Data em Tempo Real")

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

            🧠 Vamos refletir com um exemplo prático na aba ao lado.
            """)

            st.subheader("⏱️ Comparando latência: Nuvem vs Edge")
            st.markdown("Clique para simular a detecção de uma anomalia em um sensor industrial:")

            col1, col2 = st.columns(2)

            with col1:
                if st.button("☁️ Processar na Nuvem"):
                    st.write("🔄 Enviando dados para a nuvem...")
                    latency = random.uniform(0.8, 2.0)
                    time.sleep(latency)
                    st.success(f"✅ Anomalia detectada pela nuvem em {latency:.2f} segundos")

            with col2:
                if st.button("🧊 Processar na Borda"):
                    st.write("📍 Processando localmente no dispositivo...")
                    latency = random.uniform(0.1, 0.4)
                    time.sleep(latency)
                    st.success(f"✅ Anomalia detectada localmente em {latency:.2f} segundos")

            st.markdown("➡️ A diferença de tempo demonstra a **vantagem do Edge Computing** para respostas críticas.")        

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
            """)

        