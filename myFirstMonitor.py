import csv
from os import write
from time import sleep
import psutil

def read_cpu_usage():
    cpu_t = psutil.cpu_times()
    usr_sp_cputimes = cpu_t.user
    idle_times = cpu_t.idle
    cpu_dict = {"idle_times": cpu_t.idle, "usr_time": cpu_t.user}
    cpu_dict["interrupt_rime"] = cpu_t.interrupt
    write_dict_to_csv("my_first_dataset.csv",cpu_dict)
    return cpu_dict

def read_memory():
    mem_info = psutil.virtual_memory()
    mem_dict = {"mem_tot": mem_info.total/ (1024 ** 3), "mem_disp": mem_info.available / (1024 ** 3), "mem_used": mem_info.used / (1024 ** 3), "mem_percentage_used": mem_info.percent}
    return mem_dict

def read_disk():
    swap_info = psutil.swap_memory()
    dict_disk = {"total_swap":swap_info.total / (1024 ** 3),"used_swap":swap_info.used / (1024 ** 3),"free_swap":swap_info.free / (1024 ** 3),"swap_percentage_used":swap_info.percent}
    return dict_disk

def write_dict_to_csv(filename, dict_item):
    f = open(filename, 'a+')
    w = csv.DictWriter(f, dict_item.keys())
    w.writerow(dict_item)
    f.close()

if __name__ == '__main__':
    isFirst = True
    while True:
        if isFirst:
            dict_title = {"idle_times": "idle_times", "usr_time": "usr_time","interrupt_rime":"interrupt_rime"}
            write_dict_to_csv("my_first_dataset.csv",dict_title)
            isFirst = False
        print(read_cpu_usage())
        sleep(1)