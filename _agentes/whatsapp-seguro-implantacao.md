# WhatsApp seguro: checklist de implantação e contrato

> **Por que existe:** o WhatsApp da MedCode (+55 15 98804-1307, API oficial) foi banido em 9/10/2026 e a análise foi negada como permanente em 18/10/2026. O suporte da Meta não transfere caso de WhatsApp pra uma pessoa. Este documento existe pra que isso não aconteça com os clientes e, se acontecer, que esteja claro de quem é cada responsabilidade.
>
> **Status:** rascunho. Falta revisar a cláusula (de preferência com um advogado ou contador) e colocá-la no gerador de propostas do sistema.

## 1. O que aprendemos com o nosso caso

O bloqueio foi da **empresa inteira** no WhatsApp ("Business remains disabled"), não só do número: até a conta de teste caiu junto. A Meta não diz o motivo exato, mas o cadastro tinha vários sinais de risco ao mesmo tempo:

- empresa nova e **não verificada** quando a conta foi criada;
- dados incompletos no gerenciador (site era um link do Gmail, telefone e endereço faltando);
- MEI sem atividade de tecnologia no CNPJ;
- **chip novo**, sem histórico, ligado direto na API.

O número nunca enviou mensagem ativa: só respondeu quem chamou pelo site. Ou seja, mesmo usando direito, cadastro fraco já basta pra derrubar. **A ordem certa é: primeiro a empresa verificada, depois o WhatsApp.**

## 2. Checklist de implantação (antes de ligar o agente no WhatsApp)

**Cadastro da clínica na Meta (no nome dela, nunca no da MedCode)**
- [ ] Portfólio empresarial (Business Manager) criado com o e-mail da clínica, e a MedCode só como parceira/administradora
- [ ] Dados da empresa completos e iguais ao cartão CNPJ: razão social, endereço, telefone e site
- [ ] Domínio do site verificado na Meta
- [ ] **Empresa verificada** (CNPJ + comprovante). Esperar a aprovação antes de seguir
- [ ] Atividade do CNPJ compatível com o serviço (clínica, consultório etc.)

**Número**
- [ ] Preferir o **número que a clínica já usa**, com histórico. Confirmar com o GPT Maker se dá pra usar a coexistência (API e WhatsApp Business no celular no mesmo número)
- [ ] Se for chip novo: usar alguns dias normalmente antes e não começar com volume alto
- [ ] Nome de exibição igual ao nome da clínica (o que está no site e na fachada)

**Perfil do WhatsApp**
- [ ] Categoria, descrição, endereço, e-mail e site preenchidos
- [ ] Foto com o logo da clínica

**Configuração do agente**
- [ ] Só **responde** quem chamou: nada de disparo, lista comprada ou mensagem em massa
- [ ] Assunto restrito aos serviços da clínica (agente específico da empresa, não assistente geral)
- [ ] Regras de saúde do modelo base ativas: sem diagnóstico, sem indicar remédio, urgência vai pro 192
- [ ] Lembretes de consulta só pra quem agendou (e com modelo de mensagem aprovado, se for pela API)
- [ ] Passar pra recepção quando a pessoa pedir

**Primeiras semanas**
- [ ] Sem campanhas nem mensagens ativas em volume
- [ ] Acompanhar no Gerenciador do WhatsApp a classificação de qualidade (precisa ficar "Alta")
- [ ] Plano B ligado desde o primeiro dia: o mesmo agente no chat do site e no Instagram da clínica

## 3. Cláusula de contrato (rascunho)

> **Cláusula X – Plataformas de terceiros (WhatsApp/Meta)**
>
> X.1. O atendimento automatizado utiliza a API oficial do WhatsApp Business, plataforma de propriedade da Meta Platforms, Inc. A conta, o número de telefone e o portfólio empresarial na Meta são de titularidade do CONTRATANTE, cabendo à CONTRATADA apenas a configuração e a operação técnica.
>
> X.2. A CONTRATADA se compromete a configurar e operar o serviço de acordo com as políticas vigentes do WhatsApp Business e a orientar o CONTRATANTE sobre o uso adequado.
>
> X.3. O CONTRATANTE se compromete a não utilizar o número para envio de mensagens em massa, listas de contatos não autorizadas ou qualquer uso contrário às políticas do WhatsApp, inclusive por meios não operados pela CONTRATADA.
>
> X.4. Suspensões, restrições ou banimentos aplicados pela Meta são decisões unilaterais da plataforma e estão fora do controle da CONTRATADA, não configurando descumprimento deste contrato. Nesses casos, a CONTRATADA auxiliará o CONTRATANTE no pedido de revisão e manterá o atendimento pelos demais canais contratados (site e/ou Instagram), sem custo adicional pela migração.
>
> X.5. Custos cobrados diretamente pela Meta pelo uso da API (conversas e modelos de mensagem), quando houver, são de responsabilidade do CONTRATANTE.

## 4. Como falar disso na venda

> "Usamos a API oficial do WhatsApp, que é o caminho aprovado pela Meta. Antes de ligar, verificamos a empresa e configuramos tudo dentro das regras. E o agente também fica no site e no Instagram, então o atendimento nunca depende de um canal só."

Falar antes passa profissionalismo. Se um dia acontecer um bloqueio, o cliente já sabia que existe essa regra da Meta, e a responsabilidade não cai na MedCode.

## 5. Próximos passos

- [ ] Revisar a cláusula com advogado ou contador
- [ ] Colocar a cláusula no gerador de propostas do sistema (sistema.medcodedev.com)
- [ ] Confirmar com o GPT Maker se eles suportam a coexistência do número
- [ ] Usar o checklist na primeira implantação e ajustar o que faltar
