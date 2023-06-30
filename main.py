class Locator:
    #example - https://www.YouTube/video/share/OfasmvieKJFWLCFIW523527KVWghd
    def __init__(self, srl: str):

        try:
            method = srl.split('://', 1)
            kind = method[1].split('/', 1)
        except:
            raise ValueError

        def srl_valid():
            # check first
            if not method[0].islower():
                raise ValueError

            # check second
            if kind[0].startswith('.') and kind[0].endswith('.') and '.' not in kind[0]:
                raise ValueError
            if not kind[0].replace('.', '').isalnum():
                raise ValueError

            # check third
            _list_kind = kind[1].split('/')
            new_list = [x for x in _list_kind if x != '']
            if len(new_list) != (kind[1].count('/') + 1):
                raise ValueError

            return True

        if not srl_valid():
            raise ValueError

        print('Ok')

    def srl(self) -> str:
        pass

    def kind(self) -> str:
        pass

    def location(self) -> str:
        pass

    def location_parts(self) -> list[str]:
        pass

    def resource(self) -> str:
        pass

    def resource_parts(self) -> list[str]:
        pass

    def parent(self) -> 'Locator':
        pass

    def within(self, resource_part: str) -> 'Locator':
        pass

link = Locator('https://www.YouTube/video/share/Gkgprekghrps24332')