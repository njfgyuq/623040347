phone_dict = {"Jane Doe": "+27 555 5367",
              "John Smith": "+27 555 6254",
              "Bob Stone": "+27 555 5689"
              }
phone_dict["Jane Doe"] = "+27 555 1024"
phone_dict["Annna Cooper"] = "+27 555 3237"

print(phone_dict["Bob Stone"])
print(phone_dict.get("Bob Stone"))
print(phone_dict.keys())
print(phone_dict.values())
