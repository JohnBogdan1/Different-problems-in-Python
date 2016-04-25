def calculate_index(v, i, j):
    """
    Calculeaza indexul unui literal in functie de v, i si j.

    :param v: numarul de noduri din graf
    :param i: pozitia din path
    :param j: valoarea nodului
    :return: indexul unui literal, un intreg
    """
    return (i - 1) * v + j


def find_non_edges(adjacency_matrix, v):
    """
    Functia returneaza un dictionar care cuprinde perechile de noduri
    care nu sunt adiacente. Unei chei din dictionar ii este asociata o lista.

    :param adjacency_matrix: matricea de adiacenta asociata grafului
    :param v: numarul de noduri
    :return: un dictionar -> non_edges
    """

    non_edges = {}

    # ma uit la elementele care se afla deasupra diagonalei principale
    for i in range(v):
        for j in range(i + 1, v):
            # daca elementul e 0, inseamna ca nu exista muchie intre noduri
            # adaug in dictionar perechea respectiva
            if adjacency_matrix[i][j] == 0:
                non_edges.setdefault(i + 1, list()).append(j + 1)

    # ma uit la elementele care se afla sub diagonala principala
    for i in range(1, v):
        for j in range(i):
            # daca elementul e 0, inseamna ca nu exista muchie intre noduri
            # adaug in dictionar perechea respectiva
            if adjacency_matrix[i][j] == 0:
                non_edges.setdefault(i + 1, list()).append(j + 1)

    return non_edges


def generate_expression(adjacency_matrix, v):
    """
    Genereaza expresia booleana asociata grafului.

    :param adjacency_matrix: matricea de adiacenta a grafului
    :param v: numarul de noduri
    :return: un string
    """

    # creez o lista goala in care voi pune fiecare clauza
    clauses = []

    # preiau dictionarul in care se afla perechile de noduri care nu sunt adiacente
    non_edges = find_non_edges(adjacency_matrix, v)

    # pornesc de la 1 si ma opresc la v
    for j in range(1, v + 1):

        # creez o lista in care voi pune literali
        literals = []

        # fiecare nod j trebuie sa apara in path
        # sunt generate v clauze de lungime v
        for i in range(1, v + 1):
            # pentru fiecare pozitie i din path calculez indexul asociat nodului j
            # adaug literalul in lista
            literals.append("x" + str(calculate_index(v, i, j)))

        # la sfarsit unesc toti literalii prin "V" intr-un string si pun paranteze
        # string-ul va reprezenta o clauza de lungime v
        # adaug string-ul in lista de clauze
        clauses.append("(" + "V".join(literals) + ")")

        # niciun nod j nu apare de doua ori in path pe pozitii diferite, i si k
        # sunt generate O(v^3) clauze de lungime 2
        for i in range(1, v + 1):
            # intai generez un literal cu indexul dat de pozitia i si nodul j
            # pe care il pun in lista
            literals = ["~x" + str(calculate_index(v, i, j))]

            for k in range(1, v + 1):
                # pentru literalul generat anterior
                # generez cate un literal cu indexul dat de pozitia k si nodul j
                # pe care il adaug la lista
                literals.append("~x" + str(calculate_index(v, k, j)))

                # daca i < k(pentru a nu exista duplicate)
                # unesc literalii si pun rezultatul in lista de clauze
                # scot literalul, adaugat anterior, din lista pentru a face loc altui literal
                # pentru ca o clauza are 2 literali
                if i < k:
                    clauses.append("(" + "V".join(literals) + ")")
                    literals.pop()
                else:
                    # altfel, scot literalul adaugat anterior
                    literals.pop()

        # resetez lista
        literals = []

        # fiecare pozitie j din path trebuie sa fie ocupata
        # sunt generate v clauze de lungime v
        for i in range(1, v + 1):
            # pentru fiecare nod i calculez indexul asociat pozitiei j din path
            # adaug literalul in lista
            literals.append("x" + str(calculate_index(v, j, i)))

        # la sfarsit unesc toti literalii prin "V" intr-un string si pun paranteze
        # string-ul va reprezenta o clauza de lungime v
        # adaug string-ul in lista de clauze
        clauses.append("(" + "V".join(literals) + ")")

        # doua noduri i si k nu pot ocupa aceeasi pozitie j in path
        # sunt generate O(v^3) clauze de lungime 2
        for i in range(1, v + 1):
            # intai generez un literal cu indexul dat de pozitia j si nodul i
            # pe care il pun in lista
            literals = ["~x" + str(calculate_index(v, j, i))]

            for k in range(1, v + 1):
                # pentru literalul generat anterior
                # generez cate un literal cu indexul dat de pozitia j si nodul k
                # pe care il adaug la lista
                literals.append("~x" + str(calculate_index(v, j, k)))

                # daca i < k(pentru a nu exista duplicate)
                # la fel, unesc literalii, adaug clauza in lista si scot literalul adaugat anterior
                if i < k:
                    clauses.append("(" + "V".join(literals) + ")")
                    literals.pop()
                else:
                    # altfel, scot literalul adaugat anterior
                    literals.pop()

        # doua noduri care nu sunt adiacente in graf, nu pot fi adiacente in path
        # aici, pozitia j merge pana la v - 1
        # sunt generate O(v^3) clauze de lungime 2
        if j != v:
            # pentru fiecare nod(cheie) din dictionar
            for key in non_edges:
                # pun un literal in lista, al carui index este calculat cu pozitia j si nodul key
                literals = ["~x" + str(calculate_index(v, j, key))]

                # pentru fiecare valoare din lista asociata cheii
                # valorile sunt nodurile care nu sunt adiacente cu nodul key
                for value in non_edges[key]:
                    # adaug un literal in lista, al carui index este calculat cu pozitia j + 1 si nodul value
                    literals.append("~x" + str(calculate_index(v, j + 1, value)))

                    # unesc cei doi literali si adaug clauza in lista
                    clauses.append("(" + "V".join(literals) + ")")

                    # scot literalul adaugat anterior
                    literals.pop()

    # unesc toate clauzele prin "^" intr-un string si il returnez
    return "^".join(clauses)


if __name__ == '__main__':
    """
    @V: reprezinta numarul de noduri
    @E: reprezinta numarul de muchii
    @adjacency_matrix: reprezinta matricea de adiacenta asociata grafului
    """

    # deschid fisierul de input
    input_graph = open("test.in", "r")

    # preiau valorile de pe prima linie
    [V, E] = map(int, input_graph.readline().split())

    # initializez matricea de adiacenta, avand dimensiunea VxV
    adjacency_matrix = [[0 for y in range(V)] for x in range(V)]

    # citesc urmatoarele E linii din fisier
    for i in xrange(E):
        [x, y] = map(int, input_graph.readline().split())
        # Valoare egala cu 1-> exista muchie intre noduri
        # Valoarea egala cu 0-> nu exista muchie intre noduri
        # scad 1 pentru ca indexarea incepe de la 0
        adjacency_matrix[x - 1][y - 1] = 1
        adjacency_matrix[y - 1][x - 1] = 1

    # deschid fisierul de output
    output_graph = open("test.out", "w")

    # scriu rezultatul returnat in fisier
    output_graph.write(generate_expression(adjacency_matrix, V))
