from werkzeug.routing import BaseConverter

#class RegexConverter(BaseConverter):
    # sobreescrever o metodo init
    # url_map -> lista com todos os conversores do flask
    # *items -> onde esta o argumento do regex(aqui)
'''    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]'''
        # o items é 0, pq é o primeiro a ser colocado la no regex


class ListConverter(BaseConverter):
    '''nome1+nome2+nome3'''

    ##def to_python(self, value: str) -> t.Any:
    def to_python(self, value):
        return value.split("+")

    ##def to_url(self, value: t.Any) -> str:
    def to_url(self, values):
        return "+".join(
            BaseConverter.to_url(self, item)
            for item in values

        )