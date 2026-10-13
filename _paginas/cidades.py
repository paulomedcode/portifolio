"""Conteúdo das páginas de cidade (usado por gerar.py).

Cada cidade precisa de texto próprio: página igual trocando só o nome o Google ignora.
grupo: "sp" (atendimento presencial possível na região) ou "longe" (por vídeo e WhatsApp).
fuso: diferença em horas para Brasília, quando houver (aparece nas dúvidas).
"""

CIDADES = [
    # ------------------------------------------------------------ interior de São Paulo
    {
        "slug": "tatui", "nome": "Tatuí", "uf": "SP", "estado": "São Paulo", "grupo": "sp", "regiao": "Interior de São Paulo",
        "lead": "Tatuí é conhecida como a Capital da Música, mas também tem um comércio e um setor de serviços que crescem junto com a região de Sorocaba. A MedCode ajuda as empresas daqui a aparecer no Google, responder rápido no WhatsApp e organizar a rotina.",
        "mercado": [
            "Com comércio forte no centro, clínicas, escolas e muitos prestadores de serviço, Tatuí ainda é uma cidade em que o cliente chega por indicação. Mas, antes de fechar, ele quase sempre confere no Google e chama no WhatsApp.",
            "O Conservatório traz estudantes e famílias de toda a região, e isso movimenta escolas, cursos, aluguel e comércio. Quem aparece bem na busca e responde primeiro sai na frente.",
        ],
        "segmentos": [
            ("Escolas de música e cursos", "Um agente de IA que tira dúvidas sobre turmas, horários e matrícula a qualquer hora, inclusive de quem está chegando de outra cidade."),
            ("Clínicas e consultórios", "Agendamento pelo WhatsApp, confirmação na véspera e lembrete automático pra reduzir as faltas."),
            ("Comércio do centro", "Site com os produtos e os serviços da loja, levando o cliente direto pro WhatsApp de quem atende."),
            ("Prestadores de serviço", "Orçamento organizado e agenda de visitas, sem perder pedido no meio das conversas."),
        ],
        "faq_extra": ("Vocês fazem reunião presencial em Tatuí?", "Sim. Tatuí fica na nossa região de atendimento presencial, então o diagnóstico e as visitas podem ser feitos no seu negócio. O dia a dia segue pelo WhatsApp."),
    },
    {
        "slug": "sorocaba", "nome": "Sorocaba", "uf": "SP", "estado": "São Paulo", "grupo": "sp", "regiao": "Interior de São Paulo",
        "lead": "Sorocaba é um dos maiores polos de indústria e comércio do interior paulista, e por isso a concorrência também é grande: quem procura um serviço aqui tem muitas opções. A MedCode ajuda a sua empresa a ser encontrada primeiro e a responder antes do concorrente.",
        "mercado": [
            "Indústrias, um parque tecnológico, universidades, uma rede de saúde grande e um comércio que atende toda a região metropolitana. Sorocaba tem empresas de todos os tamanhos disputando o mesmo cliente.",
            "Nesse cenário, o que decide é velocidade e presença: aparecer quando alguém pesquisa o seu serviço na cidade e responder na hora, inclusive fora do horário comercial.",
        ],
        "segmentos": [
            ("Clínicas e saúde", "Agente de IA que agenda, confirma e tira dúvidas sobre convênios e preparo, liberando a recepção pro atendimento presencial."),
            ("Indústrias e fornecedores", "Site institucional que passa credibilidade pra compradores e um sistema de pedidos e orçamentos sob medida."),
            ("Comércio e varejo", "Site, catálogo e atendimento no WhatsApp e no Instagram, com o agente respondendo as perguntas que se repetem."),
            ("Escritórios e serviços profissionais", "Contabilidade, advocacia e consultorias: triagem do primeiro contato e agenda de reuniões no automático."),
        ],
        "faq_extra": ("Vocês atendem toda a região de Sorocaba?", "Sim. Atendemos Sorocaba e as cidades da região, como Votorantim, Itu, Tatuí e Itapetininga, com diagnóstico e visitas presenciais quando fizer sentido."),
    },
    {
        "slug": "itapetininga", "nome": "Itapetininga", "uf": "SP", "estado": "São Paulo", "grupo": "sp", "regiao": "Interior de São Paulo",
        "lead": "Itapetininga é referência no sudoeste paulista, com agronegócio forte e um comércio que atende cidades de toda a região. A MedCode leva pras empresas daqui as mesmas ferramentas que as grandes usam: site, agente de IA no WhatsApp, automação e sistemas sob medida.",
        "mercado": [
            "Boa parte dos clientes de Itapetininga vem das cidades vizinhas e do campo. Pra esse cliente, o WhatsApp é o principal canal: ele pergunta preço, disponibilidade e prazo antes de pegar a estrada.",
            "Responder rápido e com informação certa é o que garante a venda, e é exatamente onde um agente de IA e uma boa organização interna fazem diferença.",
        ],
        "segmentos": [
            ("Agronegócio e revendas", "Sistema de pedidos e estoque sob medida e um agente que responde o produtor rural a qualquer hora."),
            ("Comércio regional", "Atendimento pelo WhatsApp pra quem vem de outras cidades, com produtos, preços e prazos sempre à mão."),
            ("Clínicas e saúde", "Agenda organizada, confirmação automática e menos faltas de pacientes que vêm de longe."),
            ("Prestadores de serviço", "Orçamento pelo WhatsApp e agenda de visitas na cidade e na zona rural."),
        ],
        "faq_extra": ("Vocês atendem presencialmente em Itapetininga?", "Sim. Itapetininga está na nossa região de atendimento presencial. Fazemos o diagnóstico no seu negócio e seguimos o acompanhamento pelo WhatsApp."),
    },
    {
        "slug": "votorantim", "nome": "Votorantim", "uf": "SP", "estado": "São Paulo", "grupo": "sp", "regiao": "Interior de São Paulo",
        "lead": "Vizinha de Sorocaba, Votorantim tem tradição industrial e um comércio local que disputa cliente com a cidade ao lado. Pra quem empreende aqui, aparecer no Google na hora da busca e responder rápido no WhatsApp faz toda a diferença.",
        "mercado": [
            "Berço de um dos maiores grupos industriais do país, Votorantim cresceu junto com Sorocaba, e muita gente mora em uma cidade e consome na outra.",
            "Por isso, a empresa daqui precisa aparecer nas buscas das duas cidades. A represa de Itupararanga ainda movimenta turismo, gastronomia e lazer no fim de semana.",
        ],
        "segmentos": [
            ("Comércio de bairro", "Site simples e bem feito, com o endereço no Google e um botão que leva direto pro WhatsApp."),
            ("Turismo e lazer na represa", "Pousadas, restaurantes e passeios: um agente que responde sobre reservas e disponibilidade até de madrugada."),
            ("Saúde e beleza", "Agendamento pelo WhatsApp com lembrete automático e menos horário vago na agenda."),
            ("Serviços pra indústria", "Site institucional e controle de orçamentos pra quem fornece pras indústrias da região."),
        ],
        "faq_extra": ("Atendo clientes de Votorantim e de Sorocaba. O site serve pras duas?", "Serve. O site e o seu perfil no Google podem mostrar que você atende as duas cidades e a região, pra aparecer nas buscas de quem está em qualquer uma delas."),
    },
    {
        "slug": "itu", "nome": "Itu", "uf": "SP", "estado": "São Paulo", "grupo": "sp", "regiao": "Interior de São Paulo",
        "lead": "Itu une centro histórico, turismo, eventos e uma indústria forte. É uma cidade em que o cliente pesquisa bastante antes de escolher, e acaba fechando com quem aparece bem e responde primeiro.",
        "mercado": [
            "Turistas que vêm conhecer a cidade, noivos procurando espaço pra casamento, moradores dos condomínios buscando serviços: em Itu, muita venda começa numa pesquisa no Google e numa mensagem no WhatsApp.",
            "Muitas dessas mensagens chegam à noite e no fim de semana, justamente quando ninguém está pra responder.",
        ],
        "segmentos": [
            ("Eventos e casamentos", "Um agente que responde sobre datas, capacidade e pacotes a qualquer hora e já agenda a visita ao espaço."),
            ("Turismo e gastronomia", "Site bem posicionado e atendimento rápido pra reservas, cardápio e horários."),
            ("Serviços pra condomínios", "Manutenção, paisagismo e limpeza: orçamento pelo WhatsApp e agenda de visitas organizada."),
            ("Saúde e estética", "Agendamento automático, confirmação na véspera e lembrete pro cliente não faltar."),
        ],
        "faq_extra": ("Funciona pra espaço de eventos e buffet?", "Funciona muito bem. O agente responde as perguntas de sempre (datas livres, capacidade, valores de referência) e passa pra você o contato já qualificado, pronto pra visita."),
    },
    {
        "slug": "botucatu", "nome": "Botucatu", "uf": "SP", "estado": "São Paulo", "grupo": "sp", "regiao": "Interior de São Paulo",
        "lead": "Botucatu é polo universitário e de saúde do interior paulista, com uma economia que vai da indústria aeronáutica ao turismo da Cuesta. Chega muita gente de fora, e quem vem de fora pesquisa no Google.",
        "mercado": [
            "A universidade e o hospital universitário atraem estudantes, profissionais e pacientes de toda a região. Isso movimenta clínicas, moradia, alimentação e serviços o ano inteiro.",
            "Pra quem chega na cidade, o primeiro contato com o seu negócio é quase sempre uma busca no celular, seguida de uma mensagem no WhatsApp.",
        ],
        "segmentos": [
            ("Clínicas e consultórios", "Agenda pelo WhatsApp, confirmação automática e respostas sobre convênios e preparo de exames."),
            ("Moradia e serviços pra estudantes", "Imobiliárias, repúblicas e cursos: atendimento rápido pra quem está chegando e ainda não conhece a cidade."),
            ("Turismo de natureza", "Pousadas e passeios na Cuesta com site bem posicionado e reservas respondidas a qualquer hora."),
            ("Comércio e serviços", "Site, perfil no Google e atendimento organizado pra quem quer ser a primeira opção na busca."),
        ],
        "faq_extra": ("Vocês atendem presencialmente em Botucatu?", "Botucatu está na nossa região. Reuniões presenciais podem ser combinadas, e o acompanhamento do dia a dia é por vídeo e WhatsApp."),
    },
    # ------------------------------------------------------------ Norte
    {
        "slug": "porto-velho", "nome": "Porto Velho", "uf": "RO", "estado": "Rondônia", "grupo": "longe", "regiao": "Norte", "fuso": 1,
        "lead": "A MedCode tem raízes em Porto Velho. O fundador, Paulo Nogueira, cresceu e viveu a vida toda aqui antes de ir pra São Paulo, e conhece de perto o jeito de fazer negócio da cidade.",
        "mercado": [
            "Capital de Rondônia, Porto Velho cresceu muito com as usinas do Rio Madeira e com o agronegócio do estado. Chegou gente, chegaram empresas, e o comércio e os serviços cresceram junto.",
            "Por aqui, quase tudo se resolve pelo WhatsApp. A empresa que responde rápido e aparece bem no Google ainda se destaca, porque muita gente continua atendendo do jeito antigo.",
        ],
        "raiz": "Quem cresceu em Porto Velho sabe como o cliente daqui pensa: valoriza atenção, resposta rápida e indicação de quem conhece. É isso que a MedCode traz pra cada projeto: tecnologia de ponta, feita por alguém que entende a cidade.",
        "segmentos": [
            ("Clínicas e saúde", "Pacientes de todo o estado vêm se tratar na capital. O agente agenda, confirma e tira dúvidas antes da viagem."),
            ("Comércio e distribuidoras", "Pedidos pelo WhatsApp organizados num sistema, com estoque e entregas sob controle."),
            ("Prestadores de serviço", "Orçamento rápido, agenda de visitas e retorno automático pra quem pediu e sumiu."),
            ("Agro e fornecedores", "Site institucional e atendimento organizado pra quem vende pro campo."),
        ],
        "faq_extra": ("A MedCode é de Porto Velho?", "O fundador é. Paulo Nogueira cresceu e viveu a vida toda em Porto Velho e hoje está em São Paulo. O atendimento é por vídeo e WhatsApp, feito por quem conhece a cidade."),
    },
    {
        "slug": "rio-branco", "nome": "Rio Branco", "uf": "AC", "estado": "Acre", "grupo": "longe", "regiao": "Norte", "fuso": 2,
        "lead": "Rio Branco concentra boa parte do comércio, dos serviços e da saúde do Acre. A MedCode ajuda as empresas daqui a atender mais rápido no WhatsApp, aparecer no Google e organizar a rotina, com atendimento por vídeo, no seu horário.",
        "mercado": [
            "Capital e principal centro econômico do Acre, Rio Branco atende clientes de todo o estado. A ligação por estrada com o Peru ainda abre espaço pra comércio e serviços voltados à fronteira.",
            "Com clientes espalhados e distância grande entre as cidades, o WhatsApp vira o balcão da empresa. Quem atende bem por ele ganha o cliente antes da viagem.",
        ],
        "segmentos": [
            ("Comércio e varejo", "Site, catálogo e atendimento no WhatsApp pra quem compra da capital e do interior do estado."),
            ("Clínicas e saúde", "Agendamento, confirmação e orientação pra pacientes que vêm de outras cidades."),
            ("Prestadores de serviço", "Orçamento organizado e retorno automático, sem perder pedido no meio das conversas."),
            ("Empresas com clientes no interior", "Automação de pedidos e avisos, pra atender quem está longe com a mesma agilidade."),
        ],
        "faq_extra": ("A diferença de fuso atrapalha?", "Não. Rio Branco está 2 horas atrás de Brasília, e as reuniões são marcadas no seu horário. O agente de IA atende 24 horas, então o fuso nem aparece pro seu cliente."),
    },
    {
        "slug": "macapa", "nome": "Macapá", "uf": "AP", "estado": "Amapá", "grupo": "longe", "regiao": "Norte",
        "lead": "Macapá, a capital do meio do mundo, tem um comércio movimentado e um setor de serviços que cresce junto com o Amapá. A MedCode ajuda as empresas daqui a vender e atender melhor pelo WhatsApp e pelo Google.",
        "mercado": [
            "Cortada pela Linha do Equador, Macapá é o centro econômico do Amapá. Com Santana ao lado e a área de livre comércio, o varejo é forte e a disputa por cliente também.",
            "Turismo, gastronomia e serviços completam a economia. Em todos eles, o cliente pesquisa no celular e espera resposta rápida.",
        ],
        "segmentos": [
            ("Comércio e lojas", "Site com produtos e um agente que responde sobre preço, estoque e entrega no WhatsApp e no Instagram."),
            ("Clínicas e saúde", "Agenda organizada, confirmação automática e menos faltas."),
            ("Turismo e gastronomia", "Reservas e dúvidas respondidas a qualquer hora, e um site que aparece pra quem está chegando na cidade."),
            ("Prestadores de serviço", "Orçamento pelo WhatsApp e agenda organizada, com retorno automático pra quem sumiu."),
        ],
        "faq_extra": ("Atendem também Santana e outras cidades do Amapá?", "Sim. O atendimento é por vídeo e WhatsApp, então atendemos empresas de qualquer cidade do Amapá."),
    },
    {
        "slug": "boa-vista", "nome": "Boa Vista", "uf": "RR", "estado": "Roraima", "grupo": "longe", "regiao": "Norte", "fuso": 1,
        "lead": "Boa Vista é uma capital que cresceu rápido nos últimos anos, com agronegócio em expansão e comércio forte. A MedCode ajuda as empresas daqui a acompanhar esse crescimento com site, agente de IA no WhatsApp, automação e sistemas.",
        "mercado": [
            "Capital planejada de Roraima, Boa Vista concentra o comércio e os serviços do estado. A expansão das lavouras e a posição na fronteira com a Venezuela e a Guiana trouxeram mais gente e mais negócios.",
            "Cidade crescendo rápido significa cliente novo chegando todo dia, e esse cliente procura no Google e chama no WhatsApp antes de escolher.",
        ],
        "segmentos": [
            ("Agronegócio e revendas", "Sistema de pedidos e estoque sob medida e atendimento rápido pro produtor."),
            ("Comércio e varejo", "Site, perfil no Google e um agente que responde sobre produtos e entrega a qualquer hora."),
            ("Clínicas e saúde", "Agendamento pelo WhatsApp, confirmação e lembrete automáticos."),
            ("Prestadores de serviço", "Orçamentos organizados e agenda sob controle, mesmo com o volume crescendo."),
        ],
        "faq_extra": ("A diferença de fuso atrapalha?", "Não. Boa Vista está 1 hora atrás de Brasília, e as reuniões são marcadas no seu horário. E o agente de IA atende o seu cliente 24 horas."),
    },
    {
        "slug": "palmas", "nome": "Palmas", "uf": "TO", "estado": "Tocantins", "grupo": "longe", "regiao": "Norte",
        "lead": "Palmas é a capital mais nova do Brasil: uma cidade planejada, jovem e conectada. A MedCode ajuda as empresas daqui a aparecer no Google, atender no WhatsApp com agente de IA e organizar a gestão.",
        "mercado": [
            "Fundada no fim dos anos 1980, Palmas tem economia puxada pelo serviço público, pelo agronegócio do Tocantins e por um comércio que atende o estado todo.",
            "É uma cidade de população jovem, que resolve tudo pelo celular. Pra quem empreende aqui, presença digital bem feita já é o básico.",
        ],
        "segmentos": [
            ("Escritórios e serviços profissionais", "Advocacia, contabilidade e consultorias: site que passa credibilidade e triagem automática do primeiro contato."),
            ("Agronegócio", "Sistemas e automação pra revendas e fornecedores que atendem o campo."),
            ("Clínicas e saúde", "Agendamento, confirmação e lembrete automáticos no WhatsApp."),
            ("Gastronomia e lazer", "Reservas e cardápio respondidos a qualquer hora, inclusive nos fins de semana nas praias do lago."),
        ],
        "faq_extra": ("Vocês atendem outras cidades do Tocantins?", "Sim. Como o atendimento é por vídeo e WhatsApp, atendemos empresas de Palmas e de qualquer cidade do estado."),
    },
    # ------------------------------------------------------------ Nordeste
    {
        "slug": "teresina", "nome": "Teresina", "uf": "PI", "estado": "Piauí", "grupo": "longe", "regiao": "Nordeste",
        "lead": "Teresina é referência em saúde e educação no Nordeste e recebe pacientes e estudantes de vários estados. A MedCode ajuda as empresas daqui a atender esse volume com agente de IA no WhatsApp, site, automação e sistemas.",
        "mercado": [
            "Entre os rios Poti e Parnaíba, a capital do Piauí virou polo regional: hospitais, clínicas e faculdades atraem gente do interior do estado e dos estados vizinhos.",
            "Isso significa muita mensagem chegando de quem ainda não conhece a cidade, com dúvidas sobre agenda, preços e como chegar. Quem responde rápido e bem fica com o cliente.",
        ],
        "segmentos": [
            ("Clínicas e saúde", "Um agente que agenda, confirma e orienta pacientes que vêm de fora, a qualquer hora."),
            ("Educação e cursos", "Respostas sobre turmas, valores e matrícula no WhatsApp e no Instagram, com os interessados indo direto pra secretaria."),
            ("Comércio e varejo", "Site e atendimento organizado pra vender pra capital e pro interior."),
            ("Prestadores de serviço", "Orçamento organizado e retorno automático, sem perder pedido."),
        ],
        "faq_extra": ("Funciona pra clínica que atende paciente de outras cidades?", "Muito bem. O agente tira as dúvidas antes da viagem, agenda, confirma e manda lembrete, o que ajuda a reduzir as faltas de quem vem de longe."),
    },
    {
        "slug": "sao-luis", "nome": "São Luís", "uf": "MA", "estado": "Maranhão", "grupo": "longe", "regiao": "Nordeste",
        "lead": "São Luís junta patrimônio histórico, turismo, porto e um comércio que atende todo o Maranhão. A MedCode ajuda as empresas daqui a aparecer no Google, atender mais rápido no WhatsApp e organizar a operação.",
        "mercado": [
            "Capital construída numa ilha e com centro histórico reconhecido como patrimônio mundial, São Luís recebe turistas o ano todo e é a porta de entrada pra outros destinos do estado.",
            "O complexo portuário e a força do comércio completam uma economia variada, com espaço pra empresas de todos os tamanhos.",
        ],
        "segmentos": [
            ("Turismo e hospedagem", "Pousadas, agências e passeios: reservas e dúvidas respondidas a qualquer hora, em português e com rapidez."),
            ("Clínicas e saúde", "Agendamento, confirmação e lembrete automáticos no WhatsApp."),
            ("Comércio e varejo", "Site, catálogo e atendimento no Instagram e no WhatsApp com agente de IA."),
            ("Serviços e logística", "Sistemas sob medida e automação pra controlar pedidos, entregas e equipe."),
        ],
        "faq_extra": ("Funciona pra pousada e agência de turismo?", "Funciona. O turista manda mensagem em qualquer horário. O agente responde sobre disponibilidade, valores e passeios, e passa pra você a reserva quase pronta."),
    },
    {
        "slug": "aracaju", "nome": "Aracaju", "uf": "SE", "estado": "Sergipe", "grupo": "longe", "regiao": "Nordeste",
        "lead": "Aracaju é uma capital com qualidade de vida, turismo na orla e um setor de serviços forte. A MedCode ajuda as empresas daqui a ser encontradas no Google e a atender pelo WhatsApp com agente de IA, automação e sistemas.",
        "mercado": [
            "Com a orla de Atalaia, a gastronomia e o turismo, Aracaju recebe visitantes o ano todo. Ao mesmo tempo, é o centro de comércio, saúde e serviços de Sergipe.",
            "Seja o turista procurando onde comer, seja o morador procurando uma clínica, a busca começa no celular. Aparecer bem e responder rápido é o que transforma busca em cliente.",
        ],
        "segmentos": [
            ("Turismo e gastronomia na orla", "Reservas, cardápio e horários respondidos a qualquer hora, com um site que aparece pra quem está na cidade."),
            ("Clínicas e saúde", "Agendamento pelo WhatsApp, confirmação e lembrete automáticos."),
            ("Comércio e varejo", "Atendimento no Instagram e no WhatsApp com agente de IA e site com os produtos."),
            ("Serviços profissionais", "Escritórios e consultorias com site, triagem do primeiro contato e agenda organizada."),
        ],
        "faq_extra": ("Vocês atendem outras cidades de Sergipe?", "Sim. O atendimento é por vídeo e WhatsApp, então atendemos empresas de Aracaju e de qualquer cidade do estado."),
    },
]
