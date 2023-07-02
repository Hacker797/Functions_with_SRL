class Locator:
    #example - https://www.YouTube/video/share/OfasmvieKJFWLCFIW523527KVWghd
    def __init__(self, srl: str):

        try:
            self.__url = srl
            self.__method = srl.split('://', 1)
            self.__kind = self.__method[1].split('/', 1)
        except:
            raise ValueError

        def srl_valid():
            # check first
            if not self.__method[0].islower():
                raise ValueError

            # check second
            if self.__kind[0].startswith('.') and self.__kind[0].endswith('.') and '.' not in self.__kind[0]:
                raise ValueError
            if not self.__kind[0].replace('.', '').isalnum():
                raise ValueError

            # check third
            _list_kind = self.__kind[1].split('/')
            new_list = [x for x in _list_kind if x != '']
            if len(new_list) != (self.__kind[1].count('/') + 1):
                raise ValueError

            return True

        if not srl_valid():
            raise ValueError

    def srl(self) -> str:
        return self.__url

    def kind(self) -> str:
        return self.__method[0]

    def location(self) -> str:
        return self.__kind[0]

    def location_parts(self) -> list[str]:
        return self.__kind[0].split('.')

    def resource(self) -> str:
        return self.__kind[1]

    def resource_parts(self) -> list[str]:
        return self.__kind[1].split('/')

    def parent(self) -> 'Locator':
        __new_list = self.__kind[1].split('/')
        __new_list = __new_list[:-1]
        __str = '/'.join(__new_list)
        __new_srl = self.__method[0] + '://' + self.__kind[0] + __str

        return Locator(__new_srl)

    def within(self, resource_part: str) -> 'Locator':
        __new_list = '/' + self.__kind[1] + f'/{resource_part}'
        __new_srl = self.__method[0]+'://' + self.__kind[0] + __new_list

        return Locator(__new_srl)

link = Locator('https://www.YouTube/video/share/Gkgprekghrps24332/media/admin')

# print(f"""srl: {link.srl()}
# kind: {link.kind()}
# location: {link.location()}
# location_parts: {link.location_parts()}
# resources: {link.resource()}
# resources_parts: {link.resource_parts()}
# parent: {link.parent()}
# check 1: {link.parent().resource_parts()}
# within: {link.within('index')}
# check 2: {link.within('index').srl()}""")