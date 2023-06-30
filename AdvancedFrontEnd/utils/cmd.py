class Cmd:
    def __init__(self, name : str, func : callable) -> None:
        self.name = name
        self.func = func

    def exec(self, params : list[str]):
        self.func(params)

    def match (cmds : dict[str, object], input : list[str]):
        cmd = cmds.get(input[0].strip())
        
        if None == cmd:
            print('Invalid command!')

