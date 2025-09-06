from stelvio_app import stlv_app


def test_configuration_region() -> None:
    config = stlv_app.configuration("dev")
    assert config.aws.region == "us-east-1"
