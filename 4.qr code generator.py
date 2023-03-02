# install libraries qrcode and image if not installed
import qrcode

#qrcode geenration
def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants. ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")

#main 
while True:
    choice = input("Do you want to make a qrcode(Yes/No): ").lower()
    if choice == "yes":
        url = input("Enter your url: ")
        generate_qrcode(url)
    elif choice == 'no':
        print("Thank you")
        quit()
    else:
        print("Invalid input, enter yes or no")
