import qrcode

#tacking upi id as input

upi_id = input("Enter your UPI ID: ")

#upi://pay?pa=upi_id&pn=Name&am=Amount&cu=INR

phonepay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc-1234"
gpay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc-1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc-1234"
bhim_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc-1234"

#Create qr code for each payment app
phonepay_qr = qrcode.make(phonepay_url)
gpay_qr = qrcode.make(gpay_url)
paytm_qr = qrcode.make(paytm_url)
bhim_qr = qrcode.make(bhim_url)

# #save the qr code to image file(optional)
# phonepay_qr.save("phonepay_qr.png")
# gpay_qr.save("gpay_qr.png")
# paytm_qr.save("paytm_qr.png")
# bhim_qr.save("bhim_qr.png")

#Display the qr codes (you may need to install pillow: pip install pillow)
phonepay_qr.show()
gpay_qr.show()
paytm_qr.show()
bhim_qr.show()



