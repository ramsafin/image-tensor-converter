def test_import_and_version() -> None:
    import package_name

    assert hasattr(package_name, "__version__")
    assert isinstance(package_name.__version__, str)
