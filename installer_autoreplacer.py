import pip


def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])


if __name__ == '__main__':
    install('pynput')
    install('tk')
    install('pandas')
    install('pyautogui')
    install('openpyxl')
