import datetime
import pandas as pd
import email_sender

# extracting today dates
today = datetime.datetime.now().strftime("%d-%m")

# accessing excel file
df = pd.read_excel("C:\\Python\\birthdate.xlsx")
email_list = df['Email'].tolist()
to_email = ''

# extracting and matching condition if today dates == birthdates

print(email_list)


def birthday_wish():
    for index, item in df.iterrows():
        # this will show the list of birthdates if you print birthdate
        birthday_person_name = ''
        if item["Dates"] == today:
            birthdate = item["Dates"]
            if today == birthdate:
                to_email = item['Email']
                birthday_person_name = item["Names"]
                email_list.remove(to_email)
                email_sender.sendEmail(to_email, email_list, birthday_person_name)


if __name__ == '__main__':
    birthday_wish()

