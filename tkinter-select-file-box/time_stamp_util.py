#time_stamp_util.py
import datetime
import logging

def name_file_timenow_with_string(fil_nme, extension_string) -> str:
        temp_time = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        result = fil_nme  + "_" + temp_time +"." + extension_string
        print(result)
        return result

# TODO: polishing and error handling
# extention contains a dot or not could improve the handling and polishing

if __name__ == '__main__':
        print("running the invoked script standalone")
        name_file_timenow_with_string("test", "txt")