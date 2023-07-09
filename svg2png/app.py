
import io
import skia


class Svg2Png:
    @staticmethod
    def convert(svg_file: str, png_file: str, scale_width: float, scale_height: float):
        skia_stream = skia.Stream.MakeFromFile(svg_file)
        skia_svg = skia.SVGDOM.MakeFromStream(skia_stream)
        svg_width, svg_height = skia_svg.containerSize()
        surface_width, surface_height = int(svg_width * scale_width), int(svg_height * scale_height)
        surface = skia.Surface(surface_width, surface_height)
        with surface as canvas:
            canvas.scale(scale_width, scale_height)
            skia_svg.render(canvas)
        with io.BytesIO(surface.makeImageSnapshot().encodeToData()) as b:
            with open(png_file, "wb") as f:
                f.write(b.getbuffer())

    @staticmethod
    def run():
        print("Hello World...")
