from ..register import Library


class FontAwesome(Library):
    name = 'fontawesome'
    folder = 'static'
    cdn = 'https://use.{name}.com/releases/v{version}/js/{filename}'.replace('.min', '')


