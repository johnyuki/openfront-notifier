import argparse
from app.monitor import monitor_games


def validate_args(args):
    #  Validate the command line arguments and print any warnings or errors if necessary.
    if args.mode not in ["team", "ffa"]:
        if args.mode is not None:
            print("Error: Your --mode value must be either 'team' or 'ffa', or not specified.")
            return False
    return True


def parse_args():
    parser = argparse.ArgumentParser(description="OpenFront Game Notifier")

    parser.add_argument("--map", default=None)
    parser.add_argument("--mode", default=None)
    parser.add_argument("--debug", action="store_true", default=False)
    parser.add_argument("--interval", type=int, default=0)
    parser.add_argument("--autoopen", action="store_true", default=False)

    return parser.parse_args()


def main():
    args = parse_args()

    if validate_args(args): 
        #  Start monitoring the games with the specific args.
        monitor_games(
            map_filter=args.map,
            mode_filter=args.mode,
            debug=args.debug,
            interval=args.interval,
            autoopen=args.autoopen
        )
    else: 
        print("Program failed to start due to invalid arguments.")
        input("Press Enter to exit...")