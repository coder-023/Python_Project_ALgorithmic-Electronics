# Python_Project_Algorithmic-Electronics
Python based project for detecting Social distancing is carried out or not
  Project Title:Social Distancing regulator in Lift using Python
   The simple idea of this project is that it will alert if social distancing voilation is detected.I have used haarcascade model to detect faces of people in lift.Simple idea of my project is that when model detects more than 1 faces, it calculates the distance between two detected images.If(let's say) distance between them is less than 40 cm, than it will send email(through SMTP) and text messages(through Twilio) to the respected authority.
   I have also added a delay of 30 secs between the reporting of violation.


Note:I have cleared all the fields of twilio ID,sender mail id, password,etc for security purposes
