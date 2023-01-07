# Control Funcions

def flag_dev(devices):
    flag = False

    for d in devices:
        if d.dev_type.dev_type == 'IMPRESORA':
            flag = True
        else:
            flag = False

    if flag == True:
        return True
    else:
        return False
