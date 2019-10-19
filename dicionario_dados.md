# Dicionário de dados

## Tabela: `acesso`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado | Atributos                          | Padrão | Descrição                                                           |
| ---------- | ------------ | ---------------------------------- | ------ | ------------------------------------------------------------------- |
| `idACESSO` | INT          | PRIMARY, Auto increments, Not null |        | id do acesso                                                        |
| `IP`       | VARCHAR(45)  |                                    | `NULL` | IP que foi usado para executar a visualização                       |
| `Browser`  | VARCHAR(45)  |                                    | `NULL` | browser que foi utilizado no acesso em que a visualização aconteceu |
| `Aparelho` | VARCHAR(45)  |                                    | `NULL` | aparelho utilizado para executar o acesso atrelado à visualização   |

### Indices:

| Nome    | Colunas    | Tipo    | Descrição |
| ------- | ---------- | ------- | --------- |
| PRIMARY | `idACESSO` | PRIMARY |           |

## Tabela: `cidade`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado | Atributos                          | Padrão | Descrição                        |
| ---------- | ------------ | ---------------------------------- | ------ | -------------------------------- |
| `cidade`   | VARCHAR(45)  | Not null                           |        | Nome da cidade                   |
| `estado`   | VARCHAR(45)  | Not null                           |        | Estado ao qual a cidade pertence |
| `idCIDADE` | INT          | PRIMARY, Auto increments, Not null |        | Id da tabela                     |

### Indices:

| Nome    | Colunas    | Tipo    | Descrição |
| ------- | ---------- | ------- | --------- |
| PRIMARY | `idCIDADE` | PRIMARY |           |

## Tabela: `joinha`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado | Atributos         | Padrão | Descrição                                                    |
| ---------- | ------------ | ----------------- | ------ | ------------------------------------------------------------ |
| `username` | VARCHAR(45)  | PRIMARY, Not null |        | username do usuário que deu joinha no post<br /><br />**foreign key** para a coluna `username` na tabela `usuario`. |
| `reacao`   | INT          |                   | `'0'`  | **-1** não curtiu, **0** neutro e 1 curtiu                   |
| `idPOST`   | INT          | PRIMARY, Not null |        | id do post que foi curtido pelo usuário<br /><br />**foreign key** para a coluna `idPOST` na tabela `post`. |

### Indices:

| Nome    | Colunas              | Tipo    | Descrição |
| ------- | -------------------- | ------- | --------- |
| PRIMARY | `username`, `idPOST` | PRIMARY |           |
| idPOST  | `idPOST`             | INDEX   |           |

## Tabela: `passaro`

### Descrição:

### Colunas:

| Coluna         | Tipo de dado | Atributos         | Padrão | Descrição                  |
| -------------- | ------------ | ----------------- | ------ | -------------------------- |
| `tag_PASSARO`  | VARCHAR(20)  | PRIMARY, Not null |        | tag do pássaro             |
| `especie`      | VARCHAR(45)  |                   | `NULL` | espécie do pássaro         |
| `nome_popular` | VARCHAR(45)  |                   | `NULL` | nome mais usual do pássaro |

### Indices:

| Nome    | Colunas       | Tipo    | Descrição |
| ------- | ------------- | ------- | --------- |
| PRIMARY | `tag_PASSARO` | PRIMARY |           |

## Tabela: `post`

### Descrição:

### Colunas:

| Coluna       | Tipo de dado | Atributos                          | Padrão              | Descrição                                                                                 |
| ------------ | ------------ | ---------------------------------- | ------------------- | ----------------------------------------------------------------------------------------- |
| `idPOST`     | INT          | PRIMARY, Auto increments, Not null |                     | id so post                                                                                |
| `titulo`     | VARCHAR(45)  | Not null                           |                     | títilo do post                                                                            |
| `texto`      | VARCHAR(255) |                                    | `NULL`              | id do texto                                                                               |
| `URL_foto`   | VARCHAR(100) |                                    | `NULL`              | url da foto que pode estar relacionada ao post                                            |
| `deleta`     | TINYINT      | Not null                           | `'0'`               | define se o post foi ou não deletado, ou seja, se ele será ou não mostrado na rede social |
| `username`   | VARCHAR(45)  | Not null                           |                     | **foreign key** para a coluna `username` na tabela `usuario`.                             |
| `stamp_post` | TIMESTAMP    | Not null                           | `CURRENT_TIMESTAMP` | momento em que a publicação do post aconteceu                                             |

### Indices:

| Nome       | Colunas      | Tipo    | Descrição |
| ---------- | ------------ | ------- | --------- |
| PRIMARY    | `idPOST`     | PRIMARY |           |
| username   | `username`   | INDEX   |           |
| stamp_post | `stamp_post` | INDEX   |           |

## Tabela: `tag_passaro_post`

### Descrição:

### Colunas:

| Coluna        | Tipo de dado | Atributos         | Padrão | Descrição                                                                                                            |
| ------------- | ------------ | ----------------- | ------ | -------------------------------------------------------------------------------------------------------------------- |
| `tag_PASSARO` | VARCHAR(20)  | PRIMARY, Not null |        | tag do pássaro que é mencionando no post<br /><br />**foreign key** para a coluna `tag_PASSARO` na tabela `passaro`. |
| `idPOST`      | INT          | PRIMARY, Not null |        | id do post que menciona o pássaro<br /><br />**foreign key** para a coluna `idPOST` na tabela `post`.                |

### Indices:

| Nome    | Colunas                 | Tipo    | Descrição |
| ------- | ----------------------- | ------- | --------- |
| PRIMARY | `tag_PASSARO`, `idPOST` | PRIMARY |           |
| idPOST  | `idPOST`                | INDEX   |           |

## Tabela: `tag_usuario_post`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado | Atributos         | Padrão | Descrição                                                                                                            |
| ---------- | ------------ | ----------------- | ------ | -------------------------------------------------------------------------------------------------------------------- |
| `username` | VARCHAR(45)  | PRIMARY, Not null |        | usernema do usuário ao qual o post pertence<br /><br />**foreign key** para a coluna `username` na tabela `usuario`. |
| `idPOST`   | INT          | PRIMARY, Not null |        | is do post que pertence ao usuário<br /><br />**foreign key** para a coluna `idPOST` na tabela `post`.               |

### Indices:

| Nome    | Colunas              | Tipo    | Descrição |
| ------- | -------------------- | ------- | --------- |
| PRIMARY | `username`, `idPOST` | PRIMARY |           |
| idPOST  | `idPOST`             | INDEX   |           |

## Tabela: `usuario`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado | Atributos         | Padrão | Descrição                                                                                            |
| ---------- | ------------ | ----------------- | ------ | ---------------------------------------------------------------------------------------------------- |
| `username` | VARCHAR(45)  | PRIMARY, Not null |        | username que define o usuário - único PK                                                             |
| `email`    | VARCHAR(45)  | Not null          |        | Email do usuário                                                                                     |
| `nome`     | VARCHAR(45)  | Not null          |        | Nome do usuário                                                                                      |
| `idCIDADE` | INT          | Not null          |        | Cidade em que o usuário mora<br /><br />**foreign key** para a coluna `idCIDADE` na tabela `cidade`. |

### Indices:

| Nome         | Colunas    | Tipo    | Descrição |
| ------------ | ---------- | ------- | --------- |
| PRIMARY      | `username` | PRIMARY |           |
| cidadeexiste | `idCIDADE` | INDEX   |           |

## Tabela: `usuario_prefere_passaro`

### Descrição:

### Colunas:

| Coluna        | Tipo de dado | Atributos         | Padrão | Descrição                                                                                                               |
| ------------- | ------------ | ----------------- | ------ | ----------------------------------------------------------------------------------------------------------------------- |
| `username`    | VARCHAR(45)  | PRIMARY, Not null |        | username do usuário que prefere o pássaro<br /><br />**foreign key** para a coluna `username` na tabela `usuario`.      |
| `tag_PASSARO` | VARCHAR(20)  | PRIMARY, Not null |        | tag do pássaro que é preferido pelo usuário<br /><br />**foreign key** para a coluna `tag_PASSARO` na tabela `passaro`. |

### Indices:

| Nome        | Colunas                   | Tipo    | Descrição |
| ----------- | ------------------------- | ------- | --------- |
| PRIMARY     | `username`, `tag_PASSARO` | PRIMARY |           |
| tag_PASSARO | `tag_PASSARO`             | INDEX   |           |

## Tabela: `visualizacao`

### Descrição:

### Colunas:

| Coluna     | Tipo de dado | Atributos         | Padrão              | Descrição                                                                                                          |
| ---------- | ------------ | ----------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `idACESSO` | INT          | PRIMARY, Not null |                     | id do acesso em que a visualização ocorreu<br /><br />**foreign key** para a coluna `idACESSO` na tabela `acesso`. |
| `idPOST`   | INT          | PRIMARY, Not null |                     | id do post que foi visualizado<br /><br />**foreign key** para a coluna `idPOST` na tabela `post`.                 |
| `username` | VARCHAR(45)  | Not null          |                     | usuário que executou a visualização<br /><br />**foreign key** para a coluna `username` na tabela `usuario`.       |
| `stamp`    | TIMESTAMP    | PRIMARY, Not null | `CURRENT_TIMESTAMP` | momento em que a visualização aconteceu                                                                            |

### Indices:

| Nome     | Colunas                       | Tipo    | Descrição |
| -------- | ----------------------------- | ------- | --------- |
| PRIMARY  | `idACESSO`, `idPOST`, `stamp` | PRIMARY |           |
| idPOST   | `idPOST`                      | INDEX   |           |
| username | `username`                    | INDEX   |           |
