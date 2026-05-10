# PECULATO (ART. 312 CP)

## 1. Estrutura Típica Controlada

Todas as condutas abaixo seguem estrutura homogênea e preservam os elementos essenciais do tipo penal previsto no Art. 312 do Código Penal.

### Estrutura lógica aplicada:

1. Conduta típica  
2. Objeto material  
3. Situação funcional  
4. Finalidade da conduta  

---

## 2. Elementos Estruturais do Tipo Penal

### Condutas
- apropriar-se
- desviar
- subtrair
- concorrer para subtração

### Objetos
- dinheiro público
- valor público
- valor particular
- bem móvel particular

### Situação Funcional
- posse em razão do cargo
- guarda funcional
- facilidade proporcionada pelo cargo
- prerrogativas funcionais

### Finalidade
- proveito próprio
- proveito alheio

---

## 3. Controle Metodológico Aplicado

O dataset foi estruturado para manter:

- equilíbrio quantitativo entre núcleos verbais
- alternância controlada de finalidade
- uniformidade estrutural
- variação exclusivamente semântica
- preservação dos elementos jurídicos essenciais

### Distribuição Balanceada

#### Apropriação (posse)
- 2 condutas

#### Desvio (posse)
- 2 condutas

#### Subtração (sem posse direta)
- 2 condutas

#### Concurso para subtração
- 2 condutas

#### Grupo misto (controle estrutural)
- 2 condutas

---

## 4. Resultado Final

- 10 Condutas Base
- 30 Reescritas Semânticas
- Total: 40 entradas balanceadas

---

## 5. Objetivos Experimentais do Dataset

O dataset foi estruturado para testar:

### Tipificação Jurídica
Capacidade da LLM de identificar corretamente o tipo penal aplicável.

### Generalização Semântica
Capacidade do modelo de reconhecer o mesmo núcleo jurídico em construções linguísticas diferentes.

### Robustez Linguística
Capacidade da LLM de evitar dependência excessiva de palavras-chave específicas.

---

## 6. Observação Metodológica Relevante

Este conjunto apresenta:

- balanceamento por núcleo do tipo penal
- balanceamento por finalidade da conduta
- diversidade lexical controlada
- manutenção dos elementos normativos essenciais

### Objetivo científico principal

Reduzir:

- overfitting semântico
- classificação baseada apenas em palavras-chave
- enviesamento estrutural do conjunto de dados

e permitir avaliação mais rigorosa da capacidade de subsunção jurídica da LLM.

---

# PECULATO CULPOSO (ART. 312, §2º CP)

## 1. Estrutura Típica Controlada

Todas as condutas abaixo seguem estrutura homogênea e preservam os elementos essenciais do peculato culposo:

1. Sujeito ativo: funcionário público  
2. Conduta culposa:
   - negligência  
   - imprudência  
   - imperícia  
3. Situação funcional:
   - dever de guarda  
   - dever de vigilância  
   - dever de controle patrimonial/financeiro  
4. Concurso culposo para crime de terceiro  
5. Resultado:
   - subtração  
   - apropriação  
   - desvio de bem ou valor público por terceiro  
6. Ausência de dolo:
   - inexistência de intenção de favorecer o resultado

⚠️ Elemento-chave:
O agente público não pratica diretamente o peculato doloso.  
Ele concorre culposamente para que terceiro pratique o crime.

⚠️ Observação metodológica:
O dataset foi estruturado para preservar distinção rigorosa entre:

- peculato culposo  
- peculato doloso  
- mera irregularidade administrativa

---

## 2. Resultado Final

- 10 Condutas Base  
- 30 Reescritas Semânticas  
- Total: 40 entradas

---

## 3. Controle Metodológico Aplicado

Distribuição homogênea entre:

### Modalidades de Culpa
- negligência
- imprudência
- imperícia

### Situações Funcionais
- guarda de bens
- vigilância patrimonial
- controle financeiro
- administração de valores públicos

### Resultado Típico
- subtração
- apropriação
- desvio por terceiro

### Elemento Subjetivo
- ausência de intenção
- ausência de favorecimento doloso

### Linguagem
- fácil / médio / difícil

---

## 4. Observação Científica Relevante

Peculato culposo costuma ser confundido por LLMs com:

- peculato doloso  
- corrupção passiva  
- prevaricação  
- mera negligência administrativa  
- responsabilidade civil/administrativa

### Teste crítico recomendado:

- há dolo → peculato doloso  
- há culpa + crime de terceiro → peculato culposo  
- não há vínculo com subtração/desvio → fato atípico penalmente

---

## 5. Insight Experimental Relevante

Este dataset permite avaliar a capacidade da LLM de diferenciar:

- dolo vs culpa  
- autoria direta vs concurso culposo  
- crime funcional vs mera irregularidade administrativa

### Hipótese experimental possível:

LLMs tendem a apresentar maior dificuldade na identificação de elementos subjetivos negativos (ausência de dolo), confundindo peculato culposo com peculato doloso devido à proximidade estrutural das condutas.

# PECULATO MEDIANTE ERRO DE OUTREM (ART. 313 CP)

## 1. Estrutura Típica Controlada

Todos os exemplos abaixo preservam os elementos essenciais do tipo penal:

1. Sujeito ativo: funcionário público  
2. Exercício do cargo / contexto funcional  
3. Recebimento de dinheiro ou utilidade  
4. Recebimento por erro de outrem  
5. Apropriação posterior  
6. Elemento subjetivo doloso (consciência do erro + vontade de ficar)

⚠️ Importante:
Não há indução ao erro pelo agente. Se ele provoca o erro, pode haver outro enquadramento.

---

## 2. Resultado Final

- 10 Condutas Base
- 30 Reescritas Semânticas
- Total: 40 entradas

---

## 3. Controle Metodológico Aplicado

Distribuição homogênea de:

- dinheiro / utilidade
- erro material de terceiro
- contexto funcional
- apropriação dolosa posterior
- níveis de complexidade linguística

---

## 4. Observação Científica Relevante

Este crime costuma confundir LLMs com:

- apropriação indébita
- estelionato
- peculato comum
- retenção indevida civil

Seu teste pode medir isso.

---

# CONCUSSÃO (ART. 316 CP)

## 1. Estrutura Típica Controlada

Todos os exemplos preservam os elementos centrais do crime de concussão:

1. Sujeito ativo: funcionário público  
2. Exigência (imposição/ordem/coação)  
3. Vantagem indevida  
4. Para si ou para outrem  
5. Em razão da função pública  
6. Direta ou indiretamente  
7. Pode ocorrer em exercício, fora da função ou antes de assumi-la  
8. Elemento subjetivo doloso

⚠️ Núcleo do tipo: **EXIGIR**.  
Se houver mera solicitação, pode configurar corrupção passiva, não concussão.

---

## 2. Resultado Final

- 10 Condutas Base  
- 30 Reescritas Semânticas  
- Total: 40 entradas

---

## 3. Controle Metodológico Aplicado

Distribuição homogênea entre:

- para si / para outrem  
- direta / indireta  
- durante função / fora da função / antes da posse  
- dinheiro / utilidade / bem / vantagem econômica  
- níveis de complexidade textual

---

## 4. Observação Científica Relevante

Concussão costuma ser confundida por LLMs com:

- corrupção passiva (solicitar vs exigir)  
- extorsão  
- abuso de autoridade  
- advocacia administrativa

### Seu experimento pode medir especialmente a distinção entre:

**EXIGIR (concussão)** vs **SOLICITAR/RECEBER (corrupção passiva)**.

---

# CORRUPÇÃO PASSIVA (ART. 317 CP)

## 1. Estrutura Típica Controlada

Todos os exemplos preservam os elementos centrais do art. 317 caput:

1. Sujeito ativo: funcionário público  
2. Núcleo verbal:
   - solicitar  
   - receber  
   - aceitar promessa  
3. Vantagem indevida  
4. Para si ou para outrem  
5. Direta ou indiretamente  
6. Ainda que fora da função ou antes de assumi-la, mas em razão dela  
7. Elemento subjetivo doloso

⚠️ Observação metodológica:
Este dataset foca prioritariamente no **caput**, com variações pontuais relacionadas ao ato funcional.  
A distinção principal com concussão é:

- **Solicitar / Receber / Aceitar promessa** = Corrupção Passiva  
- **Exigir** = Concussão

---

## 2. Resultado Final

- 10 Condutas Base  
- 30 Reescritas Semânticas  
- Total: 40 entradas

---

## 3. Controle Metodológico Aplicado

Distribuição homogênea entre:

- solicitar / receber / aceitar promessa  
- para si / para outrem  
- direta / indireta  
- em exercício / fora da função / antes da posse  
- dinheiro / utilidade / bem / promessa  
- níveis de complexidade textual

---

## 4. Observação Científica Relevante

Corrupção passiva costuma ser confundida por LLMs com:

- concussão (exigir)  
- prevaricação  
- advocacia administrativa  
- improbidade administrativa

### Teste crítico recomendado:

- pedir = corrupção passiva  
- exigir = concussão  
- ceder a influência sem vantagem = art. 317 §2º
  
---

# PREVARICAÇÃO (ART. 319 E 319-A CP)

## 1. Estrutura Típica Controlada

Este conjunto contempla **somente prevaricação**, abrangendo:

### Art. 319
1. Sujeito ativo: funcionário público  
2. Núcleo verbal:
   - retardar ato de ofício  
   - deixar de praticar ato de ofício  
   - praticar ato contra disposição legal  
3. Indevidamente  
4. Finalidade especial:
   - satisfazer interesse pessoal, ou
   - satisfazer sentimento pessoal

### Art. 319-A
5. Diretor de penitenciária ou agente público competente  
6. Deixar de impedir acesso de preso a aparelho telefônico, rádio ou similar apto à comunicação

⚠️ Observação metodológica:
No art. 319 há **dolo específico** (interesse/sentimento pessoal).  
No art. 319-A há omissão funcional específica ligada ao ambiente prisional.

---

## 2. Resultado Final

- 10 Condutas Base  
- 30 Reescritas Semânticas  
- Total: 40 entradas

---

## 3. Controle Metodológico Aplicado

Distribuição homogênea entre:

### Art. 319
- retardar
- deixar de praticar
- praticar contra a lei
- interesse pessoal
- sentimento pessoal

### Art. 319-A
- diretor penitenciário
- agente prisional
- telefone
- rádio
- celular
- omissão de impedir comunicação

### Linguagem
- níveis fácil / médio / difícil

---

## 4. Observação Científica Relevante

LLMs costumam confundir prevaricação com:

- corrupção passiva  
- advocacia administrativa  
- condescendência criminosa  
- abuso de autoridade  
- mera ineficiência administrativa

### Teste crítico:

- motivo pessoal = art. 319  
- vantagem indevida = corrupção passiva  
- omissão sobre celular em presídio = art. 319-A

---

# CONDESCENDÊNCIA CRIMINOSA (ART. 320 CP)

## 1. Estrutura Típica Controlada

Todos os exemplos preservam os elementos essenciais do art. 320:

1. Sujeito ativo: funcionário público  
2. Conhecimento de infração funcional praticada por subordinado  
3. Vínculo hierárquico / subordinação  
4. Omissão por indulgência (tolerância, complacência, benevolência pessoal)  
5. Duas modalidades típicas:

### Modalidade A
- deixar de responsabilizar subordinado, tendo competência

### Modalidade B
- não comunicar o fato à autoridade competente, quando não tiver competência

6. Elemento subjetivo doloso específico:
- indulgência

⚠️ Não é mera negligência administrativa.  
⚠️ Não exige participação na infração do subordinado.

---

## 2. Resultado Final

- 10 Condutas Base  
- 30 Reescritas Semânticas  
- Total: 40 entradas

---

## 3. Controle Metodológico Aplicado

Distribuição homogênea entre:

### Modalidade A
- deixar de responsabilizar tendo competência

### Modalidade B
- não comunicar sem competência

### Infrações do subordinado
- fraude documental
- abandono de posto
- recebimento indevido
- desvio funcional
- falta disciplinar

### Elemento subjetivo
- indulgência
- amizade
- complacência
- benevolência
- tolerância pessoal

### Linguagem
- fácil / médio / difícil

---

## 4. Observação Científica Relevante

LLMs costumam confundir condescendência criminosa com:

- prevaricação  
- conivência administrativa  
- omissão culposa  
- corrupção passiva  
- advocacia administrativa

### Teste crítico recomendado:

- indulgência com subordinado = art. 320  
- interesse pessoal próprio = prevaricação  
- vantagem indevida = corrupção passiva

---

# ADVOCACIA ADMINISTRATIVA (ART. 321 CP)

## 1. Estrutura Típica Controlada

Todos os exemplos preservam os elementos essenciais do art. 321:

1. Sujeito ativo: funcionário público  
2. Patrocinar / defender / impulsionar interesse privado  
3. Direta ou indiretamente  
4. Perante a Administração Pública  
5. Valendo-se da qualidade de funcionário público  
6. Elemento subjetivo doloso

### Modalidades contempladas:

- Interesse privado legítimo (caput)  
- Interesse privado ilegítimo (parágrafo único)

⚠️ O núcleo não é receber vantagem, e sim **usar o cargo para favorecer interesse privado**.

⚠️ Não se exige êxito do patrocínio.

---

## 2. Resultado Final

- 10 Condutas Base  
- 30 Reescritas Semânticas  
- Total: 40 entradas

---

## 3. Controle Metodológico Aplicado

Distribuição homogênea entre:

### Interesse Privado
- amigo
- familiar
- vizinho
- comerciante
- empresa
- terceiro genérico

### Forma de Atuação
- direta
- indireta
- intercessão
- influência interna
- prioridade processual
- impulso procedimental

### Interesse
- legítimo (caput)
- ilegítimo (parágrafo único)

### Linguagem
- fácil / médio / difícil

---

## 4. Observação Científica Relevante

LLMs costumam confundir advocacia administrativa com:

- corrupção passiva  
- tráfico de influência  
- prevaricação  
- improbidade administrativa  
- mero atendimento cordial

### Teste crítico recomendado:

- usa cargo para defender interesse privado = art. 321  
- pede vantagem = corrupção passiva  
- influência sem ser servidor = tráfico de influência

---

# VIOLAÇÃO DE SIGILO FUNCIONAL (ART. 325 CP)

## 1. Estrutura Típica Controlada

Todos os exemplos preservam os elementos do art. 325 (caput e §1º):

1. Sujeito ativo: funcionário público  
2. Fonte da informação: conhecimento em razão do cargo  
3. Natureza: informação que deve permanecer em segredo  
4. Conduta típica:
   - revelar o segredo, ou  
   - facilitar a revelação, ou  
   - permitir/acesso indevido a sistemas (senha, login etc.), ou  
   - utilizar indevidamente acesso restrito  
5. Destinatário: pessoa não autorizada (explícita ou implícita)  
6. Elemento subjetivo: dolo (consciência do sigilo + vontade de revelar/facilitar)

⚠️ Observação:
- Não há exigência de vantagem (diferencia de corrupção)  
- O §2º (resultado dano) não é exigido para tipicidade, mas pode ocorrer

---

## 2. Resultado Final

- 10 Condutas Base  
- 30 Reescritas Semânticas  
- Total: 40 entradas

---

## 3. Controle Metodológico Aplicado

Distribuição homogênea entre:

### Núcleo da Conduta
- revelar
- facilitar revelação
- permitir acesso
- fornecer credenciais
- usar acesso indevido

### Objeto
- informação sigilosa
- documento
- processo
- sistema
- banco de dados

### Forma
- ação direta
- facilitação
- omissão
- uso indevido

### Linguagem
- fácil / médio / difícil

---

## 4. Observação Científica Relevante

LLMs costumam confundir violação de sigilo funcional com:

- vazamento culposo  
- improbidade administrativa  
- invasão de sistema  
- corrupção passiva  
- quebra de sigilo civil

### Teste crítico recomendado:

- revelar informação sigilosa por causa do cargo = art. 325  
- acessar sistema sem autorização externa = pode ser outro crime  
- obter vantagem = corrupção  
- erro sem dolo = atípico penalmente

---

# CONDUTAS NEGATIVAS (NÃO ENQUADRADAS NOS TIPOS ANTERIORES)

## 1. Objetivo Metodológico

Este conjunto contém **condutas que NÃO se enquadram** em:

- Peculato (todas as 3 formas)
- Concussão
- Corrupção passiva
- Prevaricação
- Condescendência criminosa
- Advocacia administrativa
- Violação de sigilo funcional

⚠️ Todas são **juridicamente atípicas penalmente** OU pertencem a outros ramos (civil/administrativo), mas **não configuram os crimes testados**.

---

## 2. Estrutura Padronizada

Cada conduta mantém:

1. Sujeito (funcionário público)  
2. Contexto funcional  
3. Ação praticada  
4. Ausência de elemento típico penal  
5. Resultado neutro ou administrativo  
6. Elemento subjetivo não doloso penalmente relevante  

--- 

## 3. Resultado Final

- 10 Condutas Base (não típicas)  
- 30 Reescritas Semânticas  
- Total: 40 entradas  

---

## 4. Controle Metodológico Aplicado

Distribuição homogênea de:

- ausência de dolo penal  
- ausência de vantagem indevida  
- ausência de vínculo com crimes do TCC  
- presença de erro, negligência ou ineficiência administrativa  
- níveis de linguagem (fácil / médio / difícil)

---

## 5. Importância Científica no Seu TCC

Esse conjunto funciona como:

✔ **Classe negativa (controle)**  
✔ Teste de falso positivo da LLM  
✔ Avaliação de overfitting por palavra-chave  

---

### 🔥 Insight importante

Se a LLM classificar muitos desses como crimes:

→ Ela está **supergeneralizando padrões linguísticos**  
→ Não está captando **elementos jurídicos estruturais**

---