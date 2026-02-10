import streamlit as st

# Configuração Master
st.set_page_config(page_title="Speed Money Pro", page_icon="💰", layout="wide")

# --- CONTROLE DE ZOOM (NOVIDADE) ---
st.sidebar.markdown("### 🔍 Ajuste de Leitura")
zoom_level = st.sidebar.slider("Tamanho da Fonte", min_value=12, max_value=30, value=18)

# Estilo de Livro Premium com Zoom Dinâmico
st.markdown(f"""
    <style>
    .main {{ background-color: #FDFBF7; }}
    /* Aplicando o zoom dinâmico em todo o corpo do texto */
    .stMarkdown, p, li, .stCheckbox {{ 
        font-size: {zoom_level}px !important; 
        line-height: 1.6;
    }}
    h1 {{ color: #1B4D3E; font-family: 'Playfair Display', serif; font-size: {zoom_level + 20}px; text-align: center; margin-bottom: 30px; border-bottom: 3px solid #D4AF37; }}
    h2 {{ color: #8B4513; border-left: 5px solid #D4AF37; padding-left: 15px; margin-top: 30px; font-size: {zoom_level + 10}px; }}
    h3 {{ font-size: {zoom_level + 5}px; }}
    .stProgress > div > div > div > div {{ background-color: #D4AF37; }}
    .card {{ background-color: #ffffff; padding: 25px; border-radius: 15px; border: 1px solid #e0e0e0; box-shadow: 5px 5px 15px rgba(0,0,0,0.05); }}
    </style>
    """, unsafe_allow_html=True)

st.title("💰 SPEED MONEY")
st.subheader("O seu guia interativo para a liberdade financeira")

# --- BARRA DE PROGRESSO GERAL ---
st.sidebar.markdown("### 📊 Seu Progresso")
progresso = st.sidebar.slider("Quantos capítulos você já concluiu?", 0, 5, 0)
st.sidebar.progress(progresso * 20)

# --- NAVEGAÇÃO ---
menu = st.sidebar.radio("📚 Capítulos", 
    ["Início", "1. Mentalidade & Gestão", "2. Freelancer de Elite", "3. Vendas & E-commerce", "4. Máquina de Afiliados", "5. Império de Conteúdo", "🧮 Simulador de Ganhos"])

if menu == "Início":
    st.image("https://images.unsplash.com/photo-1553729459-efe14ef6055d?auto=format&fit=crop&w=1000&q=80")
    st.markdown("""
    ## Comece Aqui
    Este aplicativo foi desenhado para ser o seu mentor silencioso. Ao contrário de cursos caros, aqui você tem o **caminho das pedras** direto e reto.
    
    **Como usar este app:**
    1. Escolha um método no menu lateral.
    2. Leia a teoria e observe as imagens.
    3. Execute as **Tarefas Práticas** ao final de cada página.
    4. Use o simulador para projetar seus lucros.
    """)

elif menu == "1. Mentalidade & Gestão":
    st.header("Capítulo 1: Domando o Dinheiro")
    st.image("https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=800&q=80")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("### O Método 50-30-20")
        st.write("Para prosperar, você precisa dividir seu dinheiro assim:")
        st.write("- **50% Necessidades:** Aluguel, comida, luz.")
        st.write("- **30% Desejos:** Lazer, assinaturas, hobbies.")
        st.write("- **20% Liberdade:** Investimentos e reserva.")
    
    with col2:
        st.write("### O Passo a Passo Técnico")
        st.markdown("""
        1. **Planilha de Guerra:** Crie uma lista com todas as suas dívidas.
        2. **Corte do Pequeno Gasto:** Aquele 'cafezinho' de R$ 10 por dia vira R$ 300 no mês.
        3. **Conta PJ Digital:** Abra uma conta no Inter ou Nubank exclusiva para seus ganhos online.
        """)

    st.write("---")
    st.markdown("### ✅ Desafio Prático")
    t1 = st.checkbox("Anotei todos os meus gastos dos últimos 30 dias")
    t2 = st.checkbox("Cancelei pelo menos uma assinatura que não uso")
    if t1 and t2: st.success("Excelente! Você está pronto para o Capítulo 2.")

elif menu == "2. Freelancer de Elite":
    st.header("Capítulo 2: Prestação de Serviços")
    st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80")
    
    st.write("### O Segredo do Perfil Vencedor")
    st.markdown("""
    Trabalhar como freelancer é a forma mais rápida de colocar dinheiro no bolso.
    
    **Onde agir:**
    * **Workana:** Melhor para brasileiros.
    * **Fiverr:** Ótimo para serviços rápidos de 5 dólares.
    * **99Freelas:** Focado em tecnologia e escrita.
    """)
    
    with st.expander("Clique para ver o Passo a Passo de Cadastro"):
        st.write("1. Escolha uma foto com fundo neutro e sorriso profissional.")
        st.write("2. No título, seja específico.")
        st.write("3. Crie 3 amostras de trabalho (Portfólio).")
    
    st.markdown("### ✅ Desafio Prático")
    st.checkbox("Criei meu perfil em pelo menos uma plataforma")
    st.checkbox("Enviei minha primeira proposta de serviço")

elif menu == "3. Vendas & E-commerce":
    st.header("Capítulo 3: O Poder das Vendas")
    st.image("https://images.unsplash.com/photo-1556742044-3c52d6e88c62?auto=format&fit=crop&w=800&q=80")
    
    st.write("### Nichos que mais vendem hoje:")
    st.info("Pet Shop, Casa & Cozinha, Tecnologia e Beleza.")
    
    st.write("### Como fazer Dropshipping Nacional:")
    st.markdown("""
    1. **Garimpo:** Procure vendedores locais com preço de atacado.
    2. **Anúncio:** Crie uma conta no Mercado Livre e anuncie.
    3. **Venda:** Quando o cliente comprar, você compra no fornecedor.
    """)

    st.markdown("### ✅ Desafio Prático")
    st.checkbox("Escolhi um produto para testar")
    st.checkbox("Fiz as fotos do meu primeiro anúncio")

elif menu == "4. Máquina de Afiliados":
    st.header("Capítulo 4: Comissões no Automático")
    st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80")
    
    st.write("### A Estratégia do 'Baixo Investimento'")
    st.markdown("""
    Ser afiliado é como ser um representante comercial moderno. 
    
    **O Ciclo do Sucesso:**
    1. **Cadastro:** Hotmart, Amazon, Kiwify.
    2. **A Escolha:** Escolha um produto que VOCÊ compraria.
    3. **O Tráfego:** Crie um perfil no Instagram focado no nicho.
    4. **A Conversão:** Poste 1 Reel por dia com uma dica.
    """)

    st.markdown("### ✅ Desafio Prático")
    st.checkbox("Me afiliei a um produto com boa comissão")
    st.checkbox("Criei um perfil focado apenas nesse nicho")

elif menu == "5. Império de Conteúdo":
    st.header("Capítulo 5: Criando sua Audiência")
    st.image("https://images.unsplash.com/photo-1492724441997-5dc865305da7?auto=format&fit=crop&w=800&q=80")
    
    st.write("### Como Viralizar com Estratégia")
    st.markdown("""
    O segredo do algoritmo é a **Retenção**.
    
    **Roteiro de 15 segundos:**
    * **Gancho:** 'O segredo que ninguém te conta sobre...'
    * **Valor:** Entregue a informação prometida.
    * **CTA:** 'Clique no link da bio'.
    """)
    
    st.markdown("### ✅ Desafio Prático")
    st.checkbox("Gravei meu primeiro vídeo de 15 segundos")
    st.checkbox("Postei no TikTok e no Instagram Reels")

elif menu == "🧮 Simulador de Ganhos":
    st.header("🧮 Simulador Financeiro")
    st.write("Projete sua liberdade:")
    
    meta = st.number_input("Quanto você quer ganhar por mês? (R$)", value=5000)
    tipo_trabalho = st.selectbox("Método Escolhido", ["Freelancer", "Venda de Produto", "Afiliado"])
    
    if tipo_trabalho == "Freelancer":
        valor_job = st.number_input("Valor médio por serviço (R$)", value=250)
        total = meta / valor_job
        st.success(f"Você precisa de **{int(total)} serviços** por mês.")
    elif tipo_trabalho == "Venda de Produto":
        lucro_item = st.number_input("Lucro limpo por venda (R$)", value=40)
        total = meta / lucro_item
        st.success(f"Você precisa vender **{int(total)} unidades**.")
    else:
        comissao = st.number_input("Comissão média (R$)", value=100)
        total = meta / comissao
        st.success(f"Você precisa de **{int(total)} indicações**.")

st.sidebar.info("Speed Money v2.1 - Agora com controle de zoom!")
