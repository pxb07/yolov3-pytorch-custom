import GPUtil
import time
import os
import sys

commands = []

command1 = 'python3 train.py --cfg cfg/yolov3-spp-44-ldb.cfg --data data/rubbish.data --weights weights/yolov3-sppu.pt --batch-size 16 --epochs 120 --save baseline-dropblock3'
commands.append(command1)

command2 = 'python3 train.py --cfg cfg/yolov3-spp-44.cfg --data data/rubbish.data --weights weights/yolov3-sppu.pt --batch-size 16 --epochs 120 --save baseline-sdd-aug --ssd-aug'
commands.append(command2)

command_idx = 0



while(True):
    try:
        DEVICE_ID_LIST = GPUtil.getFirstAvailable()
        command = commands[command_idx]
        print(command)
        exec_status = os.system(command)
        if exec_status:
            raise OSError("System Invoke Error!")
        command_idx += 1

    except RuntimeError:
        print ('=================GPU Information====================')
        print ("Prepare to Execute Command", command_idx)
        print ("Waiting GPU Free...")
        print (time.strftime("%F") + ' ' +  time.strftime("%T"))
        print ('====================================================')
        time.sleep(1 * 60 * 10)

    except IndexError:
        break

    except:
        print("========================================here, or not=================")
        print("Unexpected error:", sys.exc_info()[0])
        raise


print('Done!!')
