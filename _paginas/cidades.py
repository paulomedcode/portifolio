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
        "lead": "Sorocaba é um dos maiores polos de indústria e comércio do interior paulista, e por isso a concorrência também é grande: quem procura um serviço aqui tem muitas opções. A MedCode ajuda a sua empresa a ser encontrada primeiro e a responder antes do concorrente.",
        "mercado": [
            "Indústrias, um parque tecnológico, universidades, uma rede de saúde grande e um comércio que atende toda a região metropolitana. Sorocaba tem empresas de todos os tamanhos disputando o mesmo cliente.",
            "Nesse cenário, o que decide é velocidade e presença: aparecer quando alguém pesquisa o seu serviço na cidade e responder na hora, inclusive fora do horário comercial.",
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
        "lead": "Itapetininga é referência no sudoeste paulista, com agronegócio forte e um comércio que atende cidades de toda a região. A MedCode leva pras empresas daqui as mesmas ferramentas que as grandes usam: site, agente de IA no WhatsApp, automação e sistemas sob medida.",
        "mercado": [
            "Boa parte dos clientes de Itapetininga vem das cidades vizinhas e do campo. Pra esse cliente, o WhatsApp é o principal canal: ele pergunta preço, disponibilidade e prazo antes de pegar a estrada.",
            "Responder rápido e com informação certa é o que garante a venda, e é exatamente onde um agente de IA e uma boa organização interna fazem diferença.",
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
        "lead": "Vizinha de Sorocaba, Votorantim tem tradição industrial e um comércio local que disputa cliente com a cidade ao lado. Pra quem empreende aqui, aparecer no Google na hora da busca e responder rápido no WhatsApp faz toda a diferença.",
        "mercado": [
            "Berço de um dos maiores grupos industriais do país, Votorantim cresceu junto com Sorocaba, e muita gente mora em uma cidade e consome na outra.",
            "Por isso, a empresa daqui precisa aparecer nas buscas das duas cidades. A represa de Itupararanga ainda movimenta turismo, gastronomia e lazer no fim de semana.",
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
        "lead": "Itu une centro histórico, turismo, eventos e uma indústria forte. É uma cidade em que o cliente pesquisa bastante antes de escolher, e acaba fechando com quem aparece bem e responde primeiro.",
        "mercado": [
            "Turistas que vêm conhecer a cidade, noivos procurando espaço pra casamento, moradores dos condomínios buscando serviços: em Itu, muita venda começa numa pesquisa no Google e numa mensagem no WhatsApp.",
            "Muitas dessas mensagens chegam à noite e no fim de semana, justamente quando ninguém está pra responder.",
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
        "lead": "Botucatu é polo universitário e de saúde do interior paulista, com uma economia que vai da indústria aeronáutica ao turismo da Cuesta. Chega muita gente de fora, e quem vem de fora pesquisa no Google.",
        "mercado": [
            "A universidade e o hospital universitário atraem estudantes, profissionais e pacientes de toda a região. Isso movimenta clínicas, moradia, alimentação e serviços o ano inteiro.",
            "Pra quem chega na cidade, o primeiro contato com o seu negócio é quase sempre uma busca no celular, seguida de uma mensagem no WhatsApp.",
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
        "lead": "Rio Branco concentra boa parte do comércio, dos serviços e da saúde do Acre. A MedCode ajuda as empresas daqui a atender mais rápido no WhatsApp, aparecer no Google e organizar a rotina, com atendimento por vídeo, no seu horário.",
        "mercado": [
            "Capital e principal centro econômico do Acre, Rio Branco atende clientes de todo o estado. A ligação por estrada com o Peru ainda abre espaço pra comércio e serviços voltados à fronteira.",
            "Com clientes espalhados e distância grande entre as cidades, o WhatsApp vira o balcão da empresa. Quem atende bem por ele ganha o cliente antes da viagem.",
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
        "lead": "Macapá, a capital do meio do mundo, tem um comércio movimentado e um setor de serviços que cresce junto com o Amapá. A MedCode ajuda as empresas daqui a vender e atender melhor pelo WhatsApp e pelo Google.",
        "mercado": [
            "Cortada pela Linha do Equador, Macapá é o centro econômico do Amapá. Com Santana ao lado e a área de livre comércio, o varejo é forte e a disputa por cliente também.",
            "Turismo, gastronomia e serviços completam a economia. Em todos eles, o cliente pesquisa no celular e espera resposta rápida.",
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
        "lead": "Boa Vista é uma capital que cresceu rápido nos últimos anos, com agronegócio em expansão e comércio forte. A MedCode ajuda as empresas daqui a acompanhar esse crescimento com site, agente de IA no WhatsApp, automação e sistemas.",
        "mercado": [
            "Capital planejada de Roraima, Boa Vista concentra o comércio e os serviços do estado. A expansão das lavouras e a posição na fronteira com a Venezuela e a Guiana trouxeram mais gente e mais negócios.",
            "Cidade crescendo rápido significa cliente novo chegando todo dia, e esse cliente procura no Google e chama no WhatsApp antes de escolher.",
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
        "lead": "Palmas é a capital mais nova do Brasil: uma cidade planejada, jovem e conectada. A MedCode ajuda as empresas daqui a aparecer no Google, atender no WhatsApp com agente de IA e organizar a gestão.",
        "mercado": [
            "Fundada no fim dos anos 1980, Palmas tem economia puxada pelo serviço público, pelo agronegócio do Tocantins e por um comércio que atende o estado todo.",
            "É uma cidade de população jovem, que resolve tudo pelo celular. Pra quem empreende aqui, presença digital bem feita já é o básico.",
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
        "lead": "Teresina é referência em saúde e educação no Nordeste e recebe pacientes e estudantes de vários estados. A MedCode ajuda as empresas daqui a atender esse volume com agente de IA no WhatsApp, site, automação e sistemas.",
        "mercado": [
            "Entre os rios Poti e Parnaíba, a capital do Piauí virou polo regional: hospitais, clínicas e faculdades atraem gente do interior do estado e dos estados vizinhos.",
            "Isso significa muita mensagem chegando de quem ainda não conhece a cidade, com dúvidas sobre agenda, preços e como chegar. Quem responde rápido e bem fica com o cliente.",
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
        "lead": "São Luís junta patrimônio histórico, turismo, porto e um comércio que atende todo o Maranhão. A MedCode ajuda as empresas daqui a aparecer no Google, atender mais rápido no WhatsApp e organizar a operação.",
        "mercado": [
            "Capital construída numa ilha e com centro histórico reconhecido como patrimônio mundial, São Luís recebe turistas o ano todo e é a porta de entrada pra outros destinos do estado.",
            "O complexo portuário e a força do comércio completam uma economia variada, com espaço pra empresas de todos os tamanhos.",
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
        "lead": "Aracaju é uma capital com qualidade de vida, turismo na orla e um setor de serviços forte. A MedCode ajuda as empresas daqui a ser encontradas no Google e a atender pelo WhatsApp com agente de IA, automação e sistemas.",
        "mercado": [
            "Com a orla de Atalaia, a gastronomia e o turismo, Aracaju recebe visitantes o ano todo. Ao mesmo tempo, é o centro de comércio, saúde e serviços de Sergipe.",
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
]
