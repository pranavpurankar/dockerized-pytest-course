from scripts.chp2.video2.mapmaker_start import Point


def test_make_one_point():
    p1 = Point("Daker", 14.7161, 17.4677)
    assert p1.get_lat_long() == (14.7161, 17.4677)