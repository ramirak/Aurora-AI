import pefile


def pe_load(filename):
    try:
        return pefile.PE(filename)
    except OSError as e:
        print(e)
    except pefile.PEFormatError as e:
        print("PE Format Error:" + str(e.value))


def get_dlls(pe, additional_info):
    dll_list = []
    pe_imports = []
    for entry in pe.DIRECTORY_ENTRY_IMPORT:    
        if entry.dll != None:
            dll_list.append(entry.dll.decode())
            if additional_info:
                pe_imports.append(get_imported_functions(entry))
    if additional_info:
        return dll_list, pe_imports
    return dll_list


def get_imported_functions(entry):
    pe_imports = []
    for func in entry.imports:
        if func.name != None:
            pe_imports.append(func.name.decode('utf-8'))
    return pe_imports

pe = pe_load("7zFM.exe")
if pe:
    print(get_dlls(pe,True)[0])