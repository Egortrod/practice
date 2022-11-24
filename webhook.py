from discord_webhook import DiscordWebhook, DiscordEmbed

content = "some text"

webhook = DiscordWebhook(url = "your url webhook")

embed = DiscordEmbed(title="title", color=15687)
embed.set_author(name="author name", url = "author url", icon_url = "author icon url")
embed.set_footer(text="footer text")
embed.set_timestamp() 
embed.add_embed_field(name ="embed text", value = "embed lower text")
embed.set_image(url="image url")




webhook.add_embed(embed)
response = webhook.execute()