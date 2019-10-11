# Dicionário de Dados

## Tabela: `USUARIO`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado | Atributos         | Padrão | Descrição                                                    |
| ---------- | ------------ | ----------------- | ------ | ------------------------------------------------------------ |
| `username` | VARCHAR(45)  | PRIMARY, Not null |        | username que define o usuário - único PK                     |
| `email`    | VARCHAR(45)  | Not null          |        | Email do usuário                                             |
| `nome`     | VARCHAR(45)  | Not null          |        | Nome do usuário                                              |
| `idCIDADE` | VARCHAR(45)  | PRIMARY, Not null |        | Cidade em que o usuário mora<br /><br />**foreign key** para a coluna `idCIDADE` na tabela `CIDADE`. |

### Indices:

| Nome                   | Colunas                | Tipo    | Descrição |
| ---------------------- | ---------------------- | ------- | --------- |
| PRIMARY                | `username`, `idCIDADE` | PRIMARY |           |
| fk_USUARIO_CIDADE1_idx | `idCIDADE`             | INDEX   |           |

## Tabela: `PASSARO`

### Descrição:

### Colunas:

| Coluna         | Tipo de dado | Atributos         | Padrão | Descrição                  |
| -------------- | ------------ | ----------------- | ------ | -------------------------- |
| `tag_PASSARO`  | VARCHAR(20)  | PRIMARY, Not null |        | tag do pássaro             |
| `especie`      | VARCHAR(45)  |                   |        | espécie do pássaro         |
| `nome_popular` | VARCHAR(45)  |                   |        | nome mais usual do pássaro |

### Indices:

| Nome    | Colunas       | Tipo    | Descrição |
| ------- | ------------- | ------- | --------- |
| PRIMARY | `tag_PASSARO` | PRIMARY |           |

## Tabela: `USUARIO_PREFERE_PASSARO`

### Descrição:

### Colunas:

| Coluna        | Tipo de dado | Atributos         | Padrão | Descrição                                                    |
| ------------- | ------------ | ----------------- | ------ | ------------------------------------------------------------ |
| `username`    | VARCHAR(45)  | PRIMARY, Not null |        | username do usuário que prefere o pássaro<br /><br />**foreign key** para a coluna `username` na tabela `USUARIO`. |
| `tag_PASSARO` | VARCHAR(20)  | PRIMARY, Not null |        | tag do pássaro que é preferido pelo usuário<br /><br />**foreign key** para a coluna `tag_PASSARO` na tabela `PASSARO`. |

### Indices:

| Nome                                    | Colunas                   | Tipo    | Descrição |
| --------------------------------------- | ------------------------- | ------- | --------- |
| PRIMARY                                 | `username`, `tag_PASSARO` | PRIMARY |           |
| fk_USUARIO_PREFERE_PASSARO_PASSARO1_idx | `tag_PASSARO`             | INDEX   |           |

## Tabela: `CIDADE`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado | Atributos         | Padrão | Descrição                                              |
| ---------- | ------------ | ----------------- | ------ | ------------------------------------------------------ |
| `cidade`   | VARCHAR(45)  | Not null          |        |                                                        |
| `estado`   | VARCHAR(45)  | Not null          |        | Estado ao qual a cidade pertence                       |
| `idCIDADE` | VARCHAR(45)  | PRIMARY, Not null |        | Id da cidade em que o usuário mora - e seu nome também |

### Indices:

| Nome    | Colunas    | Tipo    | Descrição |
| ------- | ---------- | ------- | --------- |
| PRIMARY | `idCIDADE` | PRIMARY |           |

## Tabela: `POST`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado | Atributos                          | Padrão | Descrição                                                                                 |
| ---------- | ------------ | ---------------------------------- | ------ | ----------------------------------------------------------------------------------------- |
| `idPOST`   | INT          | PRIMARY, Auto increments, Not null |        | id so post                                                                                |
| `titulo`   | VARCHAR(45)  | Not null                           |        | títilo do post                                                                            |
| `texto`    | VARCHAR(255) |                                    |        | id do texto                                                                               |
| `URL_foto` | VARCHAR(100) |                                    |        | url da foto que pode estar relacionada ao post                                            |
| `deleta`   | TINYINT      | Not null                           |        | define se o post foi ou não deletado, ou seja, se ele será ou não mostrado na rede social |

### Indices:

| Nome    | Colunas  | Tipo    | Descrição |
| ------- | -------- | ------- | --------- |
| PRIMARY | `idPOST` | PRIMARY |           |

## Tabela: `TAG_PASSARO_POST`

### Descrição:

### Colunas:

| Coluna        | Tipo de dado | Atributos         | Padrão | Descrição                                                    |
| ------------- | ------------ | ----------------- | ------ | ------------------------------------------------------------ |
| `tag_PASSARO` | VARCHAR(20)  | PRIMARY, Not null |        | tag do pássaro que é mencionando no post<br /><br />**foreign key** para a coluna `tag_PASSARO` na tabela `PASSARO`. |
| `idPOST`      | INT          | PRIMARY, Not null |        | id do post que menciona o pássaro<br /><br />**foreign key** para a coluna `idPOST` na tabela `POST`. |

### Indices:

| Nome                     | Colunas                 | Tipo    | Descrição |
| ------------------------ | ----------------------- | ------- | --------- |
| PRIMARY                  | `tag_PASSARO`, `idPOST` | PRIMARY |           |
| fk_TAG_PASSARO_POST1_idx | `idPOST`                | INDEX   |           |

## Tabela: `VISUALIZACAO`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado  | Atributos         | Padrão | Descrição                                                                                                          |
| ---------- | ------------- | ----------------- | ------ | ------------------------------------------------------------------------------------------------------------------ |
| `idACESSO` | INT           | PRIMARY, Not null |        | id do acesso em que a visualização ocorreu<br /><br />**foreign key** para a coluna `idACESSO` na tabela `ACESSO`. |
| `idPOST`   | INT           | PRIMARY, Not null |        | id do post que foi visualizado<br /><br />**foreign key** para a coluna `idPOST` na tabela `POST`.                 |
| `username` | VARCHAR(45)   | Not null          |        | usuário que executou a visualização<br /><br />**foreign key** para a coluna `username` na tabela `USUARIO`.       |
| `stamp`    | TIMESTAMP(11) | PRIMARY, Not null |        | momento em que a visualização aconteceu                                                                            |

### Indices:

| Nome                         | Colunas                       | Tipo    | Descrição |
| ---------------------------- | ----------------------------- | ------- | --------- |
| PRIMARY                      | `idACESSO`, `idPOST`, `stamp` | PRIMARY |           |
| fk_VISUALIZACAO_POST1_idx    | `idPOST`                      | INDEX   |           |
| fk_VISUALIZACAO_USUARIO1_idx | `username`                    | INDEX   |           |

## Tabela: `ACESSO`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado | Atributos                          | Padrão | Descrição                                                           |
| ---------- | ------------ | ---------------------------------- | ------ | ------------------------------------------------------------------- |
| `idACESSO` | INT          | PRIMARY, Auto increments, Not null |        | id do acesso                                                        |
| `IP`       | VARCHAR(45)  |                                    |        | IP que foi usado para executar a visualização                       |
| `Browser`  | VARCHAR(45)  |                                    |        | browser que foi utilizado no acesso em que a visualização aconteceu |
| `Aparelho` | VARCHAR(45)  |                                    |        | aparelho utilizado para executar o acesso atrelado à visualização   |

### Indices:

| Nome    | Colunas    | Tipo    | Descrição |
| ------- | ---------- | ------- | --------- |
| PRIMARY | `idACESSO` | PRIMARY |           |

## Tabela: `TAG_USUARIO_POST`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado | Atributos         | Padrão | Descrição                                                                                                            |
| ---------- | ------------ | ----------------- | ------ | -------------------------------------------------------------------------------------------------------------------- |
| `username` | VARCHAR(45)  | PRIMARY, Not null |        | usernema do usuário ao qual o post pertence<br /><br />**foreign key** para a coluna `username` na tabela `USUARIO`. |
| `idPOST`   | INT          | PRIMARY, Not null |        | is do post que pertence ao usuário<br /><br />**foreign key** para a coluna `idPOST` na tabela `POST`.               |

### Indices:

| Nome                        | Colunas              | Tipo    | Descrição |
| --------------------------- | -------------------- | ------- | --------- |
| fk_TAG_USUARIO_USUARIO1_idx | `username`           | INDEX   |           |
| fk_TAG_USUARIO_POST1_idx    | `idPOST`             | INDEX   |           |
| PRIMARY                     | `username`, `idPOST` | PRIMARY |           |
