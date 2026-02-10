import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Speed Money", page_icon="💰", layout="centered")

# Estilização para parecer um livro
st.markdown("""
    <style>
    .main { background-color: #F5F5DC; }
    h1 { color: #8B4513; font-family: 'Georgia'; text-align: center; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #8B4513; color: white; }
    .capitulo-card { background-color: #FFF8E7; padding: 20px; border-radius: 10px; border: 1px solid #D2B48C; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (NAVEGAÇÃO) ---
st.sidebar.title("📖 Sumário")
menu = st.sidebar.radio("Ir para:", ["Início", "Quiz: Meu Perfil", "Capítulos", "Calculadora de Metas"])

# --- PÁGINA INICIAL ---
if menu == "Início":
    st.title("SPEED MONEY")
    st.image("https://via.placeholder.com/800x400.png?text=Speed+Money+-+Guia+de+Renda+Online") # Aqui entraria sua imagem
    st.write("### Bem-vindo ao seu guia definitivo para ganhar dinheiro online.")
    st.write("> *'O dinheiro no digital não é mágica, é matemática e constância.'*")
    st.info("Use o menu ao lado para navegar entre os ensinamentos, ferramentas e seu perfil.")

# --- QUIZ DE PERFIL ---
elif menu == "Quiz: Meu Perfil":
    st.title("🎯 Descubra sua Jornada")
    st.write("Responda e saiba por onde começar:")
    
    tempo = st.selectbox("Quanto tempo você tem?", ["Menos de 1h", "2h a 4h", "Tempo Integral"])
    capital = st.selectbox("Tem dinheiro para investir?", ["R$ 0,00 (Nada)", "Até R$ 500", "Acima de R$ 1000"])
    
    if st.button("Ver meu Caminho"):
        if capital == "R$ 0,00 (Nada)":
            st.success("Seu caminho ideal é: **Capítulo 2 - Freelancer** ou **Capítulo 5 - Conteúdo**.")
        elif tempo == "Menos de 1h":
            st.success("Seu caminho ideal é: **Capítulo 4 - Afiliados**.")
        else:
            st.success("Seu caminho ideal é: **Capítulo 3 - Vendas Online**.")

# --- CAPÍTULOS ---
elif menu == "Capítulos":
    st.title("📚 Os 5 Pilares da Riqueza")
    
    aba1, aba2, aba3, aba4, aba5 = st.tabs(["Cap 1", "Cap 2", "Cap 3", "Cap 4", "Cap 5"])
    
    with aba1:
        st.header("Gerenciando seu Dinheiro")
        st.write("**Passo 01:** O Diagnóstico de 7 Dias. Anote cada centavo.")
        st.write("**Passo 02:** Corte assinaturas fantasmas.")
        st.checkbox("Tarefa: Organizei meus gastos hoje")

    with aba2:
        st.header("Freelancer")
        st.write("**Passo 01:** Cadastro no Workana ou 20Pila.")
        st.write("**Passo 02:** Crie um portfólio rápido no Canva.")
        st.checkbox("Tarefa: Criei meu perfil de freelancer")

    with aba3:
        st.header("Vendas Online")
        st.write("**Passo 01:** Desapegue do que não usa no OLX.")
        st.write("**Passo 02:** Entenda o Dropshipping Nacional.")
        st.checkbox("Tarefa: Postei meu primeiro produto")

    with aba4:
        st.header("Afiliados")
        st.write("**Passo 01:** Escolha um produto na Hotmart ou Kiwify.")
        st.write("**Passo 02:** Crie conteúdo que resolva um problema.")
        st.checkbox("Tarefa: Escolhi meu produto vencedor")

    with aba5:
        st.header("Conteúdo")
        st.write("**Passo 01:** Escolha seu nicho (Finanças, Saúde, etc).")
        st.write("**Passo 02:** Poste 1 Reel/TikTok por dia durante 30 dias.")
        st.checkbox("Tarefa: Gravei meu primeiro vídeo")

# --- CALCULADORA ---
elif menu == "Calculadora de Metas":
    st.title("🧮 Simulador de Lucro")
    st.write("Quanto você precisa vender para bater sua meta?")
    
    meta = st.number_input("Sua Meta Mensal (R$):", min_value=10.0, value=1000.0)
    comissao = st.number_input("Ganho por Venda/Job (R$):", min_value=1.0, value=50.0)
    
    if comissao > 0:
        total = meta / comissao
        st.metric("Vendas Necessárias", f"{int(total)} vendas")
        st.write(f"Isso dá aproximadamente **{total/30:.1f} vendas por dia**.")
