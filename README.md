# Motor de Anonimização de Dados (DLP)

## Descrição
Script em Python focado em Prevenção de Perda de Dados (DLP) e conformidade com a LGPD. A ferramenta utiliza Expressões Regulares (Regex) para identificar e mascarar Informações Pessoalmente Identificáveis (PII), como CPFs e endereços de e-mail, em textos não estruturados.

## Funcionalidades
- Identificação precisa de padrões de CPF e E-mail via Regex.
- Mascaramento parcial de caracteres (Data Masking) para impedir a reidentificação direta.
- Arquitetura de processamento em memória, sem gravação de logs dos dados originais.

## Pré-requisitos
- Ambiente Linux (testado via CLI no Ubuntu).
- Python 3.x (biblioteca `re` nativa).

## Como Executar

Execute o script diretamente pelo terminal para visualizar o processo de mascaramento no texto de teste:

```bash
python3 anonimizador.py
```
