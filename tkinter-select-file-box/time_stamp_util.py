import datetime
import logging

def name_file_timenow_with_string(fil_nme, extension_string) -> str:
        temp_time = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        return fil_nme  + "_" + temp_time + extension_string