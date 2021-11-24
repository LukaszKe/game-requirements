class Components:
    gpu: str
    cpu: str
    ram: int
    free_space: int

    gpu_ok: bool
    cpu_ok: bool
    ram_ok: bool
    free_space_ok: bool

    # delete
    def __init__(self):
        self.gpu_ok = True
        self.cpu_ok = True
        self.ram_ok = True
        self.free_space_ok = True
