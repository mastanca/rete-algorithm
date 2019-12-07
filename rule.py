class Rule(object):
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs

    def applies(self, data):
        # print(set(self.inputs))
        # print(set(data))
        a = set(self.inputs).issubset(set(data))
        # print(a)
        return a

    def implies(self, target):
        return target in self.outputs

    def apply(self, knowledge):
        knowledge.extend(self.outputs)
    
    def __repr__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])
