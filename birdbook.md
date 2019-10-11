# Dicionário de Dados

## Tabela: `USUARIO`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado | Atributos         | Padrão | Descrição                                                  |
| ---------- | ------------ | ----------------- | ------ | ---------------------------------------------------------- |
| `username` | VARCHAR(45)  | PRIMARY, Not null |        |                                                            |
| `email`    | VARCHAR(45)  | Not null          |        |                                                            |
| `nome`     | VARCHAR(45)  | Not null          |        |                                                            |
| `idCIDADE` | VARCHAR(45)  | PRIMARY, Not null |        | **foreign key** para coluna `idCIDADE` na tabela `CIDADE`. |

### Indices:

| Nome                   | Colunas                | Tipo    | Descrição |
| ---------------------- | ---------------------- | ------- | --------- |
| PRIMARY                | `username`, `idCIDADE` | PRIMARY |           |
| fk_USUARIO_CIDADE1_idx | `idCIDADE`             | INDEX   |           |

## Tabela: `PASSARO`

### Descrição:

### Colunas:

| Coluna         | Tipo de dado | Atributos         | Padrão | Descrição                                                                      |
| -------------- | ------------ | ----------------- | ------ | ------------------------------------------------------------------------------ |
| `tag_PASSARO`  | VARCHAR(20)  | PRIMARY, Not null |        | tag é único utilizado para identificar os pássaros e para fazer tags nos posts |
| `especie`      | VARCHAR(45)  |                   |        | Espécie de cada pássaro                                                        |
| `nome_popular` | VARCHAR(45)  |                   |        | Nome popular de cada pássaro                                                   |

### Indices:

| Nome    | Colunas       | Tipo    | Descrição |
| ------- | ------------- | ------- | --------- |
| PRIMARY | `tag_PASSARO` | PRIMARY |           |

## Tabela: `USUARIO_PREFERE_PASSARO`

### Descrição:

### Colunas:

| Coluna        | Tipo de dado | Atributos         | Padrão | Descrição                                                      |
| ------------- | ------------ | ----------------- | ------ | -------------------------------------------------------------- |
| `username`    | VARCHAR(45)  | PRIMARY, Not null |        | **foreign key** para Coluna `username` na Tabela `USUARIO`.    |
| `tag_PASSARO` | VARCHAR(20)  | PRIMARY, Not null |        | **foreign key** para Coluna `tag_PASSARO` na Tabela `PASSARO`. |

### Indices:

| Nome                                    | Colunas                   | Tipo    | Descrição |
| --------------------------------------- | ------------------------- | ------- | --------- |
| PRIMARY                                 | `username`, `tag_PASSARO` | PRIMARY |           |
| fk_USUARIO_PREFERE_PASSARO_PASSARO1_idx | `tag_PASSARO`             | INDEX   |           |

## Tabela: `CIDADE`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado | Atributos         | Padrão | Descrição |
| ---------- | ------------ | ----------------- | ------ | --------- |
| `cidade`   | VARCHAR(45)  | Not null          |        |           |
| `estado`   | VARCHAR(45)  | Not null          |        |           |
| `idCIDADE` | VARCHAR(45)  | PRIMARY, Not null |        |           |

### Indices:

| Nome    | Colunas    | Tipo    | Descrição |
| ------- | ---------- | ------- | --------- |
| PRIMARY | `idCIDADE` | PRIMARY |           |

## Tabela: `POST`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado | Atributos                          | Padrão | Descrição |
| ---------- | ------------ | ---------------------------------- | ------ | --------- |
| `idPOST`   | INT          | PRIMARY, Auto increments, Not null |        |           |
| `titulo`   | VARCHAR(45)  | Not null                           |        |           |
| `texto`    | VARCHAR(255) |                                    |        |           |
| `URL_foto` | VARCHAR(100) |                                    |        |           |
| `deleta`   | TINYINT      | Not null                           |        |           |

### Indices:

| Nome    | Colunas  | Tipo    | Descrição |
| ------- | -------- | ------- | --------- |
| PRIMARY | `idPOST` | PRIMARY |           |

## Tabela: `TAG_PASSARO_POST`

### Descrição:

### Colunas:

| Coluna        | Tipo de dado | Atributos         | Padrão | Descrição                                                      |
| ------------- | ------------ | ----------------- | ------ | -------------------------------------------------------------- |
| `tag_PASSARO` | VARCHAR(20)  | PRIMARY, Not null |        | **foreign key** para Coluna `tag_PASSARO` na Tabela `PASSARO`. |
| `idPOST`      | INT          | PRIMARY, Not null |        | **foreign key** para Coluna `idPOST` na Tabela `POST`.         |

### Indices:

| Nome                     | Colunas                 | Tipo    | Descrição |
| ------------------------ | ----------------------- | ------- | --------- |
| PRIMARY                  | `tag_PASSARO`, `idPOST` | PRIMARY |           |
| fk_TAG_PASSARO_POST1_idx | `idPOST`                | INDEX   |           |

## Tabela: `VISUALIZACAO`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado  | Atributos         | Padrão | Descrição                                                   |
| ---------- | ------------- | ----------------- | ------ | ----------------------------------------------------------- |
| `idACESSO` | INT           | PRIMARY, Not null |        | **foreign key** para Coluna `idACESSO` na Tabela `ACESSO`.  |
| `idPOST`   | INT           | PRIMARY, Not null |        | **foreign key** para Coluna `idPOST` na Tabela `POST`.      |
| `username` | VARCHAR(45)   | Not null          |        | **foreign key** para Coluna `username` na Tabela `USUARIO`. |
| `stamp`    | TIMESTAMP(11) | PRIMARY, Not null |        |                                                             |

### Indices:

| Nome                         | Colunas                       | Tipo    | Descrição |
| ---------------------------- | ----------------------------- | ------- | --------- |
| PRIMARY                      | `idACESSO`, `idPOST`, `stamp` | PRIMARY |           |
| fk_VISUALIZACAO_POST1_idx    | `idPOST`                      | INDEX   |           |
| fk_VISUALIZACAO_USUARIO1_idx | `username`                    | INDEX   |           |

## Tabela: `ACESSO`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado | Atributos                          | Padrão | Descrição                                                  |
| ---------- | ------------ | ---------------------------------- | ------ | ---------------------------------------------------------- |
| `idACESSO` | INT          | PRIMARY, Auto increments, Not null |        | ID único do acesso do usuário                              |
| `IP`       | VARCHAR(45)  |                                    |        | IP de acesso                                               |
| `Browser`  | VARCHAR(45)  |                                    |        | Browser/ User-Agent                                        |
| `Aparelho` | VARCHAR(45)  |                                    |        | Aparelho que o usuário está utilizando para acessar o site |

### Indices:

| Nome    | Colunas    | Tipo    | Descrição |
| ------- | ---------- | ------- | --------- |
| PRIMARY | `idACESSO` | PRIMARY |           |

## Tabela: `TAG_USUARIO_POST`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado | Atributos         | Padrão | Descrição                                                   |
| ---------- | ------------ | ----------------- | ------ | ----------------------------------------------------------- |
| `username` | VARCHAR(45)  | PRIMARY, Not null |        | **foreign key** para Coluna `username` na Tabela `USUARIO`. |
| `idPOST`   | INT          | PRIMARY, Not null |        | **foreign key** para Coluna `idPOST` na Tabela `POST`.      |

### Indices:

| Nome                        | Coluna               | Tipo    | Descrição |
| --------------------------- | -------------------- | ------- | --------- |
| fk_TAG_USUARIO_USUARIO1_idx | `username`           | INDEX   |           |
| fk_TAG_USUARIO_POST1_idx    | `idPOST`             | INDEX   |           |
| PRIMARY                     | `username`, `idPOST` | PRIMARY |           |
