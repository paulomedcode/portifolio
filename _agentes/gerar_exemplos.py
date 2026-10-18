"""Gera os agentes de exemplo por nicho a partir de _agentes/modelo-agente-clinica.md.

Uso (na raiz do repositório): python3 _agentes/gerar_exemplos.py .
Pra um nicho novo, acrescente um item em NICHOS com os dados fictícios e o bloco de nicho.
"""
import re
import sys
from pathlib import Path

RAIZ = Path(sys.argv[1])
modelo = (RAIZ / "_agentes/modelo-agente-clinica.md").read_text(encoding="utf-8")


def bloco(nome):
    m = re.search(r"### " + re.escape(nome) + r" — ([^\n]*)\n```\n(.*?)\n```", modelo, re.S)
    return m.group(1), m.group(2)


comportamento = re.search(r"\*\*Comportamento\*\*.*?```\n(.*?)\n```", modelo, re.S).group(1)
trabalho = re.search(r"## 2\. TRABALHO.*?```\n(.*?)\n```", modelo, re.S).group(1)

N5 = ("Psicologia", """Atendimentos: [SERVIÇOS]. Sessão: [VALOR_SESSÃO], com [DURAÇÃO]. Online: [TELECONSULTA]. Reembolso: [RECIBO]. Na conversa, respeite o sigilo: não peça que a pessoa conte o que está vivendo por mensagem; diga com carinho que isso vai ser conversado na sessão, com a psicóloga. Você não faz acolhimento terapêutico, não dá conselho nem opinião sobre o caso. Se a pessoa disser que pensa em se machucar, em suicídio, ou que está em crise: responda com acolhimento, oriente a ligar 188 (CVV, gratuito, 24h) ou, se houver risco imediato, 192 ou o pronto-socorro mais próximo, e passe pra psicóloga na hora. Menor de idade: o primeiro contato e o agendamento são feitos com o responsável.""")

COMUM = {
    "[AGENDA]": "Nesta demonstração não há agenda integrada: a recepção confirma o horário",
    "[LINK_MAPS]": "(sem link nesta demonstração)",
}

NICHOS = [
    {
        "arquivo": "agente-exemplo-dentista.md",
        "titulo": "Agente exemplo – Dentista",
        "nicho": "N1",
        "dados": {
            "[NOME_AGENTE]": "Júlia", "[CLÍNICA]": "Clínica Sorriso Vivo", "[TIPO]": "clínica odontológica",
            "[CIDADE]": "Tatuí", "[ENDEREÇO]": "Rua XV de Novembro, 120, Centro", "[REFERÊNCIA]": "perto da praça da matriz",
            "[HORÁRIOS]": "segunda a sexta das 8h às 18h e sábado das 8h às 12h", "[TELEFONE]": "(15) 3251-0000",
            "[SERVIÇOS]": "avaliação, limpeza, restauração, canal, extração, clareamento, implantes, prótese, lentes de contato dental e aparelho ortodôntico",
            "[PROFISSIONAIS]": "Dra. Ana Lima (clínica geral e estética), Dr. Pedro Reis (implantes e prótese) e Dra. Carla Souza (ortodontia)",
            "[CONVÊNIOS]": "Uniodonto e OdontoPrev",
            "[NÃO_FAZ]": "atendimento de urgência 24h, sedação com anestesista, harmonização facial e exames de imagem como tomografia (a clínica indica onde fazer, sem citar nomes)",
            "[VALORES]": "avaliação gratuita; limpeza particular a partir de R$ 150; clareamento a partir de R$ 600; demais tratamentos só depois da avaliação",
            "[PAGAMENTO]": "Pix, débito e cartão de crédito em até 10x",
            "[ESTACIONAMENTO]": "vagas na rua e estacionamento conveniado ao lado",
            "[REGRAS_AGENDA]": "avaliação de 30 min; pedir pra avisar com 24h de antecedência quando precisar remarcar",
            "[VALOR_AVALIAÇÃO]": "a avaliação é gratuita", "[PERIODICIDADE_MANUTENÇÃO]": "uma vez por mês, com a Dra. Carla",
            "[URGÊNCIA_ODONTO]": "encaixe no mesmo dia, conforme a agenda",
        },
    },
    {
        "arquivo": "agente-exemplo-medico.md",
        "titulo": "Agente exemplo – Clínica médica",
        "nicho": "N3",
        "dados": {
            "[NOME_AGENTE]": "Marina", "[CLÍNICA]": "Clínica Vida Plena", "[TIPO]": "clínica médica de especialidades",
            "[CIDADE]": "Sorocaba", "[ENDEREÇO]": "Avenida Antônio Carlos Comitre, 500, sala 12, Campolim", "[REFERÊNCIA]": "no prédio ao lado do shopping",
            "[HORÁRIOS]": "segunda a sexta das 7h às 19h e sábado das 7h às 12h", "[TELEFONE]": "(15) 3222-0000",
            "[SERVIÇOS]": "consultas de clínica geral, cardiologia, ortopedia, ginecologia, pediatria e dermatologia, eletrocardiograma e pequenas cirurgias de pele",
            "[PROFISSIONAIS]": "Dr. Ricardo Alves (cardiologia), Dra. Fernanda Melo (ginecologia), Dr. Paulo Henrique (ortopedia), Dra. Luiza Campos (pediatria) e Dra. Bianca Prado (dermatologia)",
            "[CONVÊNIOS]": "Unimed, Bradesco Saúde, SulAmérica e Cabesp",
            "[NÃO_FAZ]": "pronto-socorro, internação, cirurgias de grande porte, ressonância, tomografia, endoscopia e especialidades fora das que a clínica tem (como psiquiatria, oftalmologia e neurologia)",
            "[VALORES]": "consulta particular a partir de R$ 280; eletrocardiograma particular R$ 120",
            "[PAGAMENTO]": "Pix, débito e cartão de crédito em até 3x",
            "[ESTACIONAMENTO]": "estacionamento do prédio, com a primeira hora grátis",
            "[REGRAS_AGENDA]": "consulta de 20 a 30 min; chegar 15 min antes; avisar com 24h pra remarcar",
            "[VALOR_CONSULTA]": "a partir de R$ 280", "[REGRA_RETORNO]": "sem custo em até 30 dias, com o mesmo médico",
            "[TELECONSULTA]": "disponível para retornos e algumas especialidades, a recepção confirma",
        },
    },
    {
        "arquivo": "agente-exemplo-estetica.md",
        "titulo": "Agente exemplo – Clínica de estética",
        "nicho": "N2",
        "dados": {
            "[NOME_AGENTE]": "Bia", "[CLÍNICA]": "Clínica Bella Pele", "[TIPO]": "clínica de estética",
            "[CIDADE]": "Tatuí", "[ENDEREÇO]": "Rua Coronel Lúcio Seabra, 300, Centro", "[REFERÊNCIA]": "em frente à farmácia da esquina",
            "[HORÁRIOS]": "segunda a sexta das 9h às 19h e sábado das 9h às 14h", "[TELEFONE]": "(15) 3259-0000",
            "[SERVIÇOS]": "avaliação facial, limpeza de pele, peeling, toxina botulínica, preenchimento, bioestimulador de colágeno, microagulhamento e depilação a laser",
            "[PROFISSIONAIS]": "Dra. Camila Torres (biomédica esteta) e Dra. Renata Dias (dermatologista)",
            "[CONVÊNIOS]": "nenhum convênio: atendimento só particular",
            "[NÃO_FAZ]": "cirurgia plástica, tratamentos que só médico faz em hospital, tatuagem e remoção de tatuagem, e qualquer procedimento sem avaliação antes",
            "[VALORES]": "limpeza de pele R$ 180; sessão de depilação a laser a partir de R$ 90 por área; demais procedimentos só depois da avaliação",
            "[PAGAMENTO]": "Pix e cartão de crédito em até 6x",
            "[ESTACIONAMENTO]": "vagas na rua",
            "[REGRAS_AGENDA]": "avaliação de 30 min; remarcação com 24h de antecedência",
            "[VALOR_AVALIAÇÃO]": "a avaliação custa R$ 100 e o valor é abatido se a pessoa fizer o procedimento",
        },
    },
    {
        "arquivo": "agente-exemplo-exames.md",
        "titulo": "Agente exemplo – Exames e imagem",
        "nicho": "N4",
        "dados": {
            "[NOME_AGENTE]": "Lara", "[CLÍNICA]": "Clínica Imagem Porto Feliz", "[TIPO]": "clínica de exames e diagnóstico por imagem",
            "[CIDADE]": "Porto Feliz", "[ENDEREÇO]": "Rua Cerqueira César, 80, Centro", "[REFERÊNCIA]": "a duas quadras da Santa Casa",
            "[HORÁRIOS]": "segunda a sexta das 7h às 17h30 e sábado das 7h às 11h", "[TELEFONE]": "(15) 3261-0000",
            "[SERVIÇOS]": "ultrassom, raio-X, mamografia, densitometria óssea, tomografia e ressonância magnética",
            "[PROFISSIONAIS]": "equipe de médicos radiologistas",
            "[CONVÊNIOS]": "Unimed, Bradesco Saúde, Amil, Cabesp e Iamspe",
            "[NÃO_FAZ]": "consultas médicas, exames de sangue e laboratório, endoscopia, colonoscopia, ecocardiograma e exames com sedação geral",
            "[VALORES]": "valores particulares variam por exame: a recepção informa",
            "[PAGAMENTO]": "Pix, débito e cartão de crédito",
            "[ESTACIONAMENTO]": "estacionamento próprio",
            "[REGRAS_AGENDA]": "chegar 20 min antes; trazer pedido médico, documento com foto e carteirinha",
            "[EXAMES]": "ultrassom, raio-X, mamografia, densitometria, tomografia e ressonância",
            "[REGRA_AUTORIZAÇÃO]": "Unimed e Bradesco pedem autorização prévia para tomografia e ressonância; a recepção solicita",
            "[PREPAROS]": "ultrassom de abdome total: jejum de 8h; ultrassom pélvico: bexiga cheia (tomar 4 a 6 copos de água 1h antes e não urinar); mamografia: não usar desodorante no dia",
            "[PRAZO_RESULTADOS]": "em até 3 dias úteis (ressonância e tomografia em até 5)", "[ONDE_RETIRAR]": "pelo site com a senha do protocolo ou na recepção",
        },
    },
    {
        "arquivo": "agente-exemplo-psicologia.md",
        "titulo": "Agente exemplo – Psicologia",
        "nicho": "N5",
        "dados": {
            "[NOME_AGENTE]": "Clara", "[CLÍNICA]": "Clínica Mente Leve", "[TIPO]": "clínica de psicologia",
            "[CIDADE]": "Tatuí", "[ENDEREÇO]": "Rua Treze de Maio, 45, sala 3, Centro", "[REFERÊNCIA]": "no prédio do lado da padaria",
            "[HORÁRIOS]": "segunda a sexta das 8h às 20h", "[TELEFONE]": "(15) 99999-0000",
            "[SERVIÇOS]": "psicoterapia individual para adultos e adolescentes, presencial e online",
            "[PROFISSIONAIS]": "Paula Nunes, psicóloga (terapia cognitivo-comportamental)",
            "[CONVÊNIOS]": "não atende convênio, mas emite recibo para reembolso",
            "[NÃO_FAZ]": "atendimento psiquiátrico e receita de remédio (só médico psiquiatra), atendimento de crise ou emergência, terapia de casal, atendimento infantil abaixo de 12 anos e laudos para processos judiciais",
            "[VALORES]": "sessão de R$ 150, com 50 minutos",
            "[PAGAMENTO]": "Pix ou cartão, por sessão ou pacote mensal",
            "[ESTACIONAMENTO]": "vagas na rua",
            "[REGRAS_AGENDA]": "sessões semanais no mesmo dia e horário; remarcação com 24h de antecedência",
            "[VALOR_SESSÃO]": "R$ 150", "[DURAÇÃO]": "50 minutos",
            "[TELECONSULTA]": "atendimento online por videochamada, com o mesmo valor",
            "[RECIBO]": "emite recibo para pedir reembolso ao plano",
        },
    },
]

saida = RAIZ / "_agentes/exemplos"
saida.mkdir(exist_ok=True)
problemas = []

for n in NICHOS:
    dados = {**COMUM, **n["dados"]}

    def troca(t):
        for k, v in dados.items():
            t = t.replace(k, v)
        return t

    partes = [f"# {n['titulo']}\n",
              "> **Exemplo pronto para colar no GPT Maker**, com dados **fictícios**. Pra uma clínica de verdade, troque os dados da ficha (nome, endereço, horários, serviços, convênios e valores) nos blocos e confira se nenhum passou de 1.028 caracteres. Testes e configurações: ver \"Agente modelo – Clínicas (base)\".\n",
              "## Ficha usada neste exemplo\n"]
    for k, v in n["dados"].items():
        partes.append(f"- **{k.strip('[]').replace('_', ' ').capitalize()}:** {v}")
    partes.append("\n## Perfil\n")
    partes.append(f"- **Nome:** {dados['[NOME_AGENTE]']}\n- **Cargo/descrição:** Recepção da {dados['[CLÍNICA]']}\n- **Tom:** Acolhedor e próximo · **Emojis:** Poucos · **Assinatura:** nenhuma\n- **Comportamento:**\n")
    partes.append("```\n" + troca(comportamento) + "\n```\n")
    partes.append("## Trabalho\n")
    partes.append("```\n" + troca(trabalho) + "\n```\n")
    partes.append("## Treinamentos → Texto\n")
    blocos = [f"C{i:02d}" for i in range(1, 13)]
    for b in blocos + [n["nicho"]]:
        if b == "N5":
            titulo, texto = N5
        else:
            titulo, texto = bloco(b)
        texto = troca(texto)
        sobra = re.findall(r"\[[A-ZÁÉÍÓÚÇÃÕÂÊ_]+\]", texto)
        if sobra:
            problemas.append((n["arquivo"], b, sobra))
        if len(texto) >= 1028:
            problemas.append((n["arquivo"], b, f"{len(texto)} caracteres"))
        partes.append(f"### {b} — {titulo}\n```\n{texto}\n```\n")
    (saida / n["arquivo"]).write_text("\n".join(partes), encoding="utf-8")
    print("ok", n["arquivo"])

print("problemas:", problemas or "nenhum")
