# README
==========================
Projeto criado para automatizar a coleta de CPF em planilhas e arquivos CSV.

Cenário:
Diretório com vários sub-diretórios, e cada um desses sub-diretórios possuem dezenas de arquivos XLSX, cada arquivo pode possui uma coluna com nome CPF pu CPF/CNPJ, que será lida pelo script (não importando a posição da coluna) e capturado o valor de cada linha. Este projeto faz a leitura de cada sub-diretório (nome e conteúdo) separadamente e manualmente.

# ARQUIVOS
read.py : Leitura dos arquivos em cada sub-diretório.
union.py : União dos arquivos resultantes de cada leitura em um único arquivo consolidado.

# PARÂMETROS

diretorio_planilhas : Caminho / nome do diretório com as planilhas
coluna_programa : Coluna com nome do diretório (programa que foi lido)
diretorio_resultado : Caminho / nome do diretório ontem será gravado o resultado da coleta

# NOTAS

CRIAR AMBIENTE VIRTUAL NO
python -m venv .venv

ATIVAR AMBIENTE VIRTUAL NO LINUX
source .venv/bin/activate

ATIVAR AMBIENTE VIRTUAL NO WINDOWS
.venv/Scripts/activate