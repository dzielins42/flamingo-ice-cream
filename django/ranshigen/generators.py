import numpy
import xml.etree.ElementTree

class Generator:
    def generate(self, count, referenceSolver):
        return None

    def _getValue(self, value, referenceSolver):
        if isinstance(value, Generator):
            return value.generate(1, referenceSolver)[0]
        else:
            return str(value)

class RandomGenerator(Generator):
    v = None
    p = None

    def __init__(self, values = None, probabilities = None):
        Generator.__init__(self)
        self.v = values
        self.p = probabilities

    def generate(self, count, referenceSolver):
        result = list(numpy.random.choice(self.v, p=self.p, size=count))
        return result

class JoinGenerator(Generator):
    separator = None
    values = None

    def __init__(self, values = None, separator = ""):
        Generator.__init__(self)
        self.values = values
        self.separator = separator

    def generate(self, count, referenceSolver):
        result = []
        for i in range(count):
            result.append(self.separator.join(self._getValue(value, referenceSolver) for value in self.values))
        return result

class ReferenceGenerator(Generator):
    referenceId = None

    def __init__(self, referenceId):
        Generator.__init__(self)
        self.referenceId = referenceId

    def generate(self, count, referenceSolver):
        if referenceSolver is None:
            return [""]
        return referenceSolver(self.referenceId, count)


class XmlParser:
    data = {}

    def fromFile(self, path):
        tree = xml.etree.ElementTree.parse(path)
        return self._parseGenerator(tree.getroot())

    def fromString(self, stringData):
        root = xml.etree.ElementTree.fromstring(stringData)
        return self._parseGenerator(root)

    def  _parseGenerator(self, element):
        generator = None
        if element.tag == "random":
            generator = self._parseRandomGenerator(element)
        elif element.tag == "space-join":
                generator = self._parseSpaceJoinGenerator(element)
        elif element.tag == "join":
            generator = self._parseJoinGenerator(element)
        elif element.tag == "reference":
            generator = self._parseReferenceGenerator(element)
        return generator

    def _parseRandomGenerator(self, element):
        values = []
        probabilities = []
        for child in element:
            if child.tag == "item":
                i = self._parseItem(child)
                values.append(i['value'])
                if 'probability' in i:
                    probabilities.append(float(i['probability']))
                else:
                    probabilities.append(1)
        #Probabilities are normalized
        probabilities = [float(i)/sum(probabilities) for i in probabilities]
        return RandomGenerator(values, probabilities)

    def _parseSpaceJoinGenerator(self, element):
        items = self._parseItems(element)
        values = list(map(lambda item: item['value'], items))
        return JoinGenerator(values, " ")

    def _parseJoinGenerator(self, element):
        separator = element.get("separator") if "separator" in element.attrib else ""
        items = self._parseItems(element)
        values = list(map(lambda item: item['value'], items))
        return JoinGenerator(values, separator)

    def _parseReferenceGenerator(self, element):
        referenceId = element.get("id") if "id" in element.attrib else ""
        print(referenceId)
        return ReferenceGenerator(referenceId)

    def _parseItems(self, children):
        items = []
        for child in children:
            if child.tag == "item":
                items.append(self._parseItem(child))
        return items

    def _parseItem(self, element):
        d = {}
        d.update(element.attrib)
        if self._hasChildren(element):
            #Use only 1st element
            v = self._parseGenerator(element[0])
        else:
            v = element.text
        d['value'] = v
        return d

    def _hasChildren(self, element):
        return bool(len(element))
