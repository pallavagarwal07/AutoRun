import os

def py(path, file, name):
    os.system("urxvt -e bash -c 'python2 "+ path +"; echo -e \"\\n\\nPress [ENTER] to continue\\n\"; read'")

def latex(path, file, name):
    os.system('pdflatex ' + file)
    ret = os.system('ps -eww | grep zathura')
    if ret:
        os.system('zathura ' + name + '.pdf')

def c(path, file, name):
    chk = os.system("ls makefile") and os.system("ls Makefile") and os.system("ls GNUmakefile")

    if not chk:
        cmd = "make " + name + ";"
    else:
        cmd = "gcc -o " + name + " " + path + ";"

    os.system("urxvt -e                                                       \
                    bash -c '                                                 \
                        bash -c \"                                            \
                            set -e;                                           \
                            " + cmd + "                                       \
                            echo \'------\';                                  \
                            ./"+ name + ";                                    \
                            rm " + name + ";                                  \
                            exit;                                             \
                        \";                                                   \
                        echo -e \"------\\nPress [ENTER] to continue\\n\";    \
                        read;                                                 \
                    '                                                         \
                ")

def cpp(path, file, name):
    chk = os.system("ls makefile") and os.system("ls Makefile") and os.system("ls GNUmakefile")

    if not chk:
        cmd = "make " + name + ";"
    else:
        cmd = "g++ -o " + name + " " + path + ";"

    os.system("urxvt -e                                                       \
                    bash -c '                                                 \
                        bash -c \"                                            \
                            set -e;                                           \
                            " + cmd + "                                       \
                            echo \'------\';                                  \
                            ./"+ name + ";                                    \
                            rm " + name + ";                                  \
                            exit;                                             \
                        \";                                                   \
                        echo -e \"------\\nPress [ENTER] to continue\\n\";    \
                        read;                                                 \
                    '                                                         \
                ")

def go(path, file, name):
    os.system("urxvt -e                                                       \
                    bash -c '                                                 \
                        bash -c \"                                            \
                            set -e;                                           \
                            echo \'------\';                                  \
                            go run " + path + ";                              \
                            exit;                                             \
                        \";                                                   \
                        echo -e \"------\\nPress [ENTER] to continue\\n\";    \
                        read;                                                 \
                    '                                                         \
                ")

dict = {
        'c': c,
        'cpp': cpp,
        'python': py,
        'go': go,
        'tex': latex
        }
try:
    import vim
    import time
    from threading import Thread
    a = vim.eval("$NVIM_LISTEN_ADDRESS")
    def cmdline(a):
        from neovim import attach
        nvim = attach('socket', path=a)
        type = nvim.eval('&filetype')
        path = nvim.eval("expand('%:p')")
        file = nvim.eval("expand('%')")
        name = nvim.eval("expand('%:r')")
        nvim.command('w')
        if type in dict:
            dict[type](path, file, name)
        else:
            nvim.command("echo 'Sorry, filetype "+type+" not supported'")
        exit(0)

    t = Thread(target=cmdline, args=(a,))
    t.start()
except Exception as e:
    print "Error encountered: ", e
