

import urllib.request as urllib

#checking connectivity
def main(url):
    print("Checking connectivity ")
    
    response = urllib.urlopen(url)
    print("Connected to" , url, "succesfully")
    print("The response code was: ", response.getcode())

print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")

#main part
while True:
    choice = input("Do you want to check the site connectivity(Yes/No): ").lower()
    if choice == "yes":
        main(input_url)
    elif choice == "no":
        print("Thank you")
        quit()
    else:
        print("Invalid input, please input Yes or No")

