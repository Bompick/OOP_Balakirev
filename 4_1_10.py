class Layer:
    def __init__(self, name='Layer'):
        self.name = name
        self.next_layer = None

    def __call__(self, obj):
        self.next_layer = obj
        return obj


class Input(Layer):
    def __init__(self, inputs, name='Input'):
        super().__init__(name)
        self.inputs = inputs


class Dense(Layer):
    def __init__(self, inputs, outputs, activation, name='Dense'):
        super().__init__(name)
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator():
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        temp = self.data
        while temp:
            yield temp
            temp = temp.next_layer
            if temp is None:
                break


network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

for x in NetworkIterator(network):
    print(x.name)

