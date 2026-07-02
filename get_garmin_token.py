import os
from garminconnect import Garmin

email = input("Garmin email: ")
password = input("Garmin password: ")

garmin = Garmin(email=email, password=password)
garmin.login()  # This will prompt you for your MFA code right here if needed

token_dir = "garmin_tokens"
garmin.garth.dump(token_dir)
print(f"\n✅ Tokens saved to ./{token_dir}/")
