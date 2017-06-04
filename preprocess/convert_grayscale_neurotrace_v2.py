#! /usr/bin/env python

import sys
import os
sys.path.append(os.path.join(os.environ['REPO_DIR'], 'utilities'))

from skimage.exposure import rescale_intensity

from utilities2015 import *
from registration_utilities import *
from metadata import *
from data_manager import *

########################################

import argparse
import json

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='Convert to grayscale with nissl-like intensity profile.')

parser.add_argument("stack", type=str, help="Stack")
parser.add_argument("filenames", type=str, help="filenames")
parser.add_argument("-l", "--low", type=int, help="Low intensity limit for linear contrast stretch")
parser.add_argument("-H", "--high", type=int, help="High intensity limit for linear contrast stretch")
args = parser.parse_args()

####################################

stack = args.stack
filenames = json.loads(args.filenames)

for fn in filenames:
    
    try:
    
        img_fp = DataManager.get_image_filepath(stack=stack, fn=fn, version='cropped', resol='lossless')
        download_from_s3(img_fp)

        if stack not in all_nissl_stacks and fn.split('-')[1][0] == 'F':

            t = time.time()
            img_blue = imread(img_fp)[..., 2]
            sys.stderr.write('Read: %.2f seconds\n' % (time.time() - t))
            
            if not hasattr(args, "low"):
                sys.stderr.write("No linear limits arguments are given, so use nonlinear mapping.\n")
            
                try:
                    intensity_mapping_fp = DataManager.get_ntb_to_nissl_intensity_profile_mapping_filepath(stack=stack, ntb_fn=fn)
                    download_from_s3(intensity_mapping_fp)
                    intensity_mapping_ntb_to_nissl = np.load(intensity_mapping_fp)
                except:
                    sys.stderr.write("Error loading section-specific ntb-to-nissl intensity mapping. Load a priori mapping instead.\n")
                    intensity_mapping_fp = DataManager.get_ntb_to_nissl_intensity_profile_mapping_filepath()
                    download_from_s3(intensity_mapping_fp)
                    intensity_mapping_ntb_to_nissl = np.load(intensity_mapping_fp)

                t = time.time()
                ntb_values = np.arange(0, 5000)
                img_blue_intensity_normalized = intensity_mapping_ntb_to_nissl[3000-img_blue.astype(np.int)].astype(np.uint8)
                sys.stderr.write('Convert: %.2f seconds\n' % (time.time() - t))
                
                output_fp = DataManager.get_image_filepath(stack=stack, fn=fn, version='cropped_gray', resol='lossless')

            else:
                sys.stderr.write("Linear limits arguments detected, so use linear mapping.\n")
                
                low_limit = args.low
                high_limit = args.high
                
                t = time.time()
                if low_limit > high_limit:
                    img_blue_intensity_normalized = rescale_intensity(low_limit-img_blue.astype(np.int), (0, low_limit-high_limit), (0, 255)).astype(np.uint8)
                else:
                    img_blue_intensity_normalized = rescale_intensity(img_blue.astype(np.int), (low_limit, high_limit), (0, 255)).astype(np.uint8)
                sys.stderr.write('Convert: %.2f seconds\n' % (time.time() - t))
                
                output_fp = DataManager.get_image_filepath(stack=stack, fn=fn, version='cropped_gray_linearNormalized', resol='lossless')
                
            t = time.time()
            create_parent_dir_if_not_exists(output_fp)
            imsave(output_fp, img_blue_intensity_normalized)
            sys.stderr.write('Save: %.2f seconds\n' % (time.time() - t))

            t = time.time()
            upload_to_s3(output_fp)
            sys.stderr.write('Upload: %.2f seconds\n' % (time.time() - t))

        else:

            t = time.time()
            print img_fp
            img = imread(img_fp)
            sys.stderr.write('Read: %.2f seconds\n' % (time.time() - t))

            t = time.time()
            img_gray = img_as_ubyte(rgb2gray(img))
            sys.stderr.write('Convert: %.2f seconds\n' % (time.time() - t))

            output_fp = DataManager.get_image_filepath(stack=stack, fn=fn, version='cropped_gray', resol='lossless')
            create_parent_dir_if_not_exists(output_fp)

            t = time.time()
            imsave(output_fp, img_gray)
            sys.stderr.write('Save: %.2f seconds\n' % (time.time() - t))

            t = time.time()
            upload_to_s3(output_fp)
            sys.stderr.write('Upload: %.2f seconds\n' % (time.time() - t))

        # else:
        #     sys.stderr.write("Filename %s is not F or N.\n" % fn)
    
    except Exception as e:
        sys.stderr.write('%s\n' % e)
        