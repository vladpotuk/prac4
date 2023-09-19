seconds_all=24*60*60
while True:
    input_seconds=int(input("Введіть секунди: "))
    if input_seconds<=86400:
        break
    else:
        print("Такого не може бути.")
remaining_seconds = seconds_all-input_seconds
remaining_hours = remaining_seconds//3600
remaining_minutes = (remaining_seconds%3600)//60
remaining_seconds = remaining_seconds%60
print(f"Залишилось часу: {remaining_hours}годин,{remaining_minutes}хвилин,{remaining_seconds}секунд.")


