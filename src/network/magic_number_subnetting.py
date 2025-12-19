from colorama import Fore, Back, Style, init
init()

from utils.style import green, red, blue, cyan, magenta, white, black, yellow
from utils.style import green_b, red_b, blue_b, cyan_b, magenta_b, white_b, black_b, yellow_b
from utils.style import green_d, red_d, blue_d, cyan_d, magenta_d, white_d, black_d, yellow_d

print()
print(white_b("If the subnet mask is") + green_b(" 255") + white_d(" , copy the IP address."))
print(white_b("If the subnet mask is") +  green_b(" 0") + white_d(", copy the 0."))
print(white_b("Anything not") + green_b(" 255") + white_b(" or") + green_b(" 0") + white_b(" is the interesting octet."))
print()
print(white_b("Subtract the") + cyan_b(" interesting octet") + white_b(" subnet mask from") + cyan_b(" 256."))
print(white_b("The difference is the") + magenta_b(" magic number."))
print(white_b("Split the subnet into ranges by dividing") + cyan_b(" 256") + white_b(" by the") + magenta_b(" magic number") + white_b(" and use the first IP in that range for the subnet ID."))
print()
print(white_d("i.e. IP:   165.245.77.14 ->") + red_b(" 165.245.64.0"))
print(white_d("     mask: 255.255.240.0"))

