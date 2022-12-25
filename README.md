# Data-Processor
Graphics User Interface

![image](https://user-images.githubusercontent.com/33480113/209458941-82687463-c539-4555-b37c-c83a35ab5610.png)


This is a small program that I built.

Before this program I used to have a dedicated scan team in my warehouse. They would scan every single box to a truck ID (skid ID). It would take about 60 Labor Hours every day, Now with this application I can scan up to 2 boxes per second to a truck ID. Allowing me to process a full truck in 5 Minutes.

• It takes in a list of big list of unprocessed data in RawData: input field.

• Processes the data and makes a new list of Carton ID’s.

• Those carton ID’s are scanned to a SKID ID decided by the user.

• As the Application that my company used does not have a API, I have to use a Screen based Automation Module PyAutoGUI in this script to interact with my company software.

• The GUI is build using Kivy.
