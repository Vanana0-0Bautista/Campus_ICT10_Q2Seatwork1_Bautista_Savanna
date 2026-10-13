from pyscript import document, display

Club_members = [
    "Seana Bautista",
    "Carlos Borromeo",
    "Jericho Magsalin", 
    "Anya Basuil",
    "Orange Mendoza"
    ]



def submit_form(event):
    first_name = document.getElementById("first_name").value

    last_name = document.getElementById("last_name").value

    full_name = first_name + " " + last_name

    is_member = full_name in Club_members
    messages = {

        True: "Congratulations!  " + full_name + " You are a member of the club.",
        False: "Sorry!  " + full_name + " You are not a member of the club."
    }

    document.getElementById("output").innerHTML = messages[is_member]

 
