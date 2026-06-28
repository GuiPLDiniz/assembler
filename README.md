# Hack Assembler – Project 06

## Disciplina

Compiladores

## Integrante

* **Guilherme Pessoa Lima Diniz**
* **Matrícula:** 20260001310

---

## Linguagem Utilizada

* Python 3
* Versão utilizada: Python 3.14

---

# Descrição do Projeto

Este projeto implementa um **Assembler para a arquitetura Hack**, conforme especificado no **Project 06** do curso **nand2tetris**.

O assembler é responsável por traduzir programas escritos em Assembly Hack (`.asm`) para código de máquina (`.hack`), executando o processo em duas passagens sobre o arquivo de entrada.

Durante a tradução são tratados:

- Instruções do tipo **A**
- Instruções do tipo **C**
- Labels
- Variáveis
- Símbolos pré-definidos da arquitetura Hack

Ao final da execução é gerado automaticamente um arquivo `.hack` equivalente ao programa Assembly fornecido.

---

# Funcionalidades Implementadas

## Parser

Responsável por:

- Ler arquivos `.asm`;
- Ignorar comentários;
- Ignorar linhas em branco;
- Identificar o tipo de instrução;
- Extrair os campos necessários para tradução.

Tipos de instruções reconhecidas:

- A-Instruction
- C-Instruction
- L-Instruction (labels)

---

## Tradução das A-Instructions

Implementada a tradução de instruções do tipo:

```asm
@21
```

para:

```text
0000000000010101
```

Também são suportados:

- Endereços numéricos;
- Labels;
- Variáveis.

---

## Tradução das C-Instructions

Implementada a tradução completa dos campos:

- dest
- comp
- jump

Exemplo:

```asm
D=M+1;JGT
```

é convertido automaticamente para sua representação binária correspondente.

---

## Primeira Passagem

Na primeira leitura do arquivo são identificadas todas as labels.

Exemplo:

```asm
(LOOP)
```

As labels são armazenadas na tabela de símbolos associadas ao endereço correto da ROM.

---

## Segunda Passagem

Na segunda leitura são resolvidos:

- símbolos pré-definidos;
- labels;
- variáveis.

Variáveis ainda não existentes recebem endereços automaticamente a partir da RAM 16, conforme especificação da arquitetura Hack.

---

## Tabela de Símbolos

Foram implementados todos os símbolos pré-definidos:

- SP
- LCL
- ARG
- THIS
- THAT
- R0 até R15
- SCREEN
- KBD

Além disso, são adicionadas dinamicamente:

- labels;
- variáveis do programa.

---

# Estrutura do Projeto

```text
assembler/
│
├── src/
│   ├── main.py
│   ├── parser.py
│   ├── code.py
│   ├── symbol_table.py
│   
│
├── tests/
│   ├── project06/
│       ├── add/
│       ├── max/
│       ├── rect/
│       └── pong/
│   
│
├── .gitignore
└── README.md
```

---

# Componentes do Sistema

## Parser

Responsável por:

- leitura do arquivo Assembly;
- classificação das instruções;
- extração dos campos de cada instrução.

Principais métodos:

- `has_more_commands()`
- `advance()`
- `command_type()`
- `symbol()`
- `dest()`
- `comp()`
- `jump()`

---

## Code

Responsável pela tradução das instruções Assembly para código binário.

Principais funcionalidades:

- conversão de instruções A;
- tradução dos campos `comp`;
- tradução dos campos `dest`;
- tradução dos campos `jump`.

---

## SymbolTable

Responsável pelo gerenciamento da tabela de símbolos.

Principais operações:

- adicionar símbolos;
- verificar existência;
- recuperar endereços;
- armazenar labels;
- armazenar variáveis.

---

## Main

Coordena todo o processo de montagem.

Fluxo executado:

1. leitura do arquivo `.asm`;
2. primeira passagem (labels);
3. segunda passagem (variáveis);
4. tradução das instruções;
5. geração do arquivo `.hack`.

---

# Como Executar

Exemplo:

```bash
python src/main.py tests/project06/add/Add.asm
```

O programa gera automaticamente:

```text
Add.hack
```

na mesma pasta do arquivo de entrada.

Outro exemplo:

```bash
python src/main.py tests/project06/max/Max.asm
```

---

# Exemplo de Tradução

Entrada:

```asm
@2
D=A
@3
D=D+A
@0
M=D
```

Saída:

```text
0000000000000010
1110110000010000
0000000000000011
1110000010010000
0000000000000000
1110001100001000
```

---

# Estratégia de Implementação

O desenvolvimento foi realizado de forma incremental, utilizando commits para registrar cada etapa da implementação.

As principais etapas foram:

1. criação da estrutura inicial do projeto;
2. implementação do Parser;
3. conversão de instruções A;
4. implementação das tabelas de tradução das instruções C;
5. integração do processo de geração do arquivo `.hack`;
6. implementação da tabela de símbolos;
7. implementação da primeira passagem (labels);
8. implementação da segunda passagem (variáveis);
9. suporte à execução por linha de comando;
10. validação utilizando os programas oficiais do Project 06.

Essa abordagem facilitou a identificação de erros e permitiu validar cada funcionalidade antes da implementação da etapa seguinte.

---

# Testes Realizados

Foram utilizados os programas oficiais disponibilizados para o **Project 06** do nand2tetris.

Programas testados:

- Add.asm
- Max.asm
- Rect.asm
- Pong.asm

Os arquivos Assembly foram traduzidos para código de máquina pelo assembler desenvolvido e executados no **CPU Emulator**.

Resultados obtidos:

- **Add.asm:** soma executada corretamente.
- **Max.asm:** comparação entre dois valores realizada corretamente.
- **Rect.asm:** desenho do retângulo realizado corretamente.
- **Pong.asm:** execução completa do jogo validada com sucesso.

Todos os programas executaram corretamente no CPU Emulator, demonstrando o correto funcionamento do assembler implementado.

---

# Conclusão

O projeto atende aos requisitos especificados para o **Project 06 — Hack Assembler** do curso nand2tetris.

Foram implementadas todas as funcionalidades necessárias para traduzir programas escritos em Assembly Hack para código de máquina, incluindo resolução de símbolos, labels e variáveis.

A implementação foi validada por meio da execução dos programas oficiais do Project 06 no CPU Emulator, obtendo os resultados esperados em todos os testes realizados.