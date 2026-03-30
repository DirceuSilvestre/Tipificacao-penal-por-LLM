import re
import json
import time
from google import genai

# ======================
# CONFIG
# ======================

for i in range(1, 6):
    CAMINHO_GABARITO = f"condutas_{i}.json"
    CAMINHO_SAIDA = f"respostas_llm{i}.json"


    # ======================
    # FUNÇÕES
    # ======================

    def carregar_json(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)


    def salvar_json(dados, caminho):
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)

    def limpar_resposta(texto):
        # remove ```json e ```
        texto = texto.replace("```json", "").replace("```", "")

        # tenta extrair só o JSON
        match = re.search(r"\{.*\}", texto, re.DOTALL)

        if match:
            return match.group()
        
        return texto


    def montar_prompt(texto):
        return f"""
    Você é um especialista em Direito Penal brasileiro, com foco em crimes contra a Administração Pública.

    Sua tarefa é analisar a conduta descrita abaixo e classificá-la.

    Classes possíveis:
    - peculato
    - peculato_culposo
    - peculato_mediante_erro_de_outrem
    - concussao
    - corrupcao_passiva
    - prevaricacao
    - condescendencia_criminosa
    - advocacia_administrativa
    - violacao_de_sigilo_funcional
    - nao_se_enquadra

    Responda desta forma:
    {{
    "classe": "...",
    "justificativa": "..."
    }}

    Conduta:
    {texto}
    """


    def chamar_llm(prompt):
        """
        Aqui você conecta com Gemini.
        Retorne SEMPRE um dict:
        {
            "classe": "...",
            "justificativa": "..."
        }
        """
        
        # MOCK (substituir pela API real)
        API_KEY = "sua chave"
        

        # The client gets the API key from the environment variable `GEMINI_API_KEY`.
        client = genai.Client(api_key=API_KEY)

        response = client.models.generate_content(
            model="gemini-3-flash-preview", contents=prompt
        )

        texto = response.text

        try:
            texto_limpo = limpar_resposta(texto)
            return json.loads(texto_limpo)
        except Exception as e:
            print("Erro ao converter resposta:", texto)
            return {
                "classe": "erro",
                "justificativa": "falha ao parsear resposta"
            }


    def processar_casos(casos):
        resultados = []

        for caso in casos:
            print(f"Processando ID {caso['id']}...")

            prompt = montar_prompt(caso["texto"])
            resposta = chamar_llm(prompt)

            if isinstance(resposta, str):
                try:
                    resposta = json.loads(resposta)
                except:
                    resposta = {
                        "classe": "erro",
                        "justificativa": "resposta inválida"
                    }

            resultado = {
                "id": caso["id"],
                "nivel": caso.get("nível", caso.get("nivel", "desconhecido")),
                "texto": caso["texto"],
                "classe_real": caso["classe_correta"],
                "classe_predita": resposta.get("classe", "erro"),
                "justificativa": resposta.get("justificativa", "erro"),
            }

            resultados.append(resultado)

            time.sleep(5)  # evita rate limit

        return resultados


    # ======================
    # EXECUÇÃO
    # ======================

    def main():
        casos = carregar_json(CAMINHO_GABARITO)

        resultados = processar_casos(casos)

        salvar_json(resultados, CAMINHO_SAIDA)

        print("Finalizado!")


    if __name__ == "__main__":
        main()

    time.sleep(60)