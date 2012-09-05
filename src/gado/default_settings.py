from functions import gadodir
import os

def default_settings():
    settings = dict()
    settings['image_front_prefix']  = ''
    settings['image_front_postfix'] = '_front'
    settings['image_back_prefix']   = ''
    settings['image_back_postfix']  = '_back'
    settings['image_front_delim']   = ''
    settings['image_back_delim']    = ''
    settings['image_front_concat']  = 1 # other option is 0 for false
    settings['image_back_concat']   = 1 # other option is 0 for false
    settings['scanner_dpi']         = 600
    settings['image_front_filetype']= 'tiff'
    settings['image_back_filetype'] = 'jpg'
    settings['image_front_fn']      = 'set_incrementer' # other option is id
    settings['image_back_fn']       = 'set_incrementer' # other option is id
    settings['image_path']          = imagespath()
    settings['db_directory']        = dbpath()
    settings['baudrate']            = 115200
    settings['db_filename']         = 'db.sqlite'
    settings['wizard_run']          = 0
    settings['temp_scanned_image']  = '%s/%s' % (gadodir(), 'scanned')
    settings['temp_webcam_image']   = '%s/%s' % (gadodir(), 'webcam')
    return settings()

def dbpath():
    d = gadodir()
    p = os.path.join(d, 'databases')
    try:
        os.makedirs(p)
    except:
        print 'functions\tUnable to create the images path'
    return p

def imagespath():
    d = gadodir()
    p = os.path.join(d, 'images')
    try:
        os.makedirs(p)
    except:
        print 'functions\tUnable to create the images path'
    return p
