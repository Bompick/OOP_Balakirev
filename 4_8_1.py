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

    def recurs(self, items, stop, path=[], global_path=[]):
        for item in items:
            path.append(item)
            all_smej_one_incl_item = list()
            for i in [x for row in [(val.v1, val.v2) for val in item.links] for x in row]:
                if i not in all_smej_one_incl_item:
                    all_smej_one_incl_item.append(i)
            all_smej_next = [j for j in all_smej_one_incl_item if j not in path]
            if stop not in all_smej_next:
                self.recurs(all_smej_next, stop)
            # print(f'im here: {item}')
            correct_route = path + [stop]
            # print(correct_route)
            path.remove(item)
            if stop in all_smej_next:
                global_path.append(correct_route)

        return global_path

    def find_path(self, start_v, stop_v):
        # prom = self.recurs([start_v], stop_v)
        # print(prom)
        # a = list(prom)
        # print(a)
        ttl_routes = list()
        ttl_routes.append(self.recurs([start_v], stop_v))
        ttl_routes = ttl_routes[0]
        # print(ttl_routes)
        ttl_links = list(map(self.check, ttl_routes))
        # print(ttl_links)
        ttl_times = list(map(self.find_time, ttl_links))
        ttl_times = list(map(sum, ttl_times))
        min_time_number = ttl_times.index(min(ttl_times))
        # print(ttl_times)
        # print(min_time_number)
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


map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

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
path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7
