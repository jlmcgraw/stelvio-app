from pytest import CaptureFixture
from stelvio_app.main import main


def test_raise(capsys: CaptureFixture[str]) -> None:
    main()
    assert "Ritchie Blackmore" in capsys.readouterr().out
