import smtplib

content = 'Hi Akshay, Your ASUS laptop has been logged into. Please make sure it\'s secure.'

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('akshaygandhi2101998@gmail.com', '1lovenet')
mail.sendmail('akshaygandhi2101998@gmail.com', 'aksh0299@gmail.com', content)
mail.close()

