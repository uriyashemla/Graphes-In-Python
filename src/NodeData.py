import random


class NodeData:

    def __init__(self, key:int, pos):
        self.key = key
        self.neighbors = {}
        self.neighbors_in = {}
        self.info = "White"
        self.tag = -1
        self.weight = -1
        if not pos == None:
            self.pos = Geo_location(pos[0], pos[1], pos[2])
        else:
            self.pos = None

    def get_key(self):
        return self.key

    def get_tag(self):
        return self.tag

    def get_info(self):
        return self.info

    def get_neighbors(self):
        return self.neighbors

    def get_weight(self):
        return self.weight

    def get_pos(self):
        return self.pos

    def get_neighbors_in(self):
        return self.neighbors_in

    def add_neighbor(self, key, weight):
        self.neighbors[key] = weight

    def add_neighbor_in(self,key,weight):
        self.neighbors_in[key] = weight

    def remove_neighbor(self, id):
        if id in self.neighbors:
            self.neighbors.pop(id)

    def set_weight(self, weight):
        self.weight = weight

    def set_tag(self,tag):
        self.tag = tag

    def set_pos(self, x, y, z):
        self.pos = Geo_location(x, y, z)

    def set_info(self, info):
        self.info = info

    def __lt__(self, other):
        return self.weight < other.weight




class Geo_location:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z