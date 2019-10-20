# birdbook

`David Fogelman & Manoela Campos`

## Configuração

- Instale os pacotes python descritos no `requirements.txt` com `pip3 install requirements.txt`

* Coloque as suas credencias no arquivo `./config/config_tests.json`

## Arquivos

- [Modelo Relacional](./modelo-relacional.pdf)
- [Dicionário de dados](./dicionario_dados.md)
- [Modelo entidade relacionamento](./entidade-relacionamento.pdf)

- [Modelo Workbench](./models/modelo_birdbook.mwb)

## Execução de testes

- Configure as credenciais de teste no arquivo `./config/config_tests.json`

```
cd tests
python3 test_projeto.py
```

## Execução da API

```
cd api
uvicorn main:app
```
