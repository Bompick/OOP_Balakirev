class Vertex:
    def __init__(self):
        self._links: [Link] = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1, v2, dist=1):
        self._v1 = v1
        self._v2 = v2
        self._dist = dist

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError('Попытка сравненения объектов разных  классов')

        return {self.v1, self.v2} == {other.v1, other.v2}

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, val):
        self._dist = val


class LinkedGraph:
    def __init__(self):
        self._links = []  # список из объектов класса Link
        self._vertex = []  # список из объектов класса Vertex

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        if link not in self._links:
            self._links.append(link)
            vertexes = (link.v1, link.v2)
            vert_to_add = tuple(filter(lambda x: x not in self._vertex, vertexes))
            self._vertex.extend(vert_to_add)
            for item in vertexes:
                item.links.append(link)

    def recurs(self, items, stop, path=[]):
        for item in items:
            path.append(item)
            all_smej_one_incl_item = list()
            for i in [x for row in [(val.v1, val.v2) for val in item.links] for x in row]:
                if i not in all_smej_one_incl_item:
                    all_smej_one_incl_item.append(i)
            all_smej_next = [j for j in all_smej_one_incl_item if j not in path]
            if stop not in all_smej_next:
                self.recurs(all_smej_next, stop)

            print(f'im here: {item}')
            correct_route = path + [stop]
            print(correct_route)
            path.remove(item)
            if stop in all_smej_next:
                return correct_route

    def find_path(self, start_v, stop_v):
        prom = self.recurs([start_v], stop_v)
        print(prom)
        a = list(prom)
        print(a)


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2, dist)


map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print(len(map_metro._links))
print(len(map_metro._vertex))
path = map_metro.find_path(v1, v6)
