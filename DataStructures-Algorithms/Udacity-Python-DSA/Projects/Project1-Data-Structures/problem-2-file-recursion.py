import os

def search_files(path, ext='.c', show_fullpath=True):
    '''
    Inputs:
    path -- string, directory at which files to be searched
    ext -- string, extension of the search file
    show_fullpath -- boolean, if True, display the full path where the file is located
                              if False, display only the file name
    Returns:
    None, but print the file names
    '''
    files_folders = os.listdir(path)
    for item in files_folders:
        # Full path
        fullpath = os.path.join(path, item)
        
        # Display file if found
        if fullpath.endswith(ext):
            if show_fullpath:
                print(fullpath)
            else:
                print(item)
                
        # Search in the subdirectories (recursive file search)
        if os.path.isdir(fullpath) and len(os.listdir(fullpath)) > 0:
            search_files(fullpath, ext, show_fullpath)
    return None

# Tests
# 1
print('Path for .c files:')
path = './testdir/'
search_files(path)
# Path for .c files:
# ./testdir/subdir1/a.c
# ./testdir/subdir3/subsubdir1/b.c
# ./testdir/subdir5/a.c
# ./testdir/t1.c

# 2
print('\nPaths for .h files:')
path = './testdir/'
search_files(path, ext='.h')
# Paths for .h files:
# ./testdir/subdir1/a.h
# ./testdir/subdir3/subsubdir1/b.h
# ./testdir/subdir5/a.h
# ./testdir/t1.h

# 3
print('\nNames of file with .c extension:')
path = './testdir/'
search_files(path, ext='.c', show_fullpath=False)
# Names of file with .c extension:
# a.c
# b.c
# a.c
# t1.c

