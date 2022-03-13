import pytextnow as pytn
import get_info as BlackBoard


print("Connecting to server")
#client = pytn.Client("dannychung333", sid_cookie="s%3AUzbX3dzpU2DDWhXrpnOayIeKncK0JjhN.R20zdRsZWF2tCDIS5VzjTtIDL4UqDG15qomj8%2FARM1Q", csrf_cookie="s%3A1-RmzV2mdnfXy-MFNLMpnQaT.7hPEJC5lU67MAcewwrlET%2BHSpx33uUMB4GqRIW7vNIU")
client = pytn.Client("luis29798", sid_cookie="s%3A8fhrkEnwxcHwt51RtxbgBYIOeH_bhxAS.OmVatrUGxqWWZ80coYN0VhJ2G0K15MXH5ggQUQwY%2FnM", csrf_cookie="s%3A0wmGXLUFhATOQU875LeVbnal.m7qZODeJLASfzBqdalYjMIiAccFGlZSPkLyCelL88kA")
print("[*]Connected!']")


@client.on("message")
def handler(msg):

    if msg.type == pytn.MESSAGE_TYPE:
        message = msg.content.split()
        userNumber = msg.number
        if len(message) == 3:
            BlackBoard.bot(message[0], message[1], message[2], userNumber)
        else:
            msg.send_sms("Invalid Format!")
            msg.send_sms("Format example: NetID Password Command")
