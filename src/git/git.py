
from colorama import Fore, Back, Style, init
init()

from utils.style import green, red, blue, cyan, magenta, white, black, yellow
from utils.style import green_b, red_b, blue_b, cyan_b, magenta_b, white_b, black_b, yellow_b
from utils.style import green_d, red_d, blue_d, cyan_d, magenta_d, white_d, black_d, yellow_d

print(cyan_b("git") + red_b(" remote set-url origin") + cyan_b(" git@github.com:USERNAME/REPO.git"))
print(white("- Sets the url for the remote repository."))
print(cyan_b("git") + red_b(" add"))
print(white("- Stages all changes for the next commit."))
print(cyan_b("git") + red_b(" commit"))
print(white("- Creates a snapshot of the staged changes in the local repository."))
print(cyan_b("git") + red_b(" push"))
print(white("- Uploads local commits to remote repository.") + white_d("(git push origin branch)"))
