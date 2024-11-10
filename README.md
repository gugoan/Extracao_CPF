README
=================================

Projeto criado para automatizar a coleta de CPF em planilhas e arquivos CSV.

Cenário:
Diretório com vários sub-diretórios, e cada um desses sub-diretórios possuem dezenas de arquivos XLSX, cada arquivo pode possui uma coluna com nome CPF pu CPF/CNPJ, que será lida pelo script (não importando a posição da coluna) e capturado o valor de cada linha. Este projeto faz a leitura de cada sub-diretório (nome e conteúdo) separadamente e manualmente.

TODO
------------

Possibilidade de leitura mesmo quando rótulo estiver como CONFIDENCIAL, RESTRITO, etc
Leitura recursiva dos diretórios

Antes de executar validate_cpf, limpar os registros com CPF fora do padrão (contém ".,/\") e diferente de 11 caracteres (verificar funcionamento da "função tratar_cpf")

ARQUIVOS
------------

1. read.py : Leitura dos arquivos em cada sub-diretório.
2. union.py : União dos arquivos resultantes de cada leitura em um único arquivo consolidado.
3. validate_cpf.py : Cria uma nova coluna informando se o CPF é válido.

PARÂMETROS
------------

diretorio_planilhas : Caminho / nome do diretório com as planilhas
coluna_programa : Coluna com nome do diretório (programa que foi lido)
diretorio_resultado : Caminho / nome do diretório ontem será gravado o resultado da coleta

NOTAS
------------

CRIAR AMBIENTE VIRTUAL NO
python -m venv .venv

ATIVAR AMBIENTE VIRTUAL NO LINUX
source .venv/bin/activate

ATIVAR AMBIENTE VIRTUAL NO WINDOWS
.venv/Scripts/activate
