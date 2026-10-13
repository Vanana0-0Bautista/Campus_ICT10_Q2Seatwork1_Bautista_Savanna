from pyscript import document, display

Club_members = [
    "Seana Bautista",
    "Carlos Borromeo",
    "Jericho Magsalin", 
    "Anya Basuil",
    "Orange Mendoza"
    ]



def submit_form(e):

    first_name = document.getElementById("first_name").value

    last_name = document.getElementById("last_name").value

    full_name = first_name + " " + last_name

    is_member = full_name in Club_members
    messages = {
        True: f"Welcome {full_name}! You are a member of the club.",
        False: f"Sorry {full_name}, you are not a member of the club."
    }

    document.getElementById("result").innerHTML = messages[is_member]

 
