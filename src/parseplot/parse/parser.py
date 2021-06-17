from plusminus import ArithmeticParser

from .pre_parse import pre_parse_translate


class Parser:
    """
    parseplot parser class
    """

    def __init__(self, expression: str):
        self.expression = expression
        self._expression = pre_parse_translate(expression)
        self._parser = ArithmeticParser()

    def plot(self, x_min: int = -500, x_max: int = 500) -> list[tuple[int, float]]:
        """
        Plot expression.

        :param x_min: int
        :param x_max: int
        :return: list[tuple]
        """
        self._parser.evaluate("x=0")

        xy_points: list[tuple[int, float]] = []
        for x in range(x_min, x_max + 1):
            self._parser.evaluate(f"x={x}")
            xy = (x, self._parser.evaluate(self._expression))
            xy_points.append(xy)
        return xy_points
