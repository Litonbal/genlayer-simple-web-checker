from genlayer import *


class WebChecker(gl.Contract):
    result: bool

    def __init__(self):
        self.result = False

    @gl.public.write
    def check_webpage(self) -> None:
        url = "https://example.org"

        def check_page():
            web_data = gl.nondet.web.render(url, mode="html")
            return "iana" in web_data.lower()

        self.result = gl.eq_principle.strict_eq(check_page)

    @gl.public.view
    def get_result(self) -> bool:
        return self.result
