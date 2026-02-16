import qrcode

upi_id = input("Enter your UPI ID: ")

phonepay_url = f"upi://pay?pa={upi_id}&pn=recipient%20name&mc=1234"

phonepay_qr = qrcode.make(phonepay_url)

phonepay_qr.save("phonepay_qr.png")

phonepay_qr.show()
