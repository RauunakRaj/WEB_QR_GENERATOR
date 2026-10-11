# QR code generator
import qrcode

# Take input from the user
data = input("Enter a website URL or text: ")

# Generate the QR code
qr = qrcode.make(data)

# Save the QR code as an image
qr.save("my_qr.png")

print("QR Code generated successfully!")
print("Check your project folder for my_qr.png")
