import win32gui, time
from win32con import PAGE_READWRITE, MEM_COMMIT, MEM_RESERVE, MEM_RELEASE, PROCESS_ALL_ACCESS, WM_GETTEXTLENGTH, WM_GETTEXT
from commctrl import LVS_OWNERDATA, LVM_GETITEMCOUNT, LVM_GETNEXTITEM, LVNI_SELECTED
import os
import struct
import ctypes
import win32api
import datetime
import win32com.client as win32
import win32ui
import psutil
import subprocess
import time
import urllib.parse
from zipfile import ZipFile

class file_management:
    
    def __init__(self):
        self.clsid = '{9BA05972-F6A8-11CF-A442-00A0C90A8F39}' #Valid for IE as well!

    def getEditText(self, hwnd):
        # api returns 16 bit characters so buffer needs 1 more char for null and twice the num of chars
        self.buf_size = (win32gui.SendMessage(hwnd, WM_GETTEXTLENGTH, 0, 0) +1 ) * 2
        self.target_buff = ctypes.create_string_buffer(self.buf_size)
        win32gui.SendMessage(hwnd, WM_GETTEXT, self.buf_size, ctypes.addressof(self.target_buff))
        return self.target_buff.raw.decode('utf16')[:-1]# remove the null char on the end

    def _normaliseText(self, control_text):
        '''Remove '&' characters, and lower case.
        Useful for matching control text.'''
        return control_text.lower().replace('&', '')

    def _windowEnumerationHandler(self, hwnd, result_list):
        '''Pass to win32gui.EnumWindows() to generate list of window handle,
        window text, window class tuples.'''
        result_list.append((hwnd, win32gui.GetWindowText(hwnd), win32gui.GetClassName(hwnd)))

    def searchChildWindows(self, 
                current_hwnd,
                wanted_text=None,
                wanted_class=None,
                selection_function=None):
        results = []
        child_windows = []
        try:
            win32gui.EnumChildWindows(current_hwnd,
                        self._windowEnumerationHandler,
                        child_windows)
        except win32gui.error:
            # This seems to mean that the control *cannot* have child windows,
            # i.e. not a container.
            return
        for child_hwnd, window_text, window_class in child_windows:
            descendent_matching_hwnds = self.searchChildWindows(child_hwnd)
            if descendent_matching_hwnds:
                results += descendent_matching_hwnds

            if wanted_text and \
                not self._normaliseText(wanted_text) in self._normaliseText(window_text):
                    continue
            if wanted_class and \
                not window_class == wanted_class:
                    continue
            if selection_function and \
                not selection_function(child_hwnd):
                    continue
            results.append(child_hwnd)
        return results


    def explorer_fileselection(self):
        global clsid
        self.address_1=""
        self.files = []
        shellwindows = win32.Dispatch(self.clsid)
        w=win32gui
        window = w.GetForegroundWindow()
        #print("window: %s" % window)
        if (window != 0):
            if (w.GetClassName(window) == 'CabinetWClass'): # the main explorer window
                #print("class: %s" % w.GetClassName(window))
                #print("text: %s " %w.GetWindowText(window))
                children = list(set(self.searchChildWindows(window)))
                addr_edit = None
                file_view = None
                for child in children:
                    if (w.GetClassName(child) == 'WorkerW'): # the address bar
                        addr_children = list(set(self.searchChildWindows(child)))
                        for addr_child in addr_children:
                            if (w.GetClassName(addr_child) == 'ReBarWindow32'):
                                addr_edit = addr_child
                                addr_children = list(set(self.searchChildWindows(child)))
                                for addr_child in addr_children:
                                    if (w.GetClassName(addr_child) == 'Address Band Root'):
                                        addr_edit = addr_child
                                        addr_children = list(set(self.searchChildWindows(child)))
                                        for addr_child in addr_children:
                                            if (w.GetClassName(addr_child) == 'msctls_progress32'):
                                                addr_edit = addr_child
                                                addr_children = list(set(self.searchChildWindows(child)))
                                                for addr_child in addr_children:
                                                    if (w.GetClassName(addr_child) == 'Breadcrumb Parent'):
                                                        addr_edit = addr_child
                                                        addr_children = list(set(self.searchChildWindows(child)))
                                                        for addr_child in addr_children:
                                                            if (w.GetClassName(addr_child) == 'ToolbarWindow32'):
                                                                text=self.getEditText(addr_child)
                                                                if "\\" in text:
                                                                    self.address_1=self.getEditText(addr_child)[text.index(" ")+1:]
                                                                    # print("Address --> "+self.address_1)

        for window in range(shellwindows.Count):
            window_url = urllib.parse.unquote(shellwindows[window].LocationURL,encoding='ISO 8859-1')
            self.window_dir = window_url.split("///")[1].replace("/", "\\")
            # print("Directory --> "+self.window_dir)
            if self.window_dir==self.address_1:
                selected_files = shellwindows[window].Document.SelectedItems()
                for file in range(selected_files.Count):
                    self.files.append(selected_files.Item(file).Path)
                # print("Files --> "+str(self.files))
        return self.window_dir, self.files
    
    def create_new_file(self, query):
        # create a new file of python name index
        directory, _ = self.explorer_fileselection()
        extension = ''.join(query.split()[5])
        file_name = ''.join(query.split()[7:])
        self.extension = extension
        self.file_name = file_name

        if "python" in self.extension:
            exe = ".py"
        elif "javascript" in self.extension:
            exe = ".js"
        elif "php" in self.extension:
            exe = ".php"
        elif "html" in self.extension:
            exe = ".html"
        elif "css" in self.extension:
            exe = ".css"
        else:
            exe = ".txt"

        full_file = f"{self.file_name}{exe}"
        complete_name = os.path.join(directory, full_file)
        with open(complete_name, "w"):
            pass
        
    def direc_files_list(self):
        directory, files = self.explorer_fileselection()
        files = os.listdir(directory)
        for file in files:
            print(file.lower())
    
    def zip_files(self, query):        
        # specifying the zip file name
        directory, files = self.explorer_fileselection()
        for file in files:
            file_name = file
        
        if "extract" in query:
            # opening the zip file in READ mode
            with ZipFile(file_name, 'r') as zip:
                # printing all the contents of the zip file
                zip.printdir()
            
                # extracting all the files
                print('Extracting all the files now...')
                zip.extractall(directory)
                print('Done!')
        else:
            print('Following files will be zipped:')
            for file_name in files:
                print(file_name)
        
            # writing files to a zipfile
            with ZipFile('my_python_files.zip','w') as zip:
                # writing each file one by one
                for file in files:
                    zip.write(file)
  
            print('All files zipped successfully!')  
            
    def encrypt_image(self):
        # try block to handle exception
        try:
            # take path of image as a input
            path = input(r'Enter path of Image : ')
            
            # taking encryption key as input
            key = int(input('Enter Key for encryption of Image : '))
            
            # print path of image file and encryption key that
            # we are using
            print('The path of file : ', path)
            print('Key for encryption : ', key)
            
            # open file for reading purpose
            fin = open(path, 'rb')
            
            # storing image data in variable "image"
            image = fin.read()
            fin.close()
            
            # converting image into byte array to 
            # perform encryption easily on numeric data
            image = bytearray(image)
        
            # performing XOR operation on each value of bytearray
            for index, values in enumerate(image):
                image[index] = values ^ key
        
            # opening file for writting purpose
            fin = open(path, 'wb')
            
            # writing encrypted data in image
            fin.write(image)
            fin.close()
            print('Encryption Done...')
        
            
        except Exception:
            print('Error caught : ', Exception.__name__)
            
    def decrypt_image(self):
        # try block to handle the exception
        try:
            # take path of image as a input
            path = input(r'Enter path of Image : ')
            
            # taking decryption key as input
            key = int(input('Enter Key for encryption of Image : '))
            
            # print path of image file and decryption key that we are using
            print('The path of file : ', path)
            print('Note : Encryption key and Decryption key must be same.')
            print('Key for Decryption : ', key)
            
            # open file for reading purpose
            fin = open(path, 'rb')
            
            # storing image data in variable "image"
            image = fin.read()
            fin.close()
            
            # converting image into byte array to perform decryption easily on numeric data
            image = bytearray(image)
        
            # performing XOR operation on each value of bytearray
            for index, values in enumerate(image):
                image[index] = values ^ key
        
            # opening file for writting purpose
            fin = open(path, 'wb')
            
            # writing decryption data in image
            fin.write(image)
            fin.close()
            print('Decryption Done...')
        
        
        except Exception:
            print('Error caught : ', Exception.__name__)
        
# while True:
#     try:
#         main = file_management()
#         # direc, files = main.explorer_fileselection()
#     except Exception:
#         print("No Path Found!")
#     time.sleep(1)

# main = file_management()
# time.sleep(5)
# main.create_new_file("create a new file of html name index")
# main.zip_files("extract")

