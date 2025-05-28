# Pipeline Automatizado de Dados com Airflow, Python e SQL Server

## Descrição

Este projeto implementa um pipeline automatizado para geração, armazenamento e ingestão de dados simulados de pedidos de vendas de uma loja de roupas ficticia chamada Vexus. Utiliza Python para a criação dos dados e envio dos dados para o banco, Apache Airflow para orquestração e SQL Server para armazenamento e consulta.

## Funcionalidades

- Geração diária de dados simulados com base em produtos reais do banco SQL Server.
- Armazenamento dos dados em arquivos CSV organizados por data.
- Ingestão automática dos arquivos CSV para a base SQL Server.
- Validação de dados para evitar duplicidade e garantir integridade.
- Pipeline orquestrada e agendada via Apache Airflow.

## Tecnologias Utilizadas

- Python
- Apache Airflow
- SQL Server
- pandas
- pyodbc

## Estrutura do Projeto
- scripts
  - `__init__.py`
  - `db_utils.py`
  - `fake_data_generator.py`
  - `ingestion.py`
  - .env
- airflow
- raw_data
- .gitignore
- readme.md
- requirements.txt


## Como Executar

### 1. Configure o arquivo `.env` com as credenciais do banco de dados e insira as credenciais do banco de dados:

```env
DB_SERVER=seu_servidor
DB_DATABASE=seu_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```
### 2. Dentro da sua pasta do projeto, crie e ative um ambiente virtual para o Python:
```venv python -m venv venv
source venv/bin/activate       # Linux/Mac
.\venv\Scripts\activate        # Windows
```

### 3. Instale dependências
```req
pip install -r requirements.txt 
```

### 4. Dentro do ambiente virtual, execute o airflow
```airflow
airflow standalone
```

## 🚀 Próximos passos

🔁 Integração com Jenkins para deploy automático (CI/CD)

✅ Garantir idempotência nas execuções

🔍 Implementar verificações de qualidade e consistência dos dados

📈 Monitoramento e alertas para falhas no pipeline




--------------------
--------------------
--------------------
--------------------
--------------------
--------------------
 
## 📢 Contribuição
Sinta-se à vontade para abrir issues ou fazer PRs com melhorias, ideias ou correções.

#### 🧑‍💻 Autor
Desenvolvido por __Gabriel Paliato__

# 📲 Conecte-se comigo no LinkedIn
Estou sempre aberto a trocar experiências, compartilhar aprendizados e explorar novas oportunidades na área de Engenharia de Dados, Infraestrutura e DevOps.

Vamos nos conectar!
https://www.linkedin.com/in/gabriel-paliato-49467b211/