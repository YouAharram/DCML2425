from time import sleep
import psutil

def read_cpu_usage():
    cpu_t = psutil.cpu_times()
    usr_sp_cputimes = cpu_t.user
    idle_times = cpu_t.idle
    return usr_sp_cputimes, idle_times, cpu_t

if __name__ == '__main__':
    while True:
        u_t, i_t, cpu_t = read_cpu_usage()
      #  print("user time: " +str(u_t)+ " idle time: " +str(i_t))
        print("user time: %.2f idle time: %.2f " % (u_t,i_t))
        sleep(1)