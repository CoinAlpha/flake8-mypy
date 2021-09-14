from textwrap import dedent


def test_mypy_config_load(flake8_path):
    (flake8_path / "mypy.cfg").write_text(
        dedent(
            """\
            [mypy]
            disallow_untyped_defs = True
            """
        )
    )
    (flake8_path / "setup.cfg").write_text(
        dedent(
            """\
            [flake8]
            select = T4
            mypy_config = mypy.cfg
            """
        )
    )
    (flake8_path / "example.py").write_text(
        dedent(
            """\
            def foo(a: int, b):
                return 42
            """
        )
    )
    result = flake8_path.run_flake8()
    assert result.exit_code == 1

    expected = "./example.py:1:1: T484 Function is missing a type annotation for one or more arguments"
    assert expected in result.out_lines


