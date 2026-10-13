#!/usr/bin/env python3
"""Gera as páginas internas do site (serviços, cidades e "onde atendemos") a partir do conteúdo deste arquivo.

Uso:  python3 _paginas/gerar.py
Cada página vira um .html na raiz do projeto (a Vercel serve /criacao-de-sites a partir de criacao-de-sites.html)
as cidades vão pra cidades/<slug>.html, e o sitemap.xml é refeito com todas elas.
O texto das cidades fica em _paginas/cidades.py. Edite o texto aqui, nunca direto no .html gerado.
A pasta _paginas não vai pro ar (está no .vercelignore).
"""
import html
import json
from datetime import date
from pathlib import Path
from urllib.parse import quote

from cidades import CIDADES

RAIZ = Path(__file__).resolve().parent.parent
SITE = "https://medcodedev.com"
WHATS = "5511991649612"
HOJE = date.today().isoformat()


def wa(texto, origem):
    """Link de WhatsApp com mensagem pronta; o data-origem alimenta o evento do analytics em js/site.js."""
    return (f'href="https://wa.me/{WHATS}?text={quote(texto)}" target="_blank" rel="noopener" '
            f'data-origem="{origem}"')


def attr(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- conteúdo das páginas de serviço
# Campos em HTML (lead, p, a) aceitam <strong>/<b>; os de texto puro são escapados.

SERVICOS = [
    {
        "slug": "criacao-de-sites",
        "pitch": 'Um site profissional, feito primeiro pro celular e preparado pro Google, pra quem pesquisa o seu serviço na cidade encontrar você. Cada botão leva direto pro seu WhatsApp, e o visitante pode tirar dúvidas ali mesmo com o seu agente de IA.',
        "beneficios": ['Aparece no Google pra quem busca na sua cidade', 'Visual profissional que passa confiança', 'Domínio sempre no nome da sua empresa'],
        "nome": "Criação de sites e landing pages",
        "curto": "Sites e landing pages",
        "resumo": "Site profissional, rápido no celular e pronto pro Google, levando o cliente pro WhatsApp.",
        "title": "Criação de Sites e Landing Pages | MedCode Assessoria",
        "desc": "Criação de sites e landing pages para pequenas e médias empresas: rápidos no celular, prontos para o Google e ligados ao seu WhatsApp. A partir de R$ 400.",
        "h1": "Criação de sites e landing pages que levam o cliente pro seu WhatsApp",
        "lead": "Um site profissional, rápido no celular e preparado pro Google, feito pra quem procura o seu serviço <strong>achar você e chamar na hora</strong>. Atendemos pequenas e médias empresas de todo o Brasil.",
        "oferta": ["Site ou landing page com a cara da sua marca", "Pensado primeiro pro celular", "Estrutura otimizada pro Google",
                   "Botões e chat levando pro WhatsApp", "Domínio sempre no nome da sua empresa"],
        "preco": "a partir de <b>R$ 400</b>",
        "preco_nota": "",
        "selo": "<b>Grátis</b> no combo com o agente de IA, fechando 6 meses de agente gerenciado pela MedCode.",
        "cta": ("Quero um site", "Oi! Quero saber mais sobre um site para o meu negócio."),
        "dores_titulo": "Um site faz falta quando…",
        "dores": [
            ("“Meu cliente não me acha no Google”", "Quem pesquisa o seu serviço na sua cidade encontra o concorrente. Um site bem estruturado é o primeiro passo pra aparecer nessa busca."),
            ("“Só tenho Instagram”", "O Instagram é ótimo pra mostrar o trabalho, mas aparece pouco no Google e as regras são dele. O site é o seu endereço próprio na internet."),
            ("“Meu site é antigo e não traz nada”", "Lento, ruim no celular e sem um caminho claro pro WhatsApp: o visitante chega, não acha o que queria e vai embora."),
            ("“Vou lançar um serviço e preciso divulgar”", "Uma landing page focada numa oferta só, pronta pra receber quem vem dos anúncios no Google e no Instagram."),
        ],
        "vs": {
            "kicker": "Site ou landing page?",
            "titulo": "Qual dos dois o seu negócio precisa",
            "a": ("Site institucional", "Várias páginas: início, serviços, sobre, contato.",
                  ["Apresenta a empresa inteira", "Ajuda a aparecer no Google com vários serviços", "Passa credibilidade pra quem está pesquisando", "Bom pra quem quer presença duradoura"]),
            "b": ("Landing page", "Uma página só, com um único objetivo: fazer o visitante chamar no WhatsApp.",
                  ["Focada em uma oferta ou serviço", "Ideal pra anúncios e lançamentos", "Fica pronta mais rápido", "Fácil de medir quantos contatos trouxe"]),
            "ruim": False,
            "nota": "<b>Não sabe qual escolher?</b> No diagnóstico gratuito a gente olha o seu momento e indica o caminho.",
        },
        "itens_titulo": "O que vem no seu site",
        "itens": [
            ("Visual profissional", "Layout com a cara da sua marca, não um modelo genérico igual ao de todo mundo."),
            ("Feito primeiro pro celular", "A maioria dos seus clientes vai abrir pelo celular, então é por ele que a gente começa."),
            ("Pronto pro Google", "Títulos, descrições, velocidade e dados estruturados pro Google entender o que você faz e onde atende."),
            ("Tudo leva pro WhatsApp", "Botões nos pontos certos, com a mensagem já escrita, pro cliente chamar em um toque."),
            ("Chat com agente de IA", "Se quiser, o visitante tira dúvidas ali mesmo no site, a qualquer hora, com o seu agente de IA."),
            ("Domínio no seu nome", "O endereço (seunegocio.com.br) fica registrado no nome da sua empresa. É seu, não nosso."),
        ],
        "passos": [
            ("Diagnóstico gratuito", "Entendemos o seu negócio, quem é o seu cliente e o que o site precisa fazer por você."),
            ("Proposta clara", "Você recebe prazo e valor por escrito, sem letras miúdas, antes de fechar."),
            ("Criação com você", "Você acompanha, dá opinião e pede ajustes antes de o site ir ao ar."),
            ("No ar e acompanhado", "Publicamos, deixamos tudo pronto pro Google e seguimos por perto pra ajustar."),
        ],
        "faq": [
            ("Quanto custa um site?", "A partir de R$ 400. O valor final depende do número de páginas e do que o site precisa ter, e você recebe a proposta exata antes de fechar. Fechando 6 meses de agente de IA gerenciado pela MedCode, o site sai grátis."),
            ("Quanto tempo leva pra ficar pronto?", "Trabalhamos com entregas em dias, não em meses. O prazo exato depende do tamanho do site e já vem escrito na proposta."),
            ("O site vai aparecer no Google?", "O site sai com toda a estrutura que o Google precisa pra entender o seu negócio e a região onde você atende. Chegar ao topo também depende da concorrência e de tempo, mas sem essa base não tem como aparecer."),
            ("O domínio fica no meu nome?", "Sempre. O endereço do site é registrado no nome da sua empresa. Se um dia você quiser seguir com outra pessoa, ele continua seu."),
            ("Preciso mandar textos e fotos?", "Você conta como o seu negócio funciona e a gente organiza os textos. Fotos reais do seu trabalho deixam o site muito melhor; se você não tiver, ajudamos a resolver."),
            ("E se eu quiser mudar algo depois?", "Ajustes depois da entrega fazem parte do nosso acompanhamento. Mudanças maiores, como páginas novas, a gente combina à parte."),
        ],
    },
    {
        "slug": "agente-de-ia-para-whatsapp",
        "pitch": 'Não é aquele chatbot de “digite 1, digite 2”. É como uma secretária inteligente: conversa de forma natural, entende o que o cliente escreve do jeito dele e até ouve os áudios. Responde na hora, de dia, de noite e no fim de semana, e passa a conversa pra você quando precisa.',
        "beneficios": ['Entende texto e áudio, sem menu de opções', 'Agenda, confirma e manda lembrete sozinho', 'Atende no WhatsApp, no Instagram e no site'],
        "nome": "Agente de IA para WhatsApp, Instagram e site",
        "curto": "Agente de IA para WhatsApp",
        "resumo": "Atende seus clientes 24 horas no WhatsApp, Instagram e site: tira dúvidas, agenda e passa pra você.",
        "title": "Agente de IA para WhatsApp, Instagram e Site | MedCode",
        "desc": "Agente de IA que atende seus clientes no WhatsApp, Instagram e site 24 horas: tira dúvidas, agenda e passa pra você quando precisa. A partir de R$ 147/mês, com garantia.",
        "h1": "Agente de IA para WhatsApp que atende seus clientes 24 horas",
        "lead": "Não é aquele robô do “digite 1”. É uma <strong>secretária inteligente</strong> que conversa de verdade, entende o que o cliente escreve (e até os áudios) e resolve na hora, no WhatsApp, no Instagram e no seu site. Quando precisa de você, passa a conversa.",
        "oferta": ["Conversa natural e entende até áudio", "Tira dúvidas, agenda, confirma e lembra", "Atende no WhatsApp, no Instagram e no site",
                   "Treinado com as informações do seu negócio", "A equipe toda atende junto, no mesmo número"],
        "preco": "plataforma a partir de <b>R$ 147/mês</b>",
        "preco_nota": "+ implantação, com valor no diagnóstico gratuito",
        "garantia": "<b>Garantia de 30 dias:</b> se no primeiro mês o agente não fizer sentido pro seu negócio, devolvemos o valor da implantação.",
        "cta": ("Quero um agente", "Oi! Quero saber mais sobre o agente de IA no WhatsApp."),
        "dores_titulo": "Um agente de IA resolve quando…",
        "dores": [
            ("“Perco cliente porque demoro a responder”", "Quem não recebe resposta rápida chama o próximo da lista. O agente responde em segundos, a qualquer hora."),
            ("“Chega mensagem fora do horário”", "À noite, no fim de semana, no feriado: o agente atende, tira a dúvida e já deixa o horário marcado."),
            ("“Respondo as mesmas perguntas o dia todo”", "Preço, horário, endereço, como funciona. O agente cuida disso e você fica com o que realmente precisa de você."),
            ("“Minha equipe não dá conta do WhatsApp”", "O agente faz a triagem e passa pra pessoa certa só as conversas que pedem atendimento humano."),
        ],
        "vs": {
            "kicker": "Robô de menu x agente de IA",
            "titulo": "Não é chatbot de “digite 1”",
            "a": ("Robô de menu", "O que a maioria das empresas usa hoje.",
                  ["“Digite 1 para agendamento, 2 para…”", "Não entende quando o cliente escreve diferente", "Trava, e o cliente desiste no meio", "Respostas engessadas, sempre iguais"]),
            "b": ("Agente de IA da MedCode", "Uma conversa de verdade, do jeito que o cliente escreve.",
                  ["Conversa natural, sem menu", "Entende o que o cliente quer, por texto ou por áudio", "Tira dúvida, agenda, confirma e manda lembrete", "Passa pra você quando o assunto pede uma pessoa"]),
            "ruim": True,
            "nota": "<b>Quer sentir a diferença?</b> Converse com a Ana, a nossa agente, do jeito que os seus clientes conversariam com o seu.",
        },
        "itens_titulo": "Exemplos por tipo de negócio",
        "itens": [
            ("Clínicas e consultórios", "Agenda consultas, confirma na véspera, manda lembrete e tira dúvidas sobre convênios e preparo."),
            ("Salões e barbearias", "Mostra serviços e valores, encontra um horário livre e lembra o cliente pra ele não faltar."),
            ("Lojas e comércio", "Responde sobre produtos, preços, entrega e pagamento, e passa o pedido pronto pra equipe."),
            ("Prestadores de serviço", "Entende o que o cliente precisa, junta as informações do orçamento e agenda a visita."),
            ("Escritórios e consultorias", "Faz a primeira triagem, explica como funciona o atendimento e marca a reunião."),
            ("Escolas e cursos", "Tira dúvidas sobre turmas, valores e matrícula, e encaminha os interessados pra secretaria."),
        ],
        "passos": [
            ("Diagnóstico gratuito", "Entendemos como o seu atendimento funciona hoje e o que o agente precisa resolver."),
            ("Treinamento", "Montamos o conhecimento do agente com seus serviços, preços, regras e o jeito de falar da sua marca."),
            ("Teste com você", "Antes de ligar pros clientes, você conversa com o agente e aprova as respostas."),
            ("No ar e ajuste fino", "No primeiro mês acompanhamos as conversas de perto e afinamos o que for preciso."),
        ],
        "faq": [
            ("Quanto custa um agente de IA?", "A plataforma custa a partir de R$ 147 por mês, mais a implantação, que tem o valor definido no diagnóstico gratuito. E tem garantia: se no primeiro mês o agente não fizer sentido pro seu negócio, devolvemos o valor da implantação."),
            ("Funciona no meu número de WhatsApp atual?", "Na maioria dos casos, sim. No diagnóstico avaliamos o seu número e indicamos a forma de conexão mais segura pro seu caso."),
            ("O agente entende áudio?", "Entende. O cliente pode mandar áudio, do jeito que já está acostumado no WhatsApp, e o agente compreende e responde normalmente, sem pedir pra ele digitar."),
            ("Atende também no Instagram e no site?", "Sim. O mesmo agente pode responder no WhatsApp, nas mensagens do Instagram e num chat dentro do seu site, com as mesmas informações."),
            ("E se o cliente quiser falar com uma pessoa?", "O agente passa a conversa pra você ou pra sua equipe. Ele também é configurado pra encaminhar quando não sabe a resposta, em vez de chutar."),
            ("O agente pode errar?", "Ele responde com base nas informações que você aprovou. No primeiro mês acompanhamos as conversas de perto justamente pra corrigir o que não estiver do jeito certo."),
            ("Preciso entender de tecnologia?", "Não. Você só precisa conhecer o seu negócio. Toda a parte técnica fica com a gente, e na entrega mostramos como acompanhar as conversas."),
        ],
    },
    {
        "slug": "automacao-para-empresas",
        "pitch": 'As tarefas que se repetem todo dia passam a acontecer sozinhas: lembrete na véspera, retorno pra quem pediu orçamento, contato salvo sem ninguém digitar, aviso pra equipe na hora. Menos erro, menos esquecimento e mais tempo pro que importa.',
        "beneficios": ['Lembretes e confirmações automáticos', 'Nenhum orçamento esquecido', 'Ferramentas que você já usa trabalhando juntas'],
        "nome": "Automação de atendimento e processos",
        "curto": "Automação para empresas",
        "resumo": "Lembretes, retornos, cadastros e tarefas repetitivas rodando sozinhos, sem erro e sem esquecer ninguém.",
        "title": "Automação para Empresas: Atendimento e Processos | MedCode",
        "desc": "Automação de atendimento e de processos para pequenas e médias empresas: lembretes, retorno de orçamentos, cadastro de contatos e tarefas repetitivas rodando sozinhas.",
        "h1": "Automação para empresas: o trabalho repetitivo roda sozinho",
        "lead": "Lembrete de horário, retorno pra quem pediu orçamento, contato do site indo direto pra planilha… Tudo que a sua equipe faz no piloto automático pode ser feito por <strong>automação, sem erro e sem esquecer ninguém</strong>.",
        "oferta": ["Automação de atendimento no WhatsApp", "Lembretes e confirmações automáticas", "Retorno pra quem pediu orçamento e sumiu",
                   "Contatos organizados sem digitar nada", "As ferramentas que você já usa conversando entre si"],
        "preco": "<b>Valor no diagnóstico gratuito</b>",
        "preco_nota": "depende do que vai ser automatizado",
        "cta": ("Quero automatizar", "Oi! Quero saber mais sobre automação para a minha empresa."),
        "dores_titulo": "Sinais de que a sua empresa precisa de automação",
        "dores": [
            ("“Esqueço de dar retorno pro cliente”", "Orçamento enviado, cliente sumiu, e ninguém voltou a falar com ele. Venda que ficou pelo caminho."),
            ("“Passo o dia copiando e colando”", "Do WhatsApp pra planilha, da planilha pro sistema, do sistema pro grupo da equipe. Tempo que podia ir pro cliente."),
            ("“Cliente falta e não avisa”", "Lembrete e confirmação automáticos na véspera ajudam o cliente a lembrar e liberam o horário de quem não vem."),
            ("“Cada ferramenta vive num mundo”", "Agenda, planilha, WhatsApp e sistema que não conversam entre si, e a equipe fazendo a ponte na mão."),
        ],
        "vs": {
            "kicker": "Dois tipos de automação",
            "titulo": "Na frente do cliente e por trás dele",
            "a": ("Automação de atendimento", "O que acontece na conversa com o cliente.",
                  ["Resposta imediata, a qualquer hora", "Agendamento, confirmação e lembrete", "Retorno pra quem pediu orçamento", "Pós-venda e pedido de avaliação"]),
            "b": ("Automação de processos", "O que acontece por trás, na rotina da empresa.",
                  ["Contato cadastrado sozinho na planilha ou no sistema", "Aviso pra equipe quando chega pedido ou agendamento", "Relatórios prontos, sem montar planilha", "Ferramentas ligadas entre si"]),
            "ruim": False,
            "nota": "<b>Juntas rendem mais:</b> o atendimento capta o cliente e os processos fazem o resto andar sozinho.",
        },
        "itens_titulo": "Exemplos do que dá pra automatizar",
        "itens": [
            ("Lembrete com confirmação", "Na véspera, o cliente recebe o lembrete e confirma com uma resposta. A agenda já fica atualizada."),
            ("Retorno de orçamento", "Quem pediu orçamento e não respondeu recebe uma mensagem gentil alguns dias depois."),
            ("Contato direto pro lugar certo", "Quem chega pelo site ou pelo Instagram já cai no WhatsApp e fica salvo na sua lista de contatos."),
            ("Pós-venda", "Mensagem de agradecimento depois do atendimento e pedido de avaliação no Google."),
            ("Aviso pra equipe", "Novo pedido, agendamento ou pagamento chega na hora pra pessoa responsável."),
            ("Resumo do dia", "Atendimentos, agendamentos e vendas do dia num resumo, sem ninguém montar planilha."),
        ],
        "passos": [
            ("Mapeamos a rotina", "Olhamos o dia a dia da empresa e listamos tudo que se repete do mesmo jeito."),
            ("Escolhemos o primeiro passo", "Começamos pelo que dá mais resultado com menos mudança pra sua equipe."),
            ("Montamos e testamos", "A automação roda primeiro em teste, com você acompanhando, antes de valer de verdade."),
            ("Acompanhamos", "Seguimos por perto, ajustamos e, quando fizer sentido, automatizamos o próximo processo."),
        ],
        "faq": [
            ("O que dá pra automatizar?", "Quase toda tarefa que se repete sempre do mesmo jeito: mensagens de lembrete e retorno, cadastro de contatos, avisos pra equipe, relatórios e a troca de informação entre as ferramentas que você usa."),
            ("Preciso trocar as ferramentas que já uso?", "Na maioria dos casos, não. A ideia é ligar o que você já usa, como WhatsApp, planilhas, agenda e sistema, em vez de começar do zero."),
            ("Automação e agente de IA são a mesma coisa?", "Não. O agente de IA conversa com o cliente; a automação executa tarefas sozinha, com ou sem conversa. Funcionam muito bem juntos, mas dá pra começar por qualquer um dos dois."),
            ("Quanto custa?", "Depende do que vai ser automatizado. No diagnóstico gratuito a gente entende a sua rotina e você recebe a proposta com prazo e valor antes de fechar."),
            ("Empresa pequena precisa de automação?", "Principalmente ela. Na empresa pequena, cada hora gasta com tarefa repetitiva sai do tempo do dono ou de uma equipe enxuta."),
            ("Preciso entender de tecnologia?", "Não. Você conta como a empresa funciona, e a parte técnica fica com a gente."),
        ],
    },
    {
        "slug": "sistemas-personalizados",
        "pitch": 'Sistema pronto é sapato de numeração; o nosso é luva. A gente entende como a sua empresa trabalha e desenha o sistema a partir disso: vendas, estoque, agenda e financeiro num painel só, no computador e no celular.',
        "beneficios": ['Feito do jeito que a sua empresa trabalha', 'Sai do caderno e das planilhas', 'Mostra o que vende e como está o caixa'],
        "nome": "Sistemas personalizados",
        "curto": "Sistemas personalizados",
        "resumo": "Vendas, estoque, agenda e financeiro num painel só, feito do jeito que a sua empresa trabalha.",
        "title": "Sistemas Personalizados para Empresas | MedCode Assessoria",
        "desc": "Sistema personalizado feito na medida da sua empresa: vendas, estoque, agenda e financeiro num painel só, no computador e no celular. Diagnóstico gratuito.",
        "h1": "Sistema personalizado, feito na medida da sua empresa",
        "lead": "Sistema pronto é sapato de numeração: você se ajeita no que couber. <strong>O nosso é luva.</strong> A gente entende como a sua empresa trabalha e só depois desenha o sistema: vendas, estoque, agenda e financeiro num painel só.",
        "oferta": ["Visita pra entender a sua rotina (ou por vídeo)", "Sai do caderno e das planilhas", "Mostra o que vende, o que parou e como está o caixa",
                   "Funciona no computador e no celular", "Pode se ligar ao agente de IA e ao WhatsApp"],
        "preco": "<b>Valor no diagnóstico gratuito</b>",
        "preco_nota": "depende do tamanho da operação",
        "cta": ("Quero um sistema", "Oi! Quero saber mais sobre um sistema sob medida."),
        "dores_titulo": "Hora de ter um sistema quando…",
        "dores": [
            ("“Minha empresa cresceu e virou bagunça”", "O que funcionava com poucos clientes não funciona mais. Informação espalhada e retrabalho todo dia."),
            ("“Vivo de planilha e caderno”", "Cada um anota de um jeito, a planilha quebra, e ninguém sabe qual é a versão certa."),
            ("“Não sei quanto lucro de verdade”", "Dinheiro entra e sai, mas o resultado do mês só aparece (ou não) quando a conta não fecha."),
            ("“Já testei sistema pronto e não serviu”", "Um monte de tela que você não usa e falta justamente o que a sua empresa precisa."),
        ],
        "vs": {
            "kicker": "Pronto x sob medida",
            "titulo": "Por que um sistema feito pra você",
            "a": ("Sistema pronto", "Feito pra servir pra todo mundo.",
                  ["Você adapta a empresa ao sistema", "Telas e campos que você nunca usa", "Falta o que é específico do seu negócio", "Mensalidade por usuário que só cresce"]),
            "b": ("Sistema sob medida", "Feito a partir de como a sua empresa trabalha.",
                  ["O sistema se adapta à sua rotina", "Só o que você usa, do jeito que você chama", "Cresce junto com a empresa", "Pode conversar com o seu WhatsApp e o agente de IA"]),
            "ruim": True,
            "nota": "<b>Nem sempre o sob medida é o melhor caminho</b>, e a gente fala isso no diagnóstico quando um sistema pronto resolve.",
        },
        "itens_titulo": "O que o sistema pode ter",
        "itens": [
            ("Agenda e atendimentos", "Horários, profissionais e histórico de cada cliente num lugar só."),
            ("Vendas e pedidos", "Do pedido à entrega, com o status de cada um à vista da equipe."),
            ("Estoque", "O que tem, o que está acabando e o que parou de sair."),
            ("Financeiro e caixa", "Entradas, saídas e o resultado do mês sem depender de planilha."),
            ("Clientes", "Cadastro, histórico de compras e atendimentos, pra conhecer quem compra de você."),
            ("Painel do dono", "Os números que importam numa tela só, no computador ou no celular."),
        ],
        "passos": [
            ("Imersão na rotina", "Vamos até a sua empresa (ou fazemos por vídeo) e acompanhamos como o trabalho acontece."),
            ("Desenho e proposta", "Você vê como o sistema vai ficar e recebe prazo e valor antes de começar."),
            ("Construção com você", "Você testa as partes conforme ficam prontas e pede ajustes no caminho."),
            ("Treinamento e suporte", "Ensinamos a equipe a usar e seguimos por perto depois da entrega."),
        ],
        "faq": [
            ("Quanto custa um sistema personalizado?", "Depende do tamanho da operação e do que o sistema precisa fazer. No diagnóstico gratuito a gente entende a sua rotina e você recebe a proposta com prazo e valor antes de fechar."),
            ("Quanto tempo leva?", "Depende do tamanho do sistema. Sempre que possível começamos pelo essencial, pra você usar logo, e o restante entra em etapas. O prazo vem descrito na proposta."),
            ("Funciona no celular?", "Sim. O sistema funciona no computador e no celular, direto no navegador."),
            ("Vocês vão até a minha empresa?", "Quando dá, sim: acompanhar a rotina de perto faz toda a diferença. Se você estiver longe, fazemos a imersão por vídeo."),
            ("Dá pra ligar o sistema ao WhatsApp e ao agente de IA?", "Dá. Um agendamento feito pelo agente, por exemplo, pode cair direto na agenda do sistema."),
            ("E se a minha empresa mudar depois?", "O sistema pode crescer junto. Ajustes e novas partes são combinados conforme a necessidade."),
        ],
    },
    {
        "slug": "consultoria-de-gestao",
        "pitch": 'Acompanhamento individual com o Paulo Nogueira, que passou por todas as cadeiras de uma empresa, do atendimento a COO. Pra organizar processos, equipe, financeiro e vendas, com um plano prático e acompanhamento de perto.',
        "beneficios": ['Visão de quem já foi do atendimento à diretoria', 'Plano de ação prático, não teoria', 'Processos, equipe, financeiro e vendas'],
        "nome": "Consultoria de gestão para pequenas e médias empresas",
        "curto": "Consultoria de gestão",
        "resumo": "Acompanhamento individual com o fundador pra organizar processos, equipe, financeiro e vendas.",
        "title": "Consultoria de Gestão para Pequenas e Médias Empresas | MedCode",
        "desc": "Consultoria de gestão com Paulo Nogueira, que passou do atendimento a COO: processos, equipe, financeiro e vendas para pequenas e médias empresas.",
        "h1": "Consultoria de gestão para pequenas e médias empresas",
        "lead": "Pra estruturar um negócio que está começando ou reorganizar um que cresceu sem processo. <strong>Acompanhamento individual com o Paulo Nogueira</strong>, que já passou por todas as cadeiras de uma empresa, do atendimento a COO.",
        "oferta": ["Acompanhamento individual com o fundador", "Processos e rotina", "Gestão de equipe", "Financeiro e caixa", "Atendimento e vendas"],
        "preco": "<b>Valor no diagnóstico gratuito</b>",
        "preco_nota": "depende do formato do acompanhamento",
        "cta": ("Quero conversar", "Olá! Vi o site e tenho interesse na Consultoria de Negócios."),
        "dores_titulo": "A consultoria ajuda quando…",
        "dores": [
            ("“Tudo depende de mim”", "Se você para, a empresa para. Sem processo, cada decisão e cada problema volta pra sua mesa."),
            ("“A empresa cresceu sem processo”", "Cada um faz de um jeito, a qualidade oscila e o retrabalho virou rotina."),
            ("“Não sei pra onde vai o dinheiro”", "Fatura bem, mas o caixa não acompanha. Falta enxergar custo, margem e resultado."),
            ("“Minha equipe não rende o que podia”", "Papéis confusos, metas que ninguém acompanha e pouca clareza do que se espera de cada um."),
        ],
        "itens_titulo": "Os quatro pilares do acompanhamento",
        "itens": [
            ("Processos e rotina", "Desenhar como o trabalho acontece, do primeiro contato do cliente à entrega, pra empresa funcionar sem depender de uma pessoa."),
            ("Gestão de equipe", "Papéis claros, rotina de acompanhamento e indicadores simples pra cada um saber o que se espera dele."),
            ("Financeiro e caixa", "Organizar entradas e saídas, entender custos e margem, e acompanhar o resultado de verdade."),
            ("Atendimento e vendas", "Revisar a jornada do cliente, o atendimento e o processo comercial pra vender mais e perder menos."),
        ],
        "sobre": True,
        "passos": [
            ("Conversa inicial", "Um bate-papo gratuito pra entender o momento da empresa e o que mais incomoda hoje."),
            ("Diagnóstico", "Olhamos processos, equipe, números e atendimento pra achar onde estão os gargalos."),
            ("Plano de ação", "Prioridades claras, do que resolve mais rápido ao que leva mais tempo."),
            ("Acompanhamento", "Encontros por vídeo ou presenciais pra colocar o plano em prática e ajustar no caminho."),
        ],
        "faq": [
            ("Como funciona a consultoria?", "É um acompanhamento individual com o Paulo Nogueira. Começamos com um diagnóstico da empresa, montamos juntos um plano de ação e seguimos com encontros periódicos pra colocar tudo em prática."),
            ("Quanto custa?", "Depende do formato e da duração do acompanhamento. Na conversa inicial, que é gratuita, a gente entende o seu momento e você recebe a proposta antes de fechar."),
            ("Preciso contratar sistema ou agente junto?", "Não. A consultoria é independente. Se em algum momento a tecnologia ajudar, a gente mostra, mas a decisão é sua."),
            ("Pra que tamanho de empresa é?", "Pra pequenas e médias empresas: de quem está estruturando o negócio a quem cresceu e precisa reorganizar processos e equipe."),
            ("É online ou presencial?", "Os dois. Os encontros podem ser por vídeo, de qualquer lugar do Brasil, ou presenciais, quando a distância permite."),
        ],
    },
]

# ---------------------------------------------------------------- pedaços de HTML repetidos

ICO_BRAND = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 8L4.5 12l4 4M15.5 8l4 4-4 4M13.2 6.5l-2.4 11"/></svg>'
ICO_CHAT = '<svg width="19" height="19" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>'
ICO_ESCUDO = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/></svg>'


def head(title, desc, caminho, jsonld):
    url = f"{SITE}/{caminho}"
    return f"""<!DOCTYPE html>
<!-- Gerado por _paginas/gerar.py: edite o conteúdo lá e rode o script de novo. -->
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{attr(title)}</title>
<meta name="description" content="{attr(desc)}">
<meta name="theme-color" content="#ffffff">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="48x48" href="/public/favicon-48.png">
<link rel="icon" type="image/png" sizes="96x96" href="/public/favicon-96.png">
<link rel="icon" type="image/png" sizes="192x192" href="/public/icon-192.png">
<link rel="icon" type="image/svg+xml" href="/public/favicon.svg">
<link rel="apple-touch-icon" href="/public/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="MedCode Assessoria">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{attr(title)}">
<meta property="og:description" content="{attr(desc)}">
<meta property="og:image" content="{SITE}/public/og-site.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/css/paginas.css">
<script>document.documentElement.classList.add('js');</script>
<script type="application/ld+json">
{json.dumps(jsonld, ensure_ascii=False, indent=1)}
</script>
</head>
<body>

<a class="skip" href="#conteudo">Pular para o conteúdo</a>

<header class="header">
  <div class="wrap header-inner">
    <a href="/" class="brand" aria-label="MedCode Assessoria, página inicial"><span class="brand-ico" aria-hidden="true">{ICO_BRAND}</span><span class="brand-name">Med<span class="grad">Code</span><small>Assessoria</small></span></a>
    <nav class="nav" aria-label="Principal">
      <a href="/#servicos" class="link">Serviços</a>
      <a href="/#como-trabalhamos" class="link">Como trabalhamos</a>
      <a href="/#sobre" class="link">Sobre</a>
      <button class="btn-wa-sm" type="button" data-open-ana>Fale com a gente</button>
    </nav>
  </div>
</header>
"""


def footer():
    servicos = "\n".join(f'        <a href="/{s["slug"]}">{html.escape(s["curto"])}</a>' for s in SERVICOS)
    cidades = " · ".join(f'<a href="/cidades/{c["slug"]}">{html.escape(c["nome"])}</a>' for c in CIDADES)
    return f"""
<footer class="footer">
  <div class="wrap footer-top">
    <div class="footer-brand">
      <a href="/" class="brand" aria-label="MedCode Assessoria, página inicial"><span class="brand-ico" aria-hidden="true">{ICO_BRAND}</span><span class="brand-name">Med<span class="grad">Code</span></span></a>
      <p>Agentes de IA, sites, automação e sistemas sob medida para pequenos e médios negócios de todo o Brasil.</p>
    </div>
    <div class="footer-cols">
      <div>
        <h2 class="footer-h">Serviços</h2>
{servicos}
      </div>
      <div>
        <h2 class="footer-h">Empresa</h2>
        <a href="/#sobre">Sobre a MedCode</a>
        <a href="/#como-trabalhamos">Como trabalhamos</a>
        <a href="/privacidade">Política de Privacidade</a>
      </div>
      <div>
        <h2 class="footer-h">Contato</h2>
        <a {wa("Oi! Vi o site da MedCode e queria conversar.", "rodape")}>WhatsApp (11) 99164-9612</a>
        <a href="mailto:contato@medcodedev.com">contato@medcodedev.com</a>
      </div>
    </div>
  </div>
  <div class="wrap footer-cities">
    <h2 class="footer-h"><a href="/onde-atendemos">Onde atendemos</a></h2>
    <p>{cidades} · <a href="/onde-atendemos">e todo o Brasil</a></p>
  </div>
  <div class="footer-bottom"><div class="wrap">© MedCode Assessoria · 68.955.873 Paulo Nogueira Januario · CNPJ 68.955.873/0001-91</div></div>
</footer>

<!-- CHAT COM A ANA (o comportamento está em js/site.js) -->
<dialog class="ana-chat" id="anaChat" aria-labelledby="anaChatTitle">
  <div class="ac-head">
    <div class="avatar"><img src="/public/perfil_assistente.webp" alt="" width="36" height="36"></div>
    <div><b id="anaChatTitle">Ana · MedCode</b><span>● agente de IA, online agora</span></div>
    <button class="ac-close" type="button" data-close-ana aria-label="Fechar conversa">×</button>
  </div>
  <div class="ac-frame" id="anaFrame" hidden></div>
  <p class="ac-privacy">Conversa com agente de IA. Ao continuar, você concorda com a <a href="/privacidade" target="_blank" rel="noopener">Política de Privacidade</a>.</p>
  <button class="ac-x" type="button" data-close-ana aria-label="Fechar conversa">×</button>
</dialog>

<button class="wa-float" type="button" data-open-ana aria-label="Conversar com a Ana, nossa agente de IA">{ICO_CHAT}<span>Fale com a Ana</span></button>
<script src="/js/site.js" defer></script>
<script defer src="/_vercel/insights/script.js"></script>
</body>
</html>
"""


def bloco_ana(origem):
    return f"""
<section class="ana" aria-labelledby="ana-title">
  <div class="wrap ana-grid">
    <div class="ana-photo"><img src="/public/perfil_assistente.webp" alt="" width="92" height="92" loading="lazy"></div>
    <div>
      <span class="online"><i aria-hidden="true"></i> Online agora</span>
      <h2 id="ana-title">Quer ver um agente de IA funcionando?</h2>
      <p>A nossa agente se chama Ana. Mande um oi e converse com ela, do jeito que os seus clientes conversariam com o seu agente.</p>
    </div>
    <div class="ana-actions">
      <button class="btn-light" type="button" data-open-ana>{ICO_CHAT} Conversar com a Ana</button>
      <a class="ana-wa" {wa("Oi! Vi o site da MedCode e queria conversar.", origem)}>ou fale com a gente no WhatsApp</a>
    </div>
  </div>
</section>
"""


def faq_html(faq):
    itens = "\n".join(
        f'      <details class="faq-item" name="faq">\n        <summary>{html.escape(q)}</summary>\n        <p>{html.escape(a)}</p>\n      </details>'
        for q, a in faq)
    return f"""
<section class="sec" id="duvidas">
  <div class="wrap faq-wrap">
    <div class="faq-side reveal">
      <span class="kicker">Dúvidas</span>
      <h2 class="h2">Perguntas frequentes</h2>
      <p class="sub">Não achou o que procurava? A Ana responde na hora.</p>
      <button class="btn-ghost" type="button" data-open-ana>Perguntar pra Ana</button>
    </div>
    <div class="faq reveal">
{itens}
    </div>
  </div>
</section>
"""


TRAJETORIA = """      <div class="path-box">
        <p class="path-title">Trajetória do fundador</p>
        <ol class="path">
          <li><b>Atendimento e recepção</b><span>Atendente, recepcionista e secretário</span></li>
          <li><b>Supervisão de atendimento</b><span>Liderança de equipe e rotina</span></li>
          <li><b>Faturamento e financeiro</b><span>Onde o dinheiro entra e sai</span></li>
          <li><b>Gerência</b><span>Resultado, pessoas e processos</span></li>
          <li class="top"><b>Diretor executivo e COO</b><span>Visão e operação do negócio inteiro</span></li>
        </ol>
      </div>"""


def pagina_servico(s):
    url = f"{SITE}/{s['slug']}"
    origem = "pagina-" + s["slug"]
    jsonld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Service", "@id": url + "#servico", "name": s["nome"], "serviceType": s["nome"],
             "description": s["desc"], "url": url,
             "provider": {"@id": SITE + "/#org"},
             "areaServed": {"@type": "Country", "name": "Brasil"}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": s["curto"], "item": url}]},
            {"@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faq"]]},
        ],
    }

    oferta = "\n".join(f"          <li>{html.escape(i)}</li>" for i in s["oferta"])
    preco_nota = f"<small>{s['preco_nota']}</small>" if s.get("preco_nota") else ""
    extra = ""
    if s.get("garantia"):
        extra += f'\n        <p class="badge-ok">{ICO_ESCUDO}<span>{s["garantia"]}</span></p>'
    if s.get("selo"):
        extra += f'\n        <p class="badge-ok">{ICO_ESCUDO}<span>{s["selo"]}</span></p>'
    cta_txt, cta_msg = s["cta"]

    dores = "\n".join(
        f'      <div class="pain reveal"><h3>{html.escape(t)}</h3><p>{html.escape(p)}</p></div>' for t, p in s["dores"])

    vs = ""
    if s.get("vs"):
        v = s["vs"]
        def col(c, cls):
            li = "\n".join(f"          <li>{html.escape(x)}</li>" for x in c[2])
            return (f'      <div class="vs-col {cls} reveal">\n        <h3>{html.escape(c[0])}</h3>\n        <p>{html.escape(c[1])}</p>\n'
                    f'        <ul>\n{li}\n        </ul>\n      </div>')
        vs = f"""
<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="kicker">{html.escape(v["kicker"])}</span>
      <h2 class="h2">{html.escape(v["titulo"])}</h2>
    </div>
    <div class="vs">
{col(v["a"], "ruim" if v["ruim"] else "")}
{col(v["b"], "bom")}
    </div>
    <p class="vs-note reveal">{v["nota"]}</p>
  </div>
</section>
"""

    itens = "\n".join(
        f'      <div class="feat reveal"><span class="feat-n" aria-hidden="true">{n:02d}</span><h3>{html.escape(t)}</h3><p>{html.escape(p)}</p></div>'
        for n, (t, p) in enumerate(s["itens"], 1))
    feats_cls = "sec-alt" if s.get("vs") else "sec"

    sobre = ""
    if s.get("sobre"):
        sobre = f"""
<section class="sec">
  <div class="wrap about-row">
    <img class="reveal" src="/public/quem_sou.webp" alt="Paulo Nogueira, fundador da MedCode Assessoria" width="1000" height="750" loading="lazy">
    <div class="reveal">
      <span class="kicker">Quem conduz</span>
      <h2 class="h2">Gestão de quem já esteve em todas as cadeiras</h2>
      <p class="sub">O Paulo Nogueira tem mais de 15 anos dentro de empresas: começou no atendimento e chegou a diretor executivo e COO. Por isso a consultoria é prática: ele já viveu os problemas que você está enfrentando, dos dois lados do balcão.</p>
{TRAJETORIA}
    </div>
  </div>
</section>
"""

    passos = "\n".join(
        f'      <div class="step reveal"><div class="step-n">{n}</div><h3>{html.escape(t)}</h3><p>{html.escape(p)}</p></div>'
        for n, (t, p) in enumerate(s["passos"], 1))

    outros = "\n".join(
        f'      <a class="reveal" href="/{o["slug"]}"><b>{html.escape(o["curto"])}</b><span>{html.escape(o["resumo"])}</span><em>Saiba mais →</em></a>'
        for o in SERVICOS if o["slug"] != s["slug"])

    corpo = f"""
<main id="conteudo">
<section class="hero">
  <nav class="wrap crumbs" aria-label="Você está em">
    <ol><li><a href="/">Início</a></li><li aria-current="page">{html.escape(s["curto"])}</li></ol>
  </nav>
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow"><i aria-hidden="true"></i> {html.escape(s["curto"])}</span>
      <h1>{html.escape(s["h1"])}</h1>
      <p class="lead">{s["lead"]}</p>
      <div class="ctas">
        <a class="btn-primary" {wa(cta_msg, origem)}>{ICO_CHAT} {html.escape(cta_txt)}</a>
        <button class="btn-ghost" type="button" data-open-ana>Tirar dúvidas com a Ana</button>
      </div>
      <div class="founder">
        <img src="/public/quem_sou-avatar.webp" alt="" width="44" height="44">
        <p><b>Fundada por Paulo Nogueira</b>mais de 15 anos dentro de empresas, do atendimento à diretoria</p>
      </div>
    </div>
    <aside class="offer" aria-label="Resumo do serviço">
      <p class="offer-title">O que você recebe</p>
      <ul class="check">
{oferta}
      </ul>
      <p class="price">{s["preco"]}{preco_nota}</p>{extra}
      <a class="btn-primary" {wa("Oi! Quero agendar o diagnóstico gratuito sobre " + s["curto"].lower() + ".", origem + "-card")}>Agendar diagnóstico gratuito</a>
    </aside>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="kicker">Pra quem é</span>
      <h2 class="h2">{html.escape(s["dores_titulo"])}</h2>
    </div>
    <div class="pains">
{dores}
    </div>
  </div>
</section>
{vs}
<section class="sec {feats_cls}">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="kicker">Na prática</span>
      <h2 class="h2">{html.escape(s["itens_titulo"])}</h2>
    </div>
    <div class="feats">
{itens}
    </div>
  </div>
</section>
{sobre}
<section class="sec{' sec-alt' if feats_cls == 'sec' else ''}" id="como-funciona">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="kicker">Como funciona</span>
      <h2 class="h2">Do primeiro contato até a entrega</h2>
    </div>
    <div class="steps">
{passos}
    </div>
  </div>
</section>
{bloco_ana(origem + "-ana")}{faq_html(s["faq"])}
<section class="sec sec-alt">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="kicker">Outros serviços</span>
      <h2 class="h2">As soluções se somam</h2>
      <p class="sub">O site atrai, o agente atende, a automação e o sistema organizam. Comece pelo que mais dói hoje.</p>
    </div>
    <div class="more">
{outros}
    </div>
  </div>
</section>
</main>
"""
    return head(s["title"], s["desc"], s["slug"], jsonld) + corpo + footer()


# ---------------------------------------------------------------- páginas de cidade

REGIOES = ["Interior de São Paulo", "Norte", "Nordeste"]

# "Como ajudamos" nas cidades: um card por serviço; "Ideal pra" vem de nichos em cidades.py.
AJUDA = [
    ("agente", "agente-de-ia-para-whatsapp", "Agente de IA no WhatsApp",
     "Seus clientes respondidos em segundos, de dia, de noite e no fim de semana: ninguém fica sem resposta. O agente conversa de verdade, entende até áudio, tira dúvidas e agenda, e passa pra você quando precisa. A sua atendente foca só nos clientes quentes, e a equipe toda atende no mesmo número."),
    ("site", "criacao-de-sites", "Sites e landing pages",
     "Quem pesquisa no Google em {nome} encontra a sua empresa, vê um site profissional e rápido no celular e chama no WhatsApp com um toque. É uma vitrine aberta 24 horas, com o domínio no nome da sua empresa."),
    ("automacao", "automacao-para-empresas", "Automação de atendimento e processos",
     "Lembrete na véspera, confirmação de horário, retorno pra quem pediu orçamento e sumiu, aviso pra equipe quando chega pedido: tudo acontece sozinho. Menos falta, menos esquecimento e mais tempo pra atender bem."),
    ("sistemas", "sistemas-personalizados", "Sistemas personalizados",
     "Vendas, estoque, agenda e financeiro num painel só, feito do jeito que a sua empresa trabalha. Chega de caderno e planilha: você sabe o que vende, o que parou e como está o caixa, no computador ou no celular."),
    ("consultoria", "consultoria-de-gestao", "Consultoria de gestão",
     "Se tudo depende de você, o acompanhamento individual com o Paulo organiza processos, equipe, financeiro e vendas. Plano prático, sem teoria, e acompanhamento de perto até a empresa andar com as próprias pernas."),
]

# "estado do Acre", mas "estado de São Paulo"
DO_ESTADO = {"Acre": "do", "Amapá": "do", "Tocantins": "do", "Piauí": "do", "Maranhão": "do", "Ceará": "do"}

# Abertura das páginas de cidade: a história do fundador, adaptada pela região.
LEAD_FUNDADOR = {
    "Interior de São Paulo": "O fundador da MedCode, Paulo Nogueira, nasceu e cresceu em Porto Velho, Rondônia, e veio pra São Paulo, o maior mercado do Brasil, onde aproveitou tudo o que o estado tem a ensinar sobre gestão, tecnologia e vendas. Hoje atende de perto as empresas de {nome} e região, com esse know-how e o olhar de quem já viveu o dia a dia do outro lado do balcão.",
    "Norte": "A MedCode tem raízes no Norte. O fundador, Paulo Nogueira, nasceu e cresceu em Porto Velho, Rondônia, e conhece de perto o jeito de fazer negócio das capitais da região. Depois foi pra São Paulo, a maior cidade do Brasil, onde aproveitou tudo o que essa cidade tem a ensinar sobre gestão, tecnologia e vendas. Agora traz essa experiência e esse know-how pros negócios de {nome}.",
    "Nordeste": "O fundador da MedCode, Paulo Nogueira, nasceu e cresceu em Porto Velho, Rondônia, e sabe o que é empreender longe do eixo Rio–São Paulo. Depois foi pra São Paulo, a maior cidade do Brasil, onde aproveitou tudo o que essa cidade tem a ensinar sobre gestão, tecnologia e vendas. Agora traz essa experiência e esse know-how pros negócios de {nome}.",
}


def lista_cidades(atual=None):
    blocos = []
    for r in REGIOES:
        atual_attr = ' aria-current="page"'
        links = "\n".join(
            f'        <li><a href="/cidades/{c["slug"]}"{atual_attr if c["slug"] == atual else ""}>{html.escape(c["nome"])} <small>{c["uf"]}</small></a></li>'
            for c in CIDADES if c["regiao"] == r)
        blocos.append(f'    <div class="reveal">\n      <h3 class="chips-h">{r}</h3>\n      <ul class="chips">\n{links}\n      </ul>\n    </div>')
    return "\n".join(blocos)


def pagina_cidade(c):
    nome, slug = c["nome"], c["slug"]
    url = f"{SITE}/cidades/{slug}"
    origem = "cidade-" + slug
    perto = c["grupo"] == "sp"
    jeito = (f"Atendimento presencial em {nome} e região" if perto
             else "Atendimento por vídeo e WhatsApp, no seu horário")
    title = f"Sites, Agente de IA e Automação em {nome} - {c['uf']} | MedCode"
    desc = (f"Criação de sites, agente de IA para WhatsApp, automação e sistemas para empresas de {nome} ({c['uf']}). "
            + ("Atendimento presencial na região." if perto else "Atendimento por vídeo e WhatsApp.") + " Diagnóstico gratuito.")

    faq = [
        (f"Vocês atendem empresas de {nome}?",
         f"Sim. A MedCode atende pequenas e médias empresas de {nome} e de todo o estado {DO_ESTADO.get(c['estado'], 'de')} {c['estado']}, "
         + ("com diagnóstico e visitas presenciais quando fizer sentido." if perto
            else "com reuniões por vídeo e acompanhamento pelo WhatsApp.")),
        (f"Quanto custa um site ou um agente de IA em {nome}?",
         "Os valores são os mesmos em qualquer cidade: sites a partir de R$ 400 (ou grátis no combo com 6 meses de agente gerenciado), "
         "agente de IA com plataforma a partir de R$ 147/mês mais a implantação, e sistemas, automação e consultoria com valor definido no diagnóstico gratuito."),
        c["faq_extra"],
        ("Quanto tempo leva pra ficar pronto?",
         "Trabalhamos com entregas em dias, não em meses. O prazo exato depende do projeto e já vem escrito na proposta."),
        ("Preciso entender de tecnologia?",
         "Não. Você só precisa conhecer o seu negócio. Toda a parte técnica fica com a gente, e na entrega mostramos como usar no dia a dia."),
    ]

    jsonld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Service", "@id": url + "#servico",
             "name": f"Sites, agentes de IA, automação e sistemas em {nome}",
             "serviceType": "Criação de sites, agentes de IA para WhatsApp, automação e sistemas personalizados",
             "description": desc, "url": url, "provider": {"@id": SITE + "/#org"},
             "areaServed": {"@type": "City", "name": nome,
                            "containedInPlace": {"@type": "State", "name": c["estado"]}}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": "Onde atendemos", "item": SITE + "/onde-atendemos"},
                {"@type": "ListItem", "position": 3, "name": nome, "item": url}]},
            {"@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]},
        ],
    }

    oferta = "\n".join(f'          <li><a href="/{s["slug"]}">{html.escape(s["curto"])}</a></li>' for s in SERVICOS)
    lead = c.get("lead_fundador") or LEAD_FUNDADOR[c["regiao"]].format(nome=nome)
    paragrafos = ([c["lead"]] if c.get("lead") else []) + c["mercado"]
    mercado = "\n".join(f'      <p class="sub">{html.escape(p)}</p>' for p in paragrafos)
    raiz = ""
    if c.get("raiz"):
        raiz = f"""
    <div class="callout reveal">
      <img src="/public/quem_sou-avatar.webp" alt="Paulo Nogueira" width="64" height="64" loading="lazy">
      <p><b>{html.escape(c.get("raiz_titulo", "Daqui de " + nome))}</b>{html.escape(c["raiz"])}</p>
    </div>"""
    segs = "\n".join(
        f'      <article class="svc-c reveal{" destaque" if i == 0 else ""}">\n'
        f'        <h3>{html.escape(titulo)}</h3>\n'
        f'        <p class="ideal"><b>Ideal pra</b> {html.escape(c["nichos"][chave])}</p>\n'
        f'        <p>{html.escape(texto.format(nome=nome))}</p>\n'
        f'        <a class="link-arrow" href="/{sl}">Ver detalhes <span aria-hidden="true">→</span></a>\n'
        f'      </article>'
        for i, (chave, sl, titulo, texto) in enumerate(AJUDA))
    if perto:
        passos = [("Conversa inicial", "Você chama no WhatsApp e a gente entende o que o seu negócio precisa."),
                  ("Diagnóstico no seu negócio", f"Vamos até a sua empresa em {nome} (ou fazemos por vídeo, se preferir), sem custo."),
                  ("Proposta e entrega", "Prazo e valor claros por escrito, e entrega em dias, não em meses."),
                  ("Acompanhamento de perto", "Seguimos pelo WhatsApp e, quando precisa, presencialmente.")]
    else:
        fuso = f" Reuniões no horário de {nome}." if c.get("fuso") else ""
        passos = [("Conversa inicial", "Você chama no WhatsApp e a gente entende o que o seu negócio precisa."),
                  ("Diagnóstico por vídeo", "Uma videochamada gratuita pra conhecer a sua empresa e a sua rotina." + fuso),
                  ("Proposta e entrega", "Prazo e valor claros por escrito, e entrega em dias, não em meses."),
                  ("Acompanhamento pelo WhatsApp", "Ajustes e suporte por perto, mesmo a quilômetros de distância.")]
    passos_html = "\n".join(
        f'      <div class="step reveal"><div class="step-n">{n}</div><h3>{html.escape(t)}</h3><p>{html.escape(p)}</p></div>'
        for n, (t, p) in enumerate(passos, 1))

    corpo = f"""
<main id="conteudo">
<section class="hero">
  <nav class="wrap crumbs" aria-label="Você está em">
    <ol><li><a href="/">Início</a></li><li><a href="/onde-atendemos">Onde atendemos</a></li><li aria-current="page">{html.escape(nome)}</li></ol>
  </nav>
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow"><i aria-hidden="true"></i> {html.escape(nome)} · {c["uf"]}</span>
      <h1>Sites, agentes de IA e automação para empresas de {html.escape(nome)}</h1>
      <p class="lead">{html.escape(lead)}</p>
      <div class="ctas">
        <a class="btn-primary" {wa(f"Oi! Tenho uma empresa em {nome} e queria conversar.", origem)}>{ICO_CHAT} Falar no WhatsApp</a>
        <button class="btn-ghost" type="button" data-open-ana>Tirar dúvidas com a Ana</button>
      </div>
      <div class="founder">
        <img src="/public/quem_sou-avatar.webp" alt="" width="44" height="44">
        <p><b>Fundada por Paulo Nogueira</b>mais de 15 anos dentro de empresas, do atendimento à diretoria</p>
      </div>
    </div>
    <aside class="offer" aria-label="O que fazemos em {attr(nome)}">
      <p class="offer-title">O que fazemos em {html.escape(nome)}</p>
      <ul class="check">
{oferta}
      </ul>
      <p class="badge-ok">{ICO_ESCUDO}<span><b>{html.escape(jeito)}</b>. Diagnóstico gratuito e sem compromisso.</span></p>
      <a class="btn-primary" {wa(f"Oi! Tenho uma empresa em {nome} e quero agendar o diagnóstico gratuito.", origem + "-card")}>Agendar diagnóstico gratuito</a>
    </aside>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="kicker">Empresas de {html.escape(nome)}</span>
      <h2 class="h2">O cliente de {html.escape(nome)} pesquisa no Google e chama no WhatsApp</h2>
{mercado}
    </div>{raiz}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="kicker">Na prática</span>
      <h2 class="h2">Como ajudamos os negócios de {html.escape(nome)}</h2>
    </div>
    <div class="svc-cards">
{segs}
    </div>
  </div>
</section>


<section class="sec sec-alt" id="como-funciona">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="kicker">Como atendemos {html.escape(nome)}</span>
      <h2 class="h2">{html.escape(jeito)}</h2>
    </div>
    <div class="steps">
{passos_html}
    </div>
  </div>
</section>
{bloco_ana(origem + "-ana")}{faq_html(faq)}
<section class="sec sec-alt">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="kicker">Onde atendemos</span>
      <h2 class="h2">Também estamos em</h2>
      <p class="sub">E em qualquer cidade do Brasil, por vídeo e WhatsApp.</p>
    </div>
    <div class="regioes">
{lista_cidades(slug)}
    </div>
  </div>
</section>
</main>
"""
    return head(title, desc, f"cidades/{slug}", jsonld) + corpo + footer()


def pagina_onde_atendemos():
    url = f"{SITE}/onde-atendemos"
    title = "Onde Atendemos: Sites, Agentes de IA e Automação | MedCode"
    desc = ("A MedCode atende pequenas e médias empresas de todo o Brasil, com atendimento presencial na região de Sorocaba "
            "e por vídeo e WhatsApp nas capitais do Norte e do Nordeste.")
    jsonld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": "Onde atendemos", "item": url}]},
        ],
    }
    corpo = f"""
<main id="conteudo">
<section class="hero">
  <nav class="wrap crumbs" aria-label="Você está em">
    <ol><li><a href="/">Início</a></li><li aria-current="page">Onde atendemos</li></ol>
  </nav>
  <div class="wrap hero-grid hero-solo">
    <div>
      <span class="eyebrow"><i aria-hidden="true"></i> Todo o Brasil</span>
      <h1>Onde a MedCode atende</h1>
      <p class="lead">Atendemos pequenas e médias empresas de <strong>todo o Brasil</strong>. Na região de Sorocaba, dá pra fazer o diagnóstico e as visitas presencialmente. Nas outras cidades, tudo acontece por vídeo e WhatsApp, com a mesma proximidade.</p>
      <div class="ctas">
        <a class="btn-primary" {wa("Oi! Queria saber se vocês atendem a minha cidade.", "onde-atendemos")}>{ICO_CHAT} Falar no WhatsApp</a>
        <button class="btn-ghost" type="button" data-open-ana>Tirar dúvidas com a Ana</button>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="kicker">Cidades</span>
      <h2 class="h2">Escolha a sua cidade</h2>
      <p class="sub">Não achou a sua? Sem problema: atendemos qualquer cidade do Brasil, por vídeo e WhatsApp.</p>
    </div>
    <div class="regioes">
{lista_cidades()}
    </div>
  </div>
</section>
{bloco_ana("onde-atendemos-ana")}</main>
"""
    return head(title, desc, "onde-atendemos", jsonld) + corpo + footer()


def sitemap(caminhos):
    urls = "\n".join(f"  <url><loc>{SITE}/{c}</loc><lastmod>{HOJE}</lastmod></url>" for c in caminhos)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n'


if __name__ == "__main__":
    caminhos = ["", "privacidade"]
    for s in SERVICOS:
        (RAIZ / f"{s['slug']}.html").write_text(pagina_servico(s), encoding="utf-8")
        caminhos.append(s["slug"])
        print("ok", s["slug"])
    (RAIZ / "onde-atendemos.html").write_text(pagina_onde_atendemos(), encoding="utf-8")
    caminhos.append("onde-atendemos")
    (RAIZ / "cidades").mkdir(exist_ok=True)
    for c in CIDADES:
        (RAIZ / "cidades" / f"{c['slug']}.html").write_text(pagina_cidade(c), encoding="utf-8")
        caminhos.append(f"cidades/{c['slug']}")
        print("ok cidades/" + c["slug"])
    (RAIZ / "sitemap.xml").write_text(sitemap(caminhos), encoding="utf-8")
    print("ok sitemap.xml,", len(caminhos), "URLs")
