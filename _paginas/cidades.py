"""Conteúdo das páginas de cidade (usado por gerar.py).

Cada cidade precisa de texto próprio: página igual trocando só o nome o Google ignora.
grupo: "sp" (atendimento presencial possível na região) ou "longe" (por vídeo e WhatsApp).
mercado: dois parágrafos sobre o comércio e o cliente da cidade (do dia a dia, não de enciclopédia). A abertura da página é a história do fundador,
adaptada pela região em gerar.py (LEAD_FUNDADOR), ou "lead_fundador" quando a cidade tem a sua própria.
fuso: diferença em horas para Brasília, quando houver (aparece nas dúvidas).
"""

CIDADES = [
    # ------------------------------------------------------------ interior de São Paulo
    {
        "slug": "tatui", "nome": "Tatuí", "uf": "SP", "estado": "São Paulo", "grupo": "sp", "regiao": "Interior de São Paulo",
        "mercado": [
            "Tatuí é cidade de comércio de rua e de indicação. No centro e nos bairros, são lojas, clínicas, escolas, salões e prestadores de serviço disputando o cliente da cidade e das cidades vizinhas.",
            "O cliente de Tatuí pode até chegar por indicação, mas antes de fechar ele pesquisa no Google e chama no WhatsApp. Quem aparece bem e responde rápido sai na frente de quem ainda atende do jeito antigo.",
        ],
        "nichos": {
            "agente": "escolas de música, clínicas, salões de beleza e pet shops",
            "site": "lojas do centro, escolas e prestadores de serviço",
            "automacao": "clínicas, escolas e salões de beleza",
            "sistemas": "lojas, distribuidoras e escolas",
            "consultoria": "comércios e empresas familiares",
        },
        "faq_extra": ("Vocês fazem reunião presencial em Tatuí?", "Sim. Tatuí fica na nossa região de atendimento presencial, então o diagnóstico e as visitas podem ser feitos no seu negócio. O dia a dia segue pelo WhatsApp."),
    },
    {
        "slug": "sorocaba", "nome": "Sorocaba", "uf": "SP", "estado": "São Paulo", "grupo": "sp", "regiao": "Interior de São Paulo",
        "mercado": [
            "Sorocaba é cidade grande, com indústria, shoppings, universidades e um comércio que atende toda a região. Pra quem empreende aqui, a concorrência é pesada: o cliente encontra várias opções na mesma busca.",
            "Ganha quem aparece primeiro no Google e responde antes, inclusive à noite e no fim de semana, quando a concorrência está fechada.",
        ],
        "nichos": {
            "agente": "clínicas, imobiliárias, academias e pet shops",
            "site": "indústrias, escritórios, clínicas e lojas",
            "automacao": "clínicas, academias e prestadores de serviço",
            "sistemas": "indústrias, distribuidoras e redes de lojas",
            "consultoria": "empresas que cresceram rápido e comércios familiares",
        },
        "faq_extra": ("Vocês atendem toda a região de Sorocaba?", "Sim. Atendemos Sorocaba e as cidades da região, como Votorantim, Itu, Tatuí e Itapetininga, com diagnóstico e visitas presenciais quando fizer sentido."),
    },
    {
        "slug": "itapetininga", "nome": "Itapetininga", "uf": "SP", "estado": "São Paulo", "grupo": "sp", "regiao": "Interior de São Paulo",
        "mercado": [
            "Itapetininga é o centro de compras de uma região inteira. Revendas agrícolas, lojas, clínicas e oficinas atendem gente da cidade, das cidades vizinhas e da zona rural.",
            "Esse cliente não quer pegar a estrada à toa: ele pergunta preço, estoque e prazo pelo WhatsApp antes de sair de casa. Quem responde rápido e com informação certa fica com a venda.",
        ],
        "nichos": {
            "agente": "revendas agrícolas, clínicas, lojas e oficinas",
            "site": "comércio regional, revendas e prestadores de serviço",
            "automacao": "clínicas, revendas e oficinas",
            "sistemas": "revendas agrícolas, distribuidoras e lojas",
            "consultoria": "comércios regionais e negócios do agro",
        },
        "faq_extra": ("Vocês atendem presencialmente em Itapetininga?", "Sim. Itapetininga está na nossa região de atendimento presencial. Fazemos o diagnóstico no seu negócio e seguimos o acompanhamento pelo WhatsApp."),
    },
    {
        "slug": "votorantim", "nome": "Votorantim", "uf": "SP", "estado": "São Paulo", "grupo": "sp", "regiao": "Interior de São Paulo",
        "mercado": [
            "Votorantim vive colada em Sorocaba: muita gente mora numa cidade e compra na outra. Comércio de bairro, salões, clínicas e restaurantes disputam esse cliente o tempo todo, e a represa enche pousadas e restaurantes no fim de semana.",
            "Por isso, aparecer no Google pra quem pesquisa nas duas cidades e responder rápido no WhatsApp faz toda a diferença.",
        ],
        "nichos": {
            "agente": "pousadas, restaurantes, salões de beleza e pet shops",
            "site": "comércio de bairro, restaurantes e prestadores de serviço",
            "automacao": "salões, clínicas e restaurantes",
            "sistemas": "fornecedores da indústria e lojas",
            "consultoria": "comércios de bairro e empresas familiares",
        },
        "faq_extra": ("Atendo clientes de Votorantim e de Sorocaba. O site serve pras duas?", "Serve. O site e o seu perfil no Google podem mostrar que você atende as duas cidades e a região, pra aparecer nas buscas de quem está em qualquer uma delas."),
    },
    {
        "slug": "itu", "nome": "Itu", "uf": "SP", "estado": "São Paulo", "grupo": "sp", "regiao": "Interior de São Paulo",
        "mercado": [
            "Itu tem um movimento que pouca cidade do interior tem: turista no fim de semana, casamento e evento o ano todo, condomínio cheio de morador procurando serviço e um comércio forte no centro.",
            "Muita venda aqui começa numa pesquisa no Google e numa mensagem no WhatsApp, e boa parte chega à noite e no fim de semana, justamente quando ninguém está pra responder.",
        ],
        "nichos": {
            "agente": "espaços de eventos, buffets, restaurantes e clínicas de estética",
            "site": "eventos, gastronomia, turismo e serviços",
            "automacao": "buffets, clínicas de estética e serviços pra condomínios",
            "sistemas": "empresas de eventos, indústrias e lojas",
            "consultoria": "negócios de turismo e eventos e empresas familiares",
        },
        "faq_extra": ("Funciona pra espaço de eventos e buffet?", "Funciona muito bem. O agente responde as perguntas de sempre (datas livres, capacidade, valores de referência) e passa pra você o contato já qualificado, pronto pra visita."),
    },
    {
        "slug": "botucatu", "nome": "Botucatu", "uf": "SP", "estado": "São Paulo", "grupo": "sp", "regiao": "Interior de São Paulo",
        "mercado": [
            "Botucatu recebe gente de fora o tempo todo: estudantes, pacientes da região que vêm se tratar na cidade e turistas atrás das trilhas e cachoeiras. Isso movimenta clínicas, imobiliárias, cursos, pousadas e o comércio o ano inteiro.",
            "Pra quem chega, o primeiro contato com o seu negócio é quase sempre uma busca no celular, seguida de uma mensagem no WhatsApp.",
        ],
        "nichos": {
            "agente": "clínicas, imobiliárias, cursos e pousadas",
            "site": "clínicas, pousadas, comércio e serviços",
            "automacao": "clínicas, cursos e imobiliárias",
            "sistemas": "clínicas, lojas e empresas de serviço",
            "consultoria": "clínicas e comércios que querem crescer",
        },
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
        "nichos": {
            "agente": "clínicas médicas, dentistas, pastelarias, pet shops e lojas",
            "site": "lojas do Centro, da Zona Sul e da Zona Leste, clínicas e prestadores de serviço",
            "automacao": "clínicas, consultórios de dentista e salões de beleza",
            "sistemas": "lojas, distribuidoras e clínicas",
            "consultoria": "comércios e clínicas que cresceram sem processo",
        },
        "faq_extra": ("A MedCode é de Porto Velho?", "O fundador é. Paulo Nogueira nasceu e cresceu em Porto Velho e hoje está em São Paulo. O atendimento é por vídeo e WhatsApp, feito por quem conhece a cidade e o jeito de vender daqui."),
    },
    {
        "slug": "rio-branco", "nome": "Rio Branco", "uf": "AC", "estado": "Acre", "grupo": "longe", "regiao": "Norte", "fuso": 2,
        "mercado": [
            "Rio Branco concentra o comércio, as clínicas e os serviços do Acre. Quem mora no interior resolve muita coisa na capital, e quem mora na capital compra de tudo pelo WhatsApp.",
            "Com clientes espalhados e distância grande entre as cidades, o WhatsApp vira o balcão da empresa. Quem atende bem por ele ganha o cliente antes mesmo da viagem.",
        ],
        "nichos": {
            "agente": "clínicas, lojas, restaurantes e pet shops",
            "site": "comércio, clínicas e prestadores de serviço",
            "automacao": "clínicas e empresas que atendem o interior do estado",
            "sistemas": "distribuidoras, lojas e clínicas",
            "consultoria": "comércios e empresas familiares",
        },
        "faq_extra": ("A diferença de fuso atrapalha?", "Não. Rio Branco está 2 horas atrás de Brasília, e as reuniões são marcadas no seu horário. O agente de IA atende 24 horas, então o fuso nem aparece pro seu cliente."),
    },
    {
        "slug": "macapa", "nome": "Macapá", "uf": "AP", "estado": "Amapá", "grupo": "longe", "regiao": "Norte",
        "mercado": [
            "Macapá é cidade de comércio forte: lojas, clínicas, restaurantes e prestadores de serviço disputam o cliente da capital e de Santana, ali do lado.",
            "E o cliente daqui pesquisa no celular e espera resposta rápida no WhatsApp e no Instagram. Quem demora perde a venda pra loja ao lado.",
        ],
        "nichos": {
            "agente": "lojas, clínicas, restaurantes e pet shops",
            "site": "comércio, turismo e gastronomia",
            "automacao": "clínicas, salões de beleza e lojas",
            "sistemas": "lojas, distribuidoras e clínicas",
            "consultoria": "comércios e empresas familiares",
        },
        "faq_extra": ("Atendem também Santana e outras cidades do Amapá?", "Sim. O atendimento é por vídeo e WhatsApp, então atendemos empresas de qualquer cidade do Amapá."),
    },
    {
        "slug": "boa-vista", "nome": "Boa Vista", "uf": "RR", "estado": "Roraima", "grupo": "longe", "regiao": "Norte", "fuso": 1,
        "mercado": [
            "Boa Vista cresceu rápido nos últimos anos e não para: chegou gente nova, abriram lojas, clínicas e empresas de serviço, e o agro do estado puxa o comércio junto.",
            "Cidade crescendo significa cliente novo todo dia, e esse cliente ainda não tem indicação: ele procura no Google e chama no WhatsApp antes de escolher.",
        ],
        "nichos": {
            "agente": "revendas agrícolas, clínicas, lojas e pet shops",
            "site": "comércio, agro e prestadores de serviço",
            "automacao": "clínicas e prestadores de serviço",
            "sistemas": "revendas, distribuidoras e lojas",
            "consultoria": "empresas crescendo rápido junto com a cidade",
        },
        "faq_extra": ("A diferença de fuso atrapalha?", "Não. Boa Vista está 1 hora atrás de Brasília, e as reuniões são marcadas no seu horário. E o agente de IA atende o seu cliente 24 horas."),
    },
    {
        "slug": "palmas", "nome": "Palmas", "uf": "TO", "estado": "Tocantins", "grupo": "longe", "regiao": "Norte",
        "mercado": [
            "Palmas é uma capital jovem, com muito escritório, clínica, restaurante e comércio atendendo uma população que resolve tudo pelo celular.",
            "Aqui, presença digital bem feita já é o básico: quem não aparece no Google e demora no WhatsApp nem entra na disputa.",
        ],
        "nichos": {
            "agente": "escritórios de advocacia, clínicas, restaurantes e pet shops",
            "site": "escritórios, consultorias, clínicas e restaurantes",
            "automacao": "clínicas, escritórios e restaurantes",
            "sistemas": "revendas do agro, lojas e escritórios",
            "consultoria": "escritórios e comércios em crescimento",
        },
        "faq_extra": ("Vocês atendem outras cidades do Tocantins?", "Sim. Como o atendimento é por vídeo e WhatsApp, atendemos empresas de Palmas e de qualquer cidade do estado."),
    },
    # ------------------------------------------------------------ Nordeste
    {
        "slug": "teresina", "nome": "Teresina", "uf": "PI", "estado": "Piauí", "grupo": "longe", "regiao": "Nordeste",
        "mercado": [
            "Teresina é referência em saúde e educação: chegam pacientes e estudantes do interior do Piauí e dos estados vizinhos, e isso movimenta clínicas, laboratórios, cursos e o comércio da cidade.",
            "Quem vem de fora manda mensagem antes de viajar, com dúvidas sobre agenda, preço e como chegar. Quem responde rápido e bem fica com o cliente.",
        ],
        "nichos": {
            "agente": "clínicas, laboratórios, cursos e pet shops",
            "site": "clínicas, escolas, comércio e serviços",
            "automacao": "clínicas, laboratórios e cursos",
            "sistemas": "clínicas, escolas e lojas",
            "consultoria": "clínicas e comércios que querem crescer com organização",
        },
        "faq_extra": ("Funciona pra clínica que atende paciente de outras cidades?", "Muito bem. O agente tira as dúvidas antes da viagem, agenda, confirma e manda lembrete, o que ajuda a reduzir as faltas de quem vem de longe."),
    },
    {
        "slug": "sao-luis", "nome": "São Luís", "uf": "MA", "estado": "Maranhão", "grupo": "longe", "regiao": "Nordeste",
        "mercado": [
            "São Luís concentra o comércio e os serviços do Maranhão e recebe turista o ano todo. Pousadas, agências, restaurantes, clínicas e lojas disputam um cliente que pesquisa tudo no celular.",
            "O turista manda mensagem a qualquer hora, e o morador também. A empresa que responde na hora e aparece bem no Google sai na frente.",
        ],
        "nichos": {
            "agente": "pousadas, agências de turismo, clínicas e pet shops",
            "site": "turismo, hospedagem, comércio e serviços",
            "automacao": "pousadas, clínicas e lojas",
            "sistemas": "empresas de logística, lojas e clínicas",
            "consultoria": "comércios e empresas familiares",
        },
        "faq_extra": ("Funciona pra pousada e agência de turismo?", "Funciona. O turista manda mensagem em qualquer horário. O agente responde sobre disponibilidade, valores e passeios, e passa pra você a reserva quase pronta."),
    },
    {
        "slug": "aracaju", "nome": "Aracaju", "uf": "SE", "estado": "Sergipe", "grupo": "longe", "regiao": "Nordeste",
        "mercado": [
            "Aracaju junta turismo na orla e um comércio forte de clínicas, lojas, escritórios e restaurantes, que atende a capital e o interior de Sergipe.",
            "Seja o turista procurando onde comer, seja o morador procurando uma clínica, a busca começa no celular. Aparecer bem e responder rápido é o que transforma busca em cliente.",
        ],
        "nichos": {
            "agente": "restaurantes da orla, clínicas, pet shops e lojas",
            "site": "turismo, gastronomia, comércio e escritórios",
            "automacao": "clínicas, restaurantes e salões de beleza",
            "sistemas": "lojas, clínicas e escritórios",
            "consultoria": "escritórios e comércios em crescimento",
        },
        "faq_extra": ("Vocês atendem outras cidades de Sergipe?", "Sim. O atendimento é por vídeo e WhatsApp, então atendemos empresas de Aracaju e de qualquer cidade do estado."),
    },
    {
        "slug": "jericoacoara", "nome": "Jericoacoara", "uf": "CE", "estado": "Ceará", "grupo": "longe", "regiao": "Nordeste",
        "mercado": [
            "Em Jeri, quase tudo gira em torno do turista: pousadas, restaurantes, agências de passeio, buggueiros, escolas de kite e lojinhas da vila disputam um visitante que fica poucos dias e decide rápido.",
            "E esse turista resolve tudo pelo celular, muitas vezes antes de chegar: manda mensagem no WhatsApp e no Instagram perguntando disponibilidade, preço e como chegar. Quem responde primeiro, mesmo de madrugada, fecha a reserva.",
        ],
        "nichos": {
            "agente": "pousadas, restaurantes, agências de passeio e escolas de kite",
            "site": "pousadas, restaurantes, passeios e lojas da vila",
            "automacao": "pousadas, agências de passeio e restaurantes",
            "sistemas": "pousadas, agências e restaurantes",
            "consultoria": "pousadas e negócios de turismo que querem crescer com organização",
        },
        "faq_extra": ("Funciona pra pousada e agência de passeio em Jeri?", "Muito bem. O turista manda mensagem a qualquer hora, de qualquer lugar do Brasil. O agente responde sobre disponibilidade, valores e passeios na hora, e passa pra você a reserva quase pronta."),
    },
]
