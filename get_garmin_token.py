from garminconnect import Garmin

email = input("Garmin email: ")
password = input("Garmin password: ")

garmin = Garmin(
    email=email,
    password=password,
    prompt_mfa=lambda: input("MFA code: ").strip(),
)

garmin.login("garmin_tokens")  # saves tokens into this folder

print("\n✅ Login successful. Tokens saved to ./garmin_tokens/")