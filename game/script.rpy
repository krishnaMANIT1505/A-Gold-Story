# Import Python's random module
init python:
    import random
# Declare the characters
define b = Character("Bhindi",color="#ff5733")
define m = Character("Madhuri",color="#f8d00b")
define k = Character("Kapti Seth",color="#470383")
default license_checked = False
default hallmark_checked = False
default huid_verified = False
default hallmark_is_fake = False
default proper_bill = False
# Start the game
label start:

    # Scene 1: Bhindi's Home
    scene bg_home
    m "Dear, I am thinking of buying a new pair of earrings."
    b "But you already have these beautiful pairs of earrings. Why do you need another?"
    m "You know how old these are. Don’t be such a kanjoos! Please get me one today."
    b "Okay, dear. I’ll go to Kapti Seth’s shop today and get you a new pair of earrings."
    m "Great! But don’t forget to check his license on the BIS Care app."

    menu:
        "Yeah, I will check it for sure.":
            $ license_checked = True
            b "Yeah, I will check it for sure."
            m "Good! Always stay cautious."
            b "(Bhindi installs the BIS Care app and verifies Kapti Seth’s license.)"
        "It’s not needed. He’s the most famous jeweller in the city.":
            $ license_checked = False
            b "It’s not needed. He’s the most famous jeweller in the city."

    # Scene 2: Kapti Seth's Shop
    scene bg_shop
    k "Namaste, Bhaisaab! What would you like to buy today?"
    b "I’m looking for a pair of earrings for my wife."
    k "Wonderful! How much is your budget?"
    b "Around ₹45,000–₹50,000."
    k "Perfect. Let me show you some options."
    k "(Presents an earring box.)"
    b "These earrings look nice. I’ll take this pair."
    k "Excellent choice! The gold weighs 5.980 grams with 916 purity. The price is ₹48,992, including GST and making charges."

    menu:
        "Can I get a magnifying glass to check the hallmark?":
            $ hallmark_checked = True
            b "Can I get a magnifying glass to check the hallmark?"
            k "Of course, bhaisaab."
            "Bhindi examines the hallmark and finds: BIS Mark, Purity (916), and 6-digit HUID."
            b "The hallmark is present and looks authentic."
        "No need for a magnifying glass. It’s fine; I trust you.":
            $ hallmark_checked = False
            b "No need for a magnifying glass. It’s fine; I trust you."
            k "As you wish!"

    # Scene 3: Checking HUID Details
    if hallmark_checked:
        b "(To himself) Should I verify the HUID on the BIS Care app?"

        menu:
            "Yes, it’s important to check.":
                $ huid_verified = True
                b "Yes, it’s important to check."
                # Randomized outcome
                $ hallmark_is_fake = random.choice([True, False])

                if hallmark_is_fake:
                    b "(Realizes the hallmark is fake!) This hallmark doesn’t seem right."
                    menu:
                        "Confront Kapti Seth.":
                            b "Sethji, this doesn’t match! The weight and jeweller details are wrong."
                            k "Oh, that must be a mistake. Let me check again. (Avoids the issue.)"
                            b "I’m not buying this. I’ll report this to BIS. (Leaves the shop.)"
                        "Leave quietly":
                            b "(Leaves the shop.)"
                    jump Consequences
                else:
                    b "Everything matches perfectly. These are authentic earrings!"
                    k "See, I told you we only sell authentic items."
                # Add further checks and subchoices here
            "No, this much checking is enough.":
                $ huid_verified = False
                b "No, this much checking is enough."

    # Scene 4: Asking for a Proper Bill
    scene bg_shop with fade
    k "Here you go, bhaisaab. Your earrings and a handwritten bill."

    menu:
        "Can I have a proper printed bill, please?":
            $ proper_bill = True
            b "Can I have a proper printed bill, please?"
            k "Sure, here you go!"
        "A handwritten bill is fine.":
            $ proper_bill = False
            b "A handwritten bill is fine."
            k "Thank you for trusting me!"

label Consequences:
    # Scene 5: At Home – Consequences
    scene bg_home with fade
    if license_checked and hallmark_checked and huid_verified and not(hallmark_is_fake) and proper_bill:
        m "Wow, these earrings are perfect! And you checked everything so thoroughly. I’m so proud of you!"
        b "(Feels confident about his purchase.)"
        m "(Feels delighted and is proud of her husband.)"
    
    if not (license_checked) and hallmark_checked and huid_verified and not(hallmark_is_fake) and proper_bill:
        b "Here are your earrings! My dear."
        m "Did you check everything? The hallmark, HUID, and the bill?"
        b "I did not check his license. Rest all is okay."
        m "You shouldn't be so careless. This would have caused us a big damage. Thankfully we didnt get fooled."
        b "I would not make such a mistake again."
        "Carelessness could cost you a fortune, dont forget to check your jeweller's license!"

    elif license_checked and hallmark_checked and huid_verified and not(hallmark_is_fake) and not (proper_bill):
        b "Here are your earrings! My dear."
        m "Did you check everything? The hallmark, HUID, and the bill?"
        b "He gave me a handwritten bill. I thought it was okay"
        m "Dont you know how important it is to have a proper bill. What if Kapti Seth denies this transaction in the future. We'll have no proof."
        m "(Dissapointed) I expected better from you"
        b "I am sorry. I will keep this in mind in the future."
        "Don't be like Bhindi! Always ask for a proper bill."

    elif huid_verified and hallmark_is_fake:
        m "Where are my earrings, dear?"
        b "I visited the shop but didn't buy them."
        m "But why?"
        b "Kapti Seth is a fake. He tried to sell me fake jewellery."
        m "Oh God! Did you report him to the BIS?"
        menu:
            "Yes I am going to report him to the BIS.":
                b "Yes I am going to report him to the BIS."
                b "(Uses the BIS Care app to report the jeweller.)"
                "Kapti Seth's license is cancelled and he can no more fool innocent people."
            "No, I don't want more problems.":
                b "No, I don't want more problems."
                "Kapti seth isn't reported and continues to sell fake jewelry to unsuspecting people who do not verify his jewelry."

    else:
        m "Did you check everything? The hallmark, HUID, and the bill?"
        b "Of course, I trust Kapti Seth."
        m "Let me have a look... (Examines the earrings closely.)"
        if not (hallmark_checked):
            m "Wait, where’s the proper hallmark? This is a 5-digit HUID, HUID must be of 6 digits, it's obviously fake. This doesn’t even look like 916 gold!"
        elif not (huid_verified):
            "(Madhuri uses the BIS Care app to check the details and discovers discrepancies."
            m "Hey! This HUID number doesn’t match the earrings. These might be fake! This doesn’t even look like 916 gold!"
        b "Fake? But Kapti Seth is so famous!"
        m "Fame doesn’t guarantee honesty. I told you to check the license and verify everything!"
        if proper_bill:
            b "Thank God, I have a proper bill.  I will complain about this on the BIS Care app and make sure his license gets cancelled."
            b "(Reports Kapti Seth on the BIS Care App.)"
            "Kapti Seth's license is cancelled and he can no more fool innocent people. Thanks to Bhindi who reported the matter to BIS."
        else:
            b "I will go to his shop tomorrow and fix everything."
            # Scene 6: Bhindi’s Attempt to Fix the Situation
            "The next day, Bhindi goes back to Kapti Seth’s shop."
            b "Sethji, these earrings don’t seem authentic. The HUID doesn’t match, and the gold doesn’t feel like 916 purity."
            k "Nonsense! I sell only genuine jewellery. You already paid and took them home. I can’t do anything now."
            b "But I need a proper bill to file a complaint!"
            k "You didn’t ask for one yesterday. I can’t help you now."
            "Bhindi leaves the shop, frustrated and dejected."

    return
