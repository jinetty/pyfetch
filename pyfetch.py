#!/usr/bin/env python
# ________  ___    ___ ________ _______  _________  ________  ___  ___
# |\   __  \|\  \  /  /|\  _____\\  ___ \|\___   ___\\   ____\|\  \|\  \
# \ \  \|\  \ \  \/  / | \  \__/\ \   __/\|___ \  \_\ \  \___|\ \  \\\  \
#  \ \   ____\ \    / / \ \   __\\ \  \_|/__  \ \  \ \ \  \    \ \   __  \
#   \ \  \___|\/  /  /   \ \  \_| \ \  \_|\ \  \ \  \ \ \  \____\ \  \ \  \
#    \ \__\ __/  / /      \ \__\   \ \_______\  \ \__\ \ \_______\ \__\ \__\
#     \|__||\___/ /        \|__|    \|_______|   \|__|  \|_______|\|__|\|__|
#         \|___|/
# Made by Kreato
# Licensed Under GPL3-Or-Later

# import stuffs
import sys, platform, psutil, os, getpass, shutil, time
from colorama import init, Fore, Back, Style

# Setup colorama
init()

# get the args
args = sys.argv[1:]

# if needed print the help!
if "-h" in args or "--help" in args:
    # enjoy this lovely table made out of entirely unicode chars
    print('''pyfetch - Stylish and simple fetch for your terminal that is customizable, and fast.
╔═════╦═══════════════════╦════════════════════════════════════════════════════╗
║ -c  ║ --cpu             ║ CPU info & usage                                   ║
╠═════╬═══════════════════╬════════════════════════════════════════════════════╣
║ -d  ║ --disk            ║ Disk usage                                         ║
╠═════╬═══════════════════╬════════════════════════════════════════════════════╣
║ -m  ║ --memory          ║ RAM usage                                          ║
╠═════╬═══════════════════╬════════════════════════════════════════════════════╣
║ -u  ║ --uptime          ║ Uptime                                             ║
╠═════╬═══════════════════╬════════════════════════════════════════════════════╣
║ -uh ║ --userhostname    ║ user@hostname                                      ║
╠═════╬═══════════════════╬════════════════════════════════════════════════════╣
║ -p  ║ --packages        ║ Installed package count                            ║
╠═════╬═══════════════════╬════════════════════════════════════════════════════╣
║ -os ║ --operatingsystem ║ Which OS you have                                  ║
╠═════╬═══════════════════╬════════════════════════════════════════════════════╣
║ -t  ║ --terminal        ║ What type of terminal you are using                ║
╠═════╬═══════════════════╬════════════════════════════════════════════════════╣
║ -wm ║ --windowmanager   ║ Your current window manager                        ║
╠═════╬═══════════════════╬════════════════════════════════════════════════════╣
║ -a  ║ --asciiart        ║ ASCII art for your Distro / OS, or a specified OS. ║
║═════╬═══════════════════╬════════════════════════════════════════════════════╣
║ -na ║ --noascii         ║ Disables ascii art                                 ║
╚═════╩═══════════════════╩════════════════════════════════════════════════════╝ ''')
    exit()

to_print = []
# this global bullshit is because python's scoping is dumb and decides that it'd
# rather shadow the var with a newly declared one than assign it a value
global print_index
print_index = 0

# ascii art
alpine = '''
   /\\ /\\     
  // \\  \\    
 //   \\  \\   
///    \\  \\  
//      \\  \\ 
         \\  \\
          \\  '''

endeavour = '''     /\\\\      
    //  \\\\\\\\  
   //    \\\\ \\\\
 / /     _) ) 
/_/___-- __-  
 /____--      '''

guix = '''|.__          __.|
|__ \\        / __|
   \\ \\      / /   
    \\ \\    / /    
     \\ \\  / /     
      \\ \\/ /      
       \\__/       '''

arch = '''      /\\      
     /^^\\     
    /\\   \\    
   /  __  \\   
  /  (  )  \\  
 / __|  |__\\\\ 
///        \\\\\\
'''

debian = '''  _____  
 /  __ \\ 
|  /    |
|  \\___- 
-_       
  --_    '''

fedora = '''     _____ 
    /   __/
   |  /    
  _|  |_   
 |_    _|  
   |  |    
 __/  |    
/____/     '''

freebsd = ''' _  _____     
/ \\\\\\`     \\`/
\\/       (__/ 
|           | 
|           | 
 \\         /  
  \\`-_____-\\` '''

gentoo = '''  .-----.      
.\\`    _  \\`.  
\\`.   (_)   \\`.
  \\`.        / 
 .\\`       .\\` 
/       .\\`    
\\____.-\\`      '''

linux = '''    ___   
   (.. \\  
   (<> |  
  //  \\ \\ 
 ( |  | /|
_/\\ __)/_ 
 \\/-__\\/  '''

macos = '''       (/    
  .---__--.  
 /         \\ 
|         /  
|         \\\\_
 \\         / 
  \\`._.-._.\\`'''

manjaro = '''||||||||| ||||
||||||||| ||||
||||      ||||
|||| |||| ||||
|||| |||| ||||
|||| |||| ||||
|||| |||| ||||'''

nixos = '''  \\\\   \\\\ //  
 ==\\\\___\\\\/ //  
   //    \\\\// 
==//      //==
 //\\\\____//   
// /\\\\   \\\\== 
  // \\\\   \\\\  '''

openbsd = '''     _____    
   \\-     -/  
\\_/         \\ 
|        O O |
|_  <   )  3 )
/ \\         / 
   /-_____-\\  '''

raspbian = '''  __  __  
 (_\\)(/_)
 (_(__)_) 
(_(_)(_)_)
 (_(__)_) 
   (__)   '''

ubuntu = '''         _  
     ---(_) 
 _/  ---  \ 
(_) |   |   
  \  --- _/ 
     ---(_) '''

void = '''    _______    
    \\_____ \\`- 
 /\\   ___ \\`- \\
| |  /   \\  | |
| |  \\___/  | |
 \\ \\`-_____  \\/
  \\`-______\\   '''

windows = '''         /__---|
 /----| |      |
|-----| |------|
                
|-----| |------|
 \\----| |      |
         \\--___|
'''


def get_ascii(current_distro=None):
    if current_distro is None:
        if os.name == 'posix':
            import distro
            current_distro = distro.linux_distribution()[0]
        elif os.name == "nt":
            current_distro = "windows"
        else:
            current_distro = ""
    # ".lower()"" and "in" because im not confident i got these 100% correct
    if "alpine" in current_distro.lower():
        ascii = alpine
        ascii_color = Fore.BLUE
    elif "arch" in current_distro.lower():
        ascii = arch
        ascii_color = Fore.BLUE
    elif "debian" in current_distro.lower():
        ascii = debian
        ascii_color = Fore.RED
    elif "fedora" in current_distro.lower():
        ascii = fedora
        ascii_color = Fore.MAGENTA
    elif "freebsd" in current_distro.lower():
        ascii = freebsd
        ascii_color = Fore.RED
    elif "gentoo" in current_distro.lower():
        ascii = gentoo
        ascii_color = Fore.MAGENTA
    elif "linux" in current_distro.lower():
        ascii = linux
        ascii_color = Fore.RESET
    elif "mac" in current_distro.lower():
        ascii = macos
        ascii_color = Fore.RESET
    elif "manjaro" in current_distro.lower():
        ascii = manjaro
        ascii_color = Fore.GREEN
    elif "nix" in current_distro.lower():
        ascii = nixos
        ascii_color = Fore.BLUE
    elif "openbsd" in current_distro.lower():
        ascii = openbsd
        ascii_color = Fore.YELLOW
    elif "raspbian" in current_distro.lower():
        ascii = raspbian
        ascii_color = Fore.RED
    elif "void" in current_distro.lower():
        ascii = void
        ascii_color = Fore.GREEN
    elif "ubuntu" in current_distro.lower():
        ascii = ubuntu
        ascii_color = Fore.RED
    elif "windows" == current_distro:
        ascii = windows
        ascii_color = Fore.BLUE
    elif "guix" in current_distro.lower():
        ascii = guix
        ascii_color = Fore.YELLOW
    elif "endeavour" in current_distro.lower():
        ascii = endeavour
        ascii_color = Fore.MAGENTA
    else:
        ascii = "\n"
        ascii_color = Fore.RESET
    return ascii, ascii_color


ascii, ascii_color = get_ascii()


# utlity functions for arrays
def append(array, index, item):
    if index + 1 < len(array):
        array[index] += item
    else:
        array.append(item)


def insert_at_start(array, index, item):
    if index < len(array):
        array[index] = item + array[index]
    else:
        array.append(item)


# define important functions
def package_count():
    global print_index
    if os.name == "nt":
        return
    if os.name == 'posix':
        import distro
        current_distro = distro.linux_distribution()
        # apt, if Debian make it red
        if len(os.popen("whereis apt").read()) > 5:
            packages = os.popen('dpkg-query -l | wc -l').read().strip()
            append(to_print, print_index, ascii_color + " " + Fore.WHITE + f"  APT:  {packages}")
            print_index += 1

        # emerge, if Gentoo make it purple
        if len(os.popen("whereis emerge").read()) > 8:
            packages = os.popen("ls -d /var/db/pkg/*/* | wc -l | awk '{printf $1 }'").read()
            append(to_print, print_index, ascii_color + " " + Fore.WHITE + f"  Emerge:  {packages}")
            print_index += 1

        # pacman, if Arch make it blue
        if len(os.popen("whereis pacman").read()) > 8:
            packages = os.popen('pacman -Q | wc -l').read().strip()
            append(to_print, print_index, ascii_color + " " + Fore.WHITE + f"  Pacman:  {packages}")
            print_index += 1
    else:
        current_distro = ""


def pcpu():
    global print_index
    try:
        getcpu = platform.processor()
        append(to_print, print_index, ascii_color + " " + Fore.WHITE + f"  {getcpu} ({cpu}%)")
        print_index += 1
    except Exception:
        pass

def puptime():
    global print_index
    try:
        getuptime = time.time() - psutil.boot_time()
        if getuptime // 3600 != 0.0:  # if its not 0 hours show hours instead of minutes
            append(to_print, print_index, ascii_color + " " + Fore.WHITE + f"  {getuptime // 3600} hours")
            print_index += 1
        elif getuptime // 3600 == 0.0: # if its 0 hours show minutes instead of hours
            append(to_print, print_index, ascii_color + " " + Fore.WHITE + f"  {getuptime // 60} minutes")
            print_index += 1
        elif getuptime // 60 == 0.0: # if its 0 minutes show seconds instead
            append(to_print, print_index, ascii_color + " " + Fore.WHITE + f"  {round(getuptime)} minutes")
            print_index += 1
    except Exception:
        pass

def pdisk():
    global print_index
    try:
        append(to_print, print_index,
               ascii_color + " " + Fore.WHITE + f"  {useddisk // (2 ** 30)}GiB / {totaldisk // (2 ** 30)}GiB ({diskpercent_used}%)")
    except Exception:
        append(to_print, print_index,
               f"   {useddisk // (2 ** 30)}GiB / {totaldisk // (2 ** 30)}GiB ({diskpercent_used}%)")
    finally:
        print_index += 1


def pmemory():
    global print_index
    try:
        if used != 0:  # if its not 0 GiB then show GiB instead of MiB
            append(to_print, print_index,
                   ascii_color + "  " + Fore.WHITE + f" {used}GiB / {total}GiB ({percent_used}%)")
            print_index += 1
        elif used == 0:  # if its 0 GiB then show MiB instead of GiB
            used2 = ram.used // (1024 ** 2)
            append(to_print, print_index,
                   ascii_color + "  " + Fore.WHITE + f" {used2}MiB / {total}GiB ({percent_used}%)")
            print_index += 1
    except Exception:
        if used == 0:
            used2 = ram.used // (1024 ** 2)
            append(to_print, print_index, f"   {used2}MiB / {total}GiB ({percent_used}%)")
            print_index += 1
        elif used != 0:
            append(to_print, print_index, f"   {used}GiB / {total}GiB ({percent_used}%)")
            print_index += 1


def puserhost():
    global print_index
    try:
        append(to_print, print_index, ascii_color + " " + Fore.WHITE + f"  {username}@{uname.node}")
    except Exception:
        append(to_print, print_index, f"   {username}@{uname.node}")
    finally:
        print_index += 1


def pos():
    global print_index
    if os.name == 'nt':
        append(to_print, print_index, ascii_color + " " + Fore.WHITE + f"  {uname.system} {uname.release}")
        print_index += 1
        return
    elif os.name == 'posix':
        import distro
        distribution = distro.linux_distribution()
        result = ' '.join(map(str, distribution))
    try:
        append(to_print, print_index, ascii_color + " " + Fore.WHITE + f"  {result} {uname.release}")
    except Exception:
        append(to_print, print_index, f"  {result} {uname.release}")
    finally:
        print_index += 1


def pterm():
    global print_index
    if "SHELL" in os.environ:
        shell = os.environ['SHELL']
        term = os.environ['TERM']  # hope this doesnt cause any issues
        if os.name == 'posix':
            import distro
            current_distro = distro.linux_distribution()
        else:
            current_distro = ""
        try:
            append(to_print, print_index, ascii_color + "  " + Fore.WHITE + f" {shell} {term}")
        except Exception:
            append(to_print, print_index, f"   {shell} {term}")
        finally:
            print_index += 1


def pwm():
    global print_index
    if os.name == 'posix':
        import distro
        distro = distro.linux_distribution()
    else:
        distro = ""
    try:
        if len(os.popen("whereis wmctrl").read()) > 8 and os.name == 'posix':
            wm = os.popen("wmctrl -m | awk -F'Name: ' '{printf $2}'").read()
            append(to_print, print_index, ascii_color + " " + Fore.WHITE + f"  {wm}")
            print_index += 1
    except Exception:
        append(to_print, print_index, f"   {wm}")
        print_index += 1


def pasciiart(current_distro=None):
    
    ascii, ascii_color = get_ascii(current_distro)

    ascii_lines = ascii.splitlines()
    for i in range(max(len(to_print), len(ascii_lines))):
        if i < len(ascii_lines):
            insert_at_start(to_print, i, ascii_color + ascii_lines[i] + " " + Fore.RESET)
        else:
            padding = ""
            for _ in ascii_lines[0]:
                padding += " "
            insert_at_start(to_print, i, padding + " ")


def noascii():
    pdisk()
    puserhost()
    pcpu()
    pmemory()
    pterm()
    puptime()
    pwm()
    pos()
    package_count()


# get system info n stuff
uname = platform.uname()
cpu = psutil.cpu_percent()
username = getpass.getuser()
ram = psutil.virtual_memory()
used = ram.used // (2 ** 30)
total = ram.total // (2 ** 30)
totaldisk, useddisk, freedisk = shutil.disk_usage("/")
diskpercent_used = round(useddisk / totaldisk * 100, 2)
percent_used = round(ram.used / ram.total * 100, 2)

# arg parser code
print_ascii = False
selected_ascii = None

#From https://www.reddit.com/r/unixporn/comments/najxnu/oc_i_was_bored_so_i_made_a_fetch_tool_in_python/gxuk7fs?utm_source=share&utm_medium=web2x&context=3
for i in range(len(args)):
    arg = args[i]
    if arg == "-c" or arg == "--cpu":
        pcpu()
    elif arg == "-d" or arg == "--disk":
        pdisk()
    elif arg == "-m" or arg == "--memory":
        pmemory()
    elif arg == "-uh" or arg == "--userhostname":
        puserhost()
    elif arg == "-p" or arg == "--packages":
        package_count()
    elif arg == "-os" or arg == "--operatingsystem":
        pos()
    elif arg == "-t" or arg == "--terminal":
        pterm()
    elif arg == "-wm" or arg == "--windowmanager":
        pwm()
    elif arg == "-u" or arg == "--uptime":
        puptime()
    elif arg == "-a" or arg == "--asciiart":
        if i + 1 < len(args) and not args[i + 1].startswith("-"):
            selected_ascii = args[i + 1]
            i += 1
        print_ascii = True
    elif arg == "-na" or arg == "--noascii":
        noascii()
    i += 1

if print_ascii:
    pasciiart(selected_ascii)

if len(args) == 0:
    pdisk()
    puserhost()
    pcpu()
    pmemory()
    pterm()
    puptime()
    pwm()
    pos()
    package_count()
    pasciiart()

for line in to_print:
    print(line)
