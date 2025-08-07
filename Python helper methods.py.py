customer_name = " JANE DOE "
clean_name = customer_name.strip()
print(f"Clean Name: {clean_name}")
lowercase_name = clean_name.lower()
print(f"Lowercase Name: {lowercase_name}")
titlecase_name = lowercase_name.title()
print(f"Tittlecase Name: {titlecase_name}")
book_title = "the little prince"
formatted_title = book_title.capitalize()
print(f"Formatted Title: {formatted_title}")
product_code = "bk-457-nOVEL"
uppercase_code = product_code.upper()
print(f"Uppercase Code: {uppercase_code}")
new_seperator_code = uppercase_code.replace("-", "/")
print(f"New Seperator Code: {new_seperator_code}")
review = "This book is great. I love this book"
book_count = review.count("book")
print(f"Book Count: {book_count}")
serial_number = "987654321"
is_digit_only = serial_number.isdigit()
print(f"Is digit Only: {is_digit_only}")
url_parts = ["the", "book", "nook", "online"]
url_string = "-".join(url_parts)
print(f"URL String: {url_string}")
sentence_string = " ".join(url_parts)
print(f"Sentence String: {sentence_string}")
offer_code = "FREESHIPPING"
is_offer_code_uppercase = offer_code.isupper()
print(f"is Offer Code Uppercase: {is_offer_code_uppercase}")
feedback_message = "I am very happy with my order!"
message_length = len(feedback_message)
print(f"Message Length: {message_length}")