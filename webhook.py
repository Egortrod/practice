from discord_webhook import DiscordWebhook, DiscordEmbed

content = "Текст для взятия авто"

webhook = DiscordWebhook(url = "https://discord.com/api/webhooks/975090004885930014/9gJXu_gK9iurqbyUktXlXJ2clKtuFvSkxSqFfaHvsZaQW7JkCrxR1-wAMNxiTS_u9o59", username="Autobot", avatar_url="https://i.postimg.cc/KjcHTmd1/444444444.png")

embed = DiscordEmbed(title="**:small_orange_diamond: Для взятия автомобиля необходимо поставить соответствующую реакцию :small_orange_diamond:**", color=242424)
embed.set_author(name="Autobot", url = "https://forum.gta5rp.com/members/richard-evil.37140/", icon_url = "https://cdn-icons-png.flaticon.com/512/89/89102.png")
embed.set_footer(text="by Egortrod")
embed.set_timestamp() 
embed.add_embed_field(name =":small_orange_diamond: На выбор 5 видов авто:\n", value = ":red_car: - Infinity FX50S\n:taxi: - Mercedes G63\n:blue_car: - Lamborghini Urus\n:pickup_truck: - Koenigsegg Gemera\n:bus: - Mercedes G65 6x6\n\n**:small_orange_diamond: После использования автомобиля необходимо\nубрать свою реакцию!**")
embed.set_image(url="https://a.d-cd.net/BYAAAgMyC-A-1920.jpg")




webhook.add_embed(embed)
response = webhook.execute()