from argparse import ArgumentParser
from .app import Svg2Png


def main():
    parser = ArgumentParser(prog='svg2png')
    parser.add_argument('--svg', help="The svg file path", required=True)
    parser.add_argument('--png', help="The png file path", required=True)
    parser.add_argument('--scale', help="scale default 1.0", required=False, type=float, default=1.0)
    args = parser.parse_args()
    Svg2Png.convert(svg_file=args.svg, png_file=args.png, scale_height=args.scale, scale_width=args.scale)


if __name__ == '__main__':
    main()
