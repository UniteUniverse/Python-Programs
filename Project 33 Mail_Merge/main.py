Placeholder="[name]"
with open(r"D:\Data\Docs PKJHA 13-09-23\B. TECH\Udemy\Python Programming\Project\Mail Merge Project Start\Input\Names\invited_names.txt") as names_file:
    names=names_file.readlines()

with open(r"Mail Merge Project Start\Input\Letters\starting_letter.txt")as letter_file:
    letter_contents=letter_file.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter_contents.replace(Placeholder, stripped_name)
        with open(rf"D:\Data\Docs PKJHA 13-09-23\B. TECH\Udemy\Python Programming\Project\Mail Merge Project Start\Output\ReadyToSend\letter_for_{stripped_name}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter)