import ctypes

dll_h = ctypes.windll.kernel32
l = hex(dll_h.GetSystemDefaultUILanguage())
print(l)
