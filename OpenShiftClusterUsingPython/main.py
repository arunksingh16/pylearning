
def main():
    try:
        from core import main
        main()
    except KeyboardInterrupt:
        from status import ExitStatus
        ExitStatus.need_to_exit()


if __name__ == '__main__':  # pragma: nocover
    import sys
    main()
