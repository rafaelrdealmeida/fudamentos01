# Mini-curso Fundamento de Análise de dados

Mini-curso de fundamentos de **analise de dados**

`ls`

## Preparação do ambiente de trabalho

### Versionamento

- GITHUB e GITLAB: rede social para compartilhamento de código
- GIT: versionador de código
- [ohshitgit](https://ohshitgit.com/)

```
git add .
```


```
git commit -m " inserir mensagem aqui"
```


```
git pull origin main
```


```
git push origin main
```
### Comando básico Linux

```
ls
cd
cd..
mkdir
cat
history
rm -r
cp caminho_origem caminho_destino
mv caminho_origem caminho_destino
touch teste.txt

```

### Editor de código

 - VScode
 - Google Colab

 ### Ambiente Virtual

 - Conda e Poetry são os dois principais software de gerenciamento de ambiente viretual em python. Utilizaremos o `conda`

 ## Configuração inicial do conda

 - [Configuração da primeira utilização](https://labriunesp.org/docs/projetos/ensino/trilha-dados/ambiente/ambiente-virtual#instru%C3%A7%C3%B5es-para-primeira-utiliza%C3%A7%C3%A3o)

 ### Criar ambiente virtual conda 

 ```
conda env create -f environment.yml 
 ```

 ### Ativar ambiente virtual

 ```
 conda activate nome_ambiente (no meu caso será fundamentos_terca)
 ```

### Atualizar bibliotecas do ambiente

- ativar ambiente e rodar o comando abaixo:

```
conda env update --prune
```
