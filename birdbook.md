# Dicionário de Dados

## Tabela: `USUARIO`

### Descrição: 

### Colunas:

| Coluna     | Tipo de dado | Atributos         | Padrão | Descrição                                              |
| ---------- | ------------ | ----------------- | ------ | ------------------------------------------------------ |
| `username` | VARCHAR(45)  | PRIMARY, Not null |        |                                                        |
| `email`    | VARCHAR(45)  | Not null          |        |                                                        |
| `nome`     | VARCHAR(45)  | Not null          |        |                                                        |
| `cidade`   | VARCHAR(45)  | Not null          |        | **foreign key** to Coluna `cidade` on Tabela `CIDADE`. |

### Indices:

| Name                     | Colunas    | Tipo    | Descrição |
| ------------------------ | ---------- | ------- | --------- |
| PRIMARY                  | `username` | PRIMARY |           |
| fk_USUARIO_ENDERECO1_idx | `cidade`   | INDEX   |           |

## Tabela: `PASSARO`

### Descrição:

### Colunas:

| Coluna         | Tipo de dado | Atributos         | Padrão | Descrição |
| -------------- | ------------ | ----------------- | ------ | --------- |
| `tag_PASSARO`  | VARCHAR(20)  | PRIMARY, Not null |        |           |
| `especie`      | VARCHAR(45)  |                   |        |           |
| `nome_popular` | VARCHAR(45)  |                   |        |           |

### Indices:

| Name    | Colunas       | Tipo    | Descrição |
| ------- | ------------- | ------- | --------- |
| PRIMARY | `tag_PASSARO` | PRIMARY |           |

## Tabela: `USUARIO_PREFERE_PASSARO`

### Descrição:

### Colunas:

| Coluna        | Tipo de dado | Atributos         | Padrão | Descrição                                                    |
| ------------- | ------------ | ----------------- | ------ | ------------------------------------------------------------ |
| `username`    | VARCHAR(45)  | PRIMARY, Not null |        | **foreign key** to Coluna `username` on Tabela `USUARIO`.    |
| `tag_PASSARO` | VARCHAR(20)  | PRIMARY, Not null |        | **foreign key** to Coluna `tag_PASSARO` on Tabela `PASSARO`. |

### Indices:

| Name                                    | Colunas                   | Tipo    | Descrição |
| --------------------------------------- | ------------------------- | ------- | --------- |
| PRIMARY                                 | `username`, `tag_PASSARO` | PRIMARY |           |
| fk_USUARIO_PREFERE_PASSARO_PASSARO1_idx | `tag_PASSARO`             | INDEX   |           |

## Tabela: `CIDADE`

### Descrição:

### Colunas:

| Coluna   | Tipo de dado | Atributos         | Padrão | Descrição |
| -------- | ------------ | ----------------- | ------ | --------- |
| `cidade` | VARCHAR(45)  | PRIMARY, Not null |        |           |

### Indices:

| Name    | Colunas  | Tipo    | Descrição |
| ------- | -------- | ------- | --------- |
| PRIMARY | `cidade` | PRIMARY |           |

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

| Name    | Colunas  | Tipo    | Descrição |
| ------- | -------- | ------- | --------- |
| PRIMARY | `idPOST` | PRIMARY |           |

## Tabela: `TAG_PASSARO_POST`

### Descrição:

### Colunas:

| Coluna        | Tipo de dado | Atributos         | Padrão | Descrição                                                    |
| ------------- | ------------ | ----------------- | ------ | ------------------------------------------------------------ |
| `tag_PASSARO` | VARCHAR(20)  | PRIMARY, Not null |        | **foreign key** to Coluna `tag_PASSARO` on Tabela `PASSARO`. |
| `idPOST`      | INT          | PRIMARY, Not null |        | **foreign key** to Coluna `idPOST` on Tabela `POST`.         |

### Indices:

| Name                     | Colunas                 | Tipo    | Descrição |
| ------------------------ | ----------------------- | ------- | --------- |
| PRIMARY                  | `tag_PASSARO`, `idPOST` | PRIMARY |           |
| fk_TAG_PASSARO_POST1_idx | `idPOST`                | INDEX   |           |

## Tabela: `VISUALIZACAO`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado  | Atributos         | Padrão | Descrição                                                 |
| ---------- | ------------- | ----------------- | ------ | --------------------------------------------------------- |
| `idACESSO` | INT           | PRIMARY, Not null |        | **foreign key** to Coluna `idACESSO` on Tabela `ACESSO`.  |
| `idPOST`   | INT           | PRIMARY, Not null |        | **foreign key** to Coluna `idPOST` on Tabela `POST`.      |
| `username` | VARCHAR(45)   | Not null          |        | **foreign key** to Coluna `username` on Tabela `USUARIO`. |
| `stamp`    | TIMESTAMP(11) | PRIMARY, Not null |        |                                                           |

### Indices:

| Name                         | Colunas                       | Tipo    | Descrição |
| ---------------------------- | ----------------------------- | ------- | --------- |
| PRIMARY                      | `idACESSO`, `idPOST`, `stamp` | PRIMARY |           |
| fk_VISUALIZACAO_POST1_idx    | `idPOST`                      | INDEX   |           |
| fk_VISUALIZACAO_USUARIO1_idx | `username`                    | INDEX   |           |

## Tabela: `ACESSO`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado | Atributos                          | Padrão | Descrição |
| ---------- | ------------ | ---------------------------------- | ------ | --------- |
| `idACESSO` | INT          | PRIMARY, Auto increments, Not null |        |           |
| `IP`       | VARCHAR(45)  |                                    |        |           |
| `Browser`  | VARCHAR(45)  |                                    |        |           |
| `Aparelho` | VARCHAR(45)  |                                    |        |           |

### Indices:

| Name    | Colunas    | Tipo    | Descrição |
| ------- | ---------- | ------- | --------- |
| PRIMARY | `idACESSO` | PRIMARY |           |

## Tabela: `TAG_USUARIO_POST`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado | Atributos         | Padrão | Descrição                                                 |
| ---------- | ------------ | ----------------- | ------ | --------------------------------------------------------- |
| `username` | VARCHAR(45)  | PRIMARY, Not null |        | **foreign key** to Coluna `username` on Tabela `USUARIO`. |
| `idPOST`   | INT          | PRIMARY, Not null |        | **foreign key** to Coluna `idPOST` on Tabela `POST`.      |

### Indices:

| Nome                        | Coluna               | Tipo    | Descrição |
| --------------------------- | -------------------- | ------- | --------- |
| fk_TAG_USUARIO_USUARIO1_idx | `username`           | INDEX   |           |
| fk_TAG_USUARIO_POST1_idx    | `idPOST`             | INDEX   |           |
| PRIMARY                     | `username`, `idPOST` | PRIMARY |           |
