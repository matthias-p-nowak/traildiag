def main() -> None:
    print("Hello from traildiag!")


def GetVersion() -> str:
    from importlib.metadata import version

    return version("traildiag")
