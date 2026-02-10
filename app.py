import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Speed Money Pro", page_icon="💰", layout="wide")

# Estilização Profissional
st.markdown("""
    <style>
    .main { background-color: #FDFBF7; }
    .stApp { max-width: 1000px; margin: 0 auto; }
    h1 { color: #1B4D3E; font-family: 'Playfair Display', serif; font-size: 50px; text-align: center; border-bottom: 2px solid #D4AF37; }
    h2 { color: #8B4513; border-left: 5px solid #D4AF37; padding-left: 15px; }
    .step-box { background-color: #FFFFFF; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); margin-bottom: 15px; border: 1px solid #E0E0E0; }
    .tip-box { background-color: #FFFDE7; border-left: 5px solid #FBC02D; padding: 10px; font-style: italic; }
    </style>
    """, unsafe_allow_html=True)

st.title("💰 SPEED MONEY: O MANUAL")

# --- NAVEGAÇÃO ---
menu = st.sidebar.selectbox("📖 Sumário do Guia", ["Início", "1. Gestão Financeira", "2. Freelancer Pro", "3. Vendas & E-commerce", "4. Império de Afiliados", "5. Criação de Conteúdo", "🧮 Calculadora de Metas"])

if menu == "Início":
    st.markdown("## Bem-vindo à sua nova realidade.")
    st.write("Este não é um app de 'ganhar dinheiro fácil'. É um mapa de execução. Escolha um capítulo e siga os passos à risca.")
    st.image("https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?auto=format&fit=crop&w=800&q=80")
    st.info("💡 Dica: Comece pela Gestão Financeira. De nada adianta ganhar mais se você não sabe segurar o que já tem.")

elif menu == "1. Gestão Financeira":
    st.header("Capítulo 1: O Alicerce Inquebrável")
    
    with st.container():
        st.write("### O Passo a Passo")
        st.markdown("""
        1. **Mapeamento de Sangria:** Abra seu extrato bancário dos últimos 30 dias. Sublinhe de vermelho tudo o que não é essencial (streamings que não vê, taxas bancárias).
        2. **O Pote da Liberdade:** Abra uma conta em um banco digital (Nubank, Inter, etc) apenas para o seu 'negócio'. Nunca misture com o dinheiro do pão.
        3. **A Regra dos 10%:** Todo dinheiro que entrar online, reserve 10% para reinvestir em ferramentas ou anúncios.
        """)
        
        st.markdown("<div class='tip-box'><b>Dica de Ouro:</b> Instale o app 'Organizze' ou 'Mobills' para automatizar o rastreio de gastos.</div>", unsafe_allow_html=True)

elif menu == "2. Freelancer Pro":
    st.header("Capítulo 2: Venda suas Horas com Lucro")
    
    st.write("### Como começar do zero:")
    st.markdown("""
    * **Passo 1: O Portfólio 'Fake':** Se não tem clientes, crie 3 projetos fictícios. Se é designer, faça logotipos para marcas famosas de mentira. Se é redator, escreva 3 artigos sobre temas em alta.
    * **Passo 2: Cadastro Estratégico:** Vá ao **Workana** ou **Upwork**. Não coloque 'Sou iniciante'. Coloque 'Especialista em resolver [Problema X]'.
    * **Passo 3: A Técnica da Primeira Estrela:** No primeiro job, cobre barato apenas para ganhar a avaliação 5 estrelas. É essa avaliação que vai te permitir cobrar caro depois.
    """)
    
    st.info("🔧 **Ferramentas:** Canva (Design), ChatGPT (Auxílio em texto), DeepL (Tradução).")

elif menu == "3. Vendas & E-commerce":
    st.header("Capítulo 3: Dominando os Marketplaces")
    
    st.write("### O Caminho da Mercadoria:")
    st.markdown("""
    1. **A Garimpagem:** Olhe para o seu quarto. O que você não usa há 6 meses? Tire 5 fotos com boa iluminação e fundo limpo.
    2. **Anúncio Magnético:** No Mercado Livre ou Shopee, use títulos com palavras-chave. Ex: 'Teclado Gamer Mecânico RGB Silencioso' em vez de 'Teclado usado'.
    3. **Dropshipping Nacional:** Pesquise por fornecedores no Brás ou na 25 de Março que façam envio direto. Você vende o produto deles e eles entregam.
    """)
    
    st.warning("⚠️ **Aviso:** O segredo da venda online não é o preço, é a CONFIANÇA. Responda as perguntas dos clientes em menos de 10 minutos.")

elif menu == "4. Império de Afiliados":
    st.header("Capítulo 4: Escala sem Estoque")
    
    st.write("### Estratégia de Execução:")
    st.markdown("""
    * **Passo 1: A Escolha do Produto:** Vá na **Hotmart** ou **Kiwify**. Escolha produtos com 'Blueprint' alto (materiais prontos).
    * **Passo 2: Estrutura Própria:** Não mande o cliente direto para o link do produtor. Mande para o SEU WhatsApp ou para uma página sua. 
    * **Passo 3: Isca Digital:** Ofereça um PDF gratuito '5 Dicas para X' para conseguir o contato da pessoa.
    """)
    
    st.markdown("<div class='tip-box'><b>Segredo:</b> O dinheiro está no 'Follow-up'. Muitas pessoas só compram no 5º contato.</div>", unsafe_allow_html=True)

elif menu == "5. Criação de Conteúdo":
    st.header("Capítulo 5: Autoridade e Viralização")
    
    st.write("### Script para Crescer:")
    st.markdown("""
    1. **O Gancho (0-3 segundos):** Comece o vídeo com uma pergunta ou algo chocante. Ex: 'Você está perdendo dinheiro por causa disso...'.
    2. **Conteúdo (3-20 segundos):** Entregue a solução rápida. Sem enrolação.
    3. **CTA (Chamada para Ação):** Diga exatamente o que fazer: 'Clique no link da bio' ou 'Me siga para mais'.
    """)
    
    st.write("### Onde focar?")
    st.table({"Plataforma": ["TikTok", "Instagram", "YouTube"], "Objetivo": ["Viralização Rápida", "Relacionamento/Venda", "Autoridade/Renda Passiva"]})

elif menu == "🧮 Calculadora de Metas":
    st.header("Planejamento de Guerra")
    meta = st.number_input("Quanto você quer ganhar por mês? (R$)", value=2000)
    lucro_unidade = st.number_input("Qual o seu lucro médio por venda/serviço? (R$)", value=50)
    
    if lucro_unidade > 0:
        total = meta / lucro_unidade
        st.subheader(f"Para ganhar R$ {meta}, você precisa de:")
        st.metric("Total de Vendas/Jobs", f"{int(total)}")
        st.write(f"Isso equivale a **{total/22:.1f}** tarefas por dia (considerando apenas dias úteis).")
