#time_stamp_util.py
import datetime

""" Script typically called early to get a file name with a time stamp
does not use logging, as logging script call some of the functions below.
So --> Use print exclusively"""

def generate_short_timestamp():
        spot_time = datetime.datetime.utcnow().strftime("%m%d_%H%M")
        return spot_time

def generate_long_timestamp():
        spot_time = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        return spot_time

def long_name_file_timenow_with_string(fil_nme, extension_string) -> str:
        temp_time = generate_long_timestamp()
        result = fil_nme  + "_" + temp_time +"." + extension_string
        print(result)
        return result

# TODO: polishing and error handling
# extention contains a dot or not could improve the handling and polishing

# TODO: use """ instead of #

if __name__ == '__main__':
        print("running the invoked script standalone")
        name_file_timenow_with_string("test", "txt")