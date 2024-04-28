class PlataformaEducacaoFinanceira:
    def __init__(self):
        self.conteudo_educacional = {}
        self.ferramentas_gestao = {}
        self.sessoes_aconselhamento = {}
        self.comunidade_online = {}
        self.parcerias = {}

    def adicionar_conteudo_educacional(self, topico, conteudo):
        self.conteudo_educacional[topico] = conteudo

    def adicionar_ferramenta_gestao(self, ferramenta, descricao):
        self.ferramentas_gestao[ferramenta] = descricao

    def agendar_sessao_aconselhamento(self, data, horario, consultor):
        if (data, horario) not in self.sessoes_aconselhamento:
            self.sessoes_aconselhamento[(data, horario)] = [consultor]
        else:
            self.sessoes_aconselhamento[(data, horario)].append(consultor)

    def criar_comunidade_online(self):
        self.comunidade_online = {'membros': [], 'posts': {}}

    def adicionar_membro_comunidade(self, membro):
        self.comunidade_online['membros'].append(membro)

    def criar_post_comunidade(self, autor, conteudo):
        post_id = len(self.comunidade_online['posts']) + 1
        self.comunidade_online['posts'][post_id] = {'autor': autor, 'conteudo': conteudo}

    def estabelecer_parceria(self, empresa, descricao):
        self.parcerias[empresa] = descricao


# Exeplos pra criação da comunidade com agendamentose e ferramentas:
plataforma = PlataformaEducacaoFinanceira()

# Adicionando conteúdo educacional
plataforma.adicionar_conteudo_educacional("Orçamento Familiar", "Aprenda a criar e manter um orçamento familiar.")
plataforma.adicionar_conteudo_educacional("Investimentos Básicos", "Conceitos básicos sobre investimentos para iniciantes.")

# Adicionando ferramentas de gestão
plataforma.adicionar_ferramenta_gestao("Calculadora de Orçamento", "Calcule seus ganhos e gastos mensais.")
plataforma.adicionar_ferramenta_gestao("Simulador de Investimentos", "Simule diferentes cenários de investimento para planejar seu futuro financeiro.")

# Agendando sessões de aconselhamento
plataforma.agendar_sessao_aconselhamento("2024-05-15", "10:00", "Ana")
plataforma.agendar_sessao_aconselhamento("2024-05-20", "14:00", "Pedro")
plataforma.agendar_sessao_aconselhamento("2024-05-22", "16:30", "Mariana")

# Criando comunidade online
plataforma.criar_comunidade_online()
plataforma.adicionar_membro_comunidade("João") #Exemplo de menbros da comunidade adicione quantos for necessário
plataforma.adicionar_membro_comunidade("Maria")

# Criando posts na comunidade
plataforma.criar_post_comunidade("João", "Olá, pessoal! Estou animado para começar nossa jornada financeira!")
plataforma.criar_post_comunidade("Maria", "Alguém tem dicas sobre como economizar dinheiro para viajar?")

# Estabelecendo parcerias
plataforma.estabelecer_parceria("Banco X", "Oferecendo taxas especiais para os usuários da plataforma.")
plataforma.estabelecer_parceria("Escola de Investimentos Y", "Descontos em cursos de investimento para os membros da plataforma.")
