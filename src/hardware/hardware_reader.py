import cpuinfo
import GPUtil
import psutil

from model.components import Components


def get_components():
    components = Components()
    components.cpu = cpuinfo.get_cpu_info()['brand_raw']
    components.gpu = GPUtil.getGPUs()[0].name
    components.ram = psutil.virtual_memory().total / 1024 / 1024
    components.free_space = psutil.disk_usage('/').free / 1024 / 1024

    return components
