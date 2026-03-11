## Installation

### Requirements

- Python 3.9+

### Using pipx

Install pipx using the command prompt:

```bash
python -m pip install pipx
python -m pipx ensurepath
```

Then: 

```bash
pipx install git+https://github.com/johnyuki/openfront-notifier.git
```

## Usage 

Run the app from command prompt or powershell using:

```bash
openfront
```

You can exit by pressing CTRL+C or just close the command prompt window.

### Args

Examples:

```bash
openfront # Uses all defaults in the table below
openfront --map "pluto" # Notifies you any time the next map is Pluto
openfront --mode "ffa" --map "gateway to the atlantic" # Notifies you any time the next mode is FFA and it will be played on Gateway To The Atlantic
```

| Arg | Description | Required | Example | Default |
|--------|--------|------------|----------|----------|
| `--map` | Name of the map, in lowercase, surrounded in quotes | No | "gateway to the atlantic" | `None` |
| `--mode` | Either "team" or "ffa" - does not need to be in quotes as it's just a single word | No | team | `None` |

Keep in mind that while both args default to "None", doing this will result in you simply being notified on every single match. 

## Updating

To update this app when a new version is released you can run:

```bash
pipx upgrade openfront-notifier
```

## To Do

Upcoming features:
- Optional argument that will auto open openfront in your default browser whenever a game that matches your flags is detected.
- Add more arguments to watch for such as max players, random spawn, starting gold, etc.  
- Allow you to specify multiple maps instead of just one.

## License

MIT
