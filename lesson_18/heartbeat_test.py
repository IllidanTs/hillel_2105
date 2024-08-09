from datetime import datetime, timedelta


def analyze_heartbeat_log(input_file, key, log_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    filtered_log = [line for line in lines if key in line]

    timestamps = []
    for line in filtered_log:
        index = line.find("Timestamp ")
        if index != -1:
            time_str = line[index + len("Timestamp "):index + len("Timestamp ") + 8]
            timestamps.append(datetime.strptime(time_str, "%H:%M:%S"))

    with open(log_file, 'w') as log:
        for i in range(len(timestamps) - 1):
            delta = timestamps[i] - timestamps[i + 1]
            if delta < timedelta(seconds=0):
                delta = timedelta(seconds=0) - delta

            if timedelta(seconds=31) < delta < timedelta(seconds=33):
                log.write(f"WARNING: {timestamps[i]} - {timestamps[i + 1]}: {delta.seconds} seconds\n")
            elif delta >= timedelta(seconds=33):
                log.write(f"ERROR: {timestamps[i]} - {timestamps[i + 1]}: {delta.seconds} seconds\n")


analyze_heartbeat_log('hblog.txt', 'Key TSTFEED0300|7E3E|0400', 'hb_test.log')
