# Найбільший однорядний цифровий пазл (Longest Sequence)
## На основі отриманного завдання були проведені експерименти з різними підходами для вирішення задачі (від прямого BruteForce до "Жадібних алгоритмів" з меморізацією), і по їх ітогам було вирішено зупинитись на варіанті Графових алгоритмів за допомогою бібліотеки NetworkX, та, у другому варінті, для прискорення виконання, розподілення обчислень за допомгою MPI

> Longest sequence: 716890565777794373556482064083064121343222972497868721751153303887119612013153750510417085100512022142771171781184759586758823141707943693917372699031562942007148831088658432465190816374922650246027977309775416923314139340173379890062028614605676733227368753511935367493

## Через специфіку вимог та використання засобів MPI на різних платформах було вирішено запакувати все у Docker контейнер.

### Інструкція по підйому контейнера:

```bash
    docker build -t python-mpi-project .
```
Запуск основного алгоритму:
```bash
    docker run --rm python-mpi-project python3 /app/main.py
```
Запуск розподіленого алгоритму:
```bash
    docker run --rm python-mpi-project mpiexec --allow-run-as-root -n 4 --oversubscribe python3 /app/mpi.py
```
> У прапорці -n 4 число змінювати опціонально в залежності від конфігурації системи, але враховуючи можливі витрати на комунікацію
