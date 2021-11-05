# Manual
## Filtro.py
O arquívo **filtro.py** é uma ferramenta para filtra texto, muito usado para <br>
filtra **e-mail** e **senha** de uma base de dados, sempre que for utilizar coloque <br> 
os dados dentro de **lista.txt** e ao finalizar o processo será criado um arquivo **filtro.txt** <br>
onde o mesmo terá todo o resultado da filtragem.

### Veja um exemplo de base de dados que é possívell filtrar
```
newton@ig.com|senha123 |Newton Pugno | Rua da 7
alura@gmail.com|password | Lucas R | Bom Lugar
```
### O resultado será assim:
```
newton@ig.com|senha123 
alura@gmail.com|password
```
### Sobre o código
É possível mudar o delimitador, dentro do arquívo tem uma linha <br>
`dl = "|` alternado para `dl = :`, você acaba de mudar o separador.
