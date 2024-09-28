VIDEO_CARD = 250.00

money = float(input())
count_video_cards = int(input())
price_video_cards = VIDEO_CARD * count_video_cards

count_processors = int(input())
price_processor1 = price_video_cards * 0.35
price_processors = price_processor1 * count_processors

ram_memory = int(input())
price_ram_memory1 = price_video_cards * 0.1
price_ram_memories = ram_memory * price_ram_memory1

full_price = price_video_cards + price_processors + price_ram_memories

if count_video_cards > count_processors:
    discount = 0.15
else:
    discount = 0

final_price = full_price - (full_price * discount)

if money >= final_price:
    leftover = money - final_price
    print(f"You have {leftover:.2f} leva left!")
else:
    more_needed = final_price - money
    print(f"Not enough money! You need {more_needed:.2f} leva more!")