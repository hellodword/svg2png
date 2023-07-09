from .context import svg2png


def test_app(capsys, example_fixture):
    # pylint: disable=W0612,W0613
    svg2png.Svg2Png.run()
    captured = capsys.readouterr()

    assert "Hello World..." in captured.out
