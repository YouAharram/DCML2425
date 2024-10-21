import csv
from time import sleep
import psutil
import pandas as pd
import signal
import sys
import openpyxl

def read_cpu_usage():
    cpu_t = psutil.cpu_times()
    cpu_dict = {"idle_times": cpu_t.idle, "usr_time": cpu_t.user, "interrupt_rime": cpu_t.interrupt}
    return cpu_dict

def read_memory():
    mem_info = psutil.virtual_memory()
    mem_dict = {"mem_tot": mem_info.total/ (1024 ** 3), "mem_disp": mem_info.available / (1024 ** 3), "mem_used": mem_info.used / (1024 ** 3), "mem_percentage_used": mem_info.percent}
    return mem_dict

def read_disk():
    swap_info = psutil.swap_memory()
    dict_disk = {"total_swap":swap_info.total / (1024 ** 3),"used_swap":swap_info.used / (1024 ** 3),"free_swap":swap_info.free / (1024 ** 3)}
    return dict_disk

def open_file(filename):
    fd = open(filename, 'a+')
    return fd

def write_dict_to_csv(filename, dict_item):
    w = csv.DictWriter(filename, dict_item.keys())
    w.writerow(dict_item)

def signal_handler(sig, frame):
    print("\nSegnale di interruzione ricevuto! Sto chiudendo il programma...")
    df = pd.read_csv('my_first_dataset.csv')
    df.to_excel('my_first_dataset2.xlsx', index=False)
    sys.exit(0)

if __name__ == '__main__':
    file_descriptor = open_file("my_first_dataset.csv")
    file_descriptor.write("idle_times, usr_time, interrupt_rime, mem_tot, mem_disp, mem_used, mem_percentage_used, total_swap, used_swap, free_swap\n")
    file_descriptor.close()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        file_descriptor = open_file("my_first_dataset.csv")
        dict_output = read_cpu_usage()
        dict_output |= read_memory()
        dict_output |= read_disk()
        write_dict_to_csv(file_descriptor,dict_output)
        print(dict_output)
        file_descriptor.close()
        sleep(1)