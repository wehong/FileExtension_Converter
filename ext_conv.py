import sys
import os

def ext_conv(cur_path, asis_ext, tobe_ext):
    try:
        files = os.listdir(cur_path);
    except FileNotFoundError:
        print("Error - \'%s\' does not exist!" % abs_path)
        quit()
    
    print("File extension conversion started...")
    print("from \'.%s\' to \'.%s\'...\n" % (asis_ext, tobe_ext))

    for f in files:
        tgt_file = os.path.join(cur_path, f)
        if os.path.isfile(tgt_file) and not f.startswith("."):
            fname, fext = os.path.splitext(tgt_file)
            if fext[1:] == asis_ext:
                new_file = fname + '.' + tobe_ext
                os.rename(tgt_file, new_file)
                new_path, new_f = os.path.split(new_file)
                print("\'%s\' is renamed to \'%s\'" % (f, new_f))

    print("\nConversion finished.\n")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        ext_conv(os.getcwd(), sys.argv[1], sys.argv[2])
    else:
        print("Please specify both as-is and to-be file extensions.")
        print("\tUsage: python ext_conv <as-is file ext> <to-be file ext>\n")
