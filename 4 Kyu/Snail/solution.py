def snail(snail_map):
    return Snail(snail_map).run()


class Snail:
    def __init__(self, matrix):
        self.matrix = matrix
        self.result = []

    def run(self):
        if self.matrix[0] is None:
            return self.result

        while len(self.matrix) > 0:
            self.go_right()
            self.go_down()
            self.go_left()
            self.go_up()
        return self.result

    def go_up(self):
        if len(self.matrix) > 0:
            self.result += [row.pop(0) for row in self.matrix[::-1]]

    def go_left(self):
        if len(self.matrix) > 0:
            self.result += self.matrix[-1][::-1]
            del self.matrix[-1]

    def go_right(self):
        if len(self.matrix) > 0:
            self.result += self.matrix[0][:]
            del self.matrix[0]

    def go_down(self):
        if len(self.matrix) > 0:
            self.result += [row.pop(-1) for row in self.matrix]
