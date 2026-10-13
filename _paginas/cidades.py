"""Conteúdo das páginas de cidade (usado por gerar.py).

Cada cidade precisa de texto próprio: página igual trocando só o nome o Google ignora.
grupo: "sp" (atendimento presencial possível na região) ou "longe" (por vídeo e WhatsApp).
lead: texto sobre a cidade (abre a seção do comércio local). A abertura da página é a história do fundador,
adaptada pela região em gerar.py (LEAD_FUNDADOR), ou "lead_fundador" quando a cidade tem a sua própria.
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
            ("Escolas de música e cursos", "Pais e alunos de toda a região perguntam sobre turmas, horários e valores, muitas vezes à noite. O agente de IA responde na hora, como uma secretária que conversa de verdade e entende até áudio, e já encaminha a matrícula pra você."),
            ("Clínicas e consultórios", "O agente agenda pelo WhatsApp, confirma na véspera e manda lembrete, sem o paciente ficar esperando a recepção responder. Com a automação, as faltas caem e a agenda fica cheia."),
            ("Comércio do centro", "Um site bonito e rápido no celular, com os produtos e serviços da loja, colocando você no Google quando alguém busca em Tatuí. Cada botão leva direto pro seu WhatsApp."),
            ("Prestadores de serviço", "Pedidos de orçamento organizados, agenda de visitas sob controle e retorno automático pra quem pediu e sumiu. Nenhum cliente fica sem resposta."),
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
            ("Clínicas e saúde", "Um agente de IA que conversa como uma recepcionista: entende o que o paciente escreve (e até os áudios), agenda, confirma e tira dúvidas sobre convênios e preparo. A recepção fica livre pra quem está na clínica."),
            ("Indústrias e fornecedores", "Site institucional que passa credibilidade pra compradores e um sistema sob medida pra pedidos e orçamentos, feito do jeito que a sua empresa já trabalha."),
            ("Comércio e varejo", "Atendimento no WhatsApp e no Instagram com agente de IA respondendo preço, estoque e entrega na hora, inclusive fora do horário. Quem pergunta primeiro é atendido primeiro."),
            ("Escritórios e serviços profissionais", "Contabilidade, advocacia e consultorias: o agente faz a triagem do primeiro contato e marca a reunião, e a consultoria de gestão ajuda a organizar processos e equipe."),
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
            ("Agronegócio e revendas", "Um sistema sob medida pra pedidos e estoque e um agente de IA que responde o produtor a qualquer hora, entendendo até os áudios que ele manda do campo."),
            ("Comércio regional", "Quem vem de outras cidades pergunta antes de pegar a estrada. O agente responde preço, disponibilidade e prazo na hora, e o site coloca a sua loja no Google da região."),
            ("Clínicas e saúde", "Agenda organizada, confirmação e lembrete automáticos pra pacientes que vêm de longe, e um agente que tira dúvidas como uma recepcionista atenciosa."),
            ("Prestadores de serviço", "Orçamentos pelo WhatsApp sem bagunça, agenda de visitas na cidade e na zona rural, e retorno automático pra quem pediu e não respondeu."),
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
            ("Comércio de bairro", "Um site bem feito e o seu negócio no Google quando alguém de Votorantim ou de Sorocaba busca o que você vende. Um toque e o cliente já está no seu WhatsApp."),
            ("Turismo e lazer na represa", "Pousadas, restaurantes e passeios recebem mensagem a toda hora. O agente responde sobre reservas e disponibilidade até de madrugada, numa conversa natural, sem menu de opções."),
            ("Saúde e beleza", "Agendamento pelo WhatsApp com o agente de IA, lembrete automático na véspera e menos horário vago na agenda."),
            ("Serviços pra indústria", "Site institucional que passa confiança e um sistema sob medida pra controlar orçamentos, pedidos e equipe."),
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
            ("Eventos e casamentos", "Noivos e clientes pesquisam à noite e no fim de semana. O agente responde sobre datas, capacidade e pacotes, entende áudio e agenda a visita ao espaço, passando pra você o contato já interessado."),
            ("Turismo e gastronomia", "Um site que aparece pra quem está visitando Itu e um agente que responde sobre reservas, cardápio e horários na hora."),
            ("Serviços pra condomínios", "Manutenção, paisagismo e limpeza: orçamento pelo WhatsApp, agenda de visitas organizada e retorno automático pra não perder nenhum pedido."),
            ("Saúde e estética", "Agendamento automático, confirmação na véspera e lembrete pro cliente não faltar, com um atendimento que conversa de verdade."),
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
            ("Clínicas e consultórios", "Pacientes da região inteira procuram atendimento na cidade. O agente agenda, confirma e explica preparo de exames e convênios, como uma recepcionista disponível 24 horas."),
            ("Moradia e serviços pra estudantes", "Imobiliárias, repúblicas e cursos: o agente responde na hora quem está chegando e ainda não conhece a cidade, e o site coloca você no Google de quem pesquisa de longe."),
            ("Turismo de natureza", "Pousadas e passeios na Cuesta com site bem posicionado e reservas respondidas a qualquer hora, inclusive por áudio."),
            ("Comércio e serviços", "Site, perfil no Google e atendimento organizado pra ser a primeira opção na busca, e um sistema sob medida quando a rotina pedir."),
        ],
        "faq_extra": ("Vocês atendem presencialmente em Botucatu?", "Botucatu está na nossa região. Reuniões presenciais podem ser combinadas, e o acompanhamento do dia a dia é por vídeo e WhatsApp."),
    },
    # ------------------------------------------------------------ Norte
    {
        "slug": "porto-velho", "nome": "Porto Velho", "uf": "RO", "estado": "Rondônia", "grupo": "longe", "regiao": "Norte", "fuso": 1,
        "lead_fundador": "A MedCode tem raízes em Porto Velho. O fundador, Paulo Nogueira, nasceu e cresceu aqui. Depois foi pra São Paulo, a maior cidade do Brasil, onde aproveitou tudo o que essa cidade tem a ensinar sobre gestão, tecnologia e vendas. Agora traz essa experiência e esse know-how pros negócios de Porto Velho.",
        "mercado": [
            "Porto Velho é cidade de comércio. Da Sete de Setembro, no Centro, aos centros comerciais da Zona Sul e da Zona Leste, são lojas, clínicas médicas, consultórios de dentista e prestadores de serviço disputando o mesmo cliente, muitas vezes na mesma rua.",
            "E por aqui quase tudo se resolve pelo WhatsApp: o cliente chama, pergunta o preço e quer resposta na hora. Quem responde rápido e aparece bem no Google sai na frente, porque muita gente ainda atende do jeito antigo.",
        ],
        "raiz_titulo": "Por que isso faz diferença pra você",
        "raiz": "Agência de fora não sabe que aqui o cliente chama no WhatsApp antes de pisar na loja, que indicação vale ouro e que demorar pra responder é perder a venda pro vizinho. O Paulo sabe, porque viveu isso do outro lado do balcão. A diferença é que agora ele chega com as ferramentas que as empresas de São Paulo usam pra crescer: atendimento com IA, automação e gestão de verdade.",
        "segmentos": [
            ("Clínicas médicas", "Clínica é o que não falta em Porto Velho, e o paciente fica com quem responde primeiro. O agente de IA conversa como uma recepcionista, entende até os áudios, agenda, confirma e manda lembrete, inclusive pra quem vem do interior do estado."),
            ("Consultórios de dentista", "Avaliação, orçamento de tratamento, retorno: o agente responde na hora e já agenda, e a automação lembra o paciente da consulta e de voltar pra manutenção."),
            ("Lojas do Centro, da Zona Sul e da Zona Leste", "Site com os seus produtos no Google e um agente respondendo preço, estoque e entrega no WhatsApp e no Instagram, pra loja continuar vendendo depois que fecha as portas."),
            ("Prestadores de serviço", "Orçamento rápido, agenda de visitas organizada e retorno automático pra quem pediu e sumiu. Nenhuma venda fica pelo caminho."),
        ],
        "faq_extra": ("A MedCode é de Porto Velho?", "O fundador é. Paulo Nogueira nasceu e cresceu em Porto Velho e hoje está em São Paulo. O atendimento é por vídeo e WhatsApp, feito por quem conhece a cidade e o jeito de vender daqui."),
    },
    {
        "slug": "rio-branco", "nome": "Rio Branco", "uf": "AC", "estado": "Acre", "grupo": "longe", "regiao": "Norte", "fuso": 2,
        "lead": "Rio Branco concentra boa parte do comércio, dos serviços e da saúde do Acre. A MedCode ajuda as empresas daqui a atender mais rápido no WhatsApp, aparecer no Google e organizar a rotina, com atendimento por vídeo, no seu horário.",
        "mercado": [
            "Capital e principal centro econômico do Acre, Rio Branco atende clientes de todo o estado. A ligação por estrada com o Peru ainda abre espaço pra comércio e serviços voltados à fronteira.",
            "Com clientes espalhados e distância grande entre as cidades, o WhatsApp vira o balcão da empresa. Quem atende bem por ele ganha o cliente antes da viagem.",
        ],
        "segmentos": [
            ("Comércio e varejo", "Site com os seus produtos e um agente de IA que atende a capital e o interior pelo WhatsApp e pelo Instagram, numa conversa natural e entendendo até áudio."),
            ("Clínicas e saúde", "Agendamento, confirmação e orientação pra pacientes que vêm de outras cidades, com lembrete automático pra ninguém perder a consulta."),
            ("Prestadores de serviço", "Orçamentos organizados, agenda sob controle e retorno automático pra quem pediu e não respondeu."),
            ("Empresas com clientes no interior", "Automação de pedidos e avisos e um sistema sob medida, pra atender quem está longe com a mesma agilidade de quem está na cidade."),
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
            ("Comércio e lojas", "Site com os produtos e um agente que responde sobre preço, estoque e entrega no WhatsApp e no Instagram, a qualquer hora e sem menu de “digite 1”."),
            ("Clínicas e saúde", "Agenda organizada, confirmação e lembrete automáticos, e um agente que conversa com o paciente como uma recepcionista atenciosa."),
            ("Turismo e gastronomia", "Reservas e dúvidas respondidas na hora e um site que aparece pra quem está chegando na cidade e pesquisa no celular."),
            ("Prestadores de serviço", "Orçamento pelo WhatsApp, agenda organizada e retorno automático pra quem sumiu, sem perder venda."),
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
            ("Agronegócio e revendas", "Sistema sob medida pra pedidos e estoque e um agente que atende o produtor na hora, entendendo até os áudios mandados do campo."),
            ("Comércio e varejo", "Site, perfil no Google e um agente que responde sobre produtos e entrega a qualquer hora, pra atender uma cidade que não para de crescer."),
            ("Clínicas e saúde", "Agendamento pelo WhatsApp numa conversa natural, confirmação e lembrete automáticos, e menos faltas na agenda."),
            ("Prestadores de serviço", "Orçamentos organizados e agenda sob controle mesmo com o volume crescendo, e consultoria de gestão pra estruturar a empresa pra esse crescimento."),
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
            ("Escritórios e serviços profissionais", "Advocacia, contabilidade e consultorias: site que passa credibilidade, agente que faz a triagem do primeiro contato e consultoria de gestão pra organizar processos e equipe."),
            ("Agronegócio", "Sistemas sob medida e automação pra revendas e fornecedores que atendem o campo, com pedidos, estoque e entregas num painel só."),
            ("Clínicas e saúde", "Agendamento, confirmação e lembrete automáticos no WhatsApp, com um agente que conversa de verdade e entende áudio."),
            ("Gastronomia e lazer", "Reservas e cardápio respondidos a qualquer hora, inclusive nos fins de semana nas praias do lago, e um site que aparece pra quem procura onde ir."),
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
            ("Clínicas e saúde", "Pacientes chegam de todo o Piauí e de estados vizinhos. O agente de IA agenda, confirma e orienta antes da viagem, conversando como uma recepcionista e entendendo até os áudios."),
            ("Educação e cursos", "Dúvidas sobre turmas, valores e matrícula respondidas na hora no WhatsApp e no Instagram, com os interessados indo direto pra secretaria."),
            ("Comércio e varejo", "Site que coloca a sua loja no Google e atendimento organizado pra vender pra capital e pro interior."),
            ("Prestadores de serviço", "Orçamento organizado, agenda sob controle e retorno automático, sem perder nenhum pedido."),
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
            ("Turismo e hospedagem", "Pousadas, agências e passeios: o turista manda mensagem a qualquer hora, e o agente responde sobre disponibilidade, valores e roteiros numa conversa natural, até por áudio."),
            ("Clínicas e saúde", "Agendamento, confirmação e lembrete automáticos no WhatsApp, com a recepção livre pra quem está na clínica."),
            ("Comércio e varejo", "Site, catálogo e atendimento no Instagram e no WhatsApp com agente de IA respondendo na hora."),
            ("Serviços e logística", "Sistemas sob medida e automação pra controlar pedidos, entregas e equipe, sem planilha e sem retrabalho."),
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
            ("Turismo e gastronomia na orla", "Reservas, cardápio e horários respondidos a qualquer hora pelo agente de IA, e um site que aparece pra quem está na cidade procurando onde ir."),
            ("Clínicas e saúde", "Agendamento pelo WhatsApp numa conversa natural, confirmação e lembrete automáticos, e menos faltas."),
            ("Comércio e varejo", "Atendimento no Instagram e no WhatsApp com um agente de IA que entende o que o cliente escreve, e até os áudios, e site com os seus produtos."),
            ("Serviços profissionais", "Escritórios e consultorias com site que passa credibilidade, triagem do primeiro contato e consultoria de gestão pra organizar a casa."),
        ],
        "faq_extra": ("Vocês atendem outras cidades de Sergipe?", "Sim. O atendimento é por vídeo e WhatsApp, então atendemos empresas de Aracaju e de qualquer cidade do estado."),
    },
]
