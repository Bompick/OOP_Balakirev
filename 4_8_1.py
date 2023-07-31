class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1, v2, dist=1):
        self._v1 = v1
        self._v2 = v2
        self._dist = dist


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

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError('Попытка сравненения объектов разных  классов')

        return {self.v1, self.v2} == {other.v1, other.v2}


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

    def recurs(self, items, stop):
        for item in items:
            self.temp_path.append(item)
            all_smej_one_incl_item = list()
            for i in [x for row in [(val.v1, val.v2) for val in item.links] for x in row]:
                if i not in all_smej_one_incl_item:
                    all_smej_one_incl_item.append(i)
            all_smej_next = [j for j in all_smej_one_incl_item if j not in self.temp_path]
            if stop not in all_smej_next:
                self.recurs(all_smej_next, stop)
            correct_route = self.temp_path + [stop]
            self.temp_path.remove(item)
            if stop in all_smej_next:
                self.global_path.append(correct_route)
        return self.global_path

    def find_path(self, start_v, stop_v):
        self.temp_path = []
        self.global_path = []
        ttl_routes = list()
        ttl_routes.append(self.recurs([start_v], stop_v))
        ttl_routes = ttl_routes[0]
        ttl_links = list(map(self.check, ttl_routes))
        ttl_times = list(map(self.find_time, ttl_links))
        ttl_times = list(map(sum, ttl_times))
        min_time_number = ttl_times.index(min(ttl_times))
        res = ttl_routes[min_time_number]
        return ttl_routes[min_time_number], ttl_links[min_time_number]

    def find_time(self, massive):
        time = []
        for item in massive:
            time.append(item._dist)
        return time

    def check(self, massiv):
        route = []
        for item in self._links:
            for i in range(len(massiv)-1):
                if massiv[i] in item.__dict__.values() and massiv[i+1] in item.__dict__.values():
                    route.append(item)
        return route

    def find_link(self, st1, st2, link):
        if st1 in link.__dict__.values() and st2 in link.__dict__.values():
            return link
        else:
            pass


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


map2 = LinkedGraph()
v1 = Vertex()
v2 = Vertex()
v3 = Vertex()
v4 = Vertex()
v5 = Vertex()

map2.add_link(Link(v1, v2))
map2.add_link(Link(v2, v3))
map2.add_link(Link(v2, v4))
map2.add_link(Link(v3, v4))
map2.add_link(Link(v4, v5))

assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"

map2.add_link(Link(v2, v1))
assert len(map2._links) == 5, "метод add_link() добавил связь Link(v2, v1), хотя уже имеется связь Link(v1, v2)"

path = map2.find_path(v1, v5)
s = sum([x.dist for x in path[1]])
assert s == 3, "неверная суммарная длина маршрута, возможно, некорректно работает объект-свойство dist"

assert issubclass(Station, Vertex) and issubclass(LinkMetro, Link), "класс Station должен наследоваться от класса Vertex, а класс LinkMetro от класса Link"

map2 = LinkedGraph()
v1 = Station("1")
v2 = Station("2")
v3 = Station("3")
v4 = Station("4")
v5 = Station("5")

map2.add_link(LinkMetro(v1, v2, 1))
map2.add_link(LinkMetro(v2, v3, 2))
map2.add_link(LinkMetro(v2, v4, 7))
map2.add_link(LinkMetro(v3, v4, 3))
map2.add_link(LinkMetro(v4, v5, 1))

assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"

path = map2.find_path(v1, v5)

assert str(path[0]) == '[1, 2, 3, 4, 5]', path[0]
s = sum([x.dist for x in path[1]])
assert s == 7, "неверная суммарная длина маршрута для карты метро"