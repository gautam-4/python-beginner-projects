import qrcode

def generate_QR(data):
    qr = qrcode.QRCode(version = 1,
                       error_correction = qrcode.constants.ERROR_CORRECT_L,
                       box_size = 10, 
                       border = 5)
    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save("customQR.png")

def main():
    #data = input("Enter data to be encoded: ")
    data = "github.com/gautam-4"
    generate_QR(data)

if __name__ == "__main__":
    main()